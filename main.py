import telebot
import requests
import urllib.parse

# ضع التوكن الخاص بك هنا
API_TOKEN = '7965345356:AAEiY2Q3UQ6WZvpFQAAmap0eebvLRvWXVuY'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    
    # تحويل النص ليكون صالحاً للروابط
    query = urllib.parse.quote(user_input)
    
    # استخدمنا الرابط المباشر للموديل الافتراضي (أقل قيوداً)
    api_url = f"https://text.pollinations.ai/{query}?model=search"
    
    try:
        # أرسل الطلب بدون Headers معقدة (أحياناً تكون هي السبب في 403)
        response = requests.get(api_url, timeout=30)
        
        if response.status_code == 200:
            ai_reply = response.text.strip()
            if ai_reply:
                bot.reply_to(message, ai_reply)
            else:
                bot.reply_to(message, "الذكاء الاصطناعي أرسل رداً فارغاً.")
        else:
            # إذا استمرت 403، سنحاول تجربة رابط بديل فوراً داخل الكود
            alt_url = f"https://text.pollinations.ai/{query}"
            response_alt = requests.get(alt_url, timeout=30)
            if response_alt.status_code == 200:
                bot.reply_to(message, response_alt.text)
            else:
                bot.reply_to(message, f"الموقع يرفض الاتصال حالياً (403). حاول بعد قليل.")
                
    except Exception as e:
        bot.reply_to(message, "فشل تقني في جلب الرد.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
