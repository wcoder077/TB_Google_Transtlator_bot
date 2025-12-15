from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

base = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿UZ ➜ RU🇷🇺", callback_data="uz-ru"),
            InlineKeyboardButton(text="🇺🇿UZ ➜ EN🇺🇸", callback_data="uz-en"),
        ],
        [
            InlineKeyboardButton(text="🇺🇸EN ➜ UZ🇺🇿", callback_data="en-uz"),
            InlineKeyboardButton(text="🇺🇸EN ➜ RU🇷🇺", callback_data="en-ru"),
        ],
        [
            InlineKeyboardButton(text="🇷🇺RU ➜ EN🇺🇸", callback_data="ru-en"),
            InlineKeyboardButton(text="🇷🇺RU ➜ UZ🇺🇿", callback_data="ru-uz"),
        ],
    ]
)
