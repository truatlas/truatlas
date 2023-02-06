import telebot
from telebot import types

bot = telebot.TeleBot("11111")

directionskeyboard = types.InlineKeyboardMarkup()
directionskeyboard.add(
    types.InlineKeyboardButton(text="БИОЛОГИЯ", callback_data="BIOLOGY"),
    types.InlineKeyboardButton(text="ФИЗИКА И ТЕХНИКА", callback_data="PHYSICS"),
    types.InlineKeyboardButton(text="ЗОЖ", callback_data="HEALTHY"),
    types.InlineKeyboardButton(text="ИСКУССТВО И КУЛЬТУРА", callback_data="ART"),
    types.InlineKeyboardButton(text="ЯЗЫКОЗНАНИЕ", callback_data="LINGUISTICS"),
    types.InlineKeyboardButton(text="МЕДИЦИНА", callback_data="MEDICS"),
    types.InlineKeyboardButton(text="ПСИХОЛОГИЯ", callback_data="PSYCHOLOGY"),
    types.InlineKeyboardButton(text="МАТЕМАТИКА И ГЕОМЕТРИЯ", callback_data="MATHEMATICS"),
    types.InlineKeyboardButton(text="ОБЩЕСТВОЗНАНИЕ И ПРАВОВЕДЕНИЕ", callback_data="JURISPRUDENCE"),
    row_width=3
)

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    ListOfLections = types.InlineKeyboardMarkup(row_width=3)
    if call.data == "CHOICE":
        mainkeyboard = types.ReplyKeyboardMarkup()
        mainkeyboard.add(
            types.KeyboardButton("Присоединиться!"),
            types.KeyboardButton("МЕНЮ С НАПРАВЛЕНИЯМИ"),
            row_width=1)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Хороший выбор! Мы ждем тебя на кружке!", reply_markup=mainkeyboard)
    elif call.data == 'BIOLOGY':
        ListOfLections.add(
            types.InlineKeyboardButton(text="Биоинженерия", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Авиценна", callback_data="CHOICE")
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "PHYSICS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Электротех", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="«Spektrum», молодёжный научно-инновационный конструкторский центр", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="«Технопарк «Профи», студенческое конструкторское бюро", callback_data="CHOICE")
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "HEALTHY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Здоровые перспективы", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Будь на спорте!", callback_data="CHOICE")
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "ART":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Культурное наследие", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="ЭтноКонцепт", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Богатство финно-угорских народов", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Красный город", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Искусство Волго-Камского региона", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Ритмы России", callback_data="CHOICE")
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "LINGUISTICS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Особенности развития марийского языка и литературы", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Английский язык для международников", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Латинский язык без границ", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Древние языки и межкультурная коммуникация", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Лингвариум", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Мастерская перевода", callback_data="CHOICE")
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "MEDICS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Хирургия", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Анатомия человека", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Офтальмология", callback_data="CHOICE"),
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "PSYCHOLOGY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Лидерство и профессиональное саморазвитие", callback_data="CHOICE"),
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "MATHEMATICS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Наглядная геометрия", callback_data="CHOICE"),
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "JURISPRUDENCE":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Гражданское право", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Семейное право", callback_data="CHOICE"),
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
@bot.message_handler(commands=['start'])
def welcome(message):
    mainkeyboard = types.ReplyKeyboardMarkup()
    mainkeyboard.add(types.KeyboardButton("START"))
    bot.send_message(message.chat.id, "Здравствуйте! Телеграм-бот МарГУ – это карманный SСIENCE-навигатор. Он поможет разобраться с траекторией твоего научного развития. Для начала работы нажми START", reply_markup=mainkeyboard)

@bot.message_handler(content_types=['text'])
def directions(message):
    if message.text == 'START' or message.text == 'МЕНЮ С НАПРАВЛЕНИЯМИ':
        global mainkeyboard
        mainkeyboard = types.ReplyKeyboardMarkup()
        mainkeyboard.add(types.KeyboardButton("МЕНЮ С НАПРАВЛЕНИЯМИ"))
        bot.send_message(message.chat.id, "Выбери направление, которое тебя интересует", reply_markup=directionskeyboard)
    elif message.text == 'Присоединиться!':
        mainkeyboard = types.ReplyKeyboardMarkup()
        mainkeyboard.add(types.KeyboardButton("МЕНЮ С НАПРАВЛЕНИЯМИ"))
        bot.send_message(message.chat.id, "Свяжись с нами и подай заявку на почту nauka@marsu.ru", reply_markup=mainkeyboard)

bot.infinity_polling()