from telebot import types

def choice():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    help = types.KeyboardButton('HELP')
    Help = types.KeyboardButton('HELP ME!!!')
    kb.add(help, Help)
    return kb