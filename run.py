from dotenv import load_dotenv

from bot import start_bot

import os



load_dotenv()  # Загружает переменные окружения из файла .env



# После этого должна быть проверка переменной TOKEN

token = os.getenv("TOKEN")

if token is None:

    raise ValueError("Токен не задан или не загружен из .env")



# Использование токена

from aiogram import Bot, Dispatcher



def start_bot():

    bot = Bot(token=token, parse_mode='HTML')

    dp = Dispatcher(bot)

    # Здесь код для запуска бота...

