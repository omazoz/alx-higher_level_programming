#!/usr/bin/node
exports.converter = function (b) {
  function base (num) {
    return num.toString(b);
  }
  return base;
};
