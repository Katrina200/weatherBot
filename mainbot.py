import telebot
import weatherparsing
import astrologiaparsing
import anekdotparsing
import misliparsing
from telebot import types
import requests
import random
from bs4 import BeautifulSoup as bot

bot = telebot.TeleBot('5685074220:AAHnl0dXFLWn4IgKoT8zIgdbYqvI2xgdhYo') # для Pomogalnic_bot

@bot.message_handler(commands=['start'])
def send_welcome(message):
        name = bot.get_me()
        print(name)
        bot.reply_to(message, f"Привет {message.from_user.first_name} !!!" \
                              f" С чего начнем? Для хорошего начала дня выберите категорию - нажмите /menu")

@bot.message_handler(commands=['menu'])
def start(message):
    a = types.InlineKeyboardMarkup(row_width=2)
    a_weather = types.InlineKeyboardButton(text='\U000026C5 Погода', callback_data='weather')
    a_astrolog = types.InlineKeyboardButton(text='\U0001F31F Астрология', callback_data='astrolog')
    a_anekdot = types.InlineKeyboardButton(text='\U0001F44F Анекдот', callback_data='anekdot')
    a_misli = types.InlineKeyboardButton(text='\U0001F4E2 Мысли великих', callback_data='misli')
    a.add(a_weather, a_astrolog, a_anekdot, a_misli)
    bot.send_message(message.chat.id, '\U0001F31E Что вас интересует?:', reply_markup=a)


