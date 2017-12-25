import discord
from discord.ext import commands
import random
from dateutil.relativedelta import relativedelta
import datetime
import os

bot = commands.Bot(description = "Very very helpful bot. For code visit https://github.com/joegibby/Discord-Bot",
                   command_prefix = ">")

@bot.event
async def on_ready():
    print("Ready")

@bot.command()
async def ping():
    await bot.say("Pong!")

@bot.command()
async def christmas():
    """Tells you how long until Christmas.
    As requested by Adam."""
    today = datetime.datetime.today()
    if today.month == 12 and today.day == 25:
        until = "CHRISTMAS IS TODAY YAY"
    else:
        nextXMasYear = today.year
        if today.month == 12 and today.day >= 25:
            nextXMasYear += 1
        until = "Christmas is in "
        rd = relativedelta(datetime.date(2017,12,25), datetime.datetime.today())
        for a in ("years","months","days","hours","minutes","seconds"):
            if rd.__dict__[a] != 0:
                if until != "Christmas is in ":
                    until += ", "
                until += str(rd.__dict__[a]) + " " + a
    await bot.say(until)

@bot.command()
async def rps():
    """Replies with Rock, Paper or Scissors.
    (You are expected to claim your action after the \"rps\")"""
    await bot.say(("Rock", "Paper", "Scissors")[random.randint(0,2)])

bot.run(os.getenv('BOT_TOKEN'))
#bot.run("") ### DELETE BOT TOKEN WHEN FINISHED EDITS ###
