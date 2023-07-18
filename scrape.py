import requests
import re
from bs4 import BeautifulSoup
import time

url = 'https://www.codechef.com/users/raasin'

while True:
    response = requests.get(url)
    if response.status_code == 200:
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
        
        with open('codechef.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        current_rating_element = soup.find('g', transform='translate(247.5,48)')
        highest_rating_element = soup.find('g', transform='translate(412.5,48)')
        problems_solved = soup.find('g', transform='translate(82.5,48)')
        if current_rating_element and highest_rating_element and problems_solved:
            current_rating_text = current_rating_element.find('text')
            highest_rating_text = highest_rating_element.find('text')
            problems_solved_text = problems_solved.find('text')
            if current_rating_text and highest_rating_text and problems_solved_text:
                current_rating_text.string = rating  
                highest_rating_text.string = highest_rating  
                problems_solved_text.string = fully_solved

        with open('codechef.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify()) 

    else:
        print("Failed to retrieve data from CodeChef.")

    time.sleep(20)
