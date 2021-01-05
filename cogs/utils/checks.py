from discord.ext import commands
from cogs.utils.errors import NotAContributorError


def is_cog_contributor():
    """Check if whoever used the command is in the bots contributors."""
    async def predicate(ctx):

        if str(ctx.author.id) in ctx.bot.contributors:
            return True
        else:
            raise NotAContributorError(f"Command {ctx.command.name} raised an error: {str(ctx.author)} is not a contributor.")

    return commands.check(predicate)


def is_in_guilds(*guild_ids):
    """Checks if the user who invoked the command is in X guilds."""
    async def predicate(ctx):

        guild = ctx.guild
        if guild is None:
            return False

        return guild.id in guild_ids

    return commands.check(predicate)