from aiogram.dispatcher.filters.state import StatesGroup

from models.custom_state import CustomState


class State(StatesGroup):
    choose_what = CustomState(
        question="q",
        widgets=[

        ]
    )
