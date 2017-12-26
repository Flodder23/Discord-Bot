import discord
from discord.ext import commands
import wolframalpha
from dateutil.relativedelta import relativedelta
import datetime

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

def setup(bot):
    bot.add_cog(Info(bot))
