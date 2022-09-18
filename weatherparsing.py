# Парсинг сайта погоды.
import requests
import bs4

URL_MINSK = 'https://world-weather.ru/pogoda/belarus/minsk/'
URL_MOGILEV= 'https://world-weather.ru/pogoda/belarus/mogilev/'
URL_GOMEL = 'https://world-weather.ru/pogoda/belarus/gomel/'
URL_GRODNO = 'https://world-weather.ru/pogoda/belarus/grodno/'
URL_VITEBSK = 'https://world-weather.ru/pogoda/belarus/vitebsk/'
URL_BREST = 'https://world-weather.ru/pogoda/belarus/brest/'
#city = input('Введите название областного центра с большой буквы : ')

def minsk_parsing(url):
    r_minsk = requests.get(url)
    soup = bs4.BeautifulSoup(r_minsk.text, 'html.parser')
    result_minsk = soup.find_all('p', class_='description-weather')
    return [c.text for c in result_minsk]
text_result_minsk = minsk_parsing(URL_MINSK)

def gomel_parsing(url):
    r_gomel = requests.get(url)
    soup = bs4.BeautifulSoup(r_gomel.text, 'html.parser')
    result_gomel = soup.find_all('p', class_='description-weather')
    return [c.text for c in result_gomel]
text_result_gomel = gomel_parsing(URL_GOMEL)

def vitebsk_parsing(url):
    r_vitebsk = requests.get(url)
    soup = bs4.BeautifulSoup(r_vitebsk.text, 'html.parser')
    result_vitebsk = soup.find_all('p', class_='description-weather')
    return [c.text for c in result_vitebsk]
text_result_vitebsk = vitebsk_parsing(URL_VITEBSK)

def grodno_parsing(url):
    r_grodno = requests.get(url)
    soup = bs4.BeautifulSoup(r_grodno.text, 'html.parser')
    result_grodno = soup.find_all('p', class_='description-weather')
    return [c.text for c in result_grodno]
text_result_grodno = grodno_parsing(URL_GRODNO)

def brest_parsing(url):
    r_brest = requests.get(url)
    soup = bs4.BeautifulSoup(r_brest.text, 'html.parser')
    result_brest = soup.find_all('p', class_='description-weather')
    return [c.text for c in result_brest]
text_result_brest = brest_parsing(URL_BREST)

def mogilev_parsing(url):
    r_mogilev = requests.get(url)
    soup = bs4.BeautifulSoup(r_mogilev.text, 'html.parser')
    result_mogilev = soup.find_all('p', class_='description-weather')
    return [c.text for c in result_mogilev]
text_result_mogilev = mogilev_parsing(URL_MOGILEV)
