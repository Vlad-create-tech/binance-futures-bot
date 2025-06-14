from config import *
import time

def check_price():
    try:
        ticker = client.futures_ticker(symbol=SYMBOL)
        current_price = float(ticker['lastPrice'])

        if current_price > float(ALERT_PRICE):
            message = f"🔔 {SYMBOL} price is {current_price}, above alert level {ALERT_PRICE}."
            bot.send_message(chat_id=CHAT_ID, text=message)

    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"❗ Error: {e}")

if __name__ == "__main__":
    while True:
        check_price()
        time.sleep(CHECK_INTERVAL)
