import discord
from discord.ext import commands
import random
import youtube_dl

TOKEN = "NTE5Njc4NjYzOTk4OTYzNzEz.DzJtbw.1UVoqTqFY3ZmhChbelYa5pNm6xo"

bot = commands.Bot(command_prefix = '!')

list_gay = [
        'gay-google-1.mp3',
        'gay-google-2.mp3',
        'gay-google-3.mp3',
        'quay-len.mp3'
    ]

list_chui = [
        'google-1.mp3',
        'google-2.mp3',
        'hung-1.mp3',
        'huy-1.mp3',
        'chui-google-1.mp3',
        'dan-hang-ngang.mp3',
        'viper-thua-mid.mp3',
        'con-cac.mp3',
        'xam-lon.mp3',
        'dm-Kun.mp3',
        'chich-ca-nha.mp3',
        'game-xam-lon.mp3',
        'ko-chat-xam.mp3',
        'quang-hai.mp3',
        'solo-mid.mp3',
        'zeratul.mp3'
    ]

players = {}
queues = {}

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def join(ctx):
    author = ctx.message.author
    channel = author.voice.voice_channel
    await bot.join_voice_channel(channel)

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

@bot.command(pass_context=True)
async def chui(ctx):
    global list_chui
    server = ctx.message.server
    if bot.is_voice_connected(server):
        voice_client = bot.voice_client_in(server)
    else:
        author = ctx.message.author
        channel = author.voice.voice_channel
        await bot.join_voice_channel(channel)
        voice_client = bot.voice_client_in(server)
    player = voice_client.create_ffmpeg_player(random.choice(list_chui), after=lambda: check_queue(server.id))
    if server.id in queues:
        queues[server.id].append(player)
        await bot.say('Voice queued.')
    else:
        queues[server.id] = [player]
    player.start()

@bot.command(pass_context=True)
async def danhang(ctx):
    global list_gay
    server = ctx.message.server
    if bot.is_voice_connected(server):
        voice_client = bot.voice_client_in(server)
    else:
        author = ctx.message.author
        channel = author.voice.voice_channel
        await bot.join_voice_channel(channel)
        voice_client = bot.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('dan-hang-ngang.mp3', after=lambda: check_queue(server.id))
    if server.id in queues:
        queues[server.id].append(player)
        await bot.say('Voice queued.')
    else:
        queues[server.id] = [player]
    player.start()

@bot.command(pass_context=True)
async def gay(ctx):
    global list_gay
    server = ctx.message.server
    if bot.is_voice_connected(server):
        voice_client = bot.voice_client_in(server)
    else:
        author = ctx.message.author
        channel = author.voice.voice_channel
        await bot.join_voice_channel(channel)
        voice_client = bot.voice_client_in(server)
    player = voice_client.create_ffmpeg_player(random.choice(list_gay), after=lambda: check_queue(server.id))
    if server.id in queues:
        queues[server.id].append(player)
        await bot.say('Voice queued.')
    else:
        queues[server.id] = [player]
    player.start()


bot.run(TOKEN)
