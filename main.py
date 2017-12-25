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
    msgTxt = message.content.lower()
    if message.author.id != "394502938094993410" :
        if msgTxt.startswith(">rock") or msgTxt.startswith(">paper") or msgTxt.startswith(">scissors"):
            await client.send_message(message.channel, (message.author.mention + "   " + ("Rock", "Paper", "Scissors")[random.randint(0,2)]))

        if msgTxt.startswith(">help"):
            import help_message
            output = ""
            if msgTxt == ">help":
                output = help_message.message["general"]
            else:
                try:
                    output = help_message.message[msgTxt[6:]]
                except:
                    output = "That doesn't seem to be something I can help you with."
            await client.send_message(message.channel, output)

        if msgTxt.startswith(">christmas"):
            today = datetime.datetime.today()
            if today.month == 12 and today.day == 25:
                until = message.author.mention + " CHRISTMAS IS TODAY YAY"
            else:
                nextXMasYear = today.year
                if today.month == 12 and today.day >= 25:
                    nextXMasYear += 1
                until = message.author.mention + " Christmas is in "
                rd = relativedelta(datetime.date(2017,12,25), datetime.datetime.today())
                for a in ("years","months","days","hours","minutes","seconds"):
                    if rd.__dict__[a] != 0:
                        if until != message.author.mention + " Christmas is in ":
                            until += ", "
                        until += str(rd.__dict__[a]) + " " + a
            await client.send_message (message.channel, until)

        if "@someone" in msgTxt or "@anyone" in msgTxt:
            members = message.server.members
            Members = []
            for member in members:
                Members.append(member.mention)
            await client.send_message(message.channel, Members[random.randint(0,len(Members)-1)])            

    if "<@!162716870506577920>" in msgTxt :# or "matej" in msgTxt:
        await client.send_message(message.channel, ("Light theme sucks.", "Never take a shot of really hot sauce.")[random.randint(0,1)])

client.run(os.getenv('BOT_TOKEN'))
#client.run("") ### DELETE BOT TOKEN WHEN FINISHED EDITS ###
