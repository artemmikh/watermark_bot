from bot.utils import send_message


def start_handler(update, context):
    """Обработчик команды /start. Отправляет приветственное сообщение с
    информацией."""
    send_message(update, context, message='Добро пожаловать! Отправьте мне '
                                          'изображение.')


def photo_handler(update, context):
    send_message(update, context, message=f'Вы отправили изображение')
