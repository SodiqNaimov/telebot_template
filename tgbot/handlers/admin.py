from telebot import TeleBot
from telebot.types import *  # ReplyKeyboardRemove, CallbackQuery

# for state
from telebot.states.sync.context import StateContext
from tgbot.states.state import Panel

# messages
from tgbot.texts.admin_message import *

# for use keyboards
from tgbot.helpers.keyboards import *  # , inline_markup
from tgbot.texts.text_reply import *

# for use database
from tgbot.helpers.database import SQLite


def open_admin(message: Message, bot: TeleBot, state: StateContext):
    bot.send_message(message.from_user.id, welcome_admin_text.format(message.from_user.first_name), reply_markup=reply_markup(admin_btn, 1))
    state.set(Panel.open_admin_st)