import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os
import voicecontrol
import textcontrol

TOKEN = os.environ['TOKEN']
my_secret = os.environ['TOKEN']

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='$')  #, intents=intents)

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
  await voicecontrol.voiceChannelCheck.start(ctx)
  
#Joins command user's voice channel
@client.command()
async def join(ctx):
  await voicecontrol.join(ctx)
  await voicecontrol.random_voice.start(ctx)

#Plays random voice clip
@client.command()
async def clip(ctx):
  await voicecontrol.voiceclip(ctx)

#Plays hello voice clip
@client.command()
async def hello(ctx):
  await voicecontrol.hello(ctx)

#Leaves the voice channel
@client.command()
async def leave(ctx):
  await voicecontrol.leave(ctx)
  
#Text Events  
@client.command()
async def shitpost(ctx):
  await textcontrol.shitpost(ctx, client)
  
@client.command()
async def emojis(ctx):
  await textcontrol.emojis(ctx)

@client.command()
async def commands(ctx):
    print("Commands are working")

#On Events
@client.event
async def on_message(message):
  if message.author == client.user:
      return
  await textcontrol.addemoji(message, client)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error    

client.run(os.getenv('TOKEN'))
