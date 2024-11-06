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
