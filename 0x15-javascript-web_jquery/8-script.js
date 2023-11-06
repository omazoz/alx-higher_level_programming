const $ = window.$;
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  let i = 0;
  while (data.results[i]) {
    $('UL#list_movies').append($('<li>').text(data.results[i].title));
    i++;
  }
});