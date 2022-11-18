from os import link
import types
import telebot
from telebot import types
API_TOKEN = '5549196144:AAH-AD47v-jTVH_hdekO-4OWWNxoJAklAH0'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет {message.from_user.first_name}, я бот для просмотра характеристик танков с игры Wot blitz. Введите /use"
    bot.send_message(message.chat.id, mess)

# choice your lvl
@bot.message_handler(commands=["use"])
def start(message):
    BtnBar = types.InlineKeyboardMarkup()
    Btn7 = types.InlineKeyboardButton(text = "7 lvl", callback_data ="7 lvl")
    Btn8 = types.InlineKeyboardButton(text = "8 lvl", callback_data ="8 lvl")
    Btn9 = types.InlineKeyboardButton(text = "9 lvl", callback_data ="9 lvl")
    Btn10 = types.InlineKeyboardButton(text = "10 lvl", callback_data ="10 lvl")
    BtnBar.add(Btn7, Btn8, Btn9, Btn10)
    bot.send_message(message.chat.id, "Виберите уровень танка", reply_markup = BtnBar)

@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    BtnBar = types.InlineKeyboardMarkup()
    Btn1 = types.InlineKeyboardButton(text = "ТТ", callback_data1="heavy tank")
    Btn2 = types.InlineKeyboardButton(text = "СТ", callback_data1="mediun tank")
    Btn3 = types.InlineKeyboardButton(text = "ЛТ", callback_data1="light tank")
    Btn4 = types.InlineKeyboardButton(text = "ПТ", callback_data1="tank destroyer")
    BtnBar.add(Btn1, Btn2, Btn3, Btn4)

    if call.data == "7 lvl":
        bot.send_message(call.message.chat.id, "Виберите класс техники", reply_markup=BtnBar)
    elif call.data == "8 lvl":
        bot.send_message(call.message.chat.id, "Виберите класс техники", reply_markup=BtnBar)
    elif call.data == "9 lvl":
        bot.send_message(call.message.chat.id, "Виберите класс техники", reply_markup=BtnBar)
    elif call.data == "10 lvl":
        bot.send_message(call.message.chat.id, "Виберите класс техники", reply_markup=BtnBar)
def Tank_nation(call):
    if call.data == "heavy tank":
        bot.send_message(call.message.chat.id, "Ok1")
    elif call.data == "medium tank":
        bot.send_message(call.message.chat.id, "Ok2")
    elif call.data == "light tank":
        bot.send_message(call.message.chat.id, "Ok3")
    elif call.data == "tank destroyer":
        bot.send_message(call.message.chat.id, "Ok4")

bot.polling(none_stop=True)