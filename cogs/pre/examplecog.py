from discord.ext import commands
from cogs.pre.utils import checks


class examplecog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.is_cog_contributor()
    @commands.command(name='examplecog')
    async def _example(self, ctx):
        await ctx.send('Hello! I am an example cog.')


def setup(bot):
    bot.add_cog(examplecog(bot))
