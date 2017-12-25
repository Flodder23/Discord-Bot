import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import math
from dateutil.relativedelta import relativedelta
import datetime
import os

Client = discord.Client()
client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print("Ready")

@client.event
async def on_message(message):
    if message.author.id != "394502938094993410" :
        if message.content.lower() in ("rock", "paper", "scissors"):
            await client.send_message(message.channel, ("<@%s>" % message.author.id + "   " + ("Rock", "Paper", "Scissors")[random.randint(0,2)]))

        if "christmas" in message.content.lower():
            await client.send_message (message.channel, "CHRISTMAS IS TODAY YAY")
#            until = "<@%s> Christmas is in " % message.author.id
#            rd = relativedelta(datetime.date(2017,12,25), datetime.datetime.today())
#            for a in ("years","months","days","hours","minutes","seconds"):
#                if rd.__dict__[a] != 0:
#                    if until != "<@%s> Christmas is in " % message.author.id:
#                        until += ", "
#                    until += str(rd.__dict__[a]) + " " + a
#            await client.send_message (message.channel, until)

    if "<@!162716870506577920>" in message.content :# or "matej" in message.content.lower():
        await client.send_message(message.channel, ("Light theme sucks.", "Never take a shot of really hot sauce.")[random.randint(0,1)])

client.run(os.getenv('BOT_TOKEN'))
