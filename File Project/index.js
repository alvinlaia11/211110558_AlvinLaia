import express from 'express';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const hostname = '127.0.0.1';
const port = 3000;

app.use(express.static('public')); //access from public

app.get('(/)', (req, res) => {
    res.sendFile(__dirname + '/public/halamanAwal.html');
});
// app.get('/logo', (req, res) => {
//     res.sendFile(__dirname + '/public/assets/logo.png');
// });
app.get('/halaman', (req, res) => {
    res.sendFile(__dirname + '/public/halamanAwal.html');
});

// app.get('/special', (req, res) => {
//     res.sendFile(__dirname + '/public/special.html');
// });
// app.get('/popular', (req, res) => {
//     res.sendFile(__dirname + '/public/popular.html');
// });

// app.get('/about', (req, res) => {
//     res.sendFile(__dirname + '/public/about.html');
// });
app.get('/product/:nama', (req, res) => {
    const nama = req.params.nama; //parameter name
    res.send(`Product Name : ${nama}`)
});
app.get('*/:nama', (req, res) => {
    const nama = req.params.nama;
    res.status(404).send(`Direktori ${nama} Tidak Tersedia`);
})
app.listen(port, () => {
    console.log(`Server Running At ${hostname}:${port}`);
});