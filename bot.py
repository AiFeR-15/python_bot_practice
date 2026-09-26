import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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

# Ця функція зловить повідомлення, коли ти натиснеш "Start" у боті
@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    # message.from_user.first_name дістає твоє ім'я прямо з налаштувань Telegram
    await message.answer(
        f"Привіт, {message.from_user.first_name}! Я живий, і ми починаємо.",
        reply_markup=main_menu)

# Головна функція запуску
async def main():
    print("Бот успішно запущено. Чекаю на повідомлення...")
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())