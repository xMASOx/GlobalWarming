import telebot

TOKEN = ("7756358632:AAHslRehr2qgSVFNSVAwYEy4Hji0lewBgHc")
bot = telebot.TeleBot("7756358632:AAHslRehr2qgSVFNSVAwYEy4Hji0lewBgHc")

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def info(self):
        return f"Машина: {self.brand}, Цвет: {self.color}"

@bot.message_handler(commands=['car'])
def car_handler(message):
    args = message.text.split()[1:] 
    if len(args) < 2:
        bot.reply_to(message, "Используйте формат: /car <цвет> <марка>")
        return
    
    color, brand = args[0], " ".join(args[1:])
    car = Car(color, brand)
    bot.reply_to(message, car.info()) 

bot.polling(none_stop=True)