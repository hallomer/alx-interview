#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Construct the URL for the Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to the API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);

  // Get the list of character URLs
  const characters = data.characters;

  // Function to print character names in order
  const printCharacter = (index) => {
    if (index >= characters.length) return;

    // Request each character's data
    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      // Parse character data and print name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);

      // Recursively print the next character
      printCharacter(index + 1);
    });
  };

  // Start printing characters
  printCharacter(0);
});
