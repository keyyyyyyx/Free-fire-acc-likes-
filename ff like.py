import telebot
import requests

# Replace with your Telegram bot token
BOT_TOKEN = "7778117419:AAFsuHDo3XTSxOHFSeAWjtD-NZk7qN7LqHo"

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Function to send likes using Free Fire API
def send_likes(uid):
    url = "https://ff-community-api.vercel.app/sendLikes"
    params = {
        "uid": uid,
        "access_key": "lufzywork"
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return f"✅ Success: {response.json()}"
    else:
        return f"❌ Error {response.status_code}: {response.text}"

# Command to start the bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Kirim UID EpEp Kalian untuk mengirim like.\nExample: `12345678`", parse_mode="Markdown")

# Handling user messages (UID input)
@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_uid(message):
    uid = message.text
    response = send_likes(uid)
    bot.reply_to(message, response)

# Run the bot
bot.infinity_polling()
