import os

from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

from logger import logger
from db import session, UserSettings

load_dotenv()


def send_message(update, context, message=None, file_path=None):
    """Отправляет сообщение в Telegram чат."""
    try:
        chat = update.effective_chat
        if file_path is not None:
            with open(file_path, 'rb') as photo:
                context.bot.send_document(chat_id=chat.id, document=photo)
            logger.debug(f'Документ успешно отправлен в чат {chat}')
        else:
            context.bot.send_message(chat.id, message)
            logger.debug(f'Сообщение успешно отправлено в Telegram: {message}')
    except Exception as error:
        logger.error(f'Сбой при отправке сообщения в Telegram: {error}')


def download_user_file(update, context):
    """Загружает в /temp изображение присланное пользователем."""
    file = context.bot.get_file(update.message.document.file_id)
    file_path = os.getenv('USER_FILE_PATH')
    file.download(file_path)
    return file_path


def remove_images(user_file_path, watermarked_file_path):
    """Удаляет изображения из /temp"""
    if os.path.exists(watermarked_file_path):
        os.remove(watermarked_file_path)
    if os.path.exists(user_file_path):
        os.remove(user_file_path)


def check_user_exists(update, context):
    """Проверяет существование пользователя в базе по chat.id"""
    return session.query(UserSettings).filter_by(
        chat_id=update.effective_chat.id).first()


def get_user_settings(update, context):
    """Возвращает настройки пользователя из базы или по умолчанию."""
    user_settings = check_user_exists(update, context)
    if user_settings:
        transparency = user_settings.transparency
        front_size = user_settings.front_size
        position_x = user_settings.position_x
        position_y = user_settings.position_y
        watermark_text = user_settings.text
    else:
        transparency = int(os.getenv('DEFAULT_TRANSPARENCY'))
        front_size = int(os.getenv('DEFAULT_FRONT_SIZE'))
        position_x = int(os.getenv('DEFAULT_POSITION_X'))
        position_y = int(os.getenv('DEFAULT_POSITION_Y'))
        watermark_text = os.getenv('DEFAULT_WATERMARK_TEXT')
    return transparency, front_size, position_x, position_y, watermark_text


def add_watermark(update, context):
    """Добавляет водяной знак на изображение."""
    user_file_path = download_user_file(update, context)
    watermarked_file_path = os.getenv('WATERMARKED_FILE_PATH')
    (transparency, front_size, position_x, position_y,
     watermark_text) = get_user_settings(update, context)
    with Image.open(user_file_path).convert('RGBA') as base:
        txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
        fnt = ImageFont.load_default(int(front_size))
        d = ImageDraw.Draw(txt)
        d.text((position_x, position_y), text=watermark_text, font=fnt,
               fill=(255, 255, 255, transparency))
        out = Image.alpha_composite(base, txt)
        out.save(watermarked_file_path,
                 os.getenv('FORMAT_WATERMARKED_IMAGE', 'PNG'))
    return watermarked_file_path, user_file_path
