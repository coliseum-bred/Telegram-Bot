import telebot
import webbrowser

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['site', 'website'])                                     
def site(message):                                                                     # command input /site
    webbrowser.open('https://github.com/coliseum-bred')                                # redirecting to the specified website


@bot.message_handler(commands=["start"])
def start(message):                                                                    # command input /start
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}")        # output: text + user's name


@bot.message_handler(commands=["help"])
def help(message):                                                                     # command input /help
    bot.send_message(message.chat.id, "<b>Help information</b>", parse_mode="html")    # output text with HTML formatting

@bot.message_handler()
def id(message):
    if message.text.lower() == 'id':                                                   # input text without command
        bot.reply_to(message, f'ID: {message.from_user.id}')                           # reply to the message + output: user's ID


bot.infinity_polling()