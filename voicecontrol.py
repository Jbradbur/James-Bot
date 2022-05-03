import discord
import random
import json
from discord.ext.tasks import loop

async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
        ctx._volume = 0.7
        print("Hello")
        await hello(ctx)
    else:
        await ctx.send("User must be in a voice channel to use this command")

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

async def hello(ctx):
    voice_client = ctx.guild.voice_client
    print("Hello")
    voice_client.play(
        discord.FFmpegPCMAudio(source='Hello.wav', executable='ffmpeg'))

async def leave(ctx):
    if (ctx.voice_client):
        random_voice.stop
        print("Goodbye")
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Good Bye")
    else:
        await ctx.send("I am not in a voice channel")

@loop(minutes=1)
async def voiceChannelCheck(ctx):
  voiceChannels = []
  print("Checking users connected in voice")
  for channel in ctx.guild.voice_channels:
    if len(channel.voice_states.keys()) >= 3:
      voiceChannels.append(channel.id)
  print("These channels have active users ")
  for channel in voiceChannels:
    rNum = random.randint(0, 59)
    if rNum == 0: 
      rChannel = ctx.guild.get_channel(channel)
    print("Connecting to server")
    await rChannel.connect()
    random_voice.start(ctx)
  print(voiceChannels)
  