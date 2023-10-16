import 'package:flutter/material.dart';
import 'package:basic/components/htpHelper.dart';
import 'package:basic/components/detail.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  HttpHelper? helper;
  List? movies;
  final String iconBase = 'https://image.tmdb.org/t/p/w92/';
  final String defaultImage =
      'https://images.freeimages.com/images/large-previews/5eb/movieclapboard-1184339.jpg';

  String selectedGenre = 'All'; // Default selected genre

  @override
  void initState() {
    super.initState();
    helper = HttpHelper();
    initialize();
  }

  Future initialize() async {
    movies = await helper?.getMovies();
    setState(() {
      movies = movies;
    });
  }

  @override
  Widget build(BuildContext context) {
    NetworkImage image;
    return Scaffold(
      appBar: AppBar(
        title: Text('Now Playing'),
        actions: <Widget>[
          DropdownButton<String>(
            value: selectedGenre,
            items: <String>['All', 'Horror', 'Romantis', 'Comedy']
                .map((String value) {
              return DropdownMenuItem<String>(
                value: value,
                child: Text(value),
              );
            }).toList(),
            onChanged: (String? newValue) {
              setState(() {
                selectedGenre = newValue!;
              });
            },
          ),
        ],
      ),
      body: ListView.builder(
        itemCount: (movies?.length == null) ? 0 : movies?.length,
        itemBuilder: (BuildContext context, int position) {
          if (movies![position].posterPath != null) {
            image = NetworkImage(iconBase + movies![position].posterPath);
          } else {
            image = NetworkImage(defaultImage);
          }

          if (selectedGenre == 'All' ||
              movies![position].genre == selectedGenre) {
            return Card(
              color: Colors.white,
              elevation: 2.0,
              child: ListTile(
                onTap: () {
                  MaterialPageRoute route = MaterialPageRoute(
                      builder: (_) => DetailScreen(movies![position]));
                  Navigator.push(context, route);
                },
                leading: CircleAvatar(
                  backgroundImage: image,
                ),
                title: Text(movies![position].title),
                subtitle: Text('Released: ' +
                    movies![position].releaseDate +
                    ' - Vote: ' +
                    movies![position].voteAverage.toString()),
              ),
            );
          } else {
            return SizedBox.shrink();
          }
        },
      ),
    );
  }
}
