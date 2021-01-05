from discord.ext.commands import errors


class NotAContributorError(errors.CheckFailure):
    """The class for the error "NotAContributorError", which is raised in the checks.py file."""
    pass
