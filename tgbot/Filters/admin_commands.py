from telebot import TeleBot
from telebot.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from tgbot.helpers.database import SQLite

db = SQLite()

# admins = [db.select_all_admin()]

admins = [866489508, 766158313]


def set_commands(bot: TeleBot) -> None:
    # Set default commands for all users
    default_commands = [
        BotCommand(
            command="start",
            description="Botni ishga tushirish"
        ),
    ]
    bot.set_my_commands(default_commands, scope=BotCommandScopeDefault())

    # Set admin-specific commands for each admin
    for admin in admins:
        print(admin)
        try:
            admin_commands = [
                BotCommand(
                    command="start",
                    description="Botni qayta ishga tushirish"
                ),
                BotCommand(
                    command="admin",
                    description="Admin panelga kirish"
                )
            ]
            bot.set_my_commands(admin_commands, scope=BotCommandScopeChat(chat_id=str(admin[0])))
        except Exception as e:
            print(e)