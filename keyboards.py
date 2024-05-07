from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

languages_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 O'zbekcha - English 🇺🇸"), KeyboardButton(text="🇺🇸 English - O'zbekcha 🇺🇿")],
        [KeyboardButton(text="🇺🇿 O'zbekcha - Русский 🇷🇺"), KeyboardButton(text="🇷🇺 Русский - O'zbekcha 🇺🇿")],
    ],
    resize_keyboard=True
)
# [KeyboardButton(text="bilmayman")]