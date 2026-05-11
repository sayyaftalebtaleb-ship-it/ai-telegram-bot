import telebot
import requests
import urllib.parse

# ضع التوكن الخاص بك هنا
API_TOKEN = '7965345356:AAEiY2Q3UQ6WZvpFQAAmap0eebvLRvWXVuY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    
    # تحويل النص ليكون صالحاً للروابط (عشان العربي والمسافات)
    query = urllib.parse.quote(user_input)
    api_url = f"https://text.pollinations.ai/{query}"
    
    try:
        # إضافة timeout لتجنب التعليق
        response = requests.get(api_url, timeout=30)
        
        if response.status_code == 200 and response.text.strip():
            bot.reply_to(message, response.text)
        else:
            bot.reply_to(message, "الذكاء الاصطناعي لم يرسل رداً، جرب سؤالاً آخر.")
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "حدث خطأ في الاتصال بالسيرفر.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
