from transliterate import to_latin , to_cyrillic
import telebot
TOKEN='1648267549:AAGQ_qkYBnt_E27FnMVXf2SzyrtVV0sPRYc'
bot = telebot.TeleBot("TOKEN", parse_mode=None)
matn=input("matin kiriting: ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, Xush kelinsiz!")
bot.polling()
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))