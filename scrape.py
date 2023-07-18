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

    # Find the fully solved number element
    fully_solved_element = soup.find('h5', text=re.compile(r'Fully Solved \(\d+\)'))
    if fully_solved_element:
        fully_solved = re.search(r'Fully Solved \((\d+)\)', fully_solved_element.text).group(1)
        print("Fully Solved:", fully_solved)
    else:
        print("Fully solved information not found on the page.")

    # Save the fully solved information to the existing text file
    with open('codechef_ratings.txt', 'a', encoding='utf-8') as file:
        file.write("Fully Solved: " + fully_solved + "\n")
    print("Fully solved information added to 'codechef_ratings.txt' file.")
else:
    print("Failed to retrieve data from CodeChef.")
