from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, Filters, \
    CallbackQueryHandler

import const
from check import check_tokens
from const import SETTINGS_TEXT
from db import session
from handlers import (
    start_handler, document_handler, photo_handler,
    settings_handler, handle_user_input, user_choice_settings_handler)
from logger import logger

load_dotenv()


def main():
    """Основная логика работы бота."""
    logger.info('Проверка переменных окружения')
    check_tokens()

    try:
        logger.info('Регистрация обработчиков')
        const.UPDATER.dispatcher.add_handler(
            CommandHandler('start', start_handler)
        )
        const.UPDATER.dispatcher.add_handler(
            MessageHandler(Filters.text([SETTINGS_TEXT]), settings_handler)
        )
        const.UPDATER.dispatcher.add_handler(
            CallbackQueryHandler(user_choice_settings_handler)
        )
        const.UPDATER.dispatcher.add_handler(
            MessageHandler(Filters.text & ~Filters.command, handle_user_input)
        )
        const.UPDATER.dispatcher.add_handler(
            MessageHandler(Filters.document, document_handler)
        )
        const.UPDATER.dispatcher.add_handler(
            MessageHandler(Filters.photo, photo_handler)
        )

        logger.info('Запуск процесса polling')
        const.UPDATER.start_polling()
        const.UPDATER.idle()
        session.close()

    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        logger.error(message)


if __name__ == '__main__':
    main()
