from aiogram import Bot, Dispatcher, types
from asyncio import run
import logging
from deep_translator import GoogleTranslator
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart
from keyboards import languages_button, bot_langauge
from dotenv import load_dotenv
import os

class Translate(StatesGroup):
    lang = State()
    trans = State()

bot = Bot(os.getenv("TOKEN"))
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
    msg = await message.answer("Tilni tanlang | select language | выберите язык", reply_markup=bot_langauge)
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
    elif data1.get("lang") == "🇺🇸 English - O'zbekcha 🇺🇿":
        text = GoogleTranslator(source='en', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇺🇿 O'zbekcha - Русский 🇷🇺":
        text = GoogleTranslator(source='uz', target='ru').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "🇷🇺 Русский - O'zbekcha 🇺🇿":
        text = GoogleTranslator(source='ru', target='uz').translate(message.text)
        await message.answer(text, reply_markup=languages_button)
    elif data1.get("lang") == "bilmayman":
        text = GoogleTranslator(source='auto', target='')
    await state.set_state(Translate.lang)

@dp.message()
async def sSs(message: types.Message):
    msg.delete()
    await message.answer(f"Salom <b>{message.from_user.full_name}</b>\nmatningiz qaysi tildaligini tanlang\nmatnni tarjima qilish uchun tilni tanlang", parse_mode='HTML', reply_markup=languages_button)

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
    run(start())