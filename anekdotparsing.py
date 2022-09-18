import requests
import random
from bs4 import BeautifulSoup as b

URL = 'https://humornet.ru/anekdot/zveri/'

def parser (url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]
an = parser(URL)
random.choice(an)




