squiimport telebot
import time
import os 
import random

bot = telebot.TeleBot("6363836014:AAHX2Aqd_--KFxJBbNc5aEiJ9Rw6Y9oD_R4")
import requests 

timeout = 60 # Increase the timeout to 60 seconds 
response = requests.get('https://api.telegram.org', timeout=timeout)


from requests.exceptions import ReadTimeout

max_retries = 3
retry_delay = 5 # seconds

for _ in range(max_retries):
    try:
        response = requests.get('https://api.telegram.org', timeout=25)
        # Process the response
        break  # Break out of the loop if the request succeeds
    except ReadTimeout as e:
        print(f"Timeout occurred: {e}")
        time.sleep(retry_delay)

# Try deploying Python as a Flask App 


# Welcome message when bot starts

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to the HaramMemeBot, Add this to your group chat along with admin permissions to use it.')
    
    
# Custom message for Squigs.eth 

@bot.message_handler(func=lambda message: message.text == "/squigs@haram_meme_bot")
def send_pee_message(message):
    print("Haram")
    username = message.from_user.username
    
    gif_path = './Memes/'
    gifs = [ '5.gif']
    random_gif = random.choice(gifs)
    bot.send_chat_action(message.chat.id, 'upload_video')
    with open(os.path.join(gif_path, random_gif), 'rb') as f:
        gif = f.read()
        bot.send_chat_action(message.chat.id, 'upload_video')
        bot.send_video_note(message.chat.id, gif, duration=5)
        
        
# Send random gif message 
   
@bot.message_handler(func=lambda message: message.text == "/haram@haram_meme_bot")
def send_pee_message(message):
    print("Haram Gif called ")
    username = message.from_user.username
    
    gif_path = './Memes/'
    gifs = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif']
    random_gif = random.choice(gifs)
    bot.send_chat_action(message.chat.id, 'upload_video')
    with open(os.path.join(gif_path, random_gif), 'rb') as f:
        gif = f.read()
        bot.send_chat_action(message.chat.id, 'upload_video')
        bot.send_video_note(message.chat.id, gif, duration=5)
        
        
        
# Send random quote message 

@bot.message_handler(func=lambda message: message.text == "/pray@haram_meme_bot")
def send_pee_message(message):
    print("Prayer inbound")
    username = message.from_user.username
    quotes = [
    "Verily, with hardship comes ease. – Quran, 94:6",
    "The best among you are those who have the best manners and character. – Prophet Muhammad (peace be upon him)",
    "Do good deeds properly, sincerely and moderately, and remember that your deeds will not make you enter Paradise. The most beloved deed to Allah's is the most regular and constant even though it were little. – Prophet Muhammad (peace be upon him)",
    "Whoever is not grateful for what he has, will not be grateful for what he receives. – Prophet Muhammad (peace be upon him)",
    "The strong person is not the one who can wrestle someone else down. The strong person is the one who can control himself when he is angry. – Prophet Muhammad (peace be upon him)",
    "Speak good or remain silent. – Prophet Muhammad (peace be upon him)",
    "The best jihad (struggle) is the one against the self. – Prophet Muhammad (peace be upon him)",
    "Seek knowledge from the cradle to the grave. – Prophet Muhammad (peace be upon him)",
    "None of you truly believes until he loves for his brother what he loves for himself. – Prophet Muhammad (peace be upon him)",
    "When you see a person who has been given more than you in money and beauty, look to those who have been given less. – Prophet Muhammad (peace be upon him)"
]
    
    random_quote = random.choice(quotes)
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, random_quote)
    
    
# Send Fed message 

@bot.message_handler(func=lambda message: message.text == "/fed@haram_meme_bot")
def send_pee_message(message):
    print("Fed investigation")
    username = message.from_user.username
    
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, "In case of an investigation by any federal entity or similar, I do not have any involvement with this group or with the Infidels in it, I do not know how I am here, probably added by a third party, My purchase of $HARAM does not show my support of any actions by the Infidels in this group.")



bot.polling()
