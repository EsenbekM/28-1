from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой хозяин!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            # await bot.ban_chat_member()
            await message.answer(
                f"{message.from_user.first_name} братан кикнул "
                f"{message.reply_to_message.from_user.full_name}"
            )
    else:
        await message.answer("Пиши в группе!")


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой хозяин!")
    else:
        users = await sql_command_all()
        for user in users:
            info = f"{user[3]} {user[4]} " \
                   f"{user[5]} {user[6]}"
            info = info + f"\n\n@{user[2]}" if user[2] else info
            await message.answer_photo(
                user[-1],
                caption=info,
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(
                        f"DELETE {user[3]}",
                        callback_data=f"delete {user[0]}"
                    )
                )
            )


async def complete_delete(call: types.CallbackQuery):
    user_id = call.data.replace("delete ", "")
    await sql_command_delete(user_id)
    await call.answer(text=f"Удалена запись с айди {user_id}",
                      show_alert=True)
    await call.message.delete()
    # await bot.delete_message(call.from_user.id, call.message.id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(delete_data, commands=['delete'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )
