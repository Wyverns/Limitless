from discord.ext import commands
from cogs.pre.utils.errors import NotAContributorError


def is_cog_contributor():
    async def predicate(ctx):
        if str(ctx.author.id) in ctx.bot.contributors:
            return True
        else:
            raise NotAContributorError()
    return commands.check(predicate)
