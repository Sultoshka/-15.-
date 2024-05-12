import telebot, buttons

bot = telebot.TeleBot('6900287057:AAGh87ROoJGRYNgUExmRKurFGsKgb1mciTM')

@bot.message_handler(commands=['Start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'Здраствуйте ? {message.from_user.first_name}!',
                     reply_markup=buttons.choice())
    bot.register_next_step_handler(message, int)



@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'usd':
        bot.send_message(user_id, 'Введите сумму сколько вы хотите разминять')
        bot.register_next_step_handler(message, currancy1)
        bot.send_message(user_id, sum())
    elif message.text.lower() == 'uzs':
            bot.send_message(user_id, 'Введите слово для перевода')
            bot.register_next_step_handler(message, currancy2)
            bot.send_message(user_id, sum(int * 12700))
    else:
        bot.send_message(user_id, 'Ошибка подщёте и системы')

bot.polling()