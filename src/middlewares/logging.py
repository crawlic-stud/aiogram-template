import logging
import datetime
import pytz

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


def get_moscow_dt():
    return datetime.datetime.now(pytz.timezone('Europe/Moscow'))


class BasicLogging(BaseMiddleware):
    def __init__(self, path="logs.log"):
        self.path = path
        super().__init__()

    async def on_process_update(self, update: types.Update, data: dict):
        message = update.message
        query = update.callback_query

        if message is not None:
            logging.info(
                f" [{get_moscow_dt()}] User {message.from_id} sent a message '{message.text}'")
        if query is not None:
            logging.info(
                f" [{get_moscow_dt()}] User {query.from_user.id} sent a query with data='{query.data}'")

    async def on_pre_process_error(self, update: types.Update, error, data: dict):
        logging.error(
            f"Process failed. {error=}")
