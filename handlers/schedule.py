import datetime

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger

from database.bot_db import sql_command_all_users
from config import bot


async def go_to_sleep(bot: Bot):
    users = await sql_command_all_users()
    for user in users:
        await bot.send_message(user[0], f"Салалукем {user[-1]}\nПора спать!")


async def set_sheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")

    scheduler.add_job(
        go_to_sleep,
        kwargs={"bot": bot},
        trigger=CronTrigger(
            day_of_week=0,
            hour=21,
            minute=47,
            start_date=datetime.datetime.now()
        )
    )

    scheduler.start()
