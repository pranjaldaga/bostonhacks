var express = require('express');
var app = express();
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.get('/Alyssa', function (req, res) {
	res.send('Hello Alyssa! I love you!');
});

app.get('/', function (req, res) {
	res.render('index');
});

var server = app.listen(3000, function () {
	var host = server.address().address;
	var port = server.address().port;

	console.log('Example app listening at http://%s:%s', host, port);
});
