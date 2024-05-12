from telebot import types

def choice():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    wiki = types.KeyboardButton('wikipedia')
    trans = types.KeyboardButton('translate')
    kb.add(wiki, trans)
    return kb