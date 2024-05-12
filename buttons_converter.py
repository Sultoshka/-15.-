from telebot import types

def choice():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    currancy1 = types.KeyboardButton('USD')
    currancy2 = types.KeyboardButton('UZS')
    kb.add(currancy1,currancy2)
    return kb