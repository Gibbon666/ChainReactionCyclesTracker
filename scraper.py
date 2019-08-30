#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.chainreactioncycles.com/fi/en/mountain-bikes?f=2258&sort=pricelow'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

prices_raw = soup.find_all("li", class_="fromamt")
prices_clean = []
for row in prices_raw:
    prices_clean.append(re.findall(r'€\d+.\d\d', str(row)))
    
print(prices_clean)

# print(re.findall('€\d+.\d\d', "€714.49</li>"))

# tag = soup.li
# print(tag["class"])
# print(soup.find(id="fromamt").get_text())


# print(prices)

