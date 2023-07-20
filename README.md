# Pdashboard (Personal Dashboard)

Pdashboard is a productivity dashboard designed to help you keep track of your productivity by displaying your GitHub streak and CodeChef streak. This project is built using Flask and Python for the backend, and it utilizes web scraping to fetch data from GitHub and CodeChef. The dashboard interface is created using HTML and JavaScript.

You can access the live version of the Pdashboard at [https://nisar-dashboard.onrender.com/](https://nisar-dashboard.onrender.com/)

## Folder Structure

- `templates/`: This folder consists of the HTML files for the dashboard interface - `index.html`, `codechef.html`, and `github.html`.
- `app.py`: This Python file contains the Flask application and handles the web scraping for GitHub and CodeChef data.
- `README.md`: The file you are currently reading, providing an overview of the project.
- `requirements.txt`: A list of Python dependencies required to run the application.

## Usage

To use Pdashboard locally, follow the instructions below:

1. Clone or download the repository to your local machine.
2. Install the required Python dependencies using `pip install -r requirements.txt`.
3. Run the Flask app using `python app.py`. The dashboard will be accessible at `http://127.0.0.1:5000/` in your web browser.
4. The dashboard will display two widgets: one for GitHub and one for CodeChef.
5. The GitHub widget shows your current streak, fetched using web scraping from your GitHub profile.
6. The CodeChef widget also displays your streak, fetched using web scraping from your CodeChef profile.

Please note that for the web scraping to work correctly, ensure you have a stable internet connection.

## Web Scraping

The Pdashboard utilizes web scraping techniques to fetch data from GitHub and CodeChef. Here are the code snippets responsible for scraping the data:

### GitHub Web Scraping

```python
    def github:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        total_contributions_element = soup.find('g', transform='translate(82.5,48)')
        current_streak = soup.find('g', transform='translate(247.5,48)')
        streak_range = soup.find('g', transform='translate(247.5,145)')
        longest_streak_element = soup.find('g', transform='translate(412.5,48)')
        longest_range_element = soup.find('g', transform='translate(412.5,114)')
        if current_streak and streak_range and total_contributions_element and longest_range_element and longest_streak_element:
            tc = total_contributions_element.find('text')
            cs = current_streak.find('text')
            sr = streak_range.find('text')
            lse = longest_streak_element.find('text')
            lre = longest_range_element.find('text')
            if tc and cs and sr and lse and lre:
                totalcontrib = tc.string
                currentstreak = cs.string
                streakrange = sr.string
                longeststreak = lse.string
                longestrange = lre.string
```

### CodeChef Web Scraping

```python
    def codechef():
    soup = BeautifulSoup(response.content, 'html.parser')
        rating_element = soup.find('div', class_='rating-number')
        if rating_element:
            rating = rating_element.get_text().strip()
            print("Rating:", rating)
        else:
            print("Rating information not found on the page.")
        fully_solved_element = soup.find('h5', text=re.compile(r'Fully Solved \(\d+\)'))
        if fully_solved_element:
            fully_solved = re.search(r'Fully Solved \((\d+)\)', fully_solved_element.text).group(1)
            print("Fully Solved:", fully_solved)
        else:
            print("Fully solved information not found on the page.")
        highest_rating_element = soup.find('small', text=re.compile(r'Highest Rating \d+'))
        if highest_rating_element:
            highest_rating = re.search(r'Highest Rating (\d+)', highest_rating_element.text).group(1)
            print("Highest Rating:", highest_rating)
        else:
            print("Highest rating information not found on the page.")
```

## Future Plans

- Enhance the dashboard with more customization options and a user-friendly interface.
- Add support for additional productivity platforms and display their streaks.
- Optimize the web scraping process for faster and more efficient data retrieval.

Feel free to customize and enhance the project further as per your requirements. Contributions and suggestions are welcome!

## Screenshot

![Dashboard Widget](Dashboard.png)

## License

This project is licensed under the [MIT License](LICENSE).