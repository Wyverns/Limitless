from discord.ext import commands
from cogs.pre.utils.errors import NotAContributorError


# Check if whoever used the command is in the bot's contributors.
def is_cog_contributor():
    
    async def predicate(ctx):
        
        # If statement, checking if the author of the command is in a list (int) of IDs stored inside the bot.
        if str(ctx.author.id) in ctx.bot.contributors:
            return True
        else:
            raise NotAContributorError(f"Command {ctx.command.name} raised an error: {str(ctx.author)} is not a contributor.") # A custom error, along with a message for some info.
    
    # Simply return a commands.check(bool), the bool returned from the async function defined above, predicate.
    return commands.check(predicate)
