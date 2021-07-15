import telegram
import logging
from dotenv import load_dotenv
import os

# configure logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


# Get parent path
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(PARENT_DIR, '.env'))


bot = telegram.Bot(token=os.getenv('BOT_TOKEN'))

# print(bot.get_me())
updates = bot.get_updates()
print(updates[0])

bot.send_message(text="xD", chat_id=os.getenv('MY_ID'))