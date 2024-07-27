from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

languages_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 O'zbekcha - English 🇺🇸"), KeyboardButton(text="🇺🇸 English - O'zbekcha 🇺🇿")],
        [KeyboardButton(text="🇺🇿 O'zbekcha - Русский 🇷🇺"), KeyboardButton(text="🇷🇺 Русский - O'zbekcha 🇺🇿")],
        [KeyboardButton(text="")]
    ],
    resize_keyboard=True
)

bot_langauge = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="O'zbekcha 🇺🇿")],
        [InlineKeyboardButton(text="English 🇺🇸")],
        [InlineKeyboardButton(text="Русский 🇷🇺")]
    ]
)
# [KeyboardButton(text="bilmayman")]