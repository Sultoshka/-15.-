import telebot, buttons3

bot = telebot.TeleBot('6708276732:AAEWhSJa41nGnoaywXHS3ugx6kTeDur0wkI')

@bot.message_handler(commands=['Start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Здраствуйте ? {message.from_user.first_name}!',
                     reply_markup=buttons.choice())
    bot.register_next_step_handler(message, text)



@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'help':
        bot.send_message(user_id, 'вам чём-то помочь?')
        bot.register_next_step_handler(message, help)
    elif message.text.lower() == 'HELP ME IM INSIDE THE CLOSET SOMEONE IN MY HOUSE WANNA TO KILL ME!!!':
        bot.send_message(user_id, 'Я ЗВАНЮ ПОЛИЦИЮ ЖДИТЕ ТАМ ГДЕ ВЫ ЕСТЬ!!!')
        bot.register_next_step_handler(message, Help)
    else:
        bot.send_message(user_id, 'Ошибка подщёте и системы')

bot.polling(non_stop=True)