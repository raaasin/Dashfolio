# Pdashboard (Personal Dashboard)

Pdashboard is a productivity dashboard designed to help you keep track of your productivity by displaying your GitHub streak and CodeChef streak. This project is built using Python for web scraping and fetching data from GitHub and CodeChef. It is planned to be migrated to JavaScript for scraping in the future. The fetched streak values are then updated in the website every 20 seconds.

## Files

- README.md: This file provides an overview of the project and its usage.
- codechef.html: HTML file to display the CodeChef streak.
- github.html: HTML file to display the GitHub streak.
- index.html: The main HTML file that serves as the dashboard interface.
- scrape.py: Python script for web scraping and updating streak values.

## Usage

To use Pdashboard, follow the instructions below:

1. Clone or download the repository to your local machine.
2. Open the `index.html` file in a web browser.
3. The dashboard will display two widgets: one for GitHub and one for CodeChef.
4. The GitHub widget shows your current streak, fetched using web scraping.
5. The CodeChef widget also displays your streak, fetched using web scraping.

## Updating Streak Values

The project currently fetches the streak values every 20 seconds using the `scrape.py` script. The script utilizes web scraping techniques in Python to extract the streak values from the respective websites. The fetched values are then updated in the `github.html` and `codechef.html` files, which are included in the main dashboard `index.html` using JavaScript.

## Future Plans

- Migrate the web scraping feature from Python to JavaScript.
- Add functionality to display my certifications and other relevant information.
- Transform the project into a portfolio website to showcase my achievements and skills.

Feel free to customize and enhance the project as per your requirements. Contributions and suggestions are welcome!

**Note:** Ensure that you have a stable internet connection for the web scraping feature to work properly.