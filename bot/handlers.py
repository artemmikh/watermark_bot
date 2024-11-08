from bot.logger import logger
from bot.utils import send_message, add_watermark


def start_handler(update, context):
    """Обработчик команды /start. Отправляет приветственное сообщение с
    информацией."""
    send_message(update, context, message='Добро пожаловать! Отправьте мне '
                                          'изображение.')


def photo_handler(update, context):
    send_message(update, context, message='ожидайте ⌛️')
    try:
        watermarked_file_path = add_watermark(update, context)
        send_message(update, context, file_path=watermarked_file_path)
    except Exception as error:
        logger.error(f'Ошибка при добавлении водяного знака: {error}')
        send_message(update, context, 'Не удалось обработать изображение.')
