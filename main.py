import asyncio
import os

from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

load_dotenv()

TOKEN = os.getenv("YOUR_BOT_TOKEN")
FLAG = os.getenv("FLAG")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.reply(f"FLAG: {FLAG}", parse_mode=ParseMode.MARKDOWN)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
