from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

load_dotenv()

app = Client(
    'SelunaBot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)

#função menu
@app.on_message(filters.command('menu'))
async def menu(client, message):
    menu = ReplyKeyboardMarkup(
        [
            ['/help', '/commands'],
            ['1', '2', '3']
        ],
        resize_keyboard=True
    )
    await message.reply(
        'Commands interface opened.',
        reply_markup=menu
        )

#comandos do bot
@app.on_message(filters.command('help'))
async def help(client, message):
    print(f"{message.chat.username}: {message.text}")
    await message.reply('Este é o menu de ajuda:')

@app.on_message(filters.command('/pic'))

@app.on_message(filters.photo)
async def hand_photo(client, message):
    print(f"{message.chat.username}: Enviou uma foto")
    await message.reply('Que bela foto!')

@app.on_message(filters.voice | filters.audio)
async def hand_audio(client, message):
    print(f"{message.chat.username}: Enviou um audio")
    await message.reply('Que bela voz!')

@app.on_message(filters.sticker)
async def hand_sticker(client, message):
    print(f'{message.chat.username}: Enviou um sticker')
    await app.send_sticker(message.chat.id, message.sticker.file_id)

# deixar abaixo de todos os comandos.
@app.on_message()
async def messages(client, message):
    print(f"{message.chat.username}: {message.text}")
    await message.reply(f'Você enviou: {message.text}')

app.run()