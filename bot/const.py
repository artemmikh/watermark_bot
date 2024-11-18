import os

import telegram
from dotenv import load_dotenv
from telegram.ext import Updater

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
BOT = telegram.Bot(token=TELEGRAM_TOKEN)
UPDATER = Updater(token=TELEGRAM_TOKEN, use_context=True)
SETTINGS_TEXT = 'Настройки'
