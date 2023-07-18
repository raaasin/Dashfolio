import requests
import re
from bs4 import BeautifulSoup

# URL of the CodeChef profile page
url = 'https://www.codechef.com/users/raasin'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the rating element
    rating_element = soup.find('div', class_='rating-number')
    if rating_element:
        rating = rating_element.get_text().strip()
        print("Rating:", rating)
    else:
        print("Rating information not found on the page.")
    
    # Find the fully solved number element
    fully_solved_element = soup.find('h5', text=re.compile(r'Fully Solved \(\d+\)'))
    if fully_solved_element:
        fully_solved = re.search(r'Fully Solved \((\d+)\)', fully_solved_element.text).group(1)
        print("Fully Solved:", fully_solved)
    else:
        print("Fully solved information not found on the page.")

    # Find the highest rating element using regular expression pattern
    highest_rating_element = soup.find('small', text=re.compile(r'Highest Rating \d+'))
    if highest_rating_element:
        highest_rating = re.search(r'Highest Rating (\d+)', highest_rating_element.text).group(1)
        print("Highest Rating:", highest_rating)
    else:
        print("Highest rating information not found on the page.")
    """file.write("Rating: " + rating + "\n")
        file.write("Highest Rating: " + highest_rating + "\n")
        file.write("Fully Solved: " + fully_solved + "\n")"""
    # Save the extracted information to a text file
    with open('codechef.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    current_rating_element = soup.find('g', transform='translate(247.5,48)')
    highest_rating_element = soup.find('g', transform='translate(412.5,48)')
    problems_solved=soup.find('g', transform='translate(82.5,48)')
    if current_rating_element and highest_rating_element:
        current_rating_text = current_rating_element.find('text')
        highest_rating_text = highest_rating_element.find('text')
        problems=problems_solved.find('text')
        if current_rating_text and highest_rating_text and problems:
            current_rating_text.string = rating  # Replace with the extracted current rating
            highest_rating_text.string = highest_rating  # Replace with the extracted highest rating
            problems.string=fully_solved
    with open('codechef.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())           
else:
    print("Failed to retrieve data from CodeChef.")
