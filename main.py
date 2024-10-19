from aiogram import Bot, Dispatcher, types
from asyncio import run
import logging
from deep_translator import GoogleTranslator
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart
from keyboards import languages_button, ReplyKeyboardRemove
from dotenv import load_dotenv
import os
from gtts import gTTS

class Translate(StatesGroup):
    lang = State()
    trans = State()

load_dotenv()

bot = Bot(str(os.getenv("TOKEN")))
dp = Dispatcher()

@dp.message(CommandStart())
async def signup(message: types.Message, state: FSMContext):
    global msg
    id = message.from_user.id
    with open('database.txt', 'r') as file:
        read = file.read()
        if str(id) not in read:
            with open('database.txt', 'a') as file:
                file.write(f"{id}\n")
        else:
            pass
    await message.answer(f"Salom <b>{message.from_user.full_name}</b>\nmatningiz qaysi tildaligini tanlang\nmatnni tarjima qilish uchun tilni tanlang", parse_mode='HTML', reply_markup=languages_button)
    await state.set_state(Translate.lang)

@dp.message(Translate.lang)
async def TranslateLang(message: types.Message, state: FSMContext):
    await state.update_data(lang=message.text)
    await message.answer("tarjima qilmoqchi bo'lgan matningizni kiriting")
    await state.set_state(Translate.trans)

@dp.message(Translate.trans)
async def translate(message: types.Message, state: FSMContext):
    data1 = await state.get_data()
    if data1.get("lang") == "🇺🇿 O'zbekcha - English 🇺🇸":
        text = GoogleTranslator(source='uz', target='en').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
        gTTS(text=text, lang='en').save('audio.mp3')
        await message.answer_audio(audio=types.FSInputFile("audio.mp3"))
    elif data1.get("lang") == "🇺🇸 English - O'zbekcha 🇺🇿":
        text = GoogleTranslator(source='en', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇺🇿 O'zbekcha - Русский 🇷🇺":
        text = GoogleTranslator(source='uz', target='ru').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
        gTTS(text=text, lang='ru').save('audio.mp3')
        await message.answer_audio(audio=types.FSInputFile("audio.mp3"))
    elif data1.get("lang") == "🇷🇺 Русский - O'zbekcha 🇺🇿":
        text = GoogleTranslator(source='ru', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇺🇿 O'zbekcha - Koreyscha 🇰🇷":
        text = GoogleTranslator(source='uz', target='ko').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
        gTTS(text=text, lang='ko').save('audio.mp3')
        await message.answer_audio(audio=types.FSInputFile("audio.mp3"))
    elif data1.get("lang") == "🇰🇷 한국인(korean) -  우즈벡어(uzbek) 🇺🇿":
        text = GoogleTranslator(source='ko', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇺🇿 O'zbekcha - Turkcha 🇹🇷":
        text = GoogleTranslator(source='uz', target='tr').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
        gTTS(text=text, lang='tr').save('audio.mp3')
        await message.answer_audio(audio=types.FSInputFile("audio.mp3"))
    elif data1.get("lang") == "🇹🇷 Türkçe(turkish) - Özbekçe(uzbek) 🇺🇿":
        text = GoogleTranslator(source='tr', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇺🇿 O'zbekcha - Nemischa 🇩🇪":
        text = GoogleTranslator(source='uz', target='de').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
        gTTS(text=text, lang='de').save('audio.mp3')
        await message.answer_audio(audio=types.FSInputFile("audio.mp3"))
    elif data1.get("lang") == "🇩🇪 Deutsch(german) - Usbekisch 🇺🇿":
        text = GoogleTranslator(source='de', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇺🇿 O'zbekcha - Ispancha 🇪🇸":
        text = GoogleTranslator(source='uz', target='es').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
        gTTS(text=text, lang='es').save('audio.mp3')
        await message.answer_audio(audio=types.FSInputFile("audio.mp3"))
    elif data1.get("lang") == "🇪🇸 Española(spanish) - Uzbeko 🇺🇿":
        text = GoogleTranslator(source='es', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    await state.set_state(Translate.lang)
    try:
        os.remove("audio.mp3")
    except:
        pass

@dp.startup()
async def startup(bot: Bot):
    try:
        await bot.send_message(chat_id=5230484991, text="Bot ishga tushdi❗")
    except:
        pass

@dp.shutdown()
async def shutdown(bot: Bot):
    try:
        await bot.send_message(chat_id=5230484991, text="Bot to'xtadi❗")
    except:
        pass

async def start():
    # session = AiohttpSession(proxy="http://proxy.server:3128/")
    # , session=session
    await bot.set_my_commands([
        types.BotCommand(command='/start', description="botni ishga tushurish")
    ])
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        run(start())
    except KeyboardInterrupt:
        print("Exitting...")