
  function fetchCodeChefData() {
    const codechefUrl = 'https://www.codechef.com/users/raasin';

    fetch(codechefUrl)
      .then((response) => response.text())
      .then((html) => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');

        const ratingElement = doc.querySelector('div.rating-number');
        const rating = ratingElement ? ratingElement.textContent.trim() : 'Rating information not found on the page.';

        const fullySolvedElement = doc.querySelector('h5:contains("Fully Solved")');
        const fullySolved = fullySolvedElement
          ? fullySolvedElement.textContent.match(/\d+/)[0]
          : 'Fully solved information not found on the page.';

        const highestRatingElement = doc.querySelector('small:contains("Highest Rating")');
        const highestRating = highestRatingElement
          ? highestRatingElement.textContent.match(/\d+/)[0]
          : 'Highest rating information not found on the page.';

        updateCodeChefHtml(rating, fullySolved, highestRating);
      })
      .catch((error) => {
        console.error('Failed to retrieve data from CodeChef.', error);
      });
  }

  function updateCodeChefHtml(rating, fullySolved, highestRating) {
    const codechefHtml = `
      <div>
        <g transform="translate(247.5,48)">
          <text>${rating}</text>
        </g>
        <g transform="translate(412.5,48)">
          <text>${highestRating}</text>
        </g>
        <g transform="translate(82.5,48)">
          <text>${fullySolved}</text>
        </g>
      </div>
    `;

    // Update the codechef.html file
    const codechefFile = new Blob([codechefHtml], { type: 'text/html' });
    const codechefUrl = URL.createObjectURL(codechefFile);
    document.querySelector('div[w3-include-html="codechef.html"]').innerHTML = `<object type="text/html" data="${codechefUrl}" ></object>`;
  }

  function fetchGitHubData() {
    const githubUrl = 'https://camo.githubusercontent.com/988eae0cabe627f25d27443aedf176fbfd283b04a06fb6e3479de60e8239d40a/68747470733a2f2f6769746875622d726561646d652d73747265616b2d73746174732e6865726f6b756170702e636f6d2f3f757365723d7261616173696e267468656d653d746f6b796f6e6967687426686964655f626f726465723d74727565';

    fetch(githubUrl)
      .then((response) => response.text())
      .then((html) => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');

        const totalContribElement = doc.querySelector('g[transform="translate(82.5,48)"] text');
        const currentStreakElement = doc.querySelector('g[transform="translate(247.5,48)"] text');
        const streakRangeElement = doc.querySelector('g[transform="translate(247.5,145)"] text');
        const longestStreakElement = doc.querySelector('g[transform="translate(412.5,48)"] text');
        const longestRangeElement = doc.querySelector('g[transform="translate(412.5,114)"] text');

        const totalContrib = totalContribElement ? totalContribElement.textContent : 'sad';
        const currentStreak = currentStreakElement ? currentStreakElement.textContent : 'sad';
        const streakRange = streakRangeElement ? streakRangeElement.textContent : 'sad';
        const longestStreak = longestStreakElement ? longestStreakElement.textContent : 'sad';
        const longestRange = longestRangeElement ? longestRangeElement.textContent : 'sad';

        updateGitHubHtml(totalContrib, currentStreak, streakRange, longestStreak, longestRange);
      })
      .catch((error) => {
        console.error('Failed to retrieve data from GitHub.', error);
      });
  }

  function updateGitHubHtml(totalContrib, currentStreak, streakRange, longestStreak, longestRange) {
    const githubHtml = `
      <div>
        <g transform="translate(82.5,48)">
          <text>${totalContrib}</text>
        </g>
        <g transform="translate(247.5,48)">
          <text>${currentStreak}</text>
        </g>
        <g transform="translate(247.5,145)">
          <text>${streakRange}</text>
        </g>
        <g transform="translate(412.5,48)">
          <text>${longestStreak}</text>
        </g>
        <g transform="translate(412.5,114)">
          <text>${longestRange}</text>
        </g>
      </div>
    `;

    // Update the github.html file
    const githubFile = new Blob([githubHtml], { type: 'text/html' });
    const githubUrl = URL.createObjectURL(githubFile);
    document.querySelector('div[w3-include-html="github.html"]').innerHTML = `<object type="text/html" data="${githubUrl}" ></object>`;
  }

  function includeHTML() {
    const elements = document.querySelectorAll('[w3-include-html]');
    elements.forEach((element) => {
      const file = element.getAttribute('w3-include-html');
      if (file) {
        fetch(file)
          .then((response) => response.text())
          .then((html) => {
            element.innerHTML = html;
          })
          .catch((error) => {
            console.error(`Failed to include "${file}"`, error);
            element.innerHTML = 'Page not found.';
          });
      }
    });
  }

  // Fetch and display CodeChef data initially
  fetchCodeChefData();

  // Fetch and display GitHub data initially
  fetchGitHubData();

  // Refresh CodeChef and GitHub data every 20 seconds
  setInterval(() => {
    fetchCodeChefData();
    fetchGitHubData();
  }, 20000);

  // Include codechef.html and github.html in the dashboard
  includeHTML();

