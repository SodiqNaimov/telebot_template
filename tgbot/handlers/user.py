from telebot import TeleBot
from telebot.types import *  # ReplyKeyboardRemove, CallbackQuery
# for get user info
from tgbot.helpers.user_information import User_info
# for state
from telebot.states.sync.context import StateContext
# for define states
from tgbot.states.state import Register, MyStates
# messages
from tgbot.texts.messages import *

# for use keyboards
from tgbot.helpers.keyboards import *  # , inline_markup
from tgbot.texts.text_reply import *

# for use database
from tgbot.helpers.database import SQLite
# for smaller function
from tgbot.helpers.small_function import *

def start_func(message: Message, bot: TeleBot, state: StateContext):
    bot.send_message(message.from_user.id, msg_start, reply_markup=reply_markup(lang_msg))
    state.set(Register.lang_st)