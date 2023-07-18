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

    # Find the streak section
    streak_section = soup.find('div', class_='user-profile-container')
    if streak_section:
        # Save the streak section to a text file
        with open('streak_section.html', 'w', encoding='utf-8') as file:
            file.write(streak_section.prettify())
        print("Streak section saved to 'streak_section.html' file.")
    else:
        print("Streak information section not found on the page.")

    # Find the problems section
    problems_section = soup.find('div', class_='user-profile-container')
    if problems_section:
        # Save the problems section to a text file
        with open('problems_section.html', 'w', encoding='utf-8') as file:
            file.write(problems_section.prettify())
        print("Problems section saved to 'problems_section.html' file.")
    else:
        print("Problems solved section not found on the page.")
else:
    print("Failed to retrieve data from CodeChef.")
