from bot.utils import send_message, add_watermark


def start_handler(update, context):
    """Обработчик команды /start. Отправляет приветственное сообщение с
    информацией."""
    send_message(update, context, message='Добро пожаловать! Отправьте мне '
                                          'изображение.')


def photo_handler(update, context):
    send_message(update, context, message='Ожидайте ⌛️')
    add_watermark(update, context)
    send_message(update, context, message=f'Вы отправили изображение как '
                                          f'документ')
