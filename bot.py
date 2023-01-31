from os import getenv
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup)
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

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
            ['/pic', '/bitcoin', '/etereum'],
            ['/utils', '/chatgpt']
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

@app.on_message(filters.command('bitcoin'))
async def get_bitcoin(client, message):
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page()
        await page.goto("https://www.google.com/search?q=pre%C3%A7o+do+bitcoin&oq=pre%C3%A7o+&aqs=chrome.1.69i57j35i39l2j0i131i433i512l2j0i457i512j0i402l2j0i67l2.2303j1j7&sourceid=chrome&ie=UTF-8")
        await page.is_visible('.card-section > div:nth-child(2)')
        html = await page.inner_html('.card-section')
        soup = BeautifulSoup(html, 'html.parser')
        price = soup.find('span', {'class': 'pclqee'}).text
        print(f'O preço do bitcoin atual é: {price} BRL')
        await browser.close()

    await message.reply(f'O preço atual do bitcoin é: {price} BRL')

@app.on_message(filters.command('etereum'))
async def get_etereum(client, message):
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page()
        await page.goto("https://www.google.com/search?q=pre%C3%A7o+do+ethereum&sxsrf=AJOqlzX77xFmaY5JDkeLBVKuolYmh3u4Mg%3A1675160680418&ei=aOzYY7eZGZSH1sQPybqEyAo&ved=0ahUKEwi37bDqy_H8AhWUg5UCHUkdAakQ4dUDCA8&uact=5&oq=pre%C3%A7o+do+ethereum&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECCMQJzIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCkoECEEYAEoECEYYAFAAWABgvgloAHABeACAAX-IAX-SAQMwLjGYAQCgAQKgAQHAAQE&sclient=gws-wiz-serp")
        await page.is_visible('.card-section > div:nth-child(2)')
        html = await page.inner_html('.card-section')
        soup = BeautifulSoup(html, 'html.parser')
        price = soup.find('span', {'class': 'pclqee'}).text
        print(f'O preço do etereum atual é: {price} BRL')
        await browser.close()

    await message.reply(f'O preço atual do etereum é: {price} BRL') 

@app.on_message(filters.command('chatgpt'))
async def chatgpt(client, message):
    await message.reply(
        f'Um novo meio de interagir com o ChatGPT'
    )

@app.on_message(filters.command('help') | filters.command('start'))
async def help(client, message):
    print(f"{message.chat.username}: {message.text}")
    await message.reply('Olá, eu sou Luna, um bot em desenvolvimento. \nEu estou sendo criada para suprir diversas necessidades. \nAinda estou em fase de desenvolvimento, mas você pode se divertir com os meus comandos! \nUse: **/commands** para ver todos os meus comandos!')

@app.on_message(filters.command('commands'))
async def ls_commands(client, message):
    await message.reply(
        f'**Aqui está a minha lista de comandos:** \n**/help** - Ajuda com a interação do bot. \n**/commands** - Lista todos os comandos do bot. \n**/pic** - **(BETA)** Retorna uma foto. \n **/utils** - Funções extras do bot. \n /bitcoin - Te permite monitorar o valor do **Bitcoin**. \n /etereum - Te permite monitorar o valor do **Etereum**.')

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
    print(f"{message.chat.username} enviou: {message.text}")
    await message.reply(f'Você enviou: {message.text}')

app.run()

