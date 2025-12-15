from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from googletrans import Translator

# Import keybords
from keyboards import base

tr = Translator()
start_router = Router()
changer_lang = "en"


# Matnlar
user_lang = {}
texts = {
    "uz": (
        "👋 Assalomu alaykum!\n\n"
        "Bu bot sizga quyidagilarni bajarishda yordam beradi:\n"
        "1️⃣ So‘zlarni tarjima qilish ✅\n"
        "2️⃣ Gaplarni tarjima qilish ✅\n"
        "3️⃣ Ko‘plab tillardan foydalanib tarjima qilish imkoniyati ✅\n\n"
        "🌐 Bot bilan ishlashni boshlash uchun qaysi tilni tanlaysiz? 👇"
    ),
    "ru": (
        "👋 Привет!\n\n"
        "Этот бот поможет вам:\n"
        "1️⃣ Перевод слов ✅\n"
        "2️⃣ Перевод предложений ✅\n"
        "3️⃣ Использовать много языков для перевода ✅\n\n"
        "🌐	Какой язык вы бы выбрали для работы с ботом? 👇"
    ),
    "en": (
        "👋 Hello!\n\n"
        "This bot can help you:\n"
        "1️⃣ Translate words ✅\n"
        "2️⃣ Translate sentences ✅\n"
        "3️⃣ Translate using multiple languages ✅\n\n"
        "🌐 Which language would you choose to work with the bot? 👇"
    ),
}


# START_FUNCTIONS
@start_router.message(Command("start"))
async def start_f(message: types.Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "Bu bot sizga quyidagilarni bajarishda yordam beradi:\n"
        "1️⃣ So‘zlarni tarjima qilish ✅\n"
        "2️⃣ Gaplarni tarjima qilish ✅\n"
        "3️⃣ Ko‘plab tillardan foydalanib tarjima qilish imkoniyati ✅\n\n"
        "🌐 Bot bilan ishlash uchun qaysi tilni tanlaysiz? 👇",
        reply_markup=base,
    )


@start_router.callback_query()
async def start_f(query: CallbackQuery):
    user_id = query.from_user.id
    if "-" in query.data:
        text, dest = query.data.split("-")
        user_lang[user_id] = dest
        # await query.message.answer(texts.get(dest, texts["en"]), reply_markup=base)
        await query.message.delete()

    await query.message.answer(
        f"Tanlangan tillar: {query.data.upper()}\nMatnni kiriting 👇"
    )


@start_router.message()
async def tr_s(message: types.Message):
    user_id = message.from_user.id
    lang = user_lang.get(user_id, "en")
    text = message.text

    translated_text = tr.translate(text=text, dest=lang).text
    await message.reply(translated_text)
