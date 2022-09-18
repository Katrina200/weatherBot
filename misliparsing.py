import requests
import random
from bs4 import BeautifulSoup as b

URL = 'https://millionstatusov.ru/source/vostochnaya-mudrost.html'

def parser (url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    misli = soup.find_all('div', class_='cont_text')
    return [c.text for c in misli]
list_of_misli = parser(URL)
random.choice(list_of_misli)

