import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.tasks import loop
import os
import random
import json
import pandas as pd
from reddit import redShitPost
from discord.ext.tasks import loop
import voicecontrol


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
