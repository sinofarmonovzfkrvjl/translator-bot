from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

languages_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 O'zbekcha - English 🇺🇸"), KeyboardButton(text="🇺🇸 English - O'zbekcha 🇺🇿")],
        [KeyboardButton(text="🇺🇿 O'zbekcha - Русский 🇷🇺"), KeyboardButton(text="🇷🇺 Русский - O'zbekcha 🇺🇿")],
        [KeyboardButton(text="🇺🇿 O'zbekcha - Koreyscha 🇰🇷"), KeyboardButton(text="🇰🇷 한국인(korean) -  우즈벡어(uzbek) 🇺🇿")],
        [KeyboardButton(text="🇺🇿 O'zbekcha - Turkcha 🇹🇷"), KeyboardButton(text="🇹🇷 Türkçe(turkish) - Özbekçe(uzbek) 🇺🇿")],
        [KeyboardButton(text="🇺🇿 O'zbekcha - Nemischa 🇩🇪"), KeyboardButton(text="🇩🇪 Deutsch(german) - Usbekisch 🇺🇿")],
        [KeyboardButton(text="🇺🇿 O'zbekcha - Ispancha 🇪🇸"), KeyboardButton(text="🇪🇸 Española(spanish) - Uzbeko 🇺🇿")]
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
