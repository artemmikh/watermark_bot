from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from logger import logger


def send_message(update, context, message):
    """Отправляет сообщение в Telegram чат."""
    try:
        chat = update.effective_chat
        context.bot.send_message(chat.id, message)
        logger.debug(f'Сообщение успешно отправлено в Telegram: {message}')
    except Exception as error:
        logger.error(f'Сбой при отправке сообщения в Telegram: {error}')


def add_watermark(update, context):
    """Добавляет водяной знак на изображение и отправляет его обратно в Telegram."""
    try:
        # файл, присланный в чат
        file = context.bot.get_file(update.message.document.file_id)

        # файл локально
        file_path = 'received_image.jpg'
        file.download(file_path)

        # Открываю изображение и добавляю водяной знак
        img = Image.open(file_path).convert("RGB")  # в режим RGB
        draw = ImageDraw.Draw(img)

        # Настройки текста водяного знака
        watermark_text = "Sample Watermark"
        font = ImageFont.load_default()  # шрифт по умолчанию
        text_position = (50, 90)  # Позиция текста
        text_color = (255, 255, 255)  # Цвет текста

        # водяной знак
        draw.text(text_position, watermark_text, fill=text_color, font=font)

        # изображение в формат JPEG
        watermarked_path = 'watermarked_image.jpg'
        img.save(watermarked_path, "JPEG")

        # обратно изображение с водяным знаком
        chat_id = update.effective_chat.id
        with open(watermarked_path, 'rb') as photo:
            context.bot.send_document(chat_id=chat_id, document=photo)

        logger.debug(
            f'Изображение с водяным знаком успешно отправлено в чат {chat_id}')

    except Exception as error:
        logger.error(f'Ошибка при добавлении водяного знака: {error}')
        send_message(update, context, "Не удалось обработать изображение.")
