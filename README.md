# Telegram Watermark Bot

Этот проект — Telegram-бот для добавления водяного знака на изображения,
отправленные пользователем в виде файлов.
Бот обрабатывает полученные изображения, добавляет на них текст водяного знака
и отправляет обратно пользователю.

### [Перейти к боту в Telegram](https://t.me/watermark_on_the_image_bot)

## Функциональность

- Получение изображений от пользователей в виде файлов.
- Наложение текстового водяного знака на изображение.
- Отправка изображения с водяным знаком обратно в виде файла.
- Поддержка изображений в форматах PNG и JPEG.
- Возможность настройки параметров водяного знака через встроенное меню.

## Установка и настройка

1. **Клонируйте репозиторий:**

    ```
    git clone <URL>
    cd telegram-watermark-bot
    ```

2. **Установите зависимости:**

    ```
    pip install -r requirements.txt
    ```

3. **Настройте переменные окружения:**

   Создайте файл `.env` и добавьте в него ваш токен Telegram-бота:

    ```
    TELEGRAM_TOKEN=YOUR_TELEGRAM_TOKEN
    BOT_DATABASE_URL=sqlite:///../watermark_bot.db
    WATERMARKED_FILE_PATH=temp/watermarked_image.png
    USER_FILE_PATH=temp/down_image.jpg
    DEFAULT_WATERMARK_TEXT=NOT FOR DISTRIBUTION
    DEFAULT_TRANSPARENCY=64
    DEFAULT_FRONT_SIZE=20
    DEFAULT_POSITION_X=10
    DEFAULT_POSITION_Y=10
    FORMAT_WATERMARKED_IMAGE=PNG
    ```

4. **Запуск бота:**

    ```
    python bot.py
    ```

## Настройка водяного знака

Через меню настроек бота вы можете изменить следующие параметры:

- **Текст водяного знака:** задаётся текст, который будет добавляться на
  изображение.
- **Прозрачность:** уровень прозрачности текста (значение от 0 до 255).
- **Размер шрифта:** размер текста (значение от 10 до 100).
- **Положение текста по оси X и Y:** координаты начала текста на изображении.

При выборе параметра бот попросит ввести новое значение. Если введено
некорректное значение, бот сообщит об ошибке.

## Пример использования

1. Пользователь отправляет изображение в виде файла.
2. Бот отвечает: "ожидайте ⌛️".
3. Бот обрабатывает изображение и добавляет водяной знак.
4. Пользователь получает обработанный файл обратно в чат.

## Требования

- Python 3.7+
- Библиотеки из `requirements.txt`

## Логирование

Ошибки и события записываются в лог с использованием встроенного логгера.

## Лицензия

Этот проект распространяется под лицензией MIT.
