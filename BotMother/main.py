#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os

from telegram import (Bot, InlineKeyboardButton, InlineKeyboardMarkup,
                      Update)
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          CommandHandler, Updater)

import config
from recurring import greet

from utils import time_control

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    context.bot.send_message(text=greet.good_morning(),
                                 chat_id=config.MY_ID)

def morning_message(arg=None):
    bot = Bot(token=config.BOT_TOKEN)
    bot.send_message(text=greet.good_morning(),
                                 chat_id=config.MOM_ID)

# TODO: pass function that initiated this call
def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if query.data == 'confirm':
        query.edit_message_text(
            text=f"Sending morning message")
        context.bot.send_message(text=greet.good_morning(),
                                 chat_id=config.MOM_ID)
    else:
        query.edit_message_text(text="Did not send message")


# TODO: show list of commands
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def send_command(update: Update, context: CallbackContext):
    """sends direct command to mom"""

    if len(context.args) > 0:
        context.bot.send_message(text=' '.join(context.args),
                                    chat_id=config.MOM_ID)
    else:
        context.bot.send_message(text="add sommething after the `/send` command",
                        chat_id=config.MY_ID)

# TODO: add an inline keyboard command to confirm
def morning_command(update: Update, context: CallbackContext) -> None:
    """Send a morning dua to mom"""
    keyboard = [
        [
            InlineKeyboardButton("Yes", callback_data='confirm'),
            InlineKeyboardButton("No", callback_data='cancel'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Do you want to send morning dua?', reply_markup=reply_markup)



def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config.BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("morning", morning_command))
    dispatcher.add_handler(CommandHandler("send", send_command))

    # Start the Bot
    updater.start_polling()

    # starts threaded scheduled morning messages
    time_control.start_scheduler(time="08:00", job=morning_message,args=[], time_interval=10800)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
