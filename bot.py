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
@app.on_callback_query()
async def callback(client, callback_query):
    pages = {
        'data': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_1'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Home'
        },
        'page_1': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='page_2'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='data'),
            'texto': 'Você está na página 1'
        },
        'page_2': {
            'proximo': InlineKeyboardButton('Próximo', callback_data='data'),
            'anterior': InlineKeyboardButton('Anterior', callback_data='page_1'),
            'texto': 'Você está na página 2'
        }
    }
    page = pages[callback_query.data]
    await callback_query.edit_message_text(
        page['texto'],
        reply_markup = InlineKeyboardMarkup([[
            page['anterior'], page['proximo']
        ]])
    )
    
@app.on_message(filters.command('utils'))
async def message_button(client, message):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton('Callback', callback_data='data'),
                InlineKeyboardButton('Git', url='https://github.com/Nevesto')
            ]
        ]
    )
    await message.reply('Navegue pelas minhas funções!', reply_markup=buttons)

@app.on_message(filters.command('help') | filters.command('start'))
async def help(client, message):
    print(f"{message.chat.username}: {message.text}")
    await message.reply('Olá, eu sou Luna, um bot em desenvolvimento. \nEu estou sendo criada para suprir diversas necessidades. \nAinda estou em fase de desenvolvimento, mas você pode se divertir com os meus comandos! \nUse: **/commands** para ver todos os meus comandos!')

@app.on_message(filters.command('commands'))
async def ls_commands(client, message):
    await message.reply(
        f'**Aqui está a minha lista de comandos:** \n**/help** - Ajuda com a interação do bot. \n**/commands** - Lista todos os comandos do bot. \n**/pic** - **(BETA)** Retorna uma foto. \n **/git** - Github do desenvolvedor. \n /bitcoin - Te permite monitorar o valor do bitcoin. \n /eth - Te permite monitorar o valor do Etherium.')



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