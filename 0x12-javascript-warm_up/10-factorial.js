#!/usr/bin/node

function factorial (number) {
    if (number < 1 || !number) {
      return 1;
    } else {
      return (number * factorial(number - 1));
    }
  }
  
  console.log(factorial(parseInt(process.argv[2])));