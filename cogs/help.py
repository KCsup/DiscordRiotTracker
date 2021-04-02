import discord
from discord.ext import commands
import util.common as common

class Help(commands.Cog):
    common = common.Common()

    def __init__(self, client):
        self.client: commands.Bot = client

    @commands.command()
    async def help(self, ctx: commands.Context):
        if ctx.channel.id == self.common.botChannelId:
            c = ''
            for x in self.client.commands:
                if not x.hidden:
                    c = c + '   ' + x.name + '\n'
            await ctx.send('```' +
                           'Current Commands: \n' + c
                           + '```')
            print(c)

def setup(client):
    client.add_cog(Help(client))