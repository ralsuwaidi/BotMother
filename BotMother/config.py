from dotenv import load_dotenv
import os

# Get parent path
PARENT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir))


# Connect the path with your '.env' file name
load_dotenv(os.path.join(PARENT_DIR, '.env'))

# chat id of your own chat with bot
MY_ID = os.getenv('MY_ID')

# bot token from BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID of group/mom chat
MOM_ID = os.getenv("MOM_ID")
