from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram_dialog import DialogRegistry

import logging

from middlewares.logging import BasicLogging
from utils.database import Database


TEST_TOKEN = ""
PROD_TOKEN = ""
API_TOKEN = TEST_TOKEN
DB_PASSWORD = ""
DB_URL = f""

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(BasicLogging())

registry = DialogRegistry(dp)

db = Database(DB_URL, db_name="test", collection_name="data")
