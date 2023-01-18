from os import getenv
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

app = Client(
    'SelunaBot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_BOT_TOKEN')
)

@app.on_message()
async def messages(client, message):
    print(message.chat.username, message.text)
    await message.reply(message.text + '????')


# async def main():
#     await app.start()
#     await app.send_message('@Nevestpq', 'Seja bem vindo ao meu mundo!')
#     await app.stop()

app.run()