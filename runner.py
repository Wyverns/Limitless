import discord
from discord.ext import commands
import json
from os import getenv

with open('cogs.json', 'r') as cog_file:
    cogs = json.load(cog_file)


class BotClass(commands.Bot):
    def __init__(self, **kwargs):
        self.token = kwargs.pop('token')
        super().__init__(**kwargs)

    def load_cogs(self):
        for cog in cogs:
            self.load_extension(cog['path-to-cog'])

    def starter(self):
        try:
            self.load_cogs()
            self.run(self.token)
        except Exception as e:
            print('Failed to connect to discord.', e)
            exit()


bot_credentials = {
    "token": getenv('TOKEN'),
    "command_prefix": "!"
}

bot = BotClass(**bot_credentials)

@bot.event
async def on_ready():
    print('Bot connected')

if __name__ == '__main__':
    bot.starter()
