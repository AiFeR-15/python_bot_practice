import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()
# Встав сюди свій токен у лапках
TOKEN = os.getenv("BOT_TOKEN")

# Ініціалізуємо бота та диспетчер (маршрутизатор повідомлень)
bot = Bot(token=TOKEN)
dp = Dispatcher()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        # Перший внутрішній список - це верхній рядок кнопок
        [KeyboardButton(text="🍕 Меню")],
        
        # Другий внутрішній список - це нижній рядок
        [KeyboardButton(text="🛒 Мій кошик"), KeyboardButton(text="👤 Профіль")]

    ],
    resize_keyboard=True
)

my_github_btn = InlineKeyboardButton(text = "🔗 Мій GitHub", url="https://github.com/AiFeR-15")
my_portfolio_btn = InlineKeyboardButton(text = "Мій портфоліо", url="https://www.google.com")
your_bonus= InlineKeyboardButton(text="🎁 Отримати бонус", callback_data="get_bonus")

inline_menu=InlineKeyboardMarkup(
    inline_keyboard=[[my_github_btn ,my_portfolio_btn],
    [your_bonus]]
)

# Ця функція зловить повідомлення, коли ти натиснеш "Start" у боті
@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    # message.from_user.first_name дістає твоє ім'я прямо з налаштувань Telegram
    await message.answer(
        f"Привіт, {message.from_user.first_name}! Я живий, і ми починаємо.",
        reply_markup=main_menu)

@dp.message(F.text == "🍕 Меню")
async def menu_handler(message: types.Message):
    await message.answer("Ось наше меню: 1. Піца, 2. Сік, 3. Печиво. Що бажаєте додати?")

@dp.message(F.text == "🛒 Мій кошик")
async def shopping_cart(message: types.Message):
    await message.answer("Поки нічого немає, ми над цим працюємо!")

@dp.message(F.text == "👤 Профіль")
async def profile(message: types.Message):
    await message.answer(f"Логін: {message.from_user.first_name}",
    reply_markup=inline_menu)

@dp.callback_query(F.data == "get_bonus")
async def bonus_handler(callback: types.CallbackQuery):
    await callback.message.answer("Твій бонус: 100 балів!")

# Головна функція запуску
async def main():
    print("Бот успішно запущено. Чекаю на повідомлення...")
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())