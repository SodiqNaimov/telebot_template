# from tgbot.helpers.database import SQLite
# from tgbot.texts.text_reply import *
# from telebot import TeleBot

# import pytz
# from datetime import datetime

# For getting lang
# set_user_lang = lambda text: 'ru' if text == lang_msg[1] else 'uz' if text == lang_msg[0] else None

# Alternative way to get one requirement data
# def return_data(message, bot, word):
#     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#         word = data.get(word)
#
#         return word



# def get_current_time_in_uzbekistan():
#     # Get the timezone for Uzbekistan
#     uzbekistan_timezone = pytz.timezone('Asia/Tashkent')
#
#     # Get the current time in UTC
#     current_time_utc = datetime.utcnow()
#
#     # Localize the UTC time to Uzbekistan timezone
#     current_time_uzbekistan = pytz.utc.localize(current_time_utc).astimezone(uzbekistan_timezone)
#
#     # Format the time as per the required format
#     formatted_time = current_time_uzbekistan.strftime("%d.%m.%Y %H:%M:%S")
#
#     return formatted_time


