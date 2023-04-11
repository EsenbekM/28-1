from aiogram import Dispatcher, types
from config import bot, dp


# @dp.message_handler()
# DRY - Don't Repeat Yourself
async def filter_bad_word(message: types.Message):
    bad_words = ['html', 'java', "дурак", "жинди"]
    username = f"@{message.from_user.username}" \
        if message.from_user.username else message.from_user.full_name
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            await message.answer(
                f"Не матерись {username}!\n"
                f"Сам ты {word}!"
            )

    if message.text.startswith('.'):
        await message.pin()
        # await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == "dice":
        a = await message.answer_dice(emoji="🎲")
        # await bot.send_dice()
        # print(a.dice.value)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(filter_bad_word)
