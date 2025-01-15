import telebot
import sqlite3

bot = telebot.TeleBot("TOKEN")
name = None

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('licey.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(60), pass VARCHAR(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Hello, we will register you now! Please enter your name.')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Please enter your password.')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('licey.sql')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('User List', callback_data='users'))
    bot.send_message(message.chat.id, 'You have been registered.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('licey.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for i in users:
        info += f'Name: {i[1]}, Password: {i[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

bot.infinity_polling()