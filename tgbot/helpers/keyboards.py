from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
# for calling text_repky
from tgbot.texts.text_reply import *

def reply_markup(texts, row_width=2, one_time_keyboard=False):
    """
    Create a ReplyKeyboardMarkup with the given texts.

    :param texts: List of button texts.
    :param row_width: Number of buttons per row.
    :return: ReplyKeyboardMarkup object.
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=one_time_keyboard, row_width=row_width)
    markup.add(*texts)
    return markup

