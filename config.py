import openai
from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMINS = (5367214519,)

openai.api_key = config("OPENAI_API_KEY")

