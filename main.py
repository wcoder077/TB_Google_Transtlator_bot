# main.py
import asyncio
from aiogram import Bot, Dispatcher
from bot_functions import start_router  

API_TOKEN = "8597347819:AAE-PrsT7QLqthGCTkzvEJcq7a1BUv7GjeU"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
dp.include_router(start_router)

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
