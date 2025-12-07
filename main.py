import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import os

TOKEN = os.getenv("7371398086:AAG_25EzLxwoE8h7_ZEqon4NoNckpCBYHaw")
CHAT_ID = os.getenv("2129500063")  # ID чата, куда отправлять сообщения

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Команда для проверки работы
@dp.message()
async def start(message: Message):
    await message.answer("Бот запущен и расписание активно!")


# Функция — что отправлять по расписанию
async def weekly_message():
    await bot.send_message(CHAT_ID, "А баня будет?")


async def main():
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")

    # 📌 Каждую субботу в 10:00 (пример)
    scheduler.add_job(
        weekly_message,
        trigger="cron",
        day_of_week="sat",
        hour=10,
        minute=0
    )

    scheduler.start()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
