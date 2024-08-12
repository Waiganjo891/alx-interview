#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    let charactersCount = characters.length;
    const charactersNames = [];

    characters.forEach((characterUrl, index) => {
        request(characterUrl, (error, response, body) => {
            if (error) {
                console.error(error);
                return;
            }

            const characterData = JSON.parse(body);
            charactersNames[index] = characterData.name;
            charactersCount--;

            if (charactersCount === 0) {
                charactersNames.forEach(name => console.log(name));
            }
        });
    });
});
