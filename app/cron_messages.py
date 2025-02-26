import datetime as dt

from aiogram import Bot

from config import CHAT_ID, UID


async def send_message_cron(bot: Bot):
    dtime = dt.datetime.now().strftime("%H:%M:%S")
    await bot.send_message(UID, text=f"Time now: {dtime}")


async def message_to_chat(bot: Bot, message: str):
    await bot.send_message(CHAT_ID, text=message)
