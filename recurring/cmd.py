import config
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          CommandHandler, Updater)

from recurring import greet


def morning_message(bot_token, chat_id):
    """send morning message"""

    # TODO: remove useless arg command
    bot = Bot(token=bot_token)
    bot.send_message(text=greet.good_morning(),
                     chat_id=chat_id)
