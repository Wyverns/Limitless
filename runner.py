# This file is for running the bot, and handling some configs. If you want to add your Cog, this might not be the correct place to be.
# Unless you are adding something to the bot class, e.g. a list, please refer to the README.md file.

from discord.ext import commands
import json
import configparser

# Define config
config = configparser.ConfigParser()
config.read('secrets.cfg')

# Load the cogs JSON file, and load it, defining a variable named cogs.
with open('cogs.json', 'r') as cog_file:
    cogs = json.load(cog_file)


# The basic Bot class.
class BotClass(commands.Bot):
    def __init__(self, **kwargs):
        self.token = kwargs.pop('token')
        self.contributors = None
        super().__init__(**kwargs)

    def before_starter(self):
        self.load_cogs()
        self.get_contributors()

    # Get the list of contributors. You can also add your own method here.
    def get_contributors(self):
        contributors = []
        for cog in cogs:
            contributors.append(cog['discord_id'])
        self.contributors = contributors
    
    # Simply load the cogs list we defined earlier, by iterating through it, then loading the path through the code.
    def load_cogs(self):
        for cog in cogs:
            self.load_extension(cog['path-to-cog']) # path-to-cog is defined in cogs.json, for each cog! Remember to add the correct path to it.

    def starter(self):
        self.before_starter()
        self.run(self.token)


bot_credentials = {
    "token": config['TOKENS']['bottoken'],
    "command_prefix": '!'
}

bot = BotClass(**bot_credentials)


@bot.event
async def on_ready():
    print('Bot connected')


if __name__ == '__main__':
    bot.starter()
