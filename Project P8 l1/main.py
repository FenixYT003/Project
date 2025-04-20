import telebot
import random
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Меры предотвращения")
    btn2 = types.KeyboardButton('Причины глоб. потепления')
    btn3 = types.KeyboardButton('Последствия глоб. потепления')
    btn4 = types.KeyboardButton('Результаты глоб. потепления')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Привет, я являюсь ботом, который может рассказать тебе факты о том, как предотвратить глобальное потепление, а также причины и последствия глоб. потепления', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Меры предотвращения":
        sovets = ['Ограничение и сокращение потребления ископаемого углеродного топлива', 'Повышение эффективности потребления энергии', 'Развитие новых экологических технологий']
        bot.send_message(message.chat.id, random.choice(sovets))

    elif message.text == "Причины глоб. потепления":
        prichina = ['Выбросы парниковых газов', 'Извержения вулканов', 'Изменение атмосферного состава', 'Изменение океанской циркуляции']
        bot.send_message(message.chat.id, random.choice(prichina))

    elif message.text == "Последствия глоб. потепления":
        sovet = ['Таяние полярных льдов', 'Повышение уровня Мирового океана', 'Изменение режима циркуляции атмосферы', 'Сдвиг климатических поясов', 'Появление новых пустынь на планете']
        bot.send_message(message.chat.id, random.choice(sovet))

    elif message.text == "Результаты глоб. потепления":
        result = ['Изменение погодных условий', 'Плавление ледников', 'Подъём уровня морей и другие негативные последствия для экосистем и человечества']
        bot.send_message(message.chat.id, random.choice(result))
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выберите одну из доступных опций.")

bot.polling()