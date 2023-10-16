import 'dart:async';

import 'package:flutter/material.dart';
import 'package:tmdblistviewtraining/detailscreen.dart';
import 'package:tmdblistviewtraining/helper.dart';
import 'package:tmdblistviewtraining/search.dart';

enum MovieCategory { latest, nowPlaying, popular, topRated, upcoming }

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  MovieCategory _selectedCategory = MovieCategory.nowPlaying;
  StreamController<List?> streamController = StreamController<List?>();

  HttpHelper? helper;
  List? movies;
  final String iconBase = 'https://image.tmdb.org/t/p/w92/';
  final String defaultImage =
      'https://images.freeimages.com/images/large-previews/5eb/movie-clapboard-1184339.jpg';

  void initialize() {
    helper?.getMovies(_selectedCategory).listen((movies) {
      streamController.add(movies);
    });
  }

  @override
  void initState() {
    helper = HttpHelper();
    Timer.periodic(Duration(seconds: 5), (Timer t) => initialize());
    super.initState();
  }

  @override
  void dispose() {
    streamController.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    NetworkImage image;
    String getAppBarTitle(MovieCategory category) {
      switch (category) {
        case MovieCategory.latest:
          return 'Latest';
        case MovieCategory.nowPlaying:
          return 'Now Playing';
        case MovieCategory.popular:
          return 'Popular';
        case MovieCategory.topRated:
          return 'Top Rated';
        case MovieCategory.upcoming:
          return 'Up Coming';
      }
      return '';
    }

    return Scaffold(
      appBar: AppBar(
        title: Text(getAppBarTitle(_selectedCategory)),
        actions: <Widget>[
          IconButton(
            onPressed: () {
              MaterialPageRoute route =
                  MaterialPageRoute(builder: (_) => const SearchMovie());
              Navigator.push(context, route);
            },
            icon: Icon(Icons.search),
          ),
        ],
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            DropdownButton<MovieCategory>(
              value: _selectedCategory,
              onChanged: (MovieCategory newValue) {
                setState(() {
                  _selectedCategory = newValue;
                  initialize();
                });
              },
              items: MovieCategory.values
                  .map((category) {
                    return DropdownMenuItem<MovieCategory>(
                      value: category,
                      child: Text(getAppBarTitle(category)),
                    );
                  })
                  .toList(),
            ),
            StreamBuilder<List?>(
              stream: streamController.stream,
              builder: (BuildContext context, AsyncSnapshot<List?> snapshot) {
                if (snapshot.hasError) {
                  return Text('Error: ${snapshot.error}');
                }
                switch (snapshot.connectionState) {
                  case ConnectionState.waiting:
                    return CircularProgressIndicator();
                  default:
                    if (snapshot.hasData) {
                      return Expanded(
                        child: ListView.builder(
                          itemCount: snapshot.data?.length ?? 0,
                          itemBuilder: (BuildContext context, int position) {
                            ImageProvider image;
                            if (snapshot.data![position].posterPath != null) {
                              image = NetworkImage(
                                  iconBase + snapshot.data![position].posterPath);
                            } else {
                              image = NetworkImage(defaultImage);
                            }
                            return Card(
                              color: Colors.white,
                              elevation: 2.0,
                              child: ListTile(
                                onTap: () {
                                  MaterialPageRoute route = MaterialPageRoute(
                                      builder: (_) =>
                                          DetailScreen(snapshot.data![position]));
                                  Navigator.push(context, route);
                                },
                                leading: CircleAvatar(
                                  backgroundImage: image,
                                ),
                                title: Text(snapshot.data![position].title),
                                subtitle: Text('Released: ' +
                                    snapshot.data![position].releaseDate +
                                    ' - Vote: ' +
                                    snapshot.data![position].voteAverage.toString()),
                              ),
                            );
                          },
                        ),
                      );
                    } else {
                      return Text('No data');
                    }
                }
              },
            ),
          ],
        ),
      ),
    );
  }
}
