import random

import config
from telegram import Bot

from recurring import greet
import time


def morning_message(bot_token, percentage_chance=75):
    """Function that has a chance to send good morning msg to mom.

    Args:
        bot_token: Bot that will send the msg.
        percentage_chance: Chance that the msg occurs as a percentage.

    """

    # create new bot instance to send the msgs
    bot = Bot(token=bot_token)

    # chance that the bot sends morning message
    if random.randint(0, 100) < percentage_chance:
        bot.send_message(text=greet.good_morning(),
                         chat_id=config.MOM_ID)

        # after sending morning message
        # 50% chance bot will follow up with good morning
        # 'act' like you are typing
        time.sleep(5)
        if random.randint(0, 100) < 50:
            bot.send_message(text='صباح الخير',
                             chat_id=config.MOM_ID)
