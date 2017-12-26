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
    """Checks the bot is working.
    Should reply with "Pong!\"."""
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
        rd = relativedelta(datetime.date(nextXMasYear,12,25), datetime.datetime.today())
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
    await bot.say(random.choice(("Rock", "Paper", "Scissors")))

@bot.command()
async def calc(*, message):
    """Performs the desired calculation.
    To use pi etc. type \"math.pi\"
    (Please do not use for evil! Thanks.)
    (also, I can't do algebra etc. yet.)"""
    if "math" in message:
        import math
    await bot.say(message + " = " + str(eval(message)))

@bot.event
async def on_message(msg):
    msgTxt = msg.content.lower()
    if "<@!162716870506577920>" in msgTxt :# or "matej" in msgTxt:
        await bot.send_message(msg.channel, (random.choice(
            ("Light theme sucks.",
             "Never take a shot of really hot sauce."))))
    if msg.author.id != "394502938094993410" :
        if "@someone" in msgTxt or "@anyone" in msgTxt:
            members = msg.server.members
            Members = []
            for member in members:
                Members.append(member.mention)
            await bot.send_message(msg.channel,
                                   Members[random.randint(0,len(Members)-1)])
    await bot.process_commands(msg)

if os.getenv('BOT_TOKEN') == None:
    print("Running using locally stored value for token")
    bot.run(open("token.txt", "r").read())
else:
    print("Running using Heroku config value for token")
    bot.run(os.getenv('BOT_TOKEN'))

