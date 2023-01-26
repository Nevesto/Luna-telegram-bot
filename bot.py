from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup)

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
            ['/pic', '/bitcoin', '/eth']
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
    await message.reply('Olá, eu sou Luna, um bot em desenvolvimento. \n Eu estou sendo criada para suprir diversas necessidades. \nAinda estou em fase de desenvolvimento, mas você pode se divertir com os meus comandos! \n Use: /commands para ver todos os meus comandos!')

@app.on_message(filters.command('commands'))
async def ls_commands(client, message):
    await message.reply(
        f'Aqui estão a minha lista de comandos: \n /help - Ajuda com a interação do bot. \n/commands - Lista todos os comandos do bot. \n /pic - **(BETA)** Retorna uma foto. \n /bitcoin - Te permite monitorar o valor do bitcoin. \n /eth - Te permite monitorar o valor do Etherium.')

@app.on_message(filters.command('git'))
async def message_button(client, message):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Nevesto Github.', url='https://github.com/Nevesto')
            ]
        ]
    )
    await message.reply('Clique no botão para acessar o github do meu criador!', reply_markup=buttons)

@app.on_message(filters.photo)
async def hand_photo(client, message):
    print(f"{message.chat.username}: Enviou uma foto")
    await message.reply('Que bela foto!')

@app.on_message(filters.voice | filters.audio)
async def hand_audio(client, message):
    print(f"{message.chat.username}: Enviou um audio")
    await message.reply('Que bela voz!')

@app.on_message(filters.command('pic'))
async def photo(client, message):
    await app.send_photo(
        message.chat.id,
        'https://aniyuki.com/wp-content/uploads/2021/12/aniyuki-sad-anime-avatar-image-51.jpg'
    )

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