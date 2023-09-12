#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let o = 0;
  list.forEach((element) => { if (searchElement === element) { o++; } });
  return (o);
};
