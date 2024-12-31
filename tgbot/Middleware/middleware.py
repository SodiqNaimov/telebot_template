from telebot.types import Message
from telebot.handler_backends import BaseMiddleware
from tgbot.helpers.database import SQLite
from telebot import TeleBot

class LanguageMiddleware(BaseMiddleware):
    def __init__(self, bot: TeleBot):
        super().__init__()
        self.bot = bot
        self.update_types = ['message']
        # Always specify update types, otherwise middlewares won't work

    def pre_process(self, message: Message, data):
        # Retrieve user's language preference from database
        user_id = message.from_user.id
        # Example: Assuming a function `get_user_language_from_db` to fetch language
        user_language = self.get_user_language_from_db(user_id)

        # Store language preference in the `data` dictionary to pass it to handlers
        data['user_language'] = user_language

    def post_process(self, message, data, exception):
        pass

    def get_user_language_from_db(self, user_id):
        # Example function to retrieve user's language from a database
        db = SQLite()
        try:
            result = db.get_user_lang(user_id)
            if result:
                return result[0]  # Assuming language is stored in the first column
            else:
                # Default language if not found
                return 'en'
        except Exception as e:
            pass




# Example usage
