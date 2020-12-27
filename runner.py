from discord.ext import commands
import json
from os import getenv

with open('cogs.json', 'r') as cog_file:
    cogs = json.load(cog_file)


class BotClass(commands.Bot):
    def __init__(self, **kwargs):
        self.token = kwargs.pop('token')
        self.contributors = None
        super().__init__(**kwargs)

    def before_starter(self):
        self.load_cogs()
        self.get_contributors()

    def get_contributors(self):
        contributors = []
        for cog in cogs:
            contributors.append(cog['discord_id'])
        self.contributors = contributors

    def load_cogs(self):
        for cog in cogs:
            self.load_extension(cog['path-to-cog'])

    def starter(self):
        self.before_starter()
        self.run(self.token)


bot_credentials = {
    "token": getenv('TOKEN'),
    "command_prefix": "!"
}

bot = BotClass(**bot_credentials)


@bot.event
async def on_ready():
    print('Bot connected')


@bot.event
async def on_message(message):
    if message.author.id == bot.id:
        return


if __name__ == '__main__':
    bot.starter()
