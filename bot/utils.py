import re

from logger import logger


def send_message(update, context, message):
    """Отправляет сообщение в Telegram чат."""
    try:
        chat = update.effective_chat
        context.bot.send_message(chat.id, message)
        logger.debug(f'Сообщение успешно отправлено в Telegram: {message}')
    except Exception as error:
        logger.error(f'Сбой при отправке сообщения в Telegram: {error}')


def check_message(message):
    """Проверяет, соответствует ли текст формату двух чисел через пробел."""
    return re.match(r'\d{1,15} \d{1,15}', message)


def parse_message(message):
    """Извлекает две группы чисел из сообщения."""
    return int(message.split(' ')[0]), int(message.split(' ')[1])
