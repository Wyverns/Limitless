from discord.ext import commands
from cogs.pre.utils import checks # You can make your own utils, or use the pre-made utils we have.


class examplecog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # An example command called examplecog. It's really simple. When run, a message will be sent with content of 'Hello! I am an example cog.'
    @checks.is_cog_contributor()
    @commands.command(name='examplecog')
    async def _example(self, ctx):
        await ctx.send('Hello! I am an example cog.')


def setup(bot):
    bot.add_cog(examplecog(bot))
