import discord
from discord.ext import commands
import random
import os

if os.getenv('BOT_TOKEN') is None:
    bot = commands.Bot(description="Very very helpful bot. For code visit https://github.com/joegibby/Discord-Bot",
                       command_prefix="<")
else:
    bot = commands.Bot(description="Very very helpful bot. For code visit https://github.com/joegibby/Discord-Bot",
                       command_prefix=">")


@bot.event
async def on_ready():
    print("Ready")
    await bot.change_presence(game=discord.Game(name="Type >help for help"))
    bot.load_extension("games_ext")
    bot.load_extension("info_ext")


@bot.event
async def on_message(msg):
    msgTxt = msg.content.lower()
    if "<@!162716870506577920>" in msgTxt:  # or "matej" in msgTxt:
        await bot.send_message(msg.channel, (random.choice(
            ("Light theme sucks.",
             "Never take a shot of really hot sauce."))))
    if msg.author.id != "394502938094993410":
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


if os.getenv('BOT_TOKEN') is None:
    print("Running using locally stored value for token")
    bot.run(open("token.txt", "r").read())
else:
    print("Running using Heroku config value for token")
    bot.run(os.getenv('BOT_TOKEN'))
