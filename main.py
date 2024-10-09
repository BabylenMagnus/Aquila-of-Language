import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import dotenv_values


config = dotenv_values(".env")

bot = Bot(
    config["TELEGRAM_TOKEN"],
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)
dp = Dispatcher()


@dp.message(F.document)
async def doc_message(message: Message):
    print(message)
    await message.answer(
        "Hello, <b>world</b>! 4543"
    )


@dp.message(F.text)
async def any_message(message: Message):
    print(message)
    await message.answer(
        "Hello, <b>world</b>!"
    )


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print("start")
    asyncio.run(main())
