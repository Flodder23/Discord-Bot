import discord
from discord.ext import commands
import random
import os
import asyncio
import datetime
from info_ext import get_time_until_xmas

if os.getenv('BOT_TOKEN') is None:
    bot = commands.Bot(description="Very very helpful bot. For code visit https://github.com/joegibby/Discord-Bot",
                       command_prefix="<")
else:
    bot = commands.Bot(description="Very very helpful bot. For code visit https://github.com/joegibby/Discord-Bot",
                       command_prefix=">")



async def every_minute():
    await bot.wait_until_ready()
    Adam = []
    for server in bot.servers:
        for member in server.members:
            if member.id in (IDs[3]):#, IDs[0]): #Adam
                Adam.append(member)
    if not Adam == []:
        while not bot.is_closed:
            today = datetime.datetime.today()
            if today.hour == 0 and today.minute == 0:
                for a in Adam:
                    await bot.send_message(a, get_time_until_xmas(minsec = False))
            await asyncio.sleep(60)

@bot.event
async def on_ready():
    print("Ready")
    await bot.change_presence(game=discord.Game(name="Type >help for help"))
    bot.load_extension("games_ext")
    bot.load_extension("info_ext")


@bot.event
async def on_message(msg):
    msgTxt = msg.content.lower()
    if "<@!%s>" % IDs[1] in msgTxt:  # or "matej" in msgTxt:
        await bot.send_message(msg.channel, random.choice(("Light theme sucks.",
                                                           "Never take a shot of really hot sauce.")))
    if "<@!%s>" % IDs[2] in msgTxt:
        await bot.send_message(msg.channel, "sosig")
    if msg.author.id != "394502938094993410": #Bot's own ID
        if "@someone" in msgTxt or "@anyone" in msgTxt:
            members = msg.server.members
            Members = []
            for member in members:
                Members.append(member.mention)
            await bot.send_message(msg.channel,
                                   random.choice(("I choose... ",
                                                  "How about ",
                                                  "I'd go for ")) +
                                   random.choice(Members))
    await bot.process_commands(msg)


@bot.event
async def on_command_error(error, ctx):
    await bot.send_message(ctx.message.channel, "Sorry, something went wrong.")


IDs = os.getenv("IDS")
if IDs is None:
    IDs = open("ids.txt", "r").read().split("\n")[:4]
else:
    IDs = IDs.split("\n")
bot.loop.create_task(every_minute())

if os.getenv('BOT_TOKEN') is None:
    print("Running using locally stored value for token")
    bot.run(open("token.txt", "r").read())
else:
    print("Running using Heroku config value for token")
    bot.run(os.getenv('BOT_TOKEN'))
