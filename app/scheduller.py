import datetime as dt

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")


async def add_sender_to_job(func, bot: Bot, **kwargs):
    """add function to scedule/

    TODO: It is necessary to add the ability to set periods and intervals for sending

    Args:
        func (Function): function for making
        bot (Bot): object bot need for sending message
    """
    print(kwargs)

    params = {"bot": bot}
    params.update(**kwargs)

    scheduler.add_job(
        func,
        trigger="interval",
        minutes=1,
        start_date=dt.datetime.now(),
        kwargs=params,
    )
