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
    for server in bot.servers:
        for member in server.members:
            if member.id == IDs[0]:
                Adam = member
            elif member.id == IDs[3]:
                Joe = member
            elif member.id == IDs[4]:
                Nathan = member
    time = os.getenv("TimeToSpam")
    if time is None:
        time = [0, 0]
    else:
        time = time.split("\n")
    while not bot.is_closed:
        if os.getenv("SpamAdam") == "Go ahead":
            today = datetime.datetime.today()
            if today.hour == int(time[0]) and today.minute == int(time[1]):
                await bot.send_message(Adam, get_time_until_xmas(minsec = False))
                await bot.send_message(Joe, get_time_until_xmas(minsec=False))

        if os.getenv("SpamNathan") == "Go ahead":
            if random.randint(0, 1000) == 666:
                await bot.send_message(Nathan, "Adam says hi")
                await bot.send_message(Joe, "Adam says hi")

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
    if "<@!%s>" % IDs[1] in msgTxt and os.getenv("SpamMatej") == "Go ahead":
        await bot.send_message(msg.channel, random.choice(("Light theme sucks.",
                                                           "Never take a shot of really hot sauce.")))
    if "<@!%s>" % IDs[2] in msgTxt and os.getenv("SpamDom") == "Go ahead":
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
    IDs = open("ids.txt", "r").read().split("\n")[:5]
else:
    IDs = IDs.split("\n")
bot.loop.create_task(every_minute())

if os.getenv('BOT_TOKEN') is None:
    print("Running using locally stored value for token")
    bot.run(open("token.txt", "r").read())
else:
    print("Running using Heroku config value for token")
    bot.run(os.getenv('BOT_TOKEN'))
