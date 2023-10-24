#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const json = JSON.parse(body);
    for (const film of json.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
