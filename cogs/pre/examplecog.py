from discord.ext import commands
from cogs.utils import checks


class examplecog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @checks.is_cog_contributor()
    @commands.command(name='examplecog')
    async def _example(self, ctx):
        """An example command called examplecog. It's really simple. When run, a message will be sent with content of 'Hello! I am an example cog."""
        await ctx.send('Hello! I am an example cog.')


def setup(bot):
    bot.add_cog(examplecog(bot))
