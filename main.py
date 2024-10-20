import asyncio

from aiogram import Bot, Dispatcher
from config import token, EDAMAM_APP_ID,EDAMAM_APP_KEY


token = token

from user_private import user_private_router

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())


