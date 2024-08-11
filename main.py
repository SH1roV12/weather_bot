import logging
import os
import asyncio

from aiogram import Bot, Dispatcher, F
from dotenv import load_dotenv

from app.handlers import router

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')