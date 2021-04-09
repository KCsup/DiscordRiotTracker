import discord
from discord.ext import commands
import json
import valorant
import riotwatcher
from riotwatcher import LolWatcher, ApiError, ValWatcher, RiotWatcher
import util.common as common
import os

# s = lol_watcher.summoner.by_name(region, 'kcsup05')
# ml = lol_watcher.match.matchlist_by_account(region=region, encrypted_account_id=s['accountId'], begin_index=0, end_index=1)
# cID = ml['matches'][0]['champion']
# print(ml)
# print(common.getChampion(cID))

# vClient = valorant.Client(rKey)
# acc = vClient.get_user_by_name('KCsup#2216', '#')
# print(acc)

# r_watcher = RiotWatcher(data['dToken'])
# player = r_watcher.account.by_riot_id(region='AMERICAS', game_name='KCsup', tag_line='2216')
# print(player)

# print(s['puuid'])
# val_watcher = ValWatcher(rKey)
# v = val_watcher.match.matchlist_by_puuid(region='NA', puuid=player['puuid'])
# print(v)

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