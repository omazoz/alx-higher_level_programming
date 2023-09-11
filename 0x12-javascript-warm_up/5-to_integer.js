#!/usr/bin/node
const args = process.argv.slice(2);
const nbr = Number(args[0]);
if (Number.isNaN(nbr)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${nbr}`);
}
