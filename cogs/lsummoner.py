import discord
from discord.ext import commands
import util.common as common
from bot import lol_watcher


class LSummoner(commands.Cog):
    common = common.Common()

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['lsum', 'ls'])
    async def lsummoner(self, ctx: commands.Context, *, username):
        region = self.common.region
        if ctx.channel.id == self.common.botChannelId:
            try:
                s = lol_watcher.summoner.by_name(region, username)
            except:
                await ctx.send("Invalid Summoner Name!")
                return

            name = s['name']
            level = s['summonerLevel']

            rs = lol_watcher.league.by_summoner(region, s['id'])
            if not rs:
                embed = discord.Embed(title=name, color=discord.Color.default())
                embed.add_field(name='Rank', value='UnRanked', inline=False)
                embed.add_field(name='Level', value=level, inline=False)
                embed.set_image(url='https://i.imgur.com/x4eP0VI.png')
                await ctx.send(embed=embed)
            else:
                tier = rs[0]['tier']
                rank = rs[0]['rank']

                color = None
                image = None

                if tier == 'IRON':
                    image = 'https://imgur.com/wb3FYKb.png'
                    color = discord.Color.dark_grey()
                elif tier == 'BRONZE':
                    image = 'https://imgur.com/Tl1GxiL.png'
                    color = discord.Color.dark_orange()
                elif tier == 'SILVER':
                    image = 'https://imgur.com/M0zDRj2.png'
                    color = discord.Color.light_grey()
                elif tier == 'GOLD':
                    image = 'https://imgur.com/3fwPURL.png'
                    color = discord.Color.gold()
                elif tier == 'PLATINUM':
                    image = 'https://imgur.com/zHwIvsH.png'
                    color = discord.Color.blue()
                elif tier == 'DIAMOND':
                    image = 'https://imgur.com/pBElbNc.png'
                    color = discord.Color.dark_blue()
                elif tier == 'MASTER':
                    image = 'https://imgur.com/SQyalXV.png'
                    color = discord.Color.purple()
                elif tier == 'GRANDMASTER':
                    image = 'https://imgur.com/6wM9MqD.png'
                    color = discord.Color.red()
                elif tier == 'CHALLENGER':
                    image = 'https://imgur.com/vcvN95g.png'
                    color = discord.Color.dark_gold()

                embed = discord.Embed(title=name, color=color)
                embed.add_field(name='Rank', value=tier + ' ' + rank, inline=False)
                embed.add_field(name='Level', value=level, inline=False)
                embed.set_image(url=image)
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(LSummoner(client))
