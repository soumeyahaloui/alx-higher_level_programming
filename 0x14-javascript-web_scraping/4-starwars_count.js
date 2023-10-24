#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18; // Wedge Antilles' character ID

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body).results;
    const count = filmsData.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
    console.log(count);
  }
});
