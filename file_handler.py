import os
import requests

from urllib.parse import urlparse, unquote


def get_filename(url):
    path = urlparse(url).path
    path = unquote(path)
    filename = os.path.basename(path)

    filename = filename.replace(' ', '_')
    return filename


def download_image(image_name, image_url, path_to_save):
    response = requests.get(image_url)
    response.raise_for_status()

    with open(f'{path_to_save}{image_name}', 'wb') as file:
        file.write(response.content)
