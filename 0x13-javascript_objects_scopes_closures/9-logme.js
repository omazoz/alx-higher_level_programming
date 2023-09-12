#!/usr/bin/node

function * counter () {
  let index = 0;
  while (true) {
    yield index++;
  }
}
const c = counter();
exports.logMe = function (item) {
  console.log(c.next().value + ': ' + item);
};
