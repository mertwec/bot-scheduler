import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.cron_messages import send_message_cron
from app.handlers import router
from app.scheduller import add_sender_to_job, scheduler
from config import TOKEN, logger
from aiogram.types.bot_command import BotCommand


async def main():

    logger.info("Starting BOT_scheduler")

    bot: Bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp: Dispatcher = Dispatcher()
    dp["some"] = "in data some"

    # scheduler for message
    await add_sender_to_job(send_message_cron, bot)
    scheduler.start()

    dp.include_router(router)

    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Run bot"),
            BotCommand(command="add", description="add message to scheduler. TODO"),
            BotCommand(command="send", description="send default cron_message from schedulle"),
        ]
    )

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
