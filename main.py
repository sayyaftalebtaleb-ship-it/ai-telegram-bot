import asyncio
import aiohttp
from telebot.async_telebot import AsyncTeleBot

BOT_TOKEN = "7965345356:AAEiY2Q3UQ6WZvpFQAAmap0eebvLRvWXVuY"
GROQ_KEY = "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"
bot = AsyncTeleBot(BOT_TOKEN)

async def groq_async(prompt):
    headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
    json_data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.groq.com/openai/v1/chat/completions",
                                headers=headers, json=json_data, timeout=30) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data["choices"][0]["message"]["content"]
            else:
                return f"خطأ: {resp.status}"

@bot.message_handler(func=lambda m: True)
async def echo_all(message):
    user_text = message.text
    # رد مبدئي لإظهار أن البوت يكتب
    await bot.send_chat_action(message.chat.id, 'typing')
    response = await groq_async(user_text)
    await bot.reply_to(message, response)

async def main():
    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())
