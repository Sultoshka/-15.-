import telebot, buttons

#creating object bot
bot = telebot.TeleBot('7158943085:AAG5eDCnMYA9NKRE9M3zll4VTT15SZchMwQ')


#command handler /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'hello ballz lover 69 {message.from_user.first_name}!',
                     reply_markup=buttons.choice())
    bot.register_next_step_handler(message, text)
    #print(message.from_user)

#
@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'wikipedia':
     bot.send_message(user_id,'Введите слово')
     bot.register_next_step_handler(message, wiki)
    elif message.text.lower() == 'translate':
        bot.send_message(user_id, 'Введите слово для перевода')
        bot.register_next_step_handler(message, trans)

def wiki(message):
    user_id = message.from_user.id
    requests = message.text
    if requests == 'Tim Cock':
        bot.send_message(user_id,
            'https://www.apple.com/leadership/tim-cook/')
    else:
        bot.send_message(user_id, 'Im sorry but i only know the Tim Cock but not the Tim Cook(')


def trans(message):
    user_id = message.from_user.id
    word = message.text
    if word == 'I dont know':
        bot.send_message(user_id, 'I dont know for real no cap i dont know anything you saying to me right now!')
    else:
        bot.send_message(user_id, 'Bro just SHUT THE FUCK UP!!!')
    #bot.send_message(user_id, 'OTKAZZZ')
    #bot.send_photo(user_id,
                   #photo='https://static.cargurus.com/images/forsale/2024/04/30/19/07/2007_kia_optima-pic'
                         #'-7217935505103808025-1024x768.jpeg', caption='Моя любимая машина')



#starting bot
bot.polling()