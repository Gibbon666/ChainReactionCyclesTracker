#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
from send_price import *
import time

def check_price():
    URL = 'https://www.chainreactioncycles.com/fi/en/mountain-bikes?f=2258&sort=pricelow'
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    prices_raw = soup.find_all("li", class_="fromamt")
    prices_clean = []
    for row in prices_raw:
        prices_clean.append(float(re.findall(r'\d+.\d\d', str(row))[0]))
        
    if min(prices_clean) < 300:
        send_simple_message(min(prices_clean), URL)

while(True):
    check_price()
    time.sleep(3600)

