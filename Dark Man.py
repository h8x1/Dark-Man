import telebot
tele = input('⌯ 5250517078:AAHHhFIGm8ZNSJQWSFFlQH9ExwzpR4QRRVs >  ') 
bot = telebot.TeleBot(tele)
@bot.message_handler(commands=["start"])
def wel(message):
 iabsd = str(message.from_user.id)
 usabser = message.from_user.username
 nabsme = message.from_user.first_name
 bot.send_message(message.chat.id,f"""⌯ Your ID : `{iabsd}` .
⌯ Your Name : `{nabsme}` .
⌯ Your User : `@{usabser}` .""",parse_mode="markdown")
bot.polling(True)