import discord
from discord.ext import commands
import wolframalpha
from dateutil.relativedelta import relativedelta
import datetime
import google
from PyDictionary import PyDictionary
import random

class Info:
    def __init__(self, bot):
        self.bot = bot

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
        await self.bot.say(until)

    @commands.command(pass_context = True)
    async def calc(self, ctx, *, msg):
        """Performs the desired calculation.
        Goes through WolframAlpha."""
        client = wolframalpha.Client("TVYA5X-8E78YXA7JL")
        res = client.query(msg)
        em = discord.Embed()
        for pod in res.pods:
            for sub in pod.subpods:
                em.set_image(url=sub["img"]["@src"])
                await self.bot.say(embed=em)

    @commands.command(pass_context = True)
    async def poll(self, ctx, *, msg):
        """Creates a poll.
        The poll should be in the following form:
        >poll question; option1; option2; etc."""
        msg=msg.split(";")
        output = "**" + ctx.message.author.name + "** asked **" + msg[0] + "**\n"
        for option in range(1, len(msg)):
            output += ":regional_indicator_" + chr(96 + option) + ": " + msg[option] + "\n"
        await self.bot.say(output + "\n React with your answer!")

    @commands.command()
    async def google(self, *, query):
        """Returns he results of a google search.
        Should be written as:
            >google [no. of results] [query]
        eg.:
            >google 5 cat videos"""
        try:
            no_requested = int(query.split(" ")[0])
            query = query.split(" ")
            q = ""
            for a in query[1:]:
                q += a + " "
            query = q
        except:
            no_requested = 5
        results = google.search(query, start=0, stop=no_requested*2)
        urls = []
        for url in results:
            urls.append(url)

        ignore = []
        for a in range(len(urls)):
            for b in range(len(urls)):
                if a != b and urls[a] in urls[b]:
                    ignore.append(b)
        no_given = 0
        for a in range(len(urls)):
            if not a in ignore:
                no_given += 1
                if no_given <= no_requested:
                    await self.bot.say(urls[a])
                else:
                    break
    @commands.command()
    async def define(self, word):
        """Defines the given word.
        This one sometimes takes a while to go through."""
        try:
            d = PyDictionary().meaning(word).items()
            output = ""
            for a in d:
                output += "\n\n**" + a[0] + "**"
                for b in a[1]:
                    output += "\n" + b
        except:
            ouput = "Sorry, something went wrong."
        await self.bot.say(output)

    @commands.command()
    async def choose(self, *, choices):
        """Selects a choice at random for you.
        seperate choices with semi-colons, like:
            choice1; choice2; choice3; etc."""
        await self.bot.say(random.choice(choices.split(";")))

def setup(bot):
    bot.add_cog(Info(bot))
