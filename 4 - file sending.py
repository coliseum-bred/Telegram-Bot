import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['give'])
def photo(message):
    file = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file) # Optionally, you can add buttons below the keyboard: bot.send_photo(message.chat.id, file, reply_markup=markup)

bot.infinity_polling()