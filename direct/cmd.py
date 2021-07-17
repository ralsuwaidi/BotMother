from telegram import (Bot, InlineKeyboardButton, InlineKeyboardMarkup,
                      Update)
from telegram.ext import (CallbackContext, CallbackQueryHandler,
                          CommandHandler, Updater)

from recurring import greet
import config

# Define a few command handlers. These usually take the two arguments update and
# context.


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    context.bot.send_message(text=greet.good_morning(),
                             chat_id=config.MY_ID)


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
