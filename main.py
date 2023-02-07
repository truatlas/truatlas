import telebot
from telebot import types
from TOKEN import TOKEN
import csv
import datetime

bot = telebot.TeleBot(TOKEN)

directionskeyboard = types.InlineKeyboardMarkup(row_width=1)
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
)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    # with open("data.csv", "a") as file:
    #     writter = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     writter.writerow([str(datetime.datetime.now()), call.from_user.first_name, call.from_user.last_name, str(call.message.chat.id), call.data])
    bot.answer_callback_query(callback_query_id=call.id)
    ListOfLections = types.InlineKeyboardMarkup(row_width=1)
    if call.data == "BACK":
        global mainkeyboard
        mainkeyboard = types.ReplyKeyboardMarkup()
        mainkeyboard.add(types.KeyboardButton("МЕНЮ С НАПРАВЛЕНИЯМИ"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбери направление, которое тебя интересует", reply_markup=directionskeyboard)
    elif call.data == "CHOICE":
        mainkeyboard = types.ReplyKeyboardMarkup()
        mainkeyboard.add(
            types.KeyboardButton("Присоединиться!"),
            types.KeyboardButton("МЕНЮ С НАПРАВЛЕНИЯМИ"),
            row_width=1)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Хороший выбор! Мы ждем тебя на кружке!", reply_markup=mainkeyboard)
    elif call.data == "BIOENGINEER":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Биоинженерия", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Попова Ольга Владимировна, канд. биол. наук, доцент;\nЕ-mail: Yasminka1@mail.ru\nКружок поможет создать у слушателей целостное представление о современной биоинженерии и познакомить с основами этой интересной науки.", reply_markup=ListOfLections)
    elif call.data == "AVICENNA":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Авиценна", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Ведерников Александр Андреевич, канд. биол. наук, доцент;\nЕ-mail: medfac@marsu.ru\nКружок познакомит с лекарственными средствами и физиологически активными веществами и их действием на организм.", reply_markup=ListOfLections)
    elif call.data == 'BIOLOGY':
        ListOfLections.add(
            types.InlineKeyboardButton(text="Биоинженерия", callback_data="BIOENGINEER"),
            types.InlineKeyboardButton(text="Авиценна", callback_data="AVICENNA")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете кружок, о котором хотите узнать подробнее:", reply_markup=ListOfLections)
    elif call.data == "ELECTROTECH":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Электротех", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Сидорова Вера Тагировна, канд. физ.-мат. наук; доцент;\nОрлов Александр Игоревич, канд. техн. наук, доцент;\nГарипов Ильсур Халилевич, канд. техн. наук, доцент;\nЕ-mail: eef@marsu.ru\nКружок познакомит с первичными знаниями и навыками в области электротехники (эволюцией электроинструментов и изучением современного оборудования)", reply_markup=ListOfLections)
    elif call.data == "SPEKTRUM":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Spektrum", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Каширин Николай Владимирович, канд. хим. наук, доцент\nЕ-mail: kaffiz@marsu.ru\nЦентр поможет в разработке новых приборов и аппаратных комплексов для научно-исследовательских и учебных лабораторий вузов, школ и др. учебных заведений", reply_markup=ListOfLections)
    elif call.data == "TECHOPARK":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Технопарк «Профи»", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Коротков Сергей Геннадьевич, канд. пед. наук, доцент\nЕ-mail: korotkov.sg@marsu.ru\nБюро даст возможность обучающимся познакомиться с новой техникой, расчетными методиками и системами проектирования, поучаствовать в реальной работе по созданию оборудования", reply_markup=ListOfLections)
    elif call.data == "PHYSICS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Электротех", callback_data="ELECTROTECH"),
            types.InlineKeyboardButton(text="«Spektrum», молодёжный научно-инновационный конструкторский центр", callback_data="SPEKTRUM"),
            types.InlineKeyboardButton(text="«Технопарк «Профи», студенческое конструкторское бюро", callback_data="TECHOPARK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете кружок, о котором хотите узнать подробнее:", reply_markup=ListOfLections)
    elif call.data == "HPDIRECTIONS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Здоровые перспективы", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Бурова Наталья Олеговна, канд. техн. наук, доцент;\nКислицына Надежда Ананьевна, преподаватель \nЕ-mail: thppr@marsu.ru\nКружок поможет узнать, что такое сбалансированное питание и чем оно полезно. ", reply_markup=ListOfLections)
    elif call.data == "SPORT":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Будь на спорте!", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Лоскутова Элеонора Анатольевна, канд. психол. наук, доцент\nЕ-mail: ffk@marsu.ru\nКружок включает в себя знания, установки, личностные ориентиры и нормы поведения, обеспечивающие сохранение и укрепление физического и психического здоровья.", reply_markup=ListOfLections)
    elif call.data == "HEALTHY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Здоровые перспективы", callback_data="HPDIRECTIONS"),
            types.InlineKeyboardButton(text="Будь на спорте!", callback_data="SPORT")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберете кружок, о котором хотите узнать подробнее:", reply_markup=ListOfLections)
    elif call.data == "CULTURE":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Культурное наследие", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Шкалина Галина Евгеньевна, д-р искусствоведения, профессор\nЕ-mail: gshkalina@mail.ru\nНа заседаниях кружка можно познакомиться с памятниками культурного наследия, узнать много нового и интересного о Республике Марий Эл, научиться навыкам научной работы и публичным выступлениям.", reply_markup=ListOfLections)
    elif call.data == "ETNO":
        ListOfLections.add(
            types.InlineKeyboardButton(text="ЭтноКонцепт", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Чузаев Родион Иванович, канд. ист. наук, доцент \nЕ-mail: chuzaev.ri@marsu.ru\nНа заседаниях кружка можно познакомиться с менталитетом народа мари, отражающего его духовность.",reply_markup=ListOfLections)
    elif call.data == "RICHOFPEOPLE":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Богатство финно-угорских народов", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Гусева Элина Витальевна, канд. филол. наук, доцент\nЕ-mail: guseva_elina@mail.ru\nКружок познакомит с ценностями и богатствами финно-угорского народа.",reply_markup=ListOfLections)
    elif call.data == "REDCITY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Красный город", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Спесивцева Надежда Викторовна, канд. пед. наук, доцент\nЕ-mail: skt@marsu.ru\nКружок даст возможность познакомиться с историей, достопримечательностями и красотой города Йошкар-Ола.",reply_markup=ListOfLections)
    elif call.data == "ARTOFVOLGA":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Искусство Волго-Камского региона", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Мамонтова Марина Сергеевна, канд. пед. наук, доцент\nЕ-mail: mamontova-ms@mail.ru\nКружок познакомит со всеми разновидностями художественного творчества конкретного региона ",reply_markup=ListOfLections)
    elif call.data == "RUSSIANRHYTHM":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Ритмы России", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Кадыкова Галина Николаевна, канд. ист. наук, доцент\nМакарова Нина Альбертовна, канд. ист. наук, доцент\nЕ-mail: Kadukova_galina@mail.ru\nКружок приобщает к музыкальному искусству через танец, как самым доступным для всех, активным видом музыкальной деятельности.",reply_markup=ListOfLections)
    elif call.data == "ART":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Культурное наследие", callback_data="CULTURE"),
            types.InlineKeyboardButton(text="ЭтноКонцепт", callback_data="ETNO"),
            types.InlineKeyboardButton(text="Богатство финно-угорских народов", callback_data="RICHOFPEOPLE"),
            types.InlineKeyboardButton(text="Красный город", callback_data="REDCITY"),
            types.InlineKeyboardButton(text="Искусство Волго-Камского региона", callback_data="ARTOFVOLGA"),
            types.InlineKeyboardButton(text="Ритмы России", callback_data="RUSSIANRHYTHM")
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "SPECIALLANGUAGE":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Особенности развития марийского языка и литературы", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Матросова Лидия Сидоровна, канд. филол. наук, доцент\nЕ-mail: lidmat@rambler.ru\nКружок дает возможность изучения основ марийского языка на базовом и продвинутом уровне, а также соприкоснуться с повседневной культурой народа мари в рамках экскурсионной программы.", reply_markup=ListOfLections)
    elif call.data == "ENGLISHFORRELATIONS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Английский язык для международников", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Филатова Анна Витальевна, канд. пед. наук, доцент\nЕ-mail: kmk687911@yandex.ru\nКружок помогает усовершенствовать знания, умения и навыки иностранного языки", reply_markup=ListOfLections)
    elif call.data == "LATINLANGUAGE":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Латинский язык без границ", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Хабибуллина Флера Яхиятовна, канд. пед. наук, доцент\nЕ-mail: khflora@yandex.ru\nКружок помогает усовершенствовать знания, умения и навыки латинского языка ", reply_markup=ListOfLections)
    elif call.data == "ANCIENTLANGUAGES":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Древние языки и межкультурная коммуникация", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель:Иванова Ираида Геннадьевна, канд. филол. наук, доцент\nЕ-mail: kaf_fundmed@mail.ru\nКружок познакомит с многообразием культур, их особенностью и поможет сформировать межкультурную компетентность.", reply_markup=ListOfLections)
    elif call.data == "LINGVARIUM":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Лингвариум", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Балышева Ксения Александровна, канд. филол. наук, доцент \nЕ-mail: qsuaka@mail.ru\nКружок помогает в создание продуктивной и принципиально новой научной среды для студентов и школьников на базе изучения языков и методики их преподавания.", reply_markup=ListOfLections)
    elif call.data == "TRANSLATIONWORKSHOP":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Мастерская перевода", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Флигинских Екатерина Евгеньевна, ст. преподаватель\nЕ-mail: katenasmile@mail.ru\nКружок помогает в освоении разговорного английского и формировании навыков коммуникации, изучении новых подходов в таких областях как теория и практика перевода, сравнительная и сопоставительная лингвистика.",reply_markup=ListOfLections)
    elif call.data == "LINGUISTICS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Особенности развития марийского языка и литературы", callback_data="SPECIALLANGUAGE"),
            types.InlineKeyboardButton(text="Английский язык для международников", callback_data="ENGLISHFORRELATIONS"),
            types.InlineKeyboardButton(text="Латинский язык без границ", callback_data="LATINLANGUAGE"),
            types.InlineKeyboardButton(text="Древние языки и межкультурная коммуникация", callback_data="ANCIENTLANGUAGES"),
            types.InlineKeyboardButton(text="Лингвариум", callback_data="LINGVARIUM"),
            types.InlineKeyboardButton(text="Мастерская перевода", callback_data="TRANSLATIONWORKSHOP")
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "SURGERY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Хирургия", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Шорников Александр Иванович, к.мед.н., доцент\nЕ-mail: drsorn@mail.ru\nКружок помогает  узнать острые и хронические заболевания, которые можно вылечить при помощи оперативного (хирургического) метода.", reply_markup=ListOfLections)
    elif call.data == "ANATOMY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Анатомия человека", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Ведерников Александр Андреевич, канд. биол. наук, доцент\nЕ-mail: medfac@marsu.ru\nКружок дает знания о форме и строении, происхождении и развитии человеческого организма, внешних формах тела человека и его частей, отдельных органов, их конструкций, микроскопического строения; основных этапов развития человека в процессе эволюции, особенностей строения органов в разные возрастные периоды.", reply_markup=ListOfLections)
    elif call.data == "OPHTHALMOLOGY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Офтальмология", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Акберова Гельнас Эльмасовна, канд. мед. наук, доцент, врач-офтальмолог\nЕ-mail: kafedravb1@mail.ru\nКружок знакомит с анатомией глаза, физиологией его болезней и лечением", reply_markup=ListOfLections)
    elif call.data == "MEDICS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Хирургия", callback_data="SURGERY"),
            types.InlineKeyboardButton(text="Анатомия человека", callback_data="ANATOMY"),
            types.InlineKeyboardButton(text="Офтальмология", callback_data="OPHTHALMOLOGY"),
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "LEADER":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Лидерство и профессиональное саморазвитие", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Акберова Гельнас Эльмасовна, канд. мед. наук, доцент, врач-офтальмолог\nЕ-mail: kafedravb1@mail.ru\nКружок знакомит с анатомией глаза, физиологией его болезней и лечением", reply_markup=ListOfLections)
    elif call.data == "PSYCHOLOGY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Лидерство и профессиональное саморазвитие", callback_data="LEADER"),
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "GEOMETRY":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Наглядная геометрия", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Домрачева Светлана Алексеевна, канд. пед. наук, доцент\nЕ-mail: domrachev70@mail.ru\nКружок помогает сформировать такие качества, как лидерство, саморазвитие, получить первые навыки публичного выступления",reply_markup=ListOfLections)
    elif call.data == "MATHEMATICS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Наглядная геометрия", callback_data="GEOMETRY"),
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
    elif call.data == "SOCRIGHTS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Гражданское право", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Кузьмина Анна Вячеславовна, к.юрид.н., доцент;\nБакулин Андрей Фдорович, ст. преподаватель\nЕ-mail: tsyplenkova@mail.ru\nКружок помогает более подробно изучить не только классическое наследие российской цивилистической науки, но и современное состояние отдельных гражданско-правовых институтов.", reply_markup=ListOfLections)
    elif call.data == "HOMERIGHTS":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Семейное право", callback_data=" "),
            types.InlineKeyboardButton(text="Продолжить", callback_data="CHOICE"),
            types.InlineKeyboardButton(text="Назад", callback_data="BACK")
        )
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Руководитель: Кондратенко Зарина Камилевна, к.юрид.н., доцент\nЕ-mail: mati07@rambler.ru\nКружок погружает в науку семейного права, приобщает к семейно-правовым ценностям, освоению современных трендов развития правового регулирования семейных отношений и знакомству с выдающимися представителями семейно-правовой науки.",reply_markup=ListOfLections)
    elif call.data == "JURISPRUDENCE":
        ListOfLections.add(
            types.InlineKeyboardButton(text="Гражданское право", callback_data="SOCRIGHTS"),
            types.InlineKeyboardButton(text="Семейное право", callback_data="HOMERIGHTS"),
        )
        bot.send_message(call.message.chat.id, "Список кружков", reply_markup=ListOfLections)
@bot.message_handler(commands=['start'])
def welcome(message):
    # with open("data.csv", "a") as file:
    #     writter = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     writter.writerow([str(datetime.datetime.now()) + ' ' + message.from_user.first_name + ' ' + message.from_user.last_name + ' ' + str(message.chat.id) + ' ' + message.text])
    mainkeyboard = types.ReplyKeyboardMarkup()
    mainkeyboard.add(types.KeyboardButton("START"))
    bot.send_message(message.chat.id, "Здравствуйте! Телеграм-бот МарГУ – это карманный SСIENCE-навигатор. Он поможет разобраться с траекторией твоего научного развития. Для начала работы нажми START", reply_markup=mainkeyboard)

@bot.message_handler(content_types=['text'])
def directions(message):
    # with open("data.csv", "a") as file:
    #     writter = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     writter.writerow([str(datetime.datetime.now()) + ' ' + message.from_user.first_name + ' ' + message.from_user.last_name + ' ' + str(message.chat.id) + ' ' + message.text])
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