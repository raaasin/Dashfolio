import requests
from bs4 import BeautifulSoup

# URL of the CodeChef profile page
url = 'https://www.codechef.com/users/raasin'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the streak element by searching for the 'Streak' label
    streak_label = soup.find('b', text='Streak:')
    if streak_label:
        # Extract the streak value from the following sibling element
        streak = streak_label.next_sibling.strip()
        print("Streak:", streak)
    else:
        print("Streak information not found on the page.")

    # Find the problems solved element by searching for the 'Problems Solved' label
    problems_label = soup.find('b', text='Problems Solved:')
    if problems_label:
        # Extract the problems solved value from the following sibling element
        problems_solved = problems_label.next_sibling.strip()
        print("Problems Solved:", problems_solved)
    else:
        print("Problems solved information not found on the page.")
else:
    print("Failed to retrieve data from CodeChef.")
