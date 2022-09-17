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
random.shuffle(list_of_misli)
#print(list_of_misli)
def jokmislis(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_misli[0])
        del list_of_misli[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру: ')