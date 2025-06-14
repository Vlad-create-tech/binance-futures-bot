import os
from binance.client import Client
import telebot
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

SYMBOL = os.getenv("SYMBOL", "BTCUSDT")
ALERT_PRICE = os.getenv("ALERT_PRICE", "70000")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
