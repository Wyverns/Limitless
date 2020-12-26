import discord
from discord.ext import commands
import json

with open('cogs.json', 'r') as cog_file:
    cogs = json.load(cog_file)


class botclass(commands.Bot):
    def __init__(self, **kwargs):
        self.token = kwargs.pop('token')
        super().__init__(**kwargs)

    def load_cogs(self):
        for cog in cogs:
            self.load_extension(cog['path-to-cog'])

    def starter(self):
        try:
            self.run(self.token)
        except Exception as e:
            print('Failed to connect to discord.', e)
            exit()

bot_credentials = {
    "token":"WIP-NO-TOKEN-YET",
    "command_prefix":"!"
}

bot = botclass(**bot_credentials)

if __name__ == '__main__':
    bot.starter()