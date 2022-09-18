# Парсинг сайта астрологии.

import requests
import bs4

URL_OVEN = 'https://horoscopes.rambler.ru/aries/'
URL_TELEC = 'https://horoscopes.rambler.ru/taurus/'
URL_BLIZNECI = 'https://horoscopes.rambler.ru/gemini/'
URL_RAK = 'https://horoscopes.rambler.ru/cancer/'
URL_LEV = 'https://horoscopes.rambler.ru/leo/'
URL_DEVA = 'https://horoscopes.rambler.ru/virgo/'
URL_VESI = 'https://horoscopes.rambler.ru/libra/'
URL_SCORPION = 'https://horoscopes.rambler.ru/scorpio/'
URL_STRELEC = 'https://horoscopes.rambler.ru/sagittarius/'
URL_KOZEROG = 'https://horoscopes.rambler.ru/capricorn/'
URL_RIBI = 'https://horoscopes.rambler.ru/pisces/'
URL_VODOLEI = 'https://horoscopes.rambler.ru/aquarius/'
#zodiak = input('Введите свой знак зодиака с большой буквы: ')

def oven_parsing(url):
    r_oven = requests.get(url)
    soup = bs4.BeautifulSoup(r_oven.text, 'html.parser')
    result_oven = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_oven]
text_result_oven = oven_parsing(URL_OVEN)

def telec_parsing(url):
    r_telec = requests.get(url)
    soup = bs4.BeautifulSoup(r_telec.text, 'html.parser')
    result_telec = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_telec]
text_result_telec = telec_parsing(URL_TELEC)

def blizneci_parsing(url):
    r_blizneci = requests.get(url)
    soup = bs4.BeautifulSoup(r_blizneci.text, 'html.parser')
    result_blizneci = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_blizneci]
text_result_blizneci = blizneci_parsing(URL_BLIZNECI)

def rak_parsing(url):
    r_rak = requests.get(url)
    soup = bs4.BeautifulSoup(r_rak.text, 'html.parser')
    result_rak = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_rak]
text_result_rak = rak_parsing(URL_RAK)

def lev_parsing(url):
    r_lev = requests.get(url)
    soup = bs4.BeautifulSoup(r_lev.text, 'html.parser')
    result_lev = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_lev]
text_result_lev = lev_parsing(URL_LEV)

def deva_parsing(url):
    r_deva = requests.get(url)
    soup = bs4.BeautifulSoup(r_deva.text, 'html.parser')
    result_deva = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_deva]
text_result_deva = deva_parsing(URL_DEVA)

def vesi_parsing(url):
    r_vesi = requests.get(url)
    soup = bs4.BeautifulSoup(r_vesi.text, 'html.parser')
    result_vesi = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_vesi]
text_result_vesi = deva_parsing(URL_VESI)

def scorpion_parsing(url):
    r_scorpion = requests.get(url)
    soup = bs4.BeautifulSoup(r_scorpion.text, 'html.parser')
    result_scorpion = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_scorpion]
text_result_scorpion = scorpion_parsing(URL_SCORPION)

def strelec_parsing(url):
    r_strelec = requests.get(url)
    soup = bs4.BeautifulSoup(r_strelec.text, 'html.parser')
    result_strelec = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_strelec]
text_result_strelec = strelec_parsing(URL_STRELEC)

def kozerog_parsing(url):
    r_kozerog = requests.get(url)
    soup = bs4.BeautifulSoup(r_kozerog.text, 'html.parser')
    result_kozerog = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_kozerog]
text_result_kozerog = kozerog_parsing(URL_KOZEROG)

def ribi_parsing(url):
    r_ribi = requests.get(url)
    soup = bs4.BeautifulSoup(r_ribi.text, 'html.parser')
    result_ribi = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_ribi]
text_result_ribi = ribi_parsing(URL_RIBI)

def vodolei_parsing(url):
    r_vodolei = requests.get(url)
    soup = bs4.BeautifulSoup(r_vodolei.text, 'html.parser')
    result_vodolei = soup.find_all('p', class_='mtZOt')
    return [c.text for c in result_vodolei]
text_result_vodolei = vodolei_parsing(URL_VODOLEI)
