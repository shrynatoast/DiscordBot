import discord
from characterai import PyCAI
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

client = PyCAI('TOKEN') #Char_token

char = 'CHAR' #ganti CHAR dengan code karakter c.ai yang di inginkan

chat = client.chat.get_chat(char)

participants = chat['participants']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def msg(ctx, *, pesan: str):
    # Mengirimkan pesan yang diterima sebagai input setelah perintah !msg

    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']

    data = client.chat.send_message(
        chat['external_id'], tgt, pesan
    )

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    await ctx.send(f"{name}: {text}")

bot.run("TOKEN_BOT_DISINI")
