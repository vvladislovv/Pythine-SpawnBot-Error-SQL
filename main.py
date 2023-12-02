import logging
from aiogram import Bot, Dispatcher, executor, types
from db import Database

logging.basicConfig(level=logging.INFO)

Boter = Bot(token="6854498285:AAHLmYgUsNXdobuTRXBNiHrrTejwH_RMNMQ")
dp = Dispatcher(Boter)
db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await Boter.send_message(message.from_user.id, "Добро пожаловать!")
        
        
@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 1182394667:
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                print(row[1])
                try:
                    print(row[1])
                    await Boter.send_message(message.from_user.id, text) # проблема в том что row не видит таблицу + не получает других пользователей проблема с SQL (Решить не удолось)
                    print(row)
                    if int(row[1]) == 1: # проблема тут
                       # await Boter.send_message(row[0], text)
                        print("fff")
                        db.set_active(row[0], 1)
                except:
                    print("SSS")
                    await Boter.send_message(message.from_user.id, "ОШИБКА")
                    print(message.text[9:])
                    db.set_active(row[0], 0)

            

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)