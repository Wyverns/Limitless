from discord.ext.commands import errors


class NotAContributorError(errors.CheckFailure):
    pass
