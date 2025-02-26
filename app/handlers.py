from aiogram import Bot, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from app.cron_messages import message_to_chat, send_message_cron
from app.scheduller import add_sender_to_job

router: Router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    uid = message.from_user.id
    await message.answer(text=f"Hello, your id: {uid}: run scheduller!")


@router.message(Command("send"))
async def manual_send_command(message: Message, bot: Bot):
    await send_message_cron(bot)


@router.message(Command("add_job"))
async def add_new_job_command(message: Message, bot: Bot):
    await add_sender_to_job(message_to_chat, bot, send_message="message to chat")
