#!/usr/bin/node
const request = require('request');
id = process.argv[2];
url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, function (error, response, body) {
	if (error) {
		console.error(error);
	}
	for (const person of JSON.parse(body).characters) {
		request(person, function (error, response, body) {
			if (error) {
				console.error(error);
			}
			console.log(JSON.parse(body).name);
		});
	}
});
