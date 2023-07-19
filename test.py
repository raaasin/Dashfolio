import requests
import re
from bs4 import BeautifulSoup
import time

url = 'https://camo.githubusercontent.com/988eae0cabe627f25d27443aedf176fbfd283b04a06fb6e3479de60e8239d40a/68747470733a2f2f6769746875622d726561646d652d73747265616b2d73746174732e6865726f6b756170702e636f6d2f3f757365723d7261616173696e267468656d653d746f6b796f6e6967687426686964655f626f726465723d74727565'

while True:
    response = requests.get(url)
    if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            total_contributions_element = soup.find('g', transform='translate(82.5,48)')
            current_streak = soup.find('g', transform='translate(247.5,48)')
            streak_range=soup.find('g', transform='translate(247.5,145)')
            longest_streak_element = soup.find('g', transform='translate(412.5,48)')
            longest_range_element= soup.find('g', transform='translate(412.5,114)')
            if current_streak and streak_range and total_contributions_element and longest_range_element and longest_streak_element:
                tc=total_contributions_element.find('text')
                cs=current_streak.find('text')
                sr=streak_range.find('text')
                lse=longest_streak_element.find('text')
                lre=longest_range_element.find('text')
                if tc and cs and sr and lse and lre:
                    totalcontrib=tc.string
                    currentstreak=cs.string
                    streakrange=sr.string
                    longeststreak=lse.string
                    longestrange=lre.string
            else:
                 print('sad')
    print(totalcontrib,currentstreak,streakrange,longeststreak,longestrange)

    time.sleep(20)

