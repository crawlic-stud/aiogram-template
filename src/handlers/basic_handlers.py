from config import dp
from aiogram.types import Message


@dp.message_handler(commands=["start"])
async def send_start(message: Message):
    await message.answer(
        "start",
        reply_markup=None
    )


@dp.message_handler(commands=["help"])
async def send_start(message):
    await message.answer(
        "start",
        reply_markup=None
    )
