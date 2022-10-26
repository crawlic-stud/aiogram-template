from aiogram.dispatcher.filters.state import State
from aiogram_dialog.widgets.text import Const


class CustomState(State):
    def __init__(self, question="", note="", options=None,
                 answer="", name="", widgets=None):

        super().__init__()

        self.question = question
        self.answer = answer
        self.name = name
        self.note = note

        if options is None:
            options = []
        self.options = options

        if widgets is None:
            widgets = [Const("")]
        self.widgets = widgets

    def get_question(self, answer=None):
        question_filled = f"<b>{self.question}</b>"
        question_unfilled = f"<b>{self.question}</b>\n<i>{self.note}</i>"

        return question_filled if answer else question_unfilled

