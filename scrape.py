from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Firefox WebDriver
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

# CodeChef URL
url = "https://www.codechef.com/users/raasin"

# Open the URL
driver.get(url)

# Wait for the streak element to be visible
streak_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="badge__progress"]')))

# Scrape the streak
streak = streak_element.text
print("Streak:", streak)

# Wait for the problems solved element to be visible
problems_solved_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="badge__progress"]')))

# Scrape the problems solved
problems_solved = problems_solved_element.text
print("Problems Solved:", problems_solved)

# Quit the WebDriver
driver.quit()
