import telebot
from config import token
import random


bot = telebot.TeleBot(token)


jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the beach? To clear its cache!",
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "Why was the math book sad? It had too many problems!"
]


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Cheep, cheep, cheep...Hi there, I am Tsyplenok.
I am here to talk with you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, """\
I am a bot Tsyplenok,cheep, cheep, cheep... created for communication and repeating your words! My main task is to entertain you.\
""")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = random.choice(jokes)
    bot.reply_to(message, f"Cheep, cheep, cheep... Here's a joke for you:\n{joke}")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id  
    file_info = bot.get_file(file_id)    
    downloaded_file = bot.download_file(file_info.file_path) 

    with open("photo.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.reply_to(message, "Cheeep Cheep, thanks for the photo! I received it!")

    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()