import openai
from aiogram import Dispatcher, types
from config import bot, dp


# @dp.message_handler()
# DRY - Don't Repeat Yourself
async def filter_bad_word(message: types.Message):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    await message.answer(
        response["choices"][0]['text']
    )

    # bad_words = ['html', 'java', "дурак", "жинди"]
    # username = f"@{message.from_user.username}" \
    #     if message.from_user.username else message.from_user.full_name
    # for word in bad_words:
    #     if word in message.text.lower().replace(" ", ""):
    #         await message.answer(
    #             f"Не матерись {username}!\n"
    #             f"Сам ты {word}!"
    #         )
    #
    # if message.text.startswith('.'):
    #     await message.pin()
    #     # await bot.pin_chat_message(message.chat.id, message.message_id)
    #
    # if message.text == "dice":
    #     player = await message.answer_dice(emoji="🎲")
    #     # bot = await message.answer_dice(emoji="🎲")
    #     # await bot.send_dice()
    #     # if player.dice.value > bot.dice.value:
    #     #     await message.answer()


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(filter_bad_word)
