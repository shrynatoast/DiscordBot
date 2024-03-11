import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot telah berhasil terhubung sebagai {bot.user.name}')


@bot.command()
async def bantuan(ctx):
    embed = discord.Embed(
        title="daftar",
        description="Daftar perintah yang tersedia:",
        color=discord.Color.blue()
    )
    embed.add_field(name="!penjelasan", value="tujuan project bot ini", inline=False)
    embed.add_field(name="!contoh", value="contoh kerajinan seni dari barang bekas", inline=False)
    embed.add_field(name="!alat", value="", inline=False)
    embed.add_field(name="!pembuatan", value="", inline=False)
    embed.add_field(name="Bonus", value="coba katakan 'hai', sambil menyebut namanya ( iroha ) ", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def contoh(ctx):
    with open('image/contoh.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('berikut contoh kerajinan barang bekas ')
    await ctx.send(file=picture)

@bot.command()
async def penjelasan(ctx):
    await ctx.send('Pengurangan Limbah: Salah satu tujuan utama adalah mengurangi jumlah sampah yang masuk ke tempat pembuangan akhir atau berakhir di lingkungan. Dengan mengubah sampah menjadi barang yang berguna atau dekoratif, kita dapat meminimalkan dampak negatifnya terhadap lingkungan.')

@bot.command()
async def pembuatan(ctx):
    await ctx.send('teks')

@bot.command()
async def alat(ctx):
    await ctx.send('teks')


bot.run('t o k e n')
