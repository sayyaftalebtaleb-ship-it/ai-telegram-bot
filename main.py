import telebot
import requests

# استبدل الكلمة بالتوكن الذي أخذته من BotFather
API_TOKEN = '7965345356:AAEiY2Q3UQ6WZvpFQAAmap0eebvLRvWXVuY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    # رابط مكتبة Pollinations للرد النصي
    api_url = f"https://text.pollinations.ai/{user_input}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            bot.reply_to(message, response.text)
        else:
            bot.reply_to(message, "عذراً، الذكاء الاصطناعي لا يرد حالياً.")
    except:
        bot.reply_to(message, "حدث خطأ في الاتصال.")

if __name__ == "__main__":
    print("البوت بدأ العمل...")
    bot.polling(none_stop=True)
