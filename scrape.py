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

    # Print the prettified HTML content
    print(soup.prettify())
else:
    print("Failed to retrieve data from CodeChef.")
