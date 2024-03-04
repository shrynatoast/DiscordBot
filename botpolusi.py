import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Bot telah berhasil terhubung sebagai {bot.user.name}')


@bot.command()
async def halo(ctx):
    await ctx.send('Halo! ')


@bot.command()
async def bantuan(ctx):
    embed = discord.Embed(
        title="daftar",
        description="Daftar perintah yang tersedia:",
        color=discord.Color.blue()
    )
    embed.add_field(name="!poin1", value="penjelasan bagaimana cara mengurai sampah menjadi seni", inline=False)
    embed.add_field(name="!poin2", value="contoh kerajinan seni dari barang bekas", inline=False)
    embed.add_field(name="!poin3", value="alat dan bahan", inline=False)
    embed.add_field(name="!poin4", value="langkah langkah", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def poin1(ctx):
    await ctx.send('Pengurangan Limbah: Salah satu tujuan utama adalah mengurangi jumlah sampah yang masuk ke tempat pembuangan akhir atau berakhir di lingkungan. Dengan mengubah sampah menjadi barang yang berguna atau dekoratif, kita dapat meminimalkan dampak negatifnya terhadap lingkungan.')
    await ctx.send('Halo! ')

@bot.command()
async def poin2(ctx):
    with open('image/contoh.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send('berikut hasil kerajinan barang bekas ')
    await ctx.send(file=picture)


bot.run('TOKEN_BOT')
