import requests
import random
from bs4 import BeautifulSoup as b

URL = 'https://humornet.ru/anekdot/zveri/'

def parser (url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]
list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)
#print(list_of_jokes)
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру: ')