from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

id_telemetr = 653851044
my_id = 1312774941

@app.on_message(filters.me)
def get_sms(client,message):
    app.send_message(chat_id=my_id,text='Запущу отложенный скрипт. Это сообщение тебе должно прийти в 14:30')
    time.sleep(63000) # Старт в 14:30

    if message.text == 'start_get_auth_stata' and message.chat.id == '1312774941':
        while True:
            app.send_message(chat_id=id_telemetr,text= '@FactorRoom')
            time.sleep(20)
            app.send_message(chat_id=id_telemetr, text='@RoomFakts')
            time.sleep(86400)


app.run()
