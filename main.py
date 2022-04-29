import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.tasks import loop
import os
import random
import json
import pandas as pd
from reddit import redShitPost


TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='$')  #, intents=intents)

#Load the james quotes from json
jamesSayings = json.load(open('jamesSayings.json', 'r'))


#Prints to console that the bot is connected
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#Adds reaction to any attachment in text channel, creates random number between 0 and 3 and then it will add 1-3 random emotes if 0 was rolled it wont add one. This uses the array of stored emojis in the json. The json needs to be populated first using the emoji function
    if message.attachments:
        storedemojis = json.load(open('emojiList.json', 'r'))
        rNum = random.randint(0, 3)
        for i in range(1, rNum):
            emoji = random.choice(storedemojis)
            await message.add_reaction(emoji)

    if message.content.startswith('Http'):
        storedemojis = json.load(open('emojiList.json', 'r'))
        rNum = random.randint(0, 3)
        for i in range(1, rNum):
            emoji = random.choice(storedemojis)
            await message.add_reaction(emoji)

#Pulls a random quote from the jamesSayings json
    if message.content.startswith('$quote'):
        await message.channel.send(random.choice(jamesSayings))
    await client.process_commands(message)

@client.command()
async def shitpost(ctx):
  df = pd.DataFrame()
  df = redShitPost(df)
  channel = client.get_channel(201887076977737728)
  rID = random.randint(0,9)
  URL = "https://www.reddit.com" + df.at[rID, 'LINK']
  await channel.send(URL)
  
#Populates the json with the current list of custom emojis formated
@client.command()
async def emojis(ctx):
    emojilist = []
    for emoji in ctx.guild.emojis:
        emojiid = str(emoji.id)
        emojilist.append("<:" + emoji.name + ":" + emojiid + ">")
    with open('emojiList.json', 'w') as f:
        json.dump(emojilist, f)

@client.command()
async def unleash(ctx):
  print("James Bot Unleashed")
  voiceChannelCheck.start(ctx)

@client.command()
async def stats(ctx):
    print("Number of users: ",
          ctx.guild.member_count,
          "Server created at: ",
          ctx.guild.created_at,
          "Region: ",
          ctx.guild.region,
          "Emojis: ",
          ctx.guild.emojis,
          "Channels: ",
          ctx.channel.id,
          sep="\n")


@client.command()
async def command(ctx):
    print("Commands are working")

@loop(minutes=1)
async def voiceChannelCheck(ctx):
  voiceChannels = []
  print("Checking users connected in voice")
  for channel in ctx.guild.voice_channels:
    if len(channel.voice_states.keys()) >= 2:
      voiceChannels.append(channel.id)
  print("These channels have active users ")
  for channel in voiceChannels:
    rNum = random.randint(0, 3)
    #if rNum == 0: 
    rChannel = ctx.guild.get_channel(channel)
    print("Connecting to server")
    await rChannel.connect()
    random_voice.start(ctx)
  print(voiceChannels)
  
@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
        voice_client = ctx.guild.voice_client
        ctx._volume = 0.7
        print("Hello")
        #voice_client.play(discord.FFmpegPCMAudio(source = 'Hello.wav', executable = 'ffmpeg'))
        random_voice.start(ctx)
    else:
        await ctx.send("User must be in a voice channel to use this command")


@client.command(pass_context=True)
async def voiceclip(ctx):
    if (ctx.author.voice):
        rVoiceList = json.load(open('voiceClips.json', 'r'))
        voice_client = ctx.guild.voice_client
        rVoice = "Voiceclips/" + random.choice(rVoiceList)
        voice_client.play(
            discord.FFmpegPCMAudio(source=rVoice, executable='ffmpeg'))


@loop(seconds=5)
async def random_voice(ctx):
    rInt = random.randrange(0, 100)
    print(rInt)
    if rInt == 0:
        await voiceclip(ctx)

@client.command()
async def hello(ctx):
    voice_client = ctx.guild.voice_client
    print("Hello")
    voice_client.play(
        discord.FFmpegPCMAudio(source='Hello.wav', executable='ffmpeg'))


@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        random_voice.stop
        print("Goodbye")
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Good Bye")
    else:
        await ctx.send("I am not in a voice channel")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


#random_voice.before_loop(client.wait_until_ready())

client.run(os.getenv('TOKEN'))
my_secret = os.environ['TOKEN']
