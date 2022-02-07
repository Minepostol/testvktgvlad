import telebot
import requests
import random
import string
from random import choice
from string import digits




token = '1419596760:AAGdM46RPB-lB_jEAL0RCSNcKuMOXeXUdo8'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def lalala(message):
    randomdig = (''.join(choice(digits) for i in range(10)))
    answer = requests.get('https://api.vk.com/method/messages.send?user_id=298862842&random_id=' + randomdig + '&message=' + message.text + '&access_token=7c5ed8ee4cbc0b523b0d4d2983a9719d395abfcc9c3d8859ace10e4bf7366ae5969c71169c1af5ce27932&v=5.131')
    bot.send_message(message.chat.id, answer)
    print('Пришло сообщение от ' + str(message.chat.id) + ' с текстом ' + message.text)
    
bot.polling(none_stop=True)