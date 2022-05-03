import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.tasks import loop
import os
import random
import json
import pandas as pd
from discord.ext.tasks import loop

import voicecontrol
import textcontrol
import stats
import reddit


TOKEN = os.environ['TOKEN']
my_secret = os.environ['TOKEN']

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='$')  #, intents=intents)
client.run(os.getenv('TOKEN'))

#On startup
#Prints to console that the bot is connected
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
  
#Voice related Commands
#Starts checking if channels are populated
@client.command()
async def unleash(ctx):
  print("James Bot Unleashed")
  voicecontrol.voiceChannelCheck.start(ctx)

#Joins command user's voice channel
@client.command()
async def join(ctx):
  voicecontrol.join(ctx)
  voicecontrol.random_voice.start(ctx)

#Plays random voice clip
@client.command()
async def clip(ctx):
  voicecontrol.voiceclip(ctx)

#Plays hello voice clip
@client.command()
async def hello(ctx):
  voicecontrol.hello(ctx)

#Leaves the voice channel
@client.command()
async def leave(ctx):
  voicecontrol.leave(ctx)

#Text Events  
@client.command()
async def shitpost(ctx, client):
  textcontrol.shitpost(ctx, client)

@client.command()
async def emojis(ctx):
  textcontrol.emojis(ctx)

@client.command()
async def commands(ctx):
    print("Commands are working")

#On Events
async def on_message(message, client):
    if message.author == client.user:
        return
    textcontrol.addemoji(message)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


