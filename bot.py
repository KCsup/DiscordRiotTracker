import discord
from discord.ext import commands
import json
import valorant
import riotwatcher
from riotwatcher import LolWatcher, ApiError, ValWatcher, RiotWatcher
import util.common as common
import os

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True

client = commands.Bot(command_prefix='$', case_insensitive=True, intents=intents)
common = common.Common()
file = open('token.json')
data = json.load(file)

client.remove_command('help')

rKey = data['riotToken']
lol_watcher = LolWatcher(rKey)
region = common.region

vKey = 'INSERT KEY HERE'
val_watcher = ValWatcher(vKey)
riot_watcher = RiotWatcher(vKey)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('a Riot Game'))
    print('RiotBot is ready.')


@client.command(hidden=True)
async def load(ctx: commands.Context, extension):
    client.load_extension(f'cogs.{extension}')


@client.command(hidden=True)
async def unload(ctx: commands.Context, extension):
    if ctx.author.guild_permissions.administrator:
        client.unload_extension(f'cogs.{extension}')
    else:
        await ctx.send('You cannot unload cogs! You must be an admin to do this!')
        print(format(ctx.author.name) + ' tried to unload a cog.')


@client.command(hidden=True)
async def reload(ctx: commands.Context, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(data['discordToken'])
file.close()
