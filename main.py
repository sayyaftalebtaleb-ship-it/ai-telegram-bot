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
    
    # الرابط الجديد مع تحديد الموديل لضمان الاستجابة
    api_url = f"https://text.pollinations.ai/{query}?model=openai&system=You are a helpful AI assistant"
    
    # إضافة Headers لخدع الموقع بأنه طلب من متصفح حقيقي
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # محاولة جلب الرد
        response = requests.get(api_url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            ai_reply = response.text.strip()
            if ai_reply:
                bot.reply_to(message, ai_reply)
            else:
                bot.reply_to(message, "وصلني رد فارغ من الذكاء الاصطناعي، جرب سؤالاً آخر.")
        else:
            # إذا فشل، سيخبرك البوت برقم الخطأ (مفيد جداً لنا)
            bot.reply_to(message, f"فشل الاتصال. كود الخطأ: {response.status_code}")
            
    except Exception as e:
        bot.reply_to(message, f"حدث خطأ تقني: {str(e)}")

if __name__ == "__main__":
    print("البوت يعمل الآن بأعلى كفاءة...")
    bot.polling(none_stop=True)
