import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start'])                   # When the bot starts, buttons will be displayed below the keyboard
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Go to website')
    btn2 = types.KeyboardButton('Delete photo')
    btn3 = types.KeyboardButton('Edit text')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Go to website':
        bot.send_message(message.chat.id, 'Website opened')
    elif message.text == 'Delete photo':
        bot.send_message(message.chat.id, 'Photo deleted')


@bot.message_handler(content_types=['photo'])              # Buttons under the messages
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to website', url='https://github.com/coliseum-bred')
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Edit text', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'What a beautiful photo', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message.id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Message edited', callback.message.chat.id, callback.message.message.id)

bot.infinity_polling()