#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    const printCharacter = (index) => {
      if (index < characterUrls.length) {
        request(characterUrls[index], (error, response, characterBody) => {
          if (error) {
            console.error(error);
          } else {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
            printCharacter(index + 1);
          }
        });
      }
    };

    printCharacter(0);
  }
});
