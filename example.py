from bs4 import BeautifulSoup
import requests

url = 'https://www.example.com'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# Find all paragraph tags
paragraphs = soup.find_all('p')

# Print the text of each paragraph
for paragraph in paragraphs:
    print(paragraph.text)

