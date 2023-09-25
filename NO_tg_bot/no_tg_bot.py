import telebot
import db
import time

bot = telebot.TeleBot('6306175857:AAEcc0Gaeqfd2HkFMKgYvgyTPnXC_UDnxXw')
# @bot.message_handler(commands=['start'])
# def send(message):
#    x = str(message.chat.id)
#    bot.send_message(message.chat.id, text = x)
   
# bot.polling()
# bot.send_message(chat_id='1171882715', text='123')
# thread_id:
# 2 - Rovenki
# 4 - Lugansk
# 6 - Antracit
# 10 - Krasnodon

# @bot.message_handler(commands=['start'])
# def start_message(message):
#   bot.send_message(message.chat.id,"Привет ✌️ ")
#   print(message)
# bot.polling()


# -----------------   
def tg_bot():
    db.make_db()
    db.make_table()
    itt = 0
    while True:
        user = db.get_unsent_user()
        if user != None:
            msg = 'Город: '+user['city']+'\nИсточник: '+user['src']+'\n\n'+user['text']+''
            if user['city'] == 'Краснодон':
                bot.send_message(chat_id='-1001950482099', text=msg, message_thread_id=10)
            elif user['city'] == 'Антрацит':
                bot.send_message(chat_id='-1001950482099', text=msg, message_thread_id=6)
            elif user['city'] == 'Ровеньки':
                bot.send_message(chat_id='-1001950482099', text=msg, message_thread_id=2)
            elif user['city'] == 'Луганск':
                bot.send_message(chat_id='-1001950482099', text=msg, message_thread_id=4)
            db.user_sent(user['user_id'])
            print(user, '\n\n')    
        elif user == None:
            itt += 1
            print('\n\nNo new messages ' + str(itt) + '\n\n')
            time.sleep(2)


while __name__ == '__main__':
    try:
        time.sleep(2)
        tg_bot()
    except Exception as e:
        print('\n\n---TG BOT EXEPTION---\n\n')
        print(e)
        print('\n\n---END OF TG BOT EXEPTION---\n\n')
