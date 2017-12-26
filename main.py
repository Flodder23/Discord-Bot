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

class Games:
    @commands.command()
    async def rps(self):
        """Replies with Rock, Paper or Scissors.
        (You are expected to claim your action after the \"rps\")"""
        await bot.say(random.choice(("Rock", "Paper", "Scissors")))
    @commands.command()
    async def ping(self):
        """Checks the bot is working.
        Should reply with "Pong!\"."""
        await bot.say("Pong!")

    @commands.command(pass_context = True)
    async def spam(self, ctx, *, msg):
        """Sends some spam.
        You can specify how much spam and what to spam with a number after the >spam command
        eg. >spam 5 Hello There! would sens "Hello There!" 5 times."""
        msg.split(" ")
        try:
            if int(msg[0]) > 50:
                await bot.say("That is too much spam. I will only spam 50x")
                msg[0] = "50"
            try:
                for _ in range(int(msg[0])):
                    await bot.say(msg[1:])
            except:
                for _ in range(int(msg[0])):
                    await bot.say("This is spam.")
        except:
            for _ in range(10):
                await bot.say("This is spam.")

class Info:
    @commands.command()
    async def christmas(self):
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

    @commands.command()
    async def calc(self, *, msg):
        """Performs the desired calculation.
        To use pi etc. type \"math.pi\"
        (Please do not use for evil! Thanks.)
        (also, I can't do algebra etc. yet.)"""
        if not ("os" in msg.lower() or
                "quit" in msg.lower() or
                "while" in msg.lower() or
                "if" in msg.lower() or
                "await" in msg.lower() or
                "print" in msg.lower() or
                "import" in msg.lower()):
            if "math" in msg:
                import math
            try:
                await bot.say(msg + " = " + str(eval(msg)))
            except:
                await bot.say("Sorry, something went wrong.")
        else:
            await bot.say("Stop trying to hack me.")

    @commands.command(pass_context = True)
    async def poll(self, ctx, *, msg):
        """Creates a poll.
        The poll should be in the following form:
        >poll question; option1; option2; optionX"""
        print("Polling...")
        msg=msg.split(";")
        print(msg)
        output = ctx.message.author.name + " asked " + msg[0] + "\n"
        for option in range(1, len(msg) - 1):
            output += ":regional_indicator_" + chr(96 + option) + ": " + msg[option] + "\n"
        await bot.say(output + "\n React with your answer!")

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
                                   random.choice(("I choose... ",
                                                 "How about ",
                                                 "I'd go for ")) +
                                   random.choice(Members))
    await bot.process_commands(msg)

bot.add_cog(Games())
bot.add_cog(Info())

if os.getenv('BOT_TOKEN') == None:
    print("Running using locally stored value for token")
    bot.run(open("token.txt", "r").read())
else:
    print("Running using Heroku config value for token")
    bot.run(os.getenv('BOT_TOKEN'))

