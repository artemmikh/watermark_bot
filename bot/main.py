from dotenv import load_dotenv
from telegram.ext import CommandHandler, MessageHandler, Filters

from bot import const
from bot.check import check_tokens
from bot.handlers import start_handler, photo_handler
from logger import logger

load_dotenv()


def main():
    """Основная логика работы бота."""

    logger.info('Провеверка переменных окружения')
    check_tokens()

    try:
        logger.info('Регистрация обработчиков')
        const.UPDATER.dispatcher.add_handler(
            CommandHandler('start', start_handler))
        const.UPDATER.dispatcher.add_handler(
            MessageHandler(Filters.document, photo_handler))

        logger.info('Запуск процесса polling')
        const.UPDATER.start_polling()
        const.UPDATER.idle()

    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        logger.error(message)


if __name__ == '__main__':
    main()
