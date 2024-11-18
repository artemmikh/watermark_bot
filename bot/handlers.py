from telegram import (ReplyKeyboardMarkup, InlineKeyboardButton,
                      InlineKeyboardMarkup)

from bot.const import SETTINGS_TEXT
from bot.db import UserSettings, session
from bot.logger import logger
from bot.utils import (send_message, add_watermark, remove_images,
                       check_user_exists, validate_user_input,
                       update_user_setting)


def start_handler(update, context):
    """Обработчик команды /start. Отправляет приветственное сообщение с
    информацией."""
    button = ReplyKeyboardMarkup(
        [[SETTINGS_TEXT]],
        resize_keyboard=True, )
    send_message(update, context,
                 buttons=button,
                 message='Добро пожаловать! Отправьте мне '
                         'изображение файлом в формате PNG или JPEG. ')


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
                     'Вы можете отправить изображение в формате PNG или JPEG')


def settings_handler(update, context):
    keyboard = [
        [InlineKeyboardButton(
            'Текст вотермарки',
            callback_data='text')],
        [InlineKeyboardButton(
            'Прозрачность',
            callback_data='transparency')],
        [InlineKeyboardButton(
            'Размер шрифта',
            callback_data='front_size')],
        [InlineKeyboardButton(
            'Позиция текста по оси X',
            callback_data='position_x')],
        [InlineKeyboardButton(
            'Позиция текста по оси Y',
            callback_data='position_y')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    send_message(update, context,
                 buttons=reply_markup,
                 message='Выберите параметр для изменения:')


def user_choice_settings_handler(update, context):
    """Обработчик нажатия кнопок настройки."""
    query = update.callback_query
    query.answer()

    setting = query.data
    context.user_data[
        'current_setting'] = setting

    setting_messages = {
        'text': 'Введите текст для водяного знака:',
        'transparency': 'Введите прозрачность (значение от 0 до 255):',
        'front_size': 'Введите размер шрифта (значение от 10 до 100):',
        'position_x': 'Введите позицию по оси X:',
        'position_y': 'Введите позицию по оси Y:'
    }

    message = setting_messages.get(setting, 'Введите значение:')
    query.edit_message_text(text=message)


def handle_user_input(update, context):
    """Основной обработчик ввода от пользователя."""
    chat_id = update.effective_chat.id
    user_input = update.message.text
    current_setting = context.user_data.get('current_setting')

    try:
        value = validate_user_input(current_setting, user_input)
        update_user_setting(chat_id, current_setting, value)
        send_message(update, context,
                     f"Настройка '{current_setting}' успешно обновлена!")
        context.user_data[
            'current_setting'] = None

    except ValueError as validation_error:
        send_message(update, context, f"Ошибка: {validation_error}")
    except Exception as update_error:
        send_message(update, context,
                     f"Ошибка при обновлении настройки: {update_error}")
