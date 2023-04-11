from aiogram import Dispatcher, types
from config import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    photo = open("media/cat.jpg", "rb")
    # await bot.send_photo()
    await message.answer_photo(photo, caption="Че нада?")
    # await bot.send_message(message.from_user.id, f"Привет хозяин {message.from_user.full_name}!")
    # await message.answer("This is an answer method!")
    # await message.reply("This is a reply method!")


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


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(help_command, commands=['help'])
