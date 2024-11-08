from bot.logger import logger
from bot.utils import send_message, add_watermark, remove_images


def start_handler(update, context):
    """Обработчик команды /start. Отправляет приветственное сообщение с
    информацией."""
    send_message(update, context, message='Добро пожаловать! Отправьте мне '
                                          'изображение файлом.')


def photo_handler(update, context):
    """Обработчик входящих фото."""
    send_message(update, context,
                 message='Не удалось обработать изображение. '
                         'Пожалуйста, отправьте изображение как файл')


def document_handler(update, context):
    """Обработчик входящих файлов."""
    send_message(update, context, message='ожидайте ⌛️')
    try:
        watermarked_file_path, user_file_path = add_watermark(update, context)
        send_message(update, context, file_path=watermarked_file_path)
        remove_images(watermarked_file_path, user_file_path)
    except Exception as error:
        logger.error(f'Ошибка при добавлении водяного знака: {error}')
        send_message(update, context,
                     'Не удалось обработать изображение. '
                     'Вы можете отправить изображение в форматах PNG или JPEG')
    remove_images(watermarked_file_path, user_file_path)
