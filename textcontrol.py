from discord.ext.tasks import loop
import random
import json
import pandas as pd
import reddit

#Load the james quotes from json
jamesSayings = json.load(open('jamesSayings.json', 'r'))

async def addemoji(message, client):
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
  if message.content.contains('james'):
    await message.channel.send(random.choice(jamesSayings))
    await client.process_commands(message)

async def shitpost(ctx, client):
  df = pd.DataFrame()
  df = reddit.redShitPost(df)
  channel = client.get_channel(201887076977737728)
  rID = random.randint(0,9)
  URL = "https://www.reddit.com" + df.at[rID, 'LINK']
  await channel.send(URL)

#Populates the json with the current list of custom emojis formated
async def emojis(ctx):
    emojilist = []
    for emoji in ctx.guild.emojis:
        emojiid = str(emoji.id)
        emojilist.append("<:" + emoji.name + ":" + emojiid + ">")
    with open('emojiList.json', 'w') as f:
        json.dump(emojilist, f)

async def commandClean(message):
  if message.content.startswith('$'):
    await message.delete()