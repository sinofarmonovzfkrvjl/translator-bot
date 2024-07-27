from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

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
        [InlineKeyboardButton(text="O'zbekcha 🇺🇿", callback_data='uz')],
        [InlineKeyboardButton(text="English 🇺🇸", callback_data='en')],
        [InlineKeyboardButton(text="Русский 🇷🇺", callback_data='ru')]
    ]
)
# [KeyboardButton(text="bilmayman")]