from dotenv import load_dotenv
from telegram.ext import CommandHandler

from bot import const
from bot.check import check_tokens
from bot.handlers import wake_up
from logger import logger

load_dotenv()


def main():
    """Основная логика работы бота."""

    logger.info('Провеверка переменных окружения')
    check_tokens()

    try:
        logger.info('Регистрация обработчиков')
        const.UPDATER.dispatcher.add_handler(
            CommandHandler('start', wake_up))

        logger.info('запуск процесса polling')
        const.UPDATER.start_polling()
        const.UPDATER.idle()

    except Exception as error:
        message = f'Сбой в работе программы: {error}'
        logger.error(message)


if __name__ == '__main__':
    main()
