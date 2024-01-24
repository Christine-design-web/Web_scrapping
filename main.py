#!/usr/bin/env python3

#importing the
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.airbnb.com/').text
soup = BeautifulSoup(html_text, 'lxml')
Jobs = soup.find_all('p')
print(Jobs)
