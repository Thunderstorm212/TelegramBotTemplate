from aiogram import types
from core.ui import ui_text
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Buttons:
    confirmBTN = [
        [
            types.KeyboardButton(text=ui_text["btn"].btn_dont_confirm),
            types.KeyboardButton(text=ui_text["btn"].btn_confirm),
        ]
    ]

