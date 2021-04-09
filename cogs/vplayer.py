import discord
from discord.ext import commands
import util.common as common
from bot import val_watcher, riot_watcher
from riotwatcher import ApiError


class VPlayer(commands.Cog):
    common = common.Common()

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def vplayer(self, ctx: commands.Context, *, name: str):
        region = self.common.region
        try:
            riotName = name.split('#')
            acc = riot_watcher.account.by_riot_id(region=region, game_name=riotName[0], tag_line='#' + riotName[1])
        except ApiError:
            await ctx.send("Invalid VALORANT Player!")
            return

        puuid = acc['puuid']
        name = acc['gameName']
        player = None

        try:
            ml = val_watcher.match.matchlist_by_puuid(puuid=puuid)
        except ApiError:
            await ctx.send("This VALORANT Player is Not in: " + region + "!")
            return

        if not ml:
            embed = discord.Embed(title=name, color=discord.Color.default())
            embed.add_field(name='Rank', value='UnRanked', inline=False)
            embed.set_image(url='https://i.imgur.com/u4flNiD.png')
            await ctx.send(embed=embed)
        else:
            lastMatchID = ml[0]['matchId']
            lastMatch = val_watcher.match.by_id(lastMatchID)
            for x in lastMatch['players']:
                if x['puuid'] == puuid:
                    player = x
                    break

            rankID = player['competitiveTier']
            rank = self.common.getVRank(rankID)
            rankName = rank['name']
            rankIcon = rank['icon']

            embed = discord.Embed(title=name, color=discord.Color.default())
            embed.add_field(name='Rank', value=rankName, inline=False)
            embed.set_image(url=rankIcon)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(VPlayer(client))
