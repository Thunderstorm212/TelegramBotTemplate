import asyncio
from aiogram import types, Router, F, BaseMiddleware
from aiogram.filters import CommandStart, BaseFilter, Filter, Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import conf
from core.ui import ui_text
from core.keyboards import Buttons
import db
from core import log

router = Router()


class SIMPLE_STATE(StatesGroup):
    MAIN = State()


class FilterText(Filter):
    def __init__(self, filtered_text):
        self.filtered_text = filtered_text

    async def __call__(self, message: types.Message):
        return message.text == self.filtered_text


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    # TODO: change markup
    markup = types.ReplyKeyboardMarkup(keyboard=Buttons.confirmBTN, resize_keyboard=True)
    await message.answer(text=ui_text["answer"].answer_cancel, reply_markup=markup)


@router.message(CommandStart())
async def start_command(message: types.Message):
    log(message, message.from_user.full_name, message.from_user.id)
    await message.answer(text=ui_text["answer"].answer_hello)
