from bs4 import BeautifulSoup
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
        current_rating_text.string = '157'  # Replace with the extracted current rating
        highest_rating_text.string = '157'  # Replace with the extracted highest rating
        problems.string='20'
with open('codechef.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
print("HTML file updated successfully.")
