import discord
import os

from discord.ext.commands import CommandNotFound
from discord.ext import commands
import time
import datetime
import asyncio
import apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()
bot = commands.Bot(command_prefix = "/")
print("started Deutschlandbot")

@bot.event
async def on_ready():
    global vc
    print(f'We have logged in as {bot.user} at {datetime.datetime.now()}')
    voicechannel = bot.get_channel(int(os.environ.get('VOICE_CHANNEL')))
    vc = await voicechannel.connect()

@bot.command()
async def deutschland(ctx):
    #if ctx.message.author.server_permissions.administrator:
    await startDeutschland()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

async def startDeutschland():
    global vc
    if not vc.is_playing():
        print('DEUTSCHLAND')
        vc.play(discord.FFmpegPCMAudio("Deutschland.m4a"), after=lambda e: print('fertig gedeutschlanded'))
    
async def announceDeutschland():
    print('Gleich ist Halb Vier')
    channel = bot.get_channel(int(os.environ.get('ANNOUNCEMENT_CHANNEL')))
    await channel.send('@everyone Gleich ist Halb Vier! Kommt in den Halb Vier Voice Channel!')

#Schedulers
scheduler.add_job(announceDeutschland, 'cron', hour='3', minute='25')
scheduler.add_job(startDeutschland, 'cron', hour='3', minute='30')
scheduler.add_job(announceDeutschland, 'cron', hour='15', minute='25')
scheduler.add_job(startDeutschland, 'cron', hour='15', minute='30')
scheduler.start()

token = os.environ.get('BOT_TOKEN')

bot.run(token)