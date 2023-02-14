import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os
import voicecontrol
import textcontrol
import random

TOKEN = os.environ['TOKEN']
my_secret = os.environ['TOKEN']

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='$') #, intents=intents)

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

@client.command()
async def dall(ctx):
  message = ctx.message
  print("Dall-E Requested")
  await textcontrol.dall(ctx, message)
  
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
#@client.event
#async def on_message(message):
  #if message.author == client.user:
     # return
 # await textcontrol.addemoji(message, client)

@client.event
async def on_message(message):
  await client.process_commands(message)
  ctx = await client.get_context(message)
  if message.author.id == "914322058383609947":
    print("Searching Dall-E for Zeitgeist Bot")
    await textcontrol.dall(ctx, message)
  else:
    if message.author.bot == True or message.content.startswith('$'):
      return
    rInt = random.randrange(0, 9)
    print("Die rolled for picture generation:")
    print(rInt)
    if rInt == 0:
        print("0 Rolled searching Dall-E")
        await textcontrol.dall(ctx, message)
    else: 
      return
  
        
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error    

client.run(os.getenv('TOKEN'))
