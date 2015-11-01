"use strict";

const express = require('express');
const bodyParser = require('body-parser');
const twilio = require('twilio');

const app = express();

const server = app.listen(3000, () => {
	console.log('listening on port 3000');
});

const io = require('socket.io')(server);

app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static('static'));

app.get('/', (req, res) => {
	res.send('HackNY r00lz');
});

app.get('/voice', (req, res) => {
	let twiml = twilio.TwimlResponse();
	twiml.play('http://gnarly.io/megaman.mp3');
	res.send(twiml.toString());
});
