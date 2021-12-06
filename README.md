# Космический Телеграм

Программа позволяет скачивать фотографии запусков SpaceX, а также фотографии, которые собирает у себя NASA. 
Но основная функция программы - публиковать скаченные фотографии в телеграм-канале. По умолчанию фотографии из локальной папки публикуются примерно раз в сутки.


## Установка зависимостей и первичная настройка

### Устанавливаем зависимости
Для запуска кода у вас уже должен быть установлен Python3.
Используйте в консоли `pip` для установки зависимостей или `pip3`, есть есть конфликт с Python2:
```
pip install -r requirements.txt
```

### Получаем токены для работы с API
Далее вам понадобиться получить токен для работы с API NASA и telegram.
Для получения токена NASA перейдите по ссылке [https://api.nasa.gov/](https://api.nasa.gov/) и зарегистрируйтесь. Токен будет показан на сайте NASA и отправлен на указанную вами почту.
Пример токена:
```
VvolhJZVcfM2A11W8NofzEewF6yvY0o2o8d2UW7Y
```
А для того, чтобы получить ключ для телеграма воспользуйте инструкцией по созданию бота [https://way23.ru/](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html).
Токен выглядит примерно так:
```
958423683:AAEAtJ5Lde5YYfkjergber
```


### Создаем файл .env
Чувствительные данные, такие как токены, хранятся в переменных окружения. Для того, чтобы у вас всё работало необходимо создать файл .env в папке, где лежат скрипты.
Через переменные окружения регулируются такие настройки как:
1. Ключ NASA - переменная под названием NASA_TOKEN.
2. Ключ Telegram - переменная под названием TELEGRAM_TOKEN.
3. Канал в Telegram для публикации фотографий - переменная под названием CHANNEL_NAME.
4. Периодичность публикации фотографий ботом в секундах - переменная под названием DELAY_SLEEP.

Пример заполненного файла .env:
```
NASA_TOKEN="your token here"
TELEGRAM_TOKEN="your token here"
DELAY_SLEEP=86400
CHANNEL_NAME="@your_channel_name"
```

## Приступаем к работе

### Структура файлов
#### fetch_nasa.py
Скрипт для получения изображения с сайта NASA. При прямом вызове данного скрипта будут выполнены две функции:
1. download_image_from_nasa_apod()
1. download_image_from_nasa_epic()

Первая функция загружаем изображения с сервиса NASA APOD, а вторая - с сервиса NASA EPIC. По умолчанию все изображения будут сохранены в папку images, данную настройку можно изменить передав в функции другое название папки.

#### fetch_spacex.py
Скрипт для получения фотографий последнего запуска SpaceX. По умолчанию фотографии будут сохранены в папку images.

#### send_photo.py
При прямом запуске скрипта будет запущена функция send_image_to_telegram_channel(), которая отправляет фотографии в ваш телеграм канал (название которого вы добавили в переменную окружения). Фотографии отправляются раз в сутки, но если вам понадобиться отрегулировать периодичность отправки, то вам нужно просто поменять значение в соответствующей переменной окружения.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/). 
