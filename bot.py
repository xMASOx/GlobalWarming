from congif import TOKEN
import telebot

API_TOKEN = '7756358632:AAHslRehr2qgSVFNSVAwYEy4Hji0lewBgHc'

bot = telebot.TeleBot('7756358632:AAHslRehr2qgSVFNSVAwYEy4Hji0lewBgHc')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['info'])
def send_welcome(message):
    bot.reply_to(message, )

@bot.message_handler(content_types=['photo'])

def gg(message):
    bot.send_message(message.chat.id, """
  10/10""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()