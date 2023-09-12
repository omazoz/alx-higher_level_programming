#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  charPrint (c) {
    let s = '';
    let h;
    if (c === undefined) { h = 'X'; } else { h = c; }
    for (let i = 0; i < this.width; i++) { s += h; }
    for (let i = 0; i < this.height; i++) { console.log(s); }
  }
}
module.exports = Square;
