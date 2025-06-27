import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")  # Railway uchun token

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men ishga tushdim ✅")

bot.polling()
