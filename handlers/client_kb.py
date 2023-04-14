from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
help_button = KeyboardButton("/help")

share_contact = KeyboardButton("Share contact", request_contact=True)
share_location = KeyboardButton("Share location", request_location=True)

start_markup.add(
    start_button, quiz_button, help_button,
    share_contact, share_location
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton("ОТМЕНА"),
)


gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton("МУЖЧИНА"),
    KeyboardButton("ЖЕНЩИНА"),
    KeyboardButton("НЕЗНАЮ"),
    KeyboardButton("ОТМЕНА"),
)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton("ДА"),
    KeyboardButton("ЗАНОВО"),
    KeyboardButton("ОТМЕНА"),
)