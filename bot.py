import discord
from discord.ext import commands
import json
import valorant
import riotwatcher
from riotwatcher import LolWatcher, ApiError, ValWatcher
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

# vClient = valorant.Client(vKey)
# acc = vClient.get_user_by_name('KCsup#2216', '#')
# for x in vClient.get_leaderboard().players:
#     print(x.gameName)
# print(acc.puuid)

rKey = data['riotToken']
lol_watcher = LolWatcher(rKey)

# my_region = 'na1'
# me = None
# try:
#     me = lol_watcher.summoner.by_name(my_region, 'kcsup05')
# except:
#     print("not a summoner")

# print(me)
#
# my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
# print(my_ranked_stats)
# print('Player name: ' + me['name'] + '\nRank: ' + my_ranked_stats[0]['tier'] + ' ' + my_ranked_stats[0]['rank'])
#
# print(common.selfUserId)

def get_common():
    return common

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('a Riot Game'))
    print('RiotBot is ready.')

@client.command()
async def load(ctx: commands.Context, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx: commands.Context, extension):
    if ctx.author.guild_permissions.administrator:
        client.unload_extension(f'cogs.{extension}')
    else:
        await ctx.send('You cannot unload cogs! You must be an admin to do this!')
        print(format(ctx.author.name) + ' tried to unload a cog.')

@client.command()
async def reload(ctx: commands.Context, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(data['discordToken'])
file.close()
