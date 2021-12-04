import os
import time
import telegram

from dotenv import load_dotenv

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
DELAY = int(os.getenv('DELAY_SLEEP'))
CHANNEL_NAME = os.getenv('CHANNEL_NAME')


def send_image_to_telegram_channel(channel_name, folder_name='images'):
    directory = folder_name
    if not os.path.exists(directory):
        os.makedirs(directory)

    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    channel_name = channel_name
    images = os.listdir(directory)

    for image in images:
        bot.send_document(chat_id=channel_name,
                          document=open(f'{directory}/{image}', 'rb'))
        time.sleep(DELAY)


def main():
    send_image_to_telegram_channel(CHANNEL_NAME)


if __name__ == "__main__":
    main()