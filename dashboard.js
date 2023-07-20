// Function to fetch and update CodeChef data
function fetchCodeChefData() {
    const urll = 'https://www.codechef.com/users/raasin';
    fetch(urll)
      .then((response) => response.text())
      .then((htmlContent) => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(htmlContent, 'text/html');
        const ratingElement = doc.querySelector('div.rating-number');
        const fullySolvedElement = doc.querySelector('h5:contains("Fully Solved")');
        const highestRatingElement = doc.querySelector('small:contains("Highest Rating")');
  
        let rating = 'Rating information not found on the page.';
        let fullySolved = 'Fully solved information not found on the page.';
        let highestRating = 'Highest rating information not found on the page.';
  
        if (ratingElement) {
          rating = ratingElement.innerText.trim();
        }
  
        if (fullySolvedElement) {
          fullySolved = fullySolvedElement.innerText.match(/\d+/)[0];
        }
  
        if (highestRatingElement) {
          highestRating = highestRatingElement.innerText.match(/\d+/)[0];
        }
  
        // Update the HTML content with the fetched data
        const codeChefHtmlContent = `
          <div>
            <p>Rating: ${rating}</p>
            <p>Fully Solved: ${fullySolved}</p>
            <p>Highest Rating: ${highestRating}</p>
          </div>
        `;
  
        // Assuming you have an element with id "codechefStreak" to display the data
        document.getElementById('codechefStreak').innerHTML = codeChefHtmlContent;
      })
      .catch((error) => {
        console.error('Failed to retrieve data from CodeChef:', error);
      });
  }
  
  // Function to fetch and update GitHub data
  function fetchGitHubData() {
    const url = 'https://camo.githubusercontent.com/988eae0cabe627f25d27443aedf176fbfd283b04a06fb6e3479de60e8239d40a/68747470733a2f2f6769746875622d726561646d652d73747265616b2d73746174732e6865726f6b756170702e636f6d2f3f757365723d7261616173696e267468656d653d746f6b796f6e6967687426686964655f626f726465723d74727565';
  
    fetch(url)
      .then((response) => response.text())
      .then((htmlContent) => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(htmlContent, 'text/html');
        const totalContributionsElement = doc.querySelector('g[transform="translate(82.5,48)"]');
        const currentStreakElement = doc.querySelector('g[transform="translate(247.5,48)"]');
        const streakRangeElement = doc.querySelector('g[transform="translate(247.5,145)"]');
        const longestStreakElement = doc.querySelector('g[transform="translate(412.5,48)"]');
        const longestRangeElement = doc.querySelector('g[transform="translate(412.5,114)"]');
  
        // Assuming you have elements with specific IDs to display the data
        document.getElementById('totalContributions').innerText = totalContributionsElement.querySelector('text').innerText;
        document.getElementById('currentStreak').innerText = currentStreakElement.querySelector('text').innerText;
        document.getElementById('streakRange').innerText = streakRangeElement.querySelector('text').innerText;
        document.getElementById('longestStreak').innerText = longestStreakElement.querySelector('text').innerText;
        document.getElementById('longestRange').innerText = longestRangeElement.querySelector('text').innerText;
      })
      .catch((error) => {
        console.error('Failed to retrieve data from GitHub:', error);
      });
  }
  
  // Function to update data every 20 seconds
  function updateData() {
    fetchCodeChefData();
    fetchGitHubData();
  
    setTimeout(updateData, 20000); // Update every 20 seconds
  }
  
  // Initial update
  updateData();
  