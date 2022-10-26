from aiogram_dialog.exceptions import UnknownIntent
from aiogram import types
from aiogram.utils.exceptions import BadRequest

from config import dp


@dp.errors_handler(exception=UnknownIntent)
async def intent_error(update: types.Update, error):
    message = update.callback_query.message
    error_text = f"К сожалению, эта сессия истекла"
    try:
        await message.edit_text(error_text, reply_markup=None)
    except BadRequest:
        await message.delete()
        await message.answer(error_text)
    return True