markupMenu= types.InlineKeyboardMarkup()
item_back = types.InlineKeyboardButton("Вернуться к меню", callback_data="menu")
markupMenu.add(item_back)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    if call.message:
        if call.data == 'anekdot':
            bot.send_message(call.message.chat.id, anekdotparsing.list_of_jokes ,reply_markup=markupMenu)


        if call.data == 'misli':
            bot.send_message(call.message.chat.id, misliparsing.list_of_misli, reply_markup=markupMenu)

        if call.data == 'weather':
            a_weather = types.InlineKeyboardMarkup()
            a_weather_1 = types.InlineKeyboardButton('\U00002705 Гомель', callback_data='gomel')
            a_weather_2 = types.InlineKeyboardButton('\U00002705 Минск', callback_data='minsk')
            a_weather_3 = types.InlineKeyboardButton('\U00002705 Витебск', callback_data='vitebsk')
            a_weather_4 = types.InlineKeyboardButton('\U00002705 Гродно', callback_data='grodno')
            a_weather_5 = types.InlineKeyboardButton('\U00002705 Могилёв', callback_data='mogilev')
            a_weather_6 = types.InlineKeyboardButton('\U00002705 Брест', callback_data='brest')
            a_weather.add(a_weather_1, a_weather_2, a_weather_3, a_weather_4, a_weather_5, a_weather_6)
            bot.send_message(call.message.chat.id, text='Выбери областной центр', reply_markup=a_weather)

        elif call.data == 'gomel':
            bot.send_message(call.message.chat.id, f'Погода в Гомеле на сегодня: {weatherparsing.text_result_gomel}', reply_markup=markupMenu)
        elif call.data == 'minsk':
            bot.send_message(call.message.chat.id, f'Погода в Минске на сегодня: {weatherparsing.text_result_minsk}', reply_markup=markupMenu)
        elif call.data == 'vitebsk':
            bot.send_message(call.message.chat.id, f'Погода в Витебске на сегодня: {weatherparsing.text_result_vitebsk}', reply_markup=markupMenu)
        elif call.data == 'grodno':
            bot.send_message(call.message.chat.id, f'Погода в Гродно на сегодня: {weatherparsing.text_result_grodno}', reply_markup=markupMenu)
        elif call.data == 'mogilev':
            bot.send_message(call.message.chat.id, f'Погода в Могилёве на сегодня: {weatherparsing.text_result_mogilev}', reply_markup=markupMenu)
        elif call.data == 'brest':
            bot.send_message(call.message.chat.id, f'Погода в Бресте на сегодня: {weatherparsing.text_result_brest}', reply_markup=markupMenu)
        elif call.data == "back":
            bot.send_message(call.message.chat.id, "Привет! Я бот, который расскажет о курсах валют в РБ 🇧🇾",reply_markup=markupStart)

        if call.data == 'astrolog':
            a_astrolog = types.InlineKeyboardMarkup()
            a_astrolog_1 = types.InlineKeyboardButton(text='\U00002652 Водолей', callback_data='vodolei')
            a_astrolog_2 = types.InlineKeyboardButton(text='\U00002653 Рыбы', callback_data='ribi')
            a_astrolog_3 = types.InlineKeyboardButton(text='\U00002648 Овен', callback_data='oven')
            a_astrolog_4 = types.InlineKeyboardButton(text='\U00002649 Телец', callback_data='telec')
            a_astrolog_5 = types.InlineKeyboardButton(text='\U0000264A Близнецы', callback_data='blizneci')
            a_astrolog_6 = types.InlineKeyboardButton(text='\U0000264B Рак', callback_data='rak')
            a_astrolog_7 = types.InlineKeyboardButton(text='\U0000264C Лев', callback_data='lev')
            a_astrolog_8 = types.InlineKeyboardButton(text='\U0000264D Дева', callback_data='deva')
            a_astrolog_9 = types.InlineKeyboardButton(text='\U00002650 Стрелец', callback_data='strelec')
            a_astrolog_10 = types.InlineKeyboardButton(text='\U0000264F Скорпион', callback_data='skorpion')
            a_astrolog_11 = types.InlineKeyboardButton(text='\U0000264E Весы', callback_data='vesi')
            a_astrolog_12 = types.InlineKeyboardButton(text='\U00002651 Козерог', callback_data='kozerog')
            a_astrolog.add(a_astrolog_1, a_astrolog_2, a_astrolog_3, a_astrolog_4, a_astrolog_5, a_astrolog_6, a_astrolog_7, a_astrolog_8, a_astrolog_9, a_astrolog_10, a_astrolog_11, a_astrolog_12)
            bot.send_message(call.message.chat.id, text='Выбери свой знак зодиака:', reply_markup=a_astrolog)

        elif call.data == 'vodolei':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для водолея на сегодня: {astrologiaparsing.text_result_vodolei}', reply_markup=markupMenu)
        elif call.data == 'ribi':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для рыб на сегодня: {astrologiaparsing.text_result_ribi}', reply_markup=markupMenu)
        elif call.data == 'oven':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для овна на сегодня: {astrologiaparsing.text_result_oven}', reply_markup=markupMenu)
        elif call.data == 'telec':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для тельца на сегодня: {astrologiaparsing.text_result_telec}', reply_markup=markupMenu)
        elif call.data == 'blizneci':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для близнеца на сегодня: {astrologiaparsing.text_result_blizneci}', reply_markup=markupMenu)
        elif call.data == 'rak':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для рака на сегодня: {astrologiaparsing.text_result_rak}', reply_markup=markupMenu)
        elif call.data == 'lev':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для льва на сегодня: {astrologiaparsing.text_result_lev}', reply_markup=markupMenu)
        elif call.data == 'deva':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для девы на сегодня: {astrologiaparsing.text_result_deva}', reply_markup=markupMenu)
        elif call.data == 'strelec':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для стрельца на сегодня: {astrologiaparsing.text_result_strelec}', reply_markup=markupMenu)
        elif call.data == 'skorpion':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для скорпиона на сегодня: {astrologiaparsing.text_result_scorpion}', reply_markup=markupMenu)
        elif call.data == 'vesi':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для весов на сегодня: {astrologiaparsing.text_result_vesi}', reply_markup=markupMenu)
        elif call.data == 'kozerog':
            bot.send_message(call.message.chat.id, f'Астрологический прогноз для козерогов на сегодня: {astrologiaparsing.text_result_kozerog}', reply_markup=markupMenu)



bot.polling(none_stop=True)
