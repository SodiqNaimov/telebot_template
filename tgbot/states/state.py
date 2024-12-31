from telebot.handler_backends import State, StatesGroup  # States

#For admin's dashboard
class Panel(StatesGroup):
    open_admin_st = State()
#For user's dashboard
class MyStates(StatesGroup):
    name = State()
#For user's registration
class Register(StatesGroup):
    lang_st = State()