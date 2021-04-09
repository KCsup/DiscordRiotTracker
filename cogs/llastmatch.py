import discord
from discord.ext import commands
import util.common as common
from bot import lol_watcher
from riotwatcher import ApiError


class LLastMatch(commands.Cog):
    common = common.Common()

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['llastm', 'llm'])
    async def llastmatch(self, ctx: commands.Context, *, username):
        region = self.common.region
        if ctx.channel.id == self.common.botChannelId:
            try:
                s = lol_watcher.summoner.by_name(region, username)
                # print(s)
            except ApiError:
                await ctx.send("Invalid Summoner Name!")
                return

            try:
                matchL = lol_watcher.match.matchlist_by_account(region=region, encrypted_account_id=s['accountId'],
                                                                begin_index=0, end_index=1)
            except ApiError:
                await ctx.send("That Summoner is Not in: " + region + "!")
                return

            champID = matchL['matches'][0]['champion']
            matchID = matchL['matches'][0]['gameId']

            lastM = lol_watcher.match.by_id(region=region, match_id=matchID)
            gameMode = lastM['gameMode']
            teamAlly = lastM['teams'][0]
            teamWin = teamAlly['win']

            champion = self.common.getChampion(champID)
            champName = champion['name']
            champImg = champion['icon']
            kills = 0

            for x in lastM['participants']:
                if x['championId'] == champID:
                    stats = x['stats']
                    kills = stats['kills']

            embed = discord.Embed(title=s['name'] + "'s Last Match:", color=discord.Color.default())
            embed.set_image(url=champImg)
            embed.add_field(name='GameMode', value=gameMode, inline=False)
            embed.add_field(name='Champion', value=champName, inline=False)
            embed.add_field(name='Win (Win/Fail)', value=teamWin, inline=False)
            embed.add_field(name='Kills', value=kills, inline=False)

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(LLastMatch(client))
