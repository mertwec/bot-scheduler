# Bot - scheduler


This project is an example of sending messages on a schedule using the `aiogram` library and `APScheduler`.


## install and run

`pip install reqirements.txt`

`python3 main.py`


## Description
The project uses aiogram to create a telegram bot and APScheduler to schedule sending messages.

## Main files:
- main.py — initialize the bot and dispatcher, start the scheduler.
- scheduller.py — configure APScheduler for periodic sending of messages.
- handlers.py — handle user commands.
- cron_messages.py — logic for sending messages.

## Available commands
- /start — start the bot.
- /send — send a message manually (on schedule).
- /add_job — add a new task to the scheduler (implementation in progress).


### TODO
Add the ability to set periods and intervals for sending messages.
Improve the processing of user commands.