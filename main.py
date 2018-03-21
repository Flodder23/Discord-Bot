import discord
from discord.ext import commands
import random
import os
import asyncio
import datetime
from info_ext import get_time_until_xmas

Token = os.getenv("BOT_TOKEN")
if Token is None:
    Token = open("token.txt", "r").read()
    print("Running using locally stored value for token")
    bot = commands.Bot(description="Open source Discord bot. For code visit https://github.com/joegibby/Discord-Bot," +
                                   "where you can also make suggestions.\nYou can type \"@anyone\" or \"@someone\" in a message and the bot will choose for you.",
                       command_prefix="<")
else:
    print("Running using Heroku config value for token")
    bot = commands.Bot(description="Open source Discord bot. For code visit https://github.com/joegibby/Discord-Bot, " +
                                   "where you can also make suggestions.\nYou can type \"@anyone\" or \"@someone\" in a message and the bot will choose for you.",
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
    while not bot.is_closed:
        time = os.getenv("TimeToSpamAdam")
        if time is None:
            time = [0, 0]
        else:
            time = time.split("\n")
        if os.getenv("SpamAdam") == "Go ahead":
            today = datetime.datetime.today()
            if today.hour == int(time[0]) and today.minute == int(time[1]):
                await bot.send_message(Adam, get_time_until_xmas(minsec=False))
                await bot.send_message(Joe, get_time_until_xmas(minsec=False))
        
        if os.getenv("SpamNathan") == "Go ahead":
            if random.randint(0, 1000) == 666:
                await bot.send_message(Nathan, "Adam says hi")
                await bot.send_message(Joe, "Adam says hi")
        
        await asyncio.sleep(60)


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Type >help for help"))
    bot.loop.create_task(every_minute())
    bot.load_extension("games_ext")
    bot.load_extension("info_ext")
    print("Ready")
    found = False
    for server in bot.servers:
        for member in server.members:
            if member.id == IDs[3] and not found:
                await bot.send_message(member, random.choice(
                    ("Guess who's back", "Back again", "Shady's back", "Tell a friend")))
                found = True


@bot.event
async def on_message(msg):
    msgTxt = msg.content.lower()
    print("here")
    if "<@!%s>" % IDs[1] in msgTxt:
        try:
            do_it = os.getenv("SpamMatej").split("\n")
            if random.randint(1, int(do_it[1])) < int(do_it[0]):
                await bot.send_message(msg.channel, random.choice(("Light theme sucks.",
                                                                   "Never take a shot of really hot sauce.")))
        except:
            pass
    
    if "<@!%s>" % IDs[2] in msgTxt:
        try:
            do_it = os.getenv("SpamDom").split("\n")
            if random.randint(1, int(do_it[1])) < int(do_it[0]):
                await bot.send_message(msg.channel, "sosig")
        except:
            pass
    
    if msg.author.id != "394502938094993410":  # Bot's own ID
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
        if "step" in msgTxt:
            await bot.send_message(msg.channel, "Oooh <@%s> A cool step question" % IDs[5])
    
    if msgTxt.startswith("i'm ") or msgTxt.startswith("im "):
        if len(msgTxt.content.split()) < 4:
            try:
                do_it = os.getenv("SpamBadJoke").split("\n")
                if random.randint(1, int(do_it[1])) < int(do_it[0]):
                    await bot.send_message(msg.channel, "Hello " + " ".join(msgTxt.split()[1:]) + ", I'm Joe's Bot.")
            except:
                pass
        
    await bot.process_commands(msg)


@bot.event
async def on_command_error(error, ctx):
    if not (error.args[0].startswith("Command ") and error.args[0].endswith(" is not found")):
        await bot.send_message(ctx.message.channel, "Sorry, something went wrong.")


IDs = os.getenv("IDS")
if IDs is None:
    IDs = open("ids.txt", "r").read().split("\n")[:6]
else:
    IDs = IDs.split("\n")

bot.run(Token)
