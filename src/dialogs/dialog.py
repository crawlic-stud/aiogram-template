from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from states.state import State
from . import data


DIALOG = Dialog(
    *[Window(
        Const(state.question),
        *state.widgets,
        state=state,
        getter=data.get,
    ) for state in State.all_states]
)
