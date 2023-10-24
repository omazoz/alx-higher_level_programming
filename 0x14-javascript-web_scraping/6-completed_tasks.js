#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body);
    const completed = {};
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (completed[json[i].userId] === undefined) {
          completed[json[i].userId] = 1;
        } else {
          completed[json[i].userId]++;
        }
      }
    }
    console.log(completed);
  }
});
