from discord.ext import commands
from runner import BotClass


def is_cog_contributor():
    async def predicate(ctx):
        return str(ctx.author) in
    return commands.check(predicate)
