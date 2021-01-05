from discord.ext.commands import errors

# The class for the error "NotAContributorError", which is raised in the checks.py file.
class NotAContributorError(errors.CheckFailure):
    pass
