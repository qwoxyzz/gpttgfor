import logging
from aiogram import Bot, Dispatcher, executor, types
from db import Database
from aiogram.dispatcher.filters import Command
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7017427981:AAHu7xiLJLosSLPG7SNogbMr6mHIdqosBJo")
dp = Dispatcher(bot)
db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            await bot.send_message(message.from_user.id, 'Привет!👋\n'
                                                     '\n'
                                                     'Осталось совсем немного!\n'
                                                     '💸Нажми на кнопку с юзернеймом ниже, чтобы завершить регистрацию и опробовать новую замену ноткоину💸\n\n'
                                                     '              * ЖМИ *\n'
                                                     '            ⬇️⬇️⬇️⬇️\n'
                                                     'https://t.me/hamster_kombat_bot?start=kentId5619598337')

@dp.message_handler(commands=['сфототекст'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5619598337:
            text = message.text[12:]
            link_start = '[-'
            link_end = '-]'
            with open('laptop.jpg', 'rb') as photo:
                if link_start in text and link_end in text:
                    start_index = text.find(link_start) + len(link_start)
                    end_index = text.find(link_end)
                    link_text = text[start_index:end_index]
                    users = db.get_users()
                    for row in users:
                        try:
                            await bot.send_photo(row[0], photo, caption=text.replace(link_start + link_text + link_end, f'<a href="http://yourlink.com">{link_text}</a>', 1), parse_mode='HTML')
                            if int(row[1]) != 1:
                                db.set_active(row[0], 1)
                        except:
                            db.set_active(row[0], 0)
                else:
                    users = db.get_users()
                    for row in users:
                        try:
                            await bot.send_photo(row[0], photo, caption=text)
                            if int(row[1]) != 1:
                                db.set_active(row[0], 1)
                        except:
                            db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")


@dp.message_handler(commands=['сфототексткноп'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5619598337:
            split_text = message.text.split(' ')
            knop = split_text[1]
            text = message.text[17 + len(knop) + 1:]
            link_start = '[-'
            link_end = '-]'
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text=knop, url="https://example.com")
            keyboard.add(button)
            with open('laptop.jpg', 'rb') as photo:
                if link_start in text and link_end in text:
                    start_index = text.find(link_start) + len(link_start)
                    end_index = text.find(link_end)
                    link_text = text[start_index:end_index]
                    users = db.get_users()
                    for row in users:
                        try:
                            await bot.send_photo(row[0], photo, caption=text.replace(link_start + link_text + link_end, f'<a href="http://yourlink.com">{link_text}</a>', 1), parse_mode='HTML', reply_markup=keyboard)
                            if int(row[1]) != 1:
                                db.set_active(row[0], 1)
                        except:
                            db.set_active(row[0], 0)
                else:
                    users = db.get_users()
                    for row in users:
                        try:
                            await bot.send_photo(row[0], photo, caption=text, reply_markup=keyboard)
                            if int(row[1]) != 1:
                                db.set_active(row[0], 1)
                        except:
                            db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")


@dp.message_handler(commands=['ссылкатекст'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5619598337:
            text = message.text[13:]
            link_start = '[-'
            link_end = '-]'
            if link_start in text and link_end in text:
                start_index = text.find(link_start) + len(link_start)
                end_index = text.find(link_end)
                link_text = text[start_index:end_index]
                users = db.get_users()
                for row in users:
                    try:
                        await bot.send_message(row[0], text.replace(link_start + link_text + link_end, f'<a href="http://yourlink.com">{link_text}</a>', 1), parse_mode='HTML')
                        if int(row[1]) != 1:
                            db.set_active(row[0], 1)
                    except:
                        db.set_active(row[0], 0)
            else:
                users = db.get_users()
                for row in users:
                    try:
                        await bot.send_message(row[0], text)
                        if int(row[1]) != 1:
                            db.set_active(row[0], 1)
                    except:
                        db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")


@dp.message_handler(commands=['ссылкатексткноп'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5619598337:
            split_text = message.text.split(' ')
            knop = split_text[1]
            text = message.text[17 + len(knop) + 1:]  # Учитываем длину команды и переменной knop, а также пробела после переменной knop
            link_start = '[-'
            link_end = '-]'
            if link_start in text and link_end in text:
                start_index = text.find(link_start) + len(link_start)
                end_index = text.find(link_end)
                link_text = text[start_index:end_index]
                keyboard = types.InlineKeyboardMarkup()
                button = types.InlineKeyboardButton(text=knop, url="https://example.com")
                keyboard.add(button)
                users = db.get_users()
                for row in users:
                    try:
                        await bot.send_message(row[0], text.replace(link_start + link_text + link_end, f'<a href="http://yourlink.com">{link_text}</a>', 1), parse_mode='HTML', reply_markup=keyboard)
                        if int(row[1]) != 1:
                            db.set_active(row[0], 1)
                    except:
                        db.set_active(row[0], 0)
            else:
                keyboard = types.InlineKeyboardMarkup()
                button = types.InlineKeyboardButton(text=knop, url="https://example.com")
                keyboard.add(button)
                users = db.get_users()
                for row in users:
                    try:
                        await bot.send_message(row[0], text, reply_markup=keyboard)
                        if int(row[1]) != 1:
                            db.set_active(row[0], 1)
                    except:
                        db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def save_photo(message: Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5619598337:
            photo = message.photo[-1]  # Получаем последнюю (самую большую) фотографию из сообщения
            file_id = photo.file_id
            file_info = await bot.get_file(file_id)
            file_path = file_info.file_path
            downloaded_file = await bot.download_file(file_path)

            with open('laptop.jpg', 'wb') as new_file:
                new_file.write(downloaded_file.read())

            await message.answer("Фото успешно сохранено под именем laptop.jpg")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)