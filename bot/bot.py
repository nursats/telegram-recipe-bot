import asyncio

from aiogram import Bot, Dispatcher
from bot.config import token


token = token

from bot.user_private import user_private_router

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())


