from datetime import datetime, timedelta

from aiogram import Dispatcher, types
from config import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .client_kb import start_markup
from database.bot_db import sql_command_random, sql_command_all_users, sql_command_insert_user
from .utils import get_ids_from_users
from parser.news import parser


async def start_command(message: types.Message):
    users = await sql_command_all_users()
    ids = get_ids_from_users(users)
    if message.from_user.id not in ids:
        await sql_command_insert_user(
            message.from_user.id,
            message.from_user.username,
            message.from_user.full_name
        )

    photo = open("media/cat.jpg", "rb")
    await message.answer_photo(photo, caption="Че нада?", reply_markup=start_markup)


async def help_command(message: types.Message):
    await message.reply("Сам разбирайся!")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="quiz_1_button")
    markup.add(button_1)

    question = "By whom invented Python?"
    answer = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Иди учись",
        open_period=10,
        reply_markup=markup
    )
    # await message.answer_poll()


async def get_random_anketa(message: types.Message):
    random_user = await sql_command_random()
    info = f"{random_user[3]} {random_user[4]} " \
           f"{random_user[5]} {random_user[6]}"
    info = info + f"\n\n@{random_user[2]}" if random_user[2] else info
    await message.answer_photo(
        random_user[-1],
        caption=info
    )


async def get_news_date(message: types.Message):
    await message.delete()
    current_date: datetime = datetime.now()
    date_list = [current_date - timedelta(days=i) for i in range(6)]
    markup = InlineKeyboardMarkup(row_width=1)
    for date in date_list:
        markup.add(
            InlineKeyboardButton(
                date.strftime("%d.%m.%Y"),
                callback_data=f"date {date.strftime('%Y-%m-%d')}"
            )
        )
    await message.answer("Выберите дату: ", reply_markup=markup)


async def send_news(call: types.CallbackQuery):
    date = call.data.replace("date ", "")
    news = parser(year=date[:4], month=date[5:7], day=date[-2:])
    for i in news[:6]:
        await call.message.answer_photo(
            photo=i['photo'],
            caption=f"{i['url']}\n"
                    f"{i['title']} {i['time']}\n"
        )
        # await call.message.answer(
        #     f"{i['url']}\n"
        #     f"{i['title']} {i['time']}\n"
        # )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(help_command, commands=['help'])
    dp.register_message_handler(get_random_anketa, commands=['get'])
    dp.register_message_handler(get_news_date, commands=['news'])
    dp.register_callback_query_handler(
        send_news,
        lambda call: call.data and call.data.startswith("date ")
    )
