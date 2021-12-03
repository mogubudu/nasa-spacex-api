import datetime as dt
import os
import requests
import telegram

from dotenv import load_dotenv
from urllib.parse import urlparse, unquote

load_dotenv()
NASA_TOKEN = os.getenv('NASA_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


def download_image(image_name, image_url, path_to_save):
    directory = path_to_save
    image_name = image_name
    image_url = image_url

    if not os.path.exists(directory):
        os.makedirs(directory)

    responce = requests.get(image_url)
    responce.raise_for_status()

    with open(f'{directory}{image_name}', 'wb') as file:
        file.write(responce.content)


def fetch_spacex_last_launch():
    spacex_api_url = 'https://api.spacexdata.com/v4/launches/'

    responce = requests.get(spacex_api_url)
    responce.raise_for_status()

    launch_spacex = responce.json()[13]
    if 'links' in launch_spacex:
        for url in launch_spacex['links']['flickr']['original']:
            download_image(create_filename(url), url, 'image_spacex/')


def get_file_extencion(url):
    path = urlparse(url)[2]
    path = unquote(path)
    extencion = os.path.splitext(path)[1]
    return extencion


def get_filename(url):
    path = urlparse(url)[2]
    path = unquote(path)
    filename = os.path.split(path)[1]
    filename = os.path.splitext(filename)[0]
    filename = filename.replace(' ', '_')
    return filename


def create_filename(url):
    filename = get_filename(url)
    extencion = get_file_extencion(url)
    return f'{filename}{extencion}'


def download_image_from_nasa_apod():
    api_url = 'https://api.nasa.gov/planetary/apod'
    api_key = NASA_TOKEN
    params = {
      'api_key': api_key,
      'count': 50,
    }

    responce = requests.get(api_url, params)
    responce = responce.json()

    for item in responce:
        if 'hdurl' in item:
            download_image(create_filename(item['hdurl']),
                           item['hdurl'],
                           'image_nasa_apod/')


def download_image_from_nasa_epic():
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    api_key = NASA_TOKEN
    params = {
        'api_key': api_key,
    }

    responce = requests.get(api_url, params)
    responce = responce.json()

    for item in responce:
        if 'image' in item:
            full_date = item['date']
            formatted_date = dt.datetime.strptime(full_date,
                                                  '%Y-%m-%d %H:%M:%S')
            formatted_date = dt.datetime.strftime(formatted_date, '%Y/%m/%d')
            image_name = item['image']

            url_archive = (f'https://api.nasa.gov/EPIC/archive/natural/'
                           f'{formatted_date}/png/{image_name}.png'
                           f'?api_key={api_key}')

            download_image(create_filename(url_archive),
                           url_archive,
                           'image_nasa_epic/')
def main():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    channel_name = '@photo_prosto_cosmos'
    #bot.send_message(text='her sobachiy', chat_id=channel_name)
    bot.send_document(chat_id=channel_name, document=open('image_nasa_apod/ngc7009_hst_big.jpg', 'rb'))



if __name__ == "__main__":
    main()


