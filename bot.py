from ctypes.wintypes import BOOLEAN
from operator import truediv
from sqlite3.dbapi2 import Timestamp
from aiosqlite import cursor
import discord
import aiosqlite
from discord import colour
from discord.enums import NotificationLevel
from akinator.async_aki import Akinator
from game import *
from discord.ext import commands
import math
import aiohttp
import DiscordUtils
import random
import io
import asyncio
from PIL import Image, ImageDraw, ImageFont
#from _typeshed import OpenTextModeReading
from asyncio.tasks import current_task, wait_for
import contextlib
from hashlib import new
from inspect import indentsize
import io
from aiohttp import request
from math import perm
import os
from discord import channel
from discord_slash import SlashCommand
from easypydb import DB
from discord.channel import VoiceChannel
import aiofiles
import math
from discord.ext.commands.converter import RoleConverter
from discord.partial_emoji import _EmojiTag
from flask import Flask
from flask import render_template
from urllib import request

import requests
from discord.flags import Intents
import aiofiles
import discord


from discord.ext import commands
import aiosqlite
import logging
import discord
import math
import aiosqlite
import asyncio
from discord.ext import commands
from discord.flags import Intents
from discord.ext import ipc

from glob import glob 
import pandas as pd
from discord.ext.commands import BucketType
from discord.ext.commands import CommandOnCooldown
from discord.ext.commands import cooldown
from discord import Embed, embeds, guild, message, permissions, user
from datetime import date, datetime
import json
from discord.utils import get
import aiohttp
import pyrandmeme
import youtube_dl
from copy import deepcopy
from dateutil.relativedelta import relativedelta
import re 
from discord import Forbidden
import sqlite3
from discord import FFmpegPCMAudio
import traceback
import joke_api

import random
import textwrap
from traceback import format_exception
import asyncio
import discord
from pathlib import Path
from discord.ext import commands, tasks
import discord
from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command
import wikipedia
from discord.ext.commands.errors import MissingRequiredArgument, NoEntryPointError

prefix = "f!"

#intents = discord.Intents.default()
intents = discord.Intents.all()
#intents.presences = True
#intents.guild
#intents.members = True
bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)
bot.ticket_configs = {}
bot.remove_command("help")
bot.multiplier = 1
bot.warnings = {}
bot.filter = {}
music = DiscordUtils.Music()



#embedhelpannounce=discord.Embed(description=f"**Command: Announce** \nDescription - Announce a specified message in a specified channel. \nUsage - `!announce [channel] [message]` \nExample - `!announce #general Hello!`", color=discord.Color.random())
            #await ctx.send(embed=embed)

#elif command == "announce":
        #if not message.author.bot:
embedannounce=discord.Embed(description=f"**Command: Announce** \nDescription - Announce a specified message in a specified channel. \nUsage - `!announce [channel] [message]` \nExample - `!announce #general Hello!`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "give":
#if not message.author.bot:
embedgive=discord.Embed(description=f"**Command: Give** \nDescription - Give a specified amount of coins to a mentioned user. \nUsage - `!give [member] [amount]` \nExample - `!give @F904 1000000`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "addrole":
#if not message.author.bot:
embedaddrole=discord.Embed(description=f"**Command: Addrole** \nDescription - Give a specified member a specified role. \nUsage - `!addrole [member] [role]` \nExample - `!addrole @F904#0605 @Master of the Universe`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "ban":
#if not message.author.bot:
embedban=discord.Embed(description=f"**Command: Ban** \nDescription - Ban a member from the guild. \nUsage - `!ban [member] [optional reason]` \nExample - `!ban @F904#0605 Being too cool`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "kick":
#if not message.author.bot:
embedkick=discord.Embed(description=f"**Command: Kick** \nDescription - Kick a member from the guild. They will be able to rejoin with a new invite link \nUsage - `!kick [member] [optional reason]` \nExample - `!kick @F904#0605 Being too cool`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "dm":
#if not message.author.bot:
embeddm=discord.Embed(description=f"**Command: DM** \nDescription - Send a given message to a user via Direct Messages. \nUsage - `!dm [member] [message]` \nExample - `!dm @F904#0605 Hey!`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "lock":
#if not message.author.bot:
embedlock=discord.Embed(description=f"**Command: Lock** \nDescription - Lock the channel you are currently in. \nUsage - `!lock [optional message]` \nExample - `!lock Raid!!!`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "lockdown":
#if not message.author.bot:
embedlockdown=discord.Embed(description=f"**Command: Lockdown** \nDescription - Lock the entire server \nUsage - `!lockdown [optional message]` \nExample - `!lockdown We have a raid!!!`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "lockdown":
#if not message.author.bot:
embedlockdownend=discord.Embed(description=f"**Command: Lockdown End** \nDescription - Unock the entire server \nUsage - `!lockdownend [optional message]` \nExample - `!lockdownend The raid is over, sorry for the inconviences.`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "mute":
#if not message.author.bot:
embedmute=discord.Embed(description=f"**Command: Mute** \nDescription - Mute a user from the guild \nUsage - `!mute [member] [optional reason]` \nExample - `!mute @F904#0605 Enough Talking!`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "mute":
#if not message.author.bot:
embednick=discord.Embed(description=f"**Command: Nick** \nDescription - Change a member's nickname \nUsage - `!nick [member] [new nickname]` \nExample - `!nick @F904#0605 Casper`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "purge":
#if not message.author.bot:
embedpurge=discord.Embed(description=f"**Command: Purge** \nDescription - Clear a specified amount of messages in a channel \nUsage - `!purge [amount]` \nExample - `!purge 50`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "roles":
#if not message.author.bot:
embedroles=discord.Embed(description=f"**Command: Roles** \nDescription - View all the roles in the guild. \nUsage - `!roles` \nExample - `!roles`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "removerole":
#if not message.author.bot:
embedremoverole=discord.Embed(description=f"**Command: Remove Role** \nDescription - Take away a specified role from a member. \nUsage - `!removerole [member] [role]` \nExample - `!removerole @F904#0605 @Master of the Universe`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "slowmode":
#if not message.author.bot:
embedslowmode=discord.Embed(description=f"**Command: Slowmode** \nDescription - Change the slowmode of the channel you are in. \nUsage - `!slowmode [seconds]` \nExample - `!slowmode 5`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "tempmute":
#if not message.author.bot:
embedtempmute=discord.Embed(description=f"**Command: Tempmute** \nDescription - Temporarily mute a member for a given time. \nUsage - `!tempmute [member] [time] [optional reason]` \nExample - `!tempmute @F904#0605 1h Please read our #rules`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "unban":
#if not message.author.bot:
embedunban=discord.Embed(description=f"**Command: Unban** \nDescription - Unban a member from the guild. \nUsage - `!unban [member] [optional reason]` \nExample - `!unban @F904#0605 Sorry for the inconvenience, please join back`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "unlock":
#if not message.author.bot:
embedunlock=discord.Embed(description=f"**Command: Unlock** \nDescription - Unlock the channel you are in. \nUsage - `!unlock [optional reason]` \nExample - `!unlock The raid is over`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "unmute":
#if not message.author.bot:
embedunmute=discord.Embed(description=f"**Command: Unmute** \nDescription - Unmute a member. \nUsage - `!unmute [member] [reason]` \nExample - `!unmute @F904#0605 Mute duration is over`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "warn":
#if not message.author.bot:
embedwarn=discord.Embed(description=f"**Command: Warn** \nDescription - Warn a member. \nUsage - `!warn [member] [reason]` \nExample - `!warn @F904#0605 Advertising content`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "warnings": 
#if not message.author.bot:
embedwarnings=discord.Embed(description=f"**Command: Warnings** \nDescription - View a member's warnings. \nUsage - `!warnings [member]` \nExample - `!warnings @F904#0605`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "whois":
#if not message.author.bot:
embedwhois=discord.Embed(description=f"**Command: Whois** \nDescription - View information about a member. \nUsage - `!whois [member]` \nExample - `!whois @F904#0605`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "av":
#if not message.author.bot:
embedavatar=discord.Embed(description=f"**Command: Avatar** \nDescription - View a members avatar. \nUsage - `!av [member]` \nExample - `!av @F904#0605`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "beg":
#if not message.author.bot:
embedbeg=discord.Embed(description=f"**Command: Beg** \nDescription - Beg to earn between 1 to 100 coins. \nUsage - `!beg` \nExample - `!beg`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "buy":
#if not message.author.bot:
embedbuy=discord.Embed(description=f"**Command: Buy** \nDescription - Buy an item in the shop. \nUsage - `!buy [item name]` \nExample - `!buy Discord Legend`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "coins":
#if not message.author.bot:
embedcoins=discord.Embed(description=f"**Command: Coins** \nDescription - View your coins. Coins can be earned through several various games. \nUsage - `!coins` \nExample - `!coins`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "dadjoke":
#if not message.author.bot:
embeddadjoke=discord.Embed(description=f"**Command: Dadjoke** \nDescription - Recieve a random bad joke. \nUsage - `!dadjoke` \nExample - `!dadjoke`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "daily":
#if not message.author.bot:
embeddaily=discord.Embed(description=f"**Command: Daily** \nDescription - Claim an amount of coins between 250 to 485 daily. \nUsage - `!daily` \nExample - `!daily`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "dice":
#if not message.author.bot:
embeddice=discord.Embed(description=f"**Command: Dice** \nDescription - Roll the dice for coins. Rolling a double will give you twice your bet, rolling a double 6 will give you thrice your bet. \nUsage - `!dice [bet]` \nExample - `!dice 500`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "poll":
#if not message.author.bot:
embedpoll=discord.Embed(description=f"**Command: Poll** \nDescription - Create a poll. Automatic thumbs up and thumbs down reactions will be placed. \nUsage - `!dice [bet]` \nExample - `!dice 500`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "rank":
#if not message.author.bot:
embedrank=discord.Embed(description=f"**Command: Rank** \nDescription - View you rank statistics. XP is earned by simply chatting. \nUsage - `!rank` \nExample - `!rank`", color=discord.Color.random())
#await ctx.send(embed=embed)
#elif command == "reminder":
#if not message.author.bot:
embedreminder=discord.Embed(description=f"**Command: Reminder** \nDescription - Set a reminder. \nUsage - `!reminder [time] [message]` \nExample - `!reminder 1h Walk my dog`", color=discord.Color.random())
#await ctx.send(embed=embed)

embedfilter=discord.Embed(description=f"**Command: Filter** \nDescription - Filter a word, anyone who is not a Server Moderator will be warned for language \nUsage - `!filter [word]` \nExample - `!filter fuck`", color=discord.Color.random())
embedunfilter=discord.Embed(description=f"**Command: Unfilter** \nDescription - Unilter a filtered word \nUsage - `!unfilter [word]` \nExample - `!unfilter fuck`", color=discord.Color.random())
#elif command == "richest":
#if not message.author.bot:
embedrichest=discord.Embed(description=f"**Command: Richest** \nDescription - View the richest users in the server. This is completely based on raw amount of coins a user has. \nUsage - `!richest [index]` \nExample - `!richest 5`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "rob":
#if not message.author.bot:
embedrob=discord.Embed(description=f"**Command: Rob** \nDescription - Rob a user. Successfully robbing can get you coins, but getting caught will charge you coins. You need at least 250 coins to be able to rob. \nUsage - `!rob [member]` \nExample - `!rob @F904#0605`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "shop":
#if not message.author.bot:
embedshop=discord.Embed(description=f"**Command: Shop** \nDescription - View the shop items. Purchase items with coins. \nUsage - `!shop` \nExample - `!shop`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "slots":
#if not message.author.bot:
embedslots=discord.Embed(description=f"**Command: Slots** \nDescription - Play slots with a chance to win up to triple your bet. \nUsage - `!slots [bet]` \nExample - `!slots 1000`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "top":
#if not message.author.bot:
embedtop=discord.Embed(description=f"**Command: Top** \nDescription - View the rank leaderboard. \nUsage - `!top` \nExample - `!top`", color=discord.Color.random())
#await ctx.send(embed=embed)

#elif command == "work":
#if not message.author.bot:
embedwork=discord.Embed(description=f"**Command: Work** \nDescription - Claim a work paycheck each hour. You can earn between 100 to 280 coins. \nUsage - `!work` \nExample - `!work`", color=discord.Color.random())
#await ctx.send(embed=embed)

    

    #elif command == "configuring":
        
        

os.chdir('C:\\Users\\menuk\\OneDrive\\Desktop\\Blazev3.4')


mainshop = [{"name": "Custom Role", "price": 5000000, "description": "Purchase a special customizable role, the name and the color of the role can be specfified by the buyer."},
            {"name": "King", "price": 1000000, "description": "Purchase a special coloured gold role."},
            {"name": "Discord Legend", "price": 500000, "description": "Purchase a special coloured pink role."},
            {"name": "Discord Mythical", "price": 750000, "description": "Purchase a special coloured black role."}]


async def connect_database():
    db = await aiosqlite.connect('database.db')




async def find_or_insert_user(member: discord.Member):
    db = await aiosqlite.connect('database.db')
    # user_id, guild_id, xp, level
    cursor = await db.cursor()
    await cursor.execute('Select * from users where user_id = ? and guild_id = ?', (member.id, member.guild.id))
    result = await cursor.fetchone()
    if result is None:
        result = (member.id, member.guild.id, 0, 0)
        await cursor.execute('Insert into users values(?, ?, ?, ?)', result)
        await db.commit()

    return result

def calculate_xp(level):
    return 100 * (level ** 2)

def calculate_level(xp):
    # Sqrt => value ** 0.5
    return round(0.1 * math.sqrt(xp))


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle)
    
    #async with aiofiles.open("ticket_configs.txt", mode="a") as temp:
        #pass

    #async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        #lines = await file.readlines()
        #for line in lines:
            #data = line.split(" ")
            #bot.ticket_configs[int(data[0])] = [int(data[1]), int(data[2]), int(data[3])]


    for guild in bot.guilds:
        bot.warnings[guild.id] = {}
        
        async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
            pass

        


        async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
            lines = await file.readlines()

            for line in lines:
                data = line.split(" ")
                member_id = int(data[0])
                admin_id = int(data[1])
                reason = " ".join(data[2:]).strip("\n")

                try:
                    bot.warnings[guild.id][member_id][0] += 1
                    bot.warnings[guild.id][member_id][1].append((admin_id, reason))

                except KeyError:
                    bot.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]

    
    async with aiofiles.open("ticket_configs.txt", mode="a") as temp:
        pass

    async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            bot.ticket_configs[int(data[0])] = [int(data[1]), int(data[2]), int(data[3])]

    print("Bot is ready")


@bot.event
async def on_message(message: discord.Message):

    db = await aiosqlite.connect('database.db')
    if message.author.bot is True or message.guild is None:
        return

    

    result = await find_or_insert_user(message.author)

    user_id, guild_id, xp, level = result
    #print(xp, level)

    xp += random.randint(5, 10)
    
    if calculate_level(xp) > level:
        level += 1
        # 1,000
        guild = message.guild
        channel = discord.utils.get(guild.channels, name='member-level-ups')
        await channel.send(f"Congratulations, {message.author.display_name}, you just advanced to level {level:,}!")

    cursor = await db.cursor()
    await cursor.execute('Update users set xp=?, level=? where user_id=? and guild_id=?', (xp, level, user_id, guild_id))
    await db.commit()




    if message.content == f"<@!{bot.user.id}> help":
        

            

        await message.channel.send(f"Heyo {message.author.mention}! My prefix is: `{prefix}`")

    if message.content == f"<@!{bot.user.id}>":
        

            

        await message.channel.send(f"Heyo {message.author.mention}! My prefix is: `{prefix}`")

    if message.content == f"<@!{bot.user.id}> prefix":
        

            

        await message.channel.send(f"Heyo {message.author.mention}! My prefix is: `{prefix}`")



    
    message_content = message.content.strip().lower()
    dbconnect = sqlite3.connect('users.db')
    cursor = dbconnect.cursor()
    records = cursor.execute("SELECT word FROM bannedwords").fetchall()
    for row in records:
        if row[0] in message_content:
            if message.author.permissions_in(message.channel).manage_messages:
                break
            else:
                await message.delete()
                msg = await message.channel.send(f"{message.author.mention}, watch your language.")
                await asyncio.sleep(3.5)
                await msg.delete()
                #channel = bot.get_channel(848062068887781437)
                channel = discord.utils.get(message.guild.channels, name='automod-logs')
                embedVar = discord.Embed(description=f"Language Warning Issued to {message.author}", color=discord.Color.red(), timestamp=datetime.utcnow())
                embedVar.set_author(name=f"{message.author}#{message.author.discriminator}", icon_url=message.author.avatar_url)
                embedVar.set_footer(text=f"ID: {message.author.id}")
                embedVar.add_field(name="User:", value=f"{message.author.mention}", inline=True)
                embedVar.add_field(name="Channel:", value=f"{message.channel.mention}", inline=True)
                #dt_string = datetime.strftime("%d/%m/%Y %H:%M:%S")
                #embedVar.add_field(name="Time:", value=f"{dt_string}", inline=True)
                embedVar.add_field(name="Message:", value=f"{message.content}", inline=False)
                await channel.send(embed=embedVar)

    



    #with open("afk.json", "r") as f:
        #afk = json.load(f)

    #for x in message.mentions:
        #if afk[f"{x.id}"]["AFK"] == "True":
            #if message.author.bot:
                #return

            #await message.channel.send(f"{message.author}, {x.display_name} is AFK!")
        


    #if not message.author.bot:
        #await update_data(afk, message.author)

        #if afk[f"{message.author.id}"]["AFK"] == 'True':
           #await message.channel.send(f"{message.author.name}, welcome back. I have removed your AFK")
            #afk[f"{message.author.id}"]["AFK"] = 'False'

            #with open("afk.json", "w") as f:
                #json.dump(afk, f)
            #try:
                #await message.author.edit(nick=f"{message.author.display_name[5:]}")

            #except:
                #pass



    #with open("afk.json", "w") as f:
        #json.dump(afk, f)

    
    




    

    await bot.process_commands(message)



    


    


@bot.event
async def on_guild_channel_delete(channel):
    guild = channel.guild
    channeltosend = discord.utils.get(channel.guild.channels, name='channel-logs')
    
    embed = discord.Embed(description=f"**Channel Deleted: {channel}** ", color=discord.Color.red(), timestamp = datetime.utcnow())
    embed.set_author(name=f"{channel.guild.name}", icon_url=f"{channel.guild.icon_url}")
    embed.set_footer(text=f"ID: {channel.id}")
    await channeltosend.send(embed=embed)

@bot.event
async def on_guild_channel_create(channel):
    guid = channel.guild
    channeltosend = discord.utils.get(channel.guild.channels, name='channel-logs')
    embed = discord.Embed(description=f"**Channel Created: {channel}** ", color=discord.Color.green(), timestamp = datetime.utcnow())
    embed.set_footer(text=f"ID: {channel.id}")
    embed.set_author(name=f"{channel.guild.name}", icon_url=f"{channel.guild.icon_url}")
    await channeltosend.send(embed=embed)

   
@bot.event
async def on_guild_role_create(role):
    guid = role.guild
    channeltosend = discord.utils.get(role.guild.channels, name='role-logs')
    embed = discord.Embed(description=f"**Role Created: {role}** ", color=discord.Color.green(), timestamp = datetime.utcnow())
    embed.set_footer(text=f"ID: {role.id}")
    embed.set_author(name=f"{role.guild.name}", icon_url=f"{role.guild.icon_url}")
    await channeltosend.send(embed=embed)


@bot.event
async def on_guild_role_remove(role):
    guid = role.guild
    channeltosend = discord.utils.get(role.guild.channels, name='role-logs')
    embed = discord.Embed(description=f"**Role Deleted: {role}**", color=discord.Color.red(), timestamp = datetime.utcnow())
    embed.set_footer(text=f"ID: {role.id}")
    embed.set_author(name=f"{role.guild.name}", icon_url=f"{role.guild.icon_url}")
    await channeltosend.send(embed=embed)


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        guild = member.guild
        channeltosend = discord.utils.get(member.guild.channels, name='channel-logs')
        embed = discord.Embed(description=f"{member.mention} has joined the voice channel <#{after.channel.id}>", color=discord.Color.blue(), timestamp = datetime.utcnow())
        embed.set_footer(text=f"ID: {member.id}")
        embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=f"{member.avatar_url}")
        await channeltosend.send(embed=embed)

    elif before.channel is not None and after.channel is None:
        guild = member.guild
        channeltosend = discord.utils.get(member.guild.channels, name='channel-logs')
        embed = discord.Embed(description=f"{member.mention} has left the voice channel <#{before.channel.id}>", color=discord.Color.red(), timestamp = datetime.utcnow())
        embed.set_footer(text=f"ID: {member.id}")
        embed.set_author(name=f"{member.name}#{member.discriminator}", icon_url=f"{member.avatar_url}")
        await channeltosend.send(embed=embed)


@bot.command()
async def afk(ctx, reason):
    with open("afk.json", "r") as f:
        afk = json.load(f)

    afk[f"{ctx.author.id}"]["AFK"] = "True"
    await ctx.send(f"{ctx.author.name}, I have set your AFK: {reason}")
    with open("afk.json", "w") as f:
        json.dump(afk, f)
        
    try:
        await ctx.author.edit(nick=f"[AFK] {ctx.author.display_name}")
    except:
        pass

    



@bot.command()
@commands.has_permissions(manage_messages=True)
async def filter(ctx, *, word=None):
    if word is None:
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Please enter a word to filter!", color=discord.Color.red())
        #return await ctx.send(embed=embed)
        return await ctx.reply(embed=embedfilter)

    

    word = word.lower()
    dbconnect = sqlite3.connect('users.db')
    cursor = dbconnect.cursor()
    cursor.execute("SELECT word FROM bannedwords WHERE word = ?", (word,))
    result = cursor.fetchone()
    if result:

        emoji = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji} That word is already filtered", color=discord.Color.red())
        await ctx.send(embed=embed)
    else:
        cursor.execute('''INSERT INTO bannedwords(word) VALUES(?)''', (word,))
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"{emoji} `{word}` has been filtered", colour=discord.Color.green())
        await ctx.send(embed=embed)
       
        channel = bot.get_channel(848064366145568798)
        embedVar = discord.Embed(title="Word Filtered", description=f"Issued by **{ctx.message.author}**", color=0xe74c3c)
        embedVar.add_field(name="Word:", value=f"**{word}**", inline=True)
        embedVar.add_field(name="Channel:", value=f"**{ctx.channel.mention}**", inline=True)
        #embedVar.add_field(name="Time:", value=f"**{ctime()}**", inline=True)
        await channel.send(embed=embedVar)
    dbconnect.commit()
    dbconnect.close()



@bot.command()
@commands.has_permissions(manage_messages=True)
async def unfilter(ctx, *, word=None):
    if word is None:
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Please enter a word to unfilter", color=discord.Color.red())
        return await ctx.reply(embed=embedunfilter)
    word = word.lower()
    dbconnect = sqlite3.connect('users.db')
    cursor = dbconnect.cursor()
    cursor.execute("SELECT word FROM bannedwords WHERE word = ?", (word,))
    result = cursor.fetchone()
    if result:
        cursor.execute("DELETE FROM bannedwords WHERE word = ?", (word,))
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"{emoji} `{word}` has been unfiltered", color=discord.Color.green())
        await ctx.send(embed=embed)
        channel = bot.get_channel(848064366145568798)
        embedVar = discord.Embed(title="Word Unfiltered", description=f"Issued by **{ctx.message.author}**", color=0xe74c3c)
        embedVar.add_field(name="Word:", value=f"**{word}**", inline=True)
        embedVar.add_field(name="Channel:", value=f"**{ctx.channel.mention}**", inline=True)
        #embedVar.add_field(name="Time:", value=f"**{ctime()}**", inline=True)
        await channel.send(embed=embedVar)
    else:
        emoji = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji} That word is not filtered", colour=discord.Color.red())
        await ctx.send(embed=embed)
    dbconnect.commit()
    dbconnect.close()



@bot.command()
async def filters(ctx):
    bannedTerms = "**The filtered words are: **\n"
    dbconnect = sqlite3.connect('users.db')
    cursor = dbconnect.cursor()
    cursor.execute("SELECT word FROM bannedwords")
    result = cursor.fetchall()
    for row in result:
        bannedTerm = row[0]
        
        bannedTerms = bannedTerms + bannedTerm + "\n"
    embed = discord.Embed(description=f"{bannedTerms}", color=discord.Color.blue())
    embed.set_footer(text=f"Note: If there are no filtered words, the embed will be blank.")
    await ctx.send(embed=embed)
    #await ctx.send(bannedTerms)
    dbconnect.commit()
    dbconnect.close()




async def make_rank_image(member: discord.Member, rank, level, xp, final_xp):
    user_avatar_image = str(member.avatar_url_as(format='png', size=512))
    async with aiohttp.ClientSession() as session:
        async with session.get(user_avatar_image) as resp:
            avatar_bytes = io.BytesIO(await resp.read())

    img = Image.new('RGB', (1000, 240))
    logo = Image.open(avatar_bytes).resize((195, 195))

    # Stack overflow helps :)
    bigsize = (logo.size[0] * 3, logo.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(logo.size, Image.ANTIALIAS)
    logo.putalpha(mask)
    ##############################
    img.paste(logo, (20, 20), mask=logo)

    # Black Circle
    draw = ImageDraw.Draw(img, 'RGB')
    #draw.ellipse((152, 152, 208, 208), fill='#000')

    # Placing offline or Online Status
    # Discord Colors (Online: '#43B581')
    
    #draw.ellipse((155, 155, 205, 205), fill='#43B581')

    



    ##################################

    # Working with fonts
    big_font = ImageFont.FreeTypeFont('ABeeZee-Regular.otf', 60)
    medium_font = ImageFont.FreeTypeFont('ABeeZee-Regular.otf', 40)
    small_font = ImageFont.FreeTypeFont('ABeeZee-Regular.otf', 32)

    # Placing Level text (right-upper part)
    text_size = draw.textsize(f"{level}", font=big_font)
    offset_x = 950-15 - text_size[0]
    offset_y = 19
    draw.text((offset_x, offset_y), f"{level}", font=big_font, fill="#11ebf2")
    text_size = draw.textsize('LEVEL', font=small_font)

    offset_x -= 5 + text_size[0]
    offset_y = 48
    draw.text((offset_x, offset_y), "LEVEL", font=small_font, fill="#11ebf2")

    # Placing Rank Text (right upper part)
    text_size = draw.textsize(f"#{rank}", font=big_font)
    offset_x -= 15 + text_size[0]
    offset_y = 19
    draw.text((offset_x, offset_y), f"#{rank}", font=big_font, fill="#fff")

    text_size = draw.textsize("RANK", font=small_font)
    offset_x -= 5 + text_size[0]
    offset_y = 48
    draw.text((offset_x, offset_y), "RANK", font=small_font, fill="#fff")

    # Placing Progress Bar
    # Background Bar
    bar_offset_x = logo.size[0] + 20 + 100
    bar_offset_y = 160
    bar_offset_x_1 = 1000 - 50
    bar_offset_y_1 = 200
    circle_size = bar_offset_y_1 - bar_offset_y

    # Progress bar rect greyier one
    draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill="#727175")
    # Placing circle in progress bar

    # Left circle
    draw.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x + circle_size//2, bar_offset_y + circle_size), fill="#727175")

    # Right Circle
    draw.ellipse((bar_offset_x_1 - circle_size//2, bar_offset_y, bar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#727175")

    # Filling Progress Bar

    bar_length = bar_offset_x_1 - bar_offset_x
    # Calculating of length
    # Bar Percentage (final_xp - current_xp)/final_xp

    # Some variables
    progress = (final_xp - xp) * 100/final_xp
    progress = 100 - progress
    progress_bar_length = round(bar_length * progress/100)
    pbar_offset_x_1 = bar_offset_x + progress_bar_length

    # Drawing Rectangle
    draw.rectangle((bar_offset_x, bar_offset_y, pbar_offset_x_1, bar_offset_y_1), fill="#11ebf2")
    # Left circle
    draw.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x + circle_size//2, bar_offset_y + circle_size), fill="#11ebf2")
    # Right Circle
    draw.ellipse((pbar_offset_x_1 - circle_size//2, bar_offset_y, pbar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#11ebf2")


    def convert_int(integer):
        integer = round(integer / 1000, 2)
        return f'{integer}K'

    # Drawing Xp Text
    text = f"/ {convert_int(final_xp)} XP"
    xp_text_size = draw.textsize(text, font=small_font)
    xp_offset_x = bar_offset_x_1 - xp_text_size[0]
    xp_offset_y = bar_offset_y - xp_text_size[1] - 15
    draw.text((xp_offset_x, xp_offset_y), text, font=small_font, fill="#727175")

    text = f'{convert_int(xp)} '
    xp_text_size = draw.textsize(text, font=small_font)
    xp_offset_x -= xp_text_size[0]
    draw.text((xp_offset_x, xp_offset_y), text, font=small_font, fill="#fff")

    text = member.name
    text_size = draw.textsize(text, font=medium_font)
    text_offset_x = bar_offset_x - 10
    text_offset_y = bar_offset_y - text_size[1] - 20
    draw.text((text_offset_x, text_offset_y), text, font=medium_font, fill="#fff")

    # Placing Discriminator
    #text = f'#{member.discriminator}'
    #text_offset_x += text_size[0] + 10
    #text_size = draw.textsize(text, font=small_font)
    #text_offset_y = bar_offset_y - text_size[1] - 27
    #draw.text((text_offset_x, text_offset_y), text, font=small_font, fill="#727175")

    bytes = io.BytesIO()
    img.save(bytes, 'PNG')
    bytes.seek(0)
    return bytes




@bot.event
async def on_member_join(member):
    role = member.guild.get_role(840105867948195860)
    await member.add_roles(role)
    #channel = member.guild.get_channel(842082286966931458) 
    channel = discord.utils.get(member.guild.channels, name="welcome-logs")
    #await channel.send(f"Hey there, {member.mention}! Welcome to Helpers Lounge <:pepesadlove:840824623431155722> \nPlease go through our <#798547735615635526>, and have a fantastic time here!")
    #memberleavejoincnl = discord.utils.get(member.guild.get_channel, name="member-logs")
    embed = discord.Embed(description=f"{member.mention} has joined the server", timestamp=datetime.utcnow(), color=discord.Color.blurple())
    embed.set_author(name="Member joined", icon_url=member.avatar_url)
    embed.set_footer(text=f"ID: {member.id}")
    await channel.send(embed=embed)

    #with open('afk.json', 'r') as f:
        #afk = json.load(f)

    #await update_data(afk, member)

    #with open('afk.json', 'w') as f:
        #json.dump(afk, f)


#async def update_data(afk, user):
    #if not f"{user.id}" in afk:
        #afk[f"{user.id}"] = {}
        #fafk[f"{user.id}"]["AFK"] = 'False'

    



@bot.event
async def on_member_ban(guild, member):
    channel = discord.utils.get(guild.channels, name="ban-logs")
    embed = discord.Embed(description=f"{member.mention} ({member.name}#{member.discriminator}) has been banned", timestamp=datetime.utcnow(), color=discord.Color.red())
    embed.set_author(name="Member Banned", icon_url=member.avatar_url)
    embed.set_footer(text=f"ID: {member.id}")
    #embed.set_thumbnail(url=f"{member.avatar_url}")
    await channel.send(embed=embed)

@bot.event
async def on_member_unban(guild, member):
    channel = discord.utils.get(guild.channels, name="unban-logs")
    embed = discord.Embed(description=f"{member.mention} ({member.name}#{member.discriminator}) has been unbanned", timestamp=datetime.utcnow(), color=discord.Color.blue())
    embed.set_author(name="Member Unanned", icon_url=member.avatar_url)
    embed.set_footer(text=f"ID: {member.id}")
    #embed.set_thumbnail(url=f"{member.avatar_url}")
    await channel.send(embed=embed)

    

    
@bot.event
async def on_member_remove(member):
    roles = member.roles[1:] 

    roles.reverse()
    memberleavejoincnl = discord.utils.get(member.guild.channels, name="goodbye-logs")
    embed = discord.Embed(description=f"{member.mention} has left the server", timestamp=datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="Roles", value=" ".join([role.mention for role in roles]))
    
    embed.set_author(name=f"Member Left", icon_url=member.avatar_url)
    embed.set_footer(text=f"ID: {member.id}")
    await memberleavejoincnl.send(embed=embed)

@bot.event
async def on_guild_join(guild):
    bot.warnings[guild.id] = {}

    async with aiofiles.open(f"filtersin{guild.id}", mode="a") as temp:
        pass

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(f'Hey there! Thank you for inviting me to this server. My prefix is `{prefix}` \nPlease, as soon as possible, configure log channels with `{prefix}help configuring` to get started! ')
        break



@bot.event
async def on_user_update(before, after):

    if before.name != after.name:
        #guild = after.guild
        #channel = discord.utils.get(guild.channels, name='member-logs')
        channel = [x for x in bot.get_all_channels() if x.type is discord.ChannelType.text and x.nane == "member-logs"]
        embed=discord.Embed(description=f"**Username change for {after.mention}** \n \n **Before:** {before.name} \n \n **After:** {after.name}", color=discord.Color.blurple(), timestamp=datetime.utcnow())
        embed.set_author(name=after.name+'#'+after.discriminator, icon_url=after.avatar_url)
        embed.set_footer(text=f"{before.id}")
        
        await channel.send(embed=embed)
        

    if before.discriminator != after.discriminator:
        #guild = after.guild
        channel = discord.utils.get(guild.channels, name='member-logs')
        embed=discord.Embed(description=f"**Discriminator change for {after.mention}** \n \n **Before:** {before.discriminator} \n \n **After:** {after.discriminator}", color=discord.Color.blurple(), timestamp=datetime.utcnow())
        embed.set_author(name=after.name+'#'+after.discriminator, icon_url=after.avatar_url)
        embed.set_footer(text=f"{before.id}")
        
        await channel.send(embed=embed)


    if before.avatar_url != after.avatar_url:
        #guild = after.guild
        channel = discord.utils.get(guild.channels, name='member-logs')
        
        embed=discord.Embed(title="Member Update", description=f"Avatar Change for {after.mention} \n [Before]({before.avatar_url})  |  [After]({after.avatar_url})", color=discord.Color.green(), timestamp=datetime.utcnow(), inline=True)
        embed.set_footer(text=f"{before.id}")
        embed.set_thumbnail(url=after.avatar_url)
        await channel.send(embed=embed)

@bot.event
async def on_member_update(before, after):
    if before.display_name != after.display_name:
        guild = after.guild
        channel = discord.utils.get(guild.channels, name='member-logs')
        embed=discord.Embed(description=f"**Nickname change for {after.mention}** \n \n **Before:** \n{before.display_name} \n \n  **After:** \n{after.display_name}", color=discord.Color.blurple(), timestamp=datetime.utcnow())
        embed.set_footer(text=f"{after.id}")
        embed.set_author(name=after.name+'#'+after.discriminator, icon_url=after.avatar_url)
        
        await channel.send(embed=embed)


    elif before.roles != after.roles:
        guild = after.guild
        channel = discord.utils.get(guild.channels, name='member-logs')
        before_roles = before.roles[1:]
        before_roles.reverse()
        after_roles = after.roles[1:]
        after_roles.reverse()
        embed=discord.Embed(title="Member Update", description=f"Role Update for {after.mention}", color=discord.Color.blurple(), timestamp=datetime.utcnow(), inline=False)
        embed.add_field(name=f'Before: Roles [{len(before_roles)}]', value=" ".join([role.mention for role in before_roles]), inline=False)
        embed.add_field(name=f'After: Roles [{len(after_roles)}]', value=" ".join([role.mention for role in after_roles]), inline=False)
        embed.set_footer(text=f"{before.id}")
        await channel.send(embed=embed)





@bot.event
async def on_message_edit(before, after):
    if not after.author.bot:
        if before.content != after.content:
            guild = after.guild
            channel = discord.utils.get(guild.channels, name='bot-message-logs')
            member = before.author 
            embed=discord.Embed(description=f"[Message edited by {after.author.mention} in {after.channel.mention}]({before.jump_url}**)\n**Before** \n{before.content} \n\n**After** \n{after.content}", color=discord.Color.blue(), timestamp=datetime.utcnow())
            #embed=discord.Embed(title="Message Edit", description=f"Edit by {after.author.display_name}", color=discord.Color.dark_gold(), timestamp=datetime.utcnow())
            embed.set_author(name=before.author.name+'#'+before.author.discriminator, icon_url=before.author.avatar_url)
            embed.set_footer(text=f"User ID: {before.author.id}" )
            #embed.add_field(name="**__Before__**", value=before.content, inline=False)
            #embed.add_field(name="**__After__**", value=after.content, inline=False)
            await channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    if not message.author.bot:
        guild = message.guild
        channel = discord.utils.get(guild.channels, name='bot-message-logs')
        embed=discord.Embed(description=f"**Message deleted by {message.author.mention} in {message.channel.mention}** \n {message.content}", color=discord.Color.red(), timestamp=datetime.utcnow())
        embed.set_author(name=message.author.display_name+'#'+message.author.discriminator, icon_url=message.author.avatar_url)
        embed.set_footer(text=f"User ID: {message.author.id} | Message ID: {message.id}")
        await channel.send(embed=embed)





@bot.command()
async def rank(ctx, member: discord.Member=None):
    db = await aiosqlite.connect('database.db')
    member = member or ctx.author
    cursor = await db.cursor()
    user = await find_or_insert_user(member)
    user_id, guild_id, xp, level = user
    await cursor.execute("Select Count(*) from users where xp > ? and guild_id=?", (xp, guild_id))
    result = await cursor.fetchone()
    rank = result[0] + 1
    final_xp = calculate_xp(level + 1)
    bytes = await make_rank_image(member, rank, level, xp, final_xp)
    file = discord.File(bytes, 'rank.png')
    await ctx.send(file=file)

@rank.error
async def rankerror(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} I could not find" + ctx.message.content.strip(f"{prefix}rank"), color=discord.Color.red())
        await ctx.reply(embed=embed)



@bot.command()
async def top(ctx): 
    buttons = {}
    for i in range(1, 6):
        buttons[f"{i}\N{COMBINING ENCLOSING KEYCAP}"] = i # only show first 5 pages

    previous_page = 0
    current = 1
    index = 1
    entries_per_page = 10

    embed = discord.Embed(title=f"Leaderboard Page {current}", description="", colour=discord.Colour.gold())
    msg = await ctx.send(embed=embed)

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        if current != previous_page:
            embed.title = f"Leaderboard Page {current}"
            embed.description = ""
            db = await aiosqlite.connect('database.db')

            async with db.execute(f"SELECT user_id, xp FROM users WHERE guild_id = ? ORDER BY xp DESC LIMIT ? OFFSET ? ", (ctx.guild.id, entries_per_page, entries_per_page*(current-1),)) as cursor:
                index = entries_per_page*(current-1)

                async for entry in cursor:
                    index += 1
                    member_id, xp = entry
                    member = ctx.guild.get_member(member_id)
                    embed.description += f"{index}) {member.mention} : **{xp}** \n \n"

                await msg.edit(embed=embed)

        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            return await msg.clear_reactions()

        else:
            previous_page = current
            await msg.remove_reaction(reaction.emoji, ctx.author)
            current = buttons[reaction.emoji]







@bot.command()
#@commands.has_guild_permissions(manage_messs)
async def ping(ctx):
    
    latency = round(bot.latency * 1000, 0)
    msg = await ctx.send(f"Pong!")
    await asyncio.sleep(0.1)
    await msg.edit(content=f"Pong! `{latency}ms`")


@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def nick(ctx, member: discord.Member=None, *, nick=None):
    if member is None:
        #return await ctx.reply(f"Invalid command usage, try using it like `{prefix}nick [member] [nickname]`")
        return await ctx.reply(embed=embednick)

    elif nick is None:
        #return await ctx.reply(f"Invalid command usage, try using it like `{prefix}nick [member] [nickname]`")
        return await ctx.reply(embed=embednick)

    emoji = bot.get_emoji(id=840089389718962176)
    
    await member.edit(nick=nick)

    embed = discord.Embed(description=f"{emoji} Nickname changed for **{member.name}#{member.discriminator}** to **{nick}**", color=discord.Color.green())
    await ctx.send(embed=embed)


@nick.error
async def nickerror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        emoji = bot.get_emoji(id=840585961497952256)
        
        embed = discord.Embed(description=f"{emoji} You cannot use that command", color=discord.Color.red())
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MemberNotFound):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} I could not find that user", color=discord.Color.red())
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} I could not perform the command.", color=discord.Color.red())
        await ctx.send(embed=embed)


    #elif isinstance(error, commands.BadArgument):
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}nick [member] [nickname]`", color=discord.Color.red())
        #await ctx.send(embed=embed)

    #elif isinstance(error, commands.MissingRequiredArgument):
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}nick [member] [nickname]`", color=discord.Color.red())
        #await ctx.send(embed=embed)


@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def av(ctx, *, member: discord.Member=None):
    if member is None:
        member = ctx.author
    embed = discord.Embed(description=f"**{member.mention}'s Avatar**", color=member.color)
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


@av.error
async def averror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        emoji = bot.get_emoji(id=840585961497952256)
        
        embed = discord.Embed(description=f"{emoji} You cannot use that command", color=discord.Color.red())
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MemberNotFound):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} I could not find that user", color=discord.Color.red())
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} The command failed", color=discord.Color.red())
        await ctx.send(embed=embed)


    elif isinstance(error, commands.BadArgument):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}av [member]`", color=discord.Color.red())
        await ctx.send(embed=embed)



@bot.command()
@commands.has_guild_permissions(manage_messages=True)
async def whois(ctx,  *, member: discord.Member = None):
#async def whois(ctx, member: commands.MemberConverter):
   

    member = member or ctx.author
    
    key_guild_perms = ["administrator", "manage_guild", "manage_roles", "manage_channels", "manage_messages", "manage_webhooks", "manage_nicknames", "manage_emojis", "kick_members", "mention_everyone"]
            


    user_has_perms = [perm for perm in key_guild_perms if getattr(member.guild_permissions, perm)]

    
    onlineemoji = bot.get_emoji(id=847139806269014096)
    idleemoji = bot.get_emoji(id=847139806164156416)
    dndemoji = bot.get_emoji(id=847139806223532042)


    roles = member.roles[1:] 

    roles.reverse()
    
    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at, description=f"{member.mention}")

    embed.set_author(name=member.name+'#'+member.discriminator, icon_url=member.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    #embed.add_field(name="Online Status", value=str(member.status).title() if member.status else "N/A \nname)}" if member.activity else 'N/A', inline=True)
    embed.set_footer(text=f'ID: {member.id}')
    embed.add_field(name="Joined on", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
    embed.add_field(name="Registed on", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
    embed.add_field(name=f'Roles [{len(roles)}]', value=" ".join([role.mention for role in roles]) if roles else "None", inline=False)
    embed.add_field(name=f'Key Permissions', value=", ".join(user_has_perms).replace("_"," ").title() if user_has_perms else "None", inline=False)
    embed.add_field(name="Online Status", value=str(member.status).title() if member.status else "N/A", inline=True)
    embed.add_field(name="Custom Status", value=f"{str(member.activity.name)}" if member.activity else "N/A" , inline=True)
    await ctx.send(embed=embed)


@whois.error
async def whoiserror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        emoji = bot.get_emoji(id=840585961497952256)
        
        embed = discord.Embed(description=f"{emoji} You cannot use that command", color=discord.Color.red())
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MemberNotFound):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} I could not find" + ctx.message.content.strip(f"{prefix}whois"), color=discord.Color.red())
        await ctx.send(embed=embed)

    elif isinstance(error, commands.CommandInvokeError):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} The command failed", color=discord.Color.red())
        await ctx.send(embed=embed)


    elif isinstance(error, commands.BadArgument):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}whois [member]`", color=discord.Color.red())
        await ctx.send(embed=embed)

    
        
    
    #if member.id == 738065875827163137:
        #embed.add_field(name="Key Acknowledgements", value="Server Owner")

    

    


    #if not roles:
        
        #try:
            
        
            
            #roles.reverse()
            #embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at, description=member.mention)
            #embed.set_author(name=member.name+'#'+member.discriminator, icon_url=member.avatar)
            #embed.set_thumbnail(url=member.avatar)
            #embed.set_footer(text=f'ID: {member.id}')
            #embed.add_field(name="Joined on", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            #embed.add_field(name="Registed on", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            # #embed.add_field(name=f'Roles [{len(roles)}]', value=" ".join([role.mention for role in roles]), inline=False)
            
            #embed.add_field(name=f'Key Permissions', value=", ".join(user_has_perms).replace("_"," ").title(), inline=False)
            #await ctx.send(embed=embed)
        

        #except:
            #roles.reverse()
            #embed = discord.Embed(colour=discord.Color.blue(), timestamp=ctx.message.created_at, description=member.mention)
            #embed.set_author(name=member.name+'#'+member.discriminator, icon_url=member.avatar)
            #embed.set_thumbnail(url=member.avatar)
            #embed.set_footer(text=f'ID: {member.id}', icon_url=ctx.author.avatar)
            #embed.add_field(name="Joined on:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            #embed.add_field(name="Registed on:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            # embed.add_field(name=f'Key Permissions', value=", ".join(user_has_perms).replace("_"," ").title(), inline=False)
            #embed.add_field(name=f'Roles [0]', value="None", inline=False)
            #await ctx.send(embed=embed)

    #elif roles:
        #try:
        

            #roles.reverse()
            #embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at, description=member.mention)
            #embed.set_author(name=member.name+'#'+member.discriminator, icon_url=member.avatar)
            #embed.set_thumbnail(url=member.avatar)
            #embed.set_footer(text=f'ID: {member.id}')
            #embed.add_field(name="Joined on", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            #embed.add_field(name="Registed on", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            #embed.add_field(name=f'Roles [{len(roles)}]', value=" ".join([role.mention for role in roles]), inline=False)
            
            #embed.add_field(name=f'Key Permissions', value=", ".join(user_has_perms).replace("_"," ").title(), inline=False)
            #await ctx.send(embed=embed)
        #except:
            #roles.reverse()
            #embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at, description=member.mention)
            #embed.set_author(name=member.name+'#'+member.discriminator, icon_url=member.avatar)
            #embed.set_thumbnail(url=member.avatar)
            #embed.set_footer(text=f'ID: {member.id}')
            #embed.add_field(name="Joined on", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            #embed.add_field(name="Registed on", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
            #embed.add_field(name=f'Roles [{len(roles)}]', value=" ".join([role.mention for role in roles]), inline=False)
            
            #embed.add_field(name=f'Key Permissions', value=", ".join(user_has_perms).replace("_"," ").title(), inline=False)
            #await ctx.send(embed=embed)


    
        #return



@bot.command()
@commands.has_guild_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int=None):
    if seconds is None:
        #return await ctx.reply("Please specify the seconds to set the slowmode to!")
        return await ctx.reply(embed=embedslowmode)

    
    await ctx.message.delete()
    await ctx.channel.edit(slowmode_delay=seconds)
    emoji = bot.get_emoji(id=840089389718962176)

    if seconds == 0:
        
        embed = discord.Embed(description=f"**{emoji} {ctx.channel.mention} no longer has slowmode**", color=discord.Color.green())
        sendembed = await ctx.send(embed=embed)
        await asyncio.sleep(2.5)
        await sendembed.delete()

    else:
        
        embed = discord.Embed(description=f"**{emoji} {ctx.channel.mention}'s slowmode has been set to `{seconds}` seconds**", color=discord.Color.green())
        sendembed = await ctx.send(embed=embed)
        await asyncio.sleep(2.5)
        await sendembed.delete()

@slowmode.error
async def slowmodeerror(ctx, error):
    if isinstance(error, commands.BadArgument):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}slowmode [seconds]`", color=discord.Color.red())
        await ctx.send(embed=embed)

    if isinstance(error, commands.MissingRequiredArgument):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}slowmode [seconds]`", color=discord.Color.red())
        await ctx.send(embed=embed)



#@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
#async def purge(ctx, amount=0):
    #f amount == 0:
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}purge [amount]`", color=discord.Color.red())
        #return await ctx.reply("Please enter an amount of messages to purge!")
        #return await ctx.send(embed=embedpurge)
    #else:
        #await ctx.message.delete()
        #await ctx.channel.purge(limit=amount+1)
        #msg = await ctx.send(f"I have cleared **{amount}** {'message' if amount == 1 else 'messages'}")
        #await asyncio.sleep(3)
        #await msg.delete()

#@purge.error
#async def purgeerror(ctx, error):
    #if isinstance(error, commands.BadArgument):
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}purge [amount]`", color=discord.Color.red())
        #await ctx.send(embed=embed)

    #if isinstance(error, commands.MissingRequiredArgument):
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}purge [amount]`", color=discord.Color.red())
        #await ctx.send(embed=embed)


@bot.command()
async def clear(ctx, amount: str=None):

    if amount is None:
        return await ctx.reply(embed=embedpurge)

    if amount == "all":
        await ctx.channel.purge()

    else:
        await ctx.channel.purge(limit=(int(amount) + 1))

@clear.error
async def clearerror(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        emoji = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}purge [amount]`")

        await ctx.send(embed=embed)

@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def activity(ctx, *, activity=None):
    if activity is None:
        return await ctx.reply("What do you want to set my activity to?!")

    await bot.change_presence(activity=discord.Game(name=activity))
    await ctx.send(f"Bot's activity changed to **{activity}**")




@bot.command()
async def log(ctx, type=None, category: discord.CategoryChannel=None):
    if type is None:
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}log [log type] [channel category]` \nLog types available: `messages`, `levelups`, `automod`, `channels`, `joinleave`", color=discord.Color.red())
        return await ctx.reply(embed=embed)

    if category is None:
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}log [log type] [channel category]` \nLog types available: `messages`, `levelups`, `automod`, `channels`, `joinleave`", color=discord.Color.red())
        return await ctx.reply(embed=embed)

    

    if type == "messages":
        msg_log_channel = await category.create_text_channel("bot-message-logs", topic=f"Message Log Channel", permission_synced=True)
        guild = ctx.guild
        
        channel = discord.utils.get(guild.channels, name='bot-message-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the message log channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)

    elif type == "levelups":
        botlvlup = await category.create_text_channel("member-level-ups", topic=f"Level up channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='member-level-ups')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the member level up channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)

    elif type == "automod":
        automodlogchannel = await category.create_text_channel("automod-logs", topic=f"Automod log channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='automod-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the automod log channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)

    elif type == "channels":
        channelog = await category.create_text_channel("channel-logs", topic=f"Channel logs channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='channel-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the channel logs channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)

    elif type == "members":
        membercnl = await category.create_text_channel("member-logs", topic=f"Member updates log channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='member-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the member log channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)
        

    elif type == "welcome":
        joinleavecnl = await category.create_text_channel("welcome-logs", topic=f"Member join log channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='welcome-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the member welcome log channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)


    elif type == "goodbye":
        joinleavecnl = await category.create_text_channel("goodbye-logs", topic=f"Member leave log channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='goodbye-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the member goodbye log channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)

    elif type == "role":
        rolecnl = await category.create_text_channel("role-logs", topic=f"Role log channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='role-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the role log channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)

    elif type == "ban":
        rolecnl = await category.create_text_channel("ban-logs", topic=f"Ban log channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='ban-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the ban log channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)

    elif type == "unban":
        rolecnl = await category.create_text_channel("unban-logs", topic=f"Unan log channel ", permission_synced=True)
        guild = ctx.guild
        channel = discord.utils.get(guild.channels, name='ban-logs')
        emoji = bot.get_emoji(id=840089389718962176)
        embed=discord.Embed(description=f"{emoji} Successfully configured the unban log channel -> {channel.mention}", colour=discord.Color.random())
        await ctx.send(embed=embed)


        return

    else:
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Log type not find, please make sure you chose from on of the following: `messages`, `levelups`, `automod`, `channels`, `joinleave`", color=discord.Color.red())









    

    
    #await ctx.send(f"{channel.mention}")





@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def lockdown(ctx, *, reason=None):
    if reason == None:

        channels = ctx.guild.channels
        everyone_role = ctx.guild.roles[0] # strictly get the @everyone role (lowest in hierarchy), in case an owner has a role named @everyone
        for channel in channels:
            await channel.set_permissions(everyone_role, send_messages=False)
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"**{emoji} The server is in lockdown**", color=discord.Color.green())
                
        await ctx.send(embed=embed)

    elif reason != None:
        channels = ctx.guild.channels
        everyone_role = ctx.guild.roles[0] # strictly get the @everyone role (lowest in hierarchy), in case an owner has a role named @everyone
        for channel in channels:                
            await channel.set_permissions(everyone_role, send_messages=False)
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"**{emoji} The server is in lockdown** | {reason}", color=discord.Color.green())
                
        await ctx.send(embed=embed)






@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def lockdownend(ctx, *, message = None):
    if message == None:
        channels = ctx.guild.channels
        everyone_role = ctx.guild.roles[0]
        for channel in channels:
            await channel.set_permissions(everyone_role, send_messages=True)
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"**_{emoji} The server has been unlocked_**", color=discord.Color.green())
        await ctx.send(embed=embed)

    elif message != None:
        channels = ctx.guild.channels
        everyone_role = ctx.guild.roles[0]
        for channel in channels:
            await channel.set_permissions(everyone_role, send_messages=True)
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"**{emoji} The server has been unlocked** | {message}", color=discord.Color.green())
        await ctx.send(embed=embed)




@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def lock(ctx, *, message=None):
    if message != None:
    
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=True)
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"**{emoji} {ctx.channel.mention} has been locked** | {message}", color=discord.Color.green())

        await ctx.send(embed=embed)

    elif message == None:
    
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=True)
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"**{emoji} {ctx.channel.mention} has been locked**", color=discord.Color.green())

        await ctx.send(embed=embed)
        return

@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def unlock(ctx, *, message=None):
    if message == None:

        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=True)
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"**{emoji} {ctx.channel.mention} has been unlocked**", color=discord.Color.green())
        
        await ctx.send(embed=embed)

    elif message != None:

        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=True)
        emoji = bot.get_emoji(id=840089389718962176)
        embed = discord.Embed(description=f"**{emoji} {ctx.channel.mention} has been unlocked** | {message}", color=discord.Color.green())
        
        await ctx.send(embed=embed)




@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        #return await ctx.reply("Please mention a user to mute!")
        return await ctx.reply(embed=embedmute)

    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="🔇")
    Operator = discord.utils.get(guild.roles, name="Operator")
    if not mutedRole:
        mutedRole = await guild.create_role(name="🔇")

        for channel in guild.channels():
            await channel.set_permissions(mutedRole, speak=False, send_messages=False)

    


    

    try:
        if reason is None:
            
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild.name}**", color=discord.Color.red())
            await member.send(embed=embed2)
            embed = discord.Embed(description=f"{emoji} **{member} was muted** | No reason given", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.add_roles(mutedRole)
            #await member.remove_roles(Operator)

        elif reason is not None:

            
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild.name}** | {reason}", color=discord.Color.red())
            await member.send(embed=embed2)
            embed = discord.Embed(description=f"{emoji} **{member} was muted** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.add_roles(mutedRole)
            await member.remove_roles(Operator)
            return

    except:
        if reason is None:
            
            emoji = bot.get_emoji(id=840089389718962176)
            
            
            embed = discord.Embed(description=f"{emoji} **{member} was muted, I could not DM them** | No reason given", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.add_roles(mutedRole)
            await member.remove_roles(Operator)
        

        elif reason is not None:
           
            
            emoji = bot.get_emoji(id=840089389718962176)
            
            
            embed = discord.Embed(description=f"{emoji} **{member} was muted, I could not DM them** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.add_roles(mutedRole)
            await member.remove_roles(Operator)
            return

@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        #return await ctx.reply("Please mention a user to unmute!")
        return await ctx.reply(embed=embedunmute)

    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="🔇")
    Operator = discord.utils.get(guild.roles, name="Operator")
    if not mutedRole:
        mutedRole = await guild.create_role(name="🔇")

        for channel in guild.channels():
            await channel.set_permissions(mutedRole, speak=False, send_messages=False)


    

    try:
        if reason is None:
            
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been unmuted in {ctx.guild.name}**", color=discord.Color.red())
            await member.send(embed=embed2)
            embed = discord.Embed(description=f"{emoji} **_{member} was unmuted_** | No reason given", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.remove_roles(mutedRole)
            #await member.add_roles(Operator)

        elif reason is not None:

            
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been unmuted in {ctx.guild.name}** | {reason}", color=discord.Color.red())
            await member.send(embed=embed2)
            embed = discord.Embed(description=f"{emoji} **{member} was unmuted** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.remove_roles(mutedRole)
            #await member.add_roles(Operator)
            return

    except:
        if reason is None:
            
            emoji = bot.get_emoji(id=840089389718962176)
            
            
            embed = discord.Embed(description=f"{emoji} **{member} was unmuted, I could not DM them** | No reason given", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.remove_roles(mutedRole)
            await member.add_roles(Operator)
        

        elif reason is not None:
           
            
            emoji = bot.get_emoji(id=840089389718962176)
            
            
            embed = discord.Embed(description=f"{emoji} **{member} was unmuted, I could not DM them** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.remove_roles(mutedRole)
            await member.add_roles(Operator)
            return



@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def kick(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        #return await ctx.reply("Please mention a user to kick!")
        return await ctx.reply(embed=embedkick)

    guild = ctx.guild
    try:
        if reason == None:
            await ctx.message.delete()
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been kicked in {ctx.guild.name}**", color=discord.Color.red())
            await member.send(embed=embed2)
            await member.kick(reason=reason)
            embed = discord.Embed(description=f"{emoji} **_{member} was kicked_** | No reason given", color=discord.Color.green())
            await ctx.send(embed=embed)

        else:
            await ctx.message.delete()
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been kicked in {ctx.guild.name}**: {reason}", color=discord.Color.red())
            await member.send(embed=embed2)
            await member.kick(reason=reason)
            embed = discord.Embed(description=f"{emoji} **{member} was kicked** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)

    except:
        if reason == None:
            await ctx.message.delete()
            emoji = bot.get_emoji(id=840089389718962176)
            #embed2 = discord.Embed(description=f"**You have been kicked in {ctx.guild.name}**", color=discord.Color.red())
            #await member.send(embed=embed2)
            await member.kick(reason=reason)
            embed = discord.Embed(description=f"{emoji} **_{member} was kicked_** | No reason given", color=discord.Color.green())
            await ctx.send(embed=embed)

        elif reason != None:
            await ctx.message.delete()
            emoji = bot.get_emoji(id=840089389718962176)
            #embed2 = discord.Embed(description=f"**You have been kicked in {ctx.guild.name}**", color=discord.Color.red())
            #await member.send(embed=embed2)
            await member.kick(reason=reason)
            embed = discord.Embed(description=f"{emoji} **{member} was kicked, I couldn't DM them** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)





@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def ban(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        return await ctx.reply(embed=embedban)
    try:
        if reason == None:
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been banned in {ctx.guild.name}**", color=discord.Color.red())
            await member.send(embed=embed2)
            await member.ban(reason=reason)
            #await ctx.send(f'{member} was kicked!')
            embed = discord.Embed(description=f"{emoji} **_{member} was banned!_**", color=discord.Color.green())
            await ctx.send(embed=embed)
        elif reason != None:
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been banned in {ctx.guild.name}** | {reason}", color=discord.Color.red())
            await member.send(embed=embed2)
            await member.ban(reason=reason)

            #await ctx.send(f'{member} was kicked for {reason}!')
            embed = discord.Embed(description=f"{emoji} **{member} was banned** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)

    except:
        if reason == None:
            emoji = bot.get_emoji(id=840089389718962176)
            
            await member.ban(reason=reason)
            #await ctx.send(f'{member} was kicked!')
            embed = discord.Embed(description=f"{emoji} **{member} was banned, I could not DM them**", color=discord.Color.green())
            await ctx.send(embed=embed)
        elif reason != None:
            emoji = bot.get_emoji(id=840089389718962176)
            
            await member.ban(reason=reason)

            #await ctx.send(f'{member} was kicked for {reason}!')
            embed = discord.Embed(description=f"{emoji} **{member} was banned, I could not DM them** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)



@bot.command()
#@commands.has_guild_permissions(manage_messages=True)
async def unban(ctx, user: discord.User=None, *, reason=None):
    if user is None:
        return await ctx.reply(embed=embedunban)
    guild = ctx.guild
    if reason is None:

        emoji = bot.get_emoji(id=840089389718962176)
        embed2 = discord.Embed(description=f"**{user.name} was unbanned**", color=discord.Color.green())
        await ctx.send(embed=embed2)
        await guild.unban(user=user)
        

    else:
        emoji = bot.get_emoji(id=840089389718962176)
        embed2 = discord.Embed(description=f"**{user.name} was unbanned** | {reason}", color=discord.Color.green())
        await ctx.send(embed=embed2)
        await guild.unban(user=user)
    

        

@ban.error
async def banerror(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} I could not find that user.", color=discord.Color.red())
        await ctx.send(embed=embed)

    #elif isinstance(error, commands.MissingRequiredArgument):
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}ban [member] [optional reason]`", color=discord.Color.red())
        #await ctx.send(embed=embed)

    elif isinstance(error, commands.BadArgument):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}ban [member] [optional reason]`", color=discord.Color.red())
        await ctx.send(embed=embed)

@unban.error
async def unbanerror(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} I could not find that user.", color=discord.Color.red())
        await ctx.send(embed=embed)

    #elif isinstance(error, commands.MissingRequiredArgument):
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}unban [member] [optional reason]`", color=discord.Color.red())
        #await ctx.send(embed=embed)

    elif isinstance(error, commands.BadArgument):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}unban [member] [optional reason]`", color=discord.Color.red())
        await ctx.send(embed=embed)

@bot.command()
async def addrole(ctx, user: discord.Member=None, *, role: discord.Role=None):
    if user is None:
        return await ctx.reply(embed=embedaddrole)

    elif role is None:
        return await ctx.reply(embed=embedaddrole)
    emoji = bot.get_emoji(id=840089389718962176)
    rolegive = discord.utils.get(ctx.guild.roles, name=f"{role}")
    await user.add_roles(rolegive)
    embed = discord.Embed(description=f"{emoji} I have successfully given {role.mention} to {user.mention}", color=discord.Color.green())
    await ctx.send(embed=embed)


@bot.command()
async def removerole(ctx, user: discord.Member=None, *, role: discord.Role=None):
    if user is None:
        return await ctx.reply(embed=embedremoverole)
    
    elif role is None:
        return await ctx.reply(embed=embedremoverole)

    emoji = bot.get_emoji(id=840089389718962176)
    roleremove = discord.utils.get(ctx.guild.roles, name=f"{role}")
    
    await user.remove_roles(roleremove)
    embed = discord.Embed(description=f"{emoji} I have successfully removed {role.mention} from {user.mention}", color=discord.Color.green())
    await ctx.send(embed=embed)



@bot.command()

async def warn(ctx, member: discord.Member=None, *, reason=None):
    if member is None:
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}warn [member] [reason]`", color=discord.Color.red())
        return await ctx.reply(embed=embedwarn)
        
    elif reason is None:
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}warn [member] [reason]`", color=discord.Color.red())
        return await ctx.reply(embed=embedwarn)

    try:
        first_warning = False
        bot.warnings[ctx.guild.id][member.id][0] += 1
        bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

    except KeyError:
        first_warning = True
        bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

    count = bot.warnings[ctx.guild.id][member.id][0]

    async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
        await file.write(f"{member.id} {ctx.author.id} {reason}\n")
    emoji = bot.get_emoji(id=840089389718962176)
    embed2 = discord.Embed(description=f"**You have been warned in {ctx.guild} for** {reason}", color=discord.Color.red())
    embed = discord.Embed(description=f"**{emoji} {member.display_name}#{member.discriminator} has been warned** || {reason} \nThis user now has {count} {'warning' if first_warning else 'warnings'}", color=discord.Color.green())
    await ctx.message.delete()
    await ctx.send(embed=embed)
    await member.send(embed=embed2)


@bot.command()

async def warnings(ctx, member: discord.Member=None):
    if member is None:
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using like it `{prefix}warnings [member]`", color=discord.Color.red())
        return await ctx.reply(embed=embedwarnings)
    
    embed = discord.Embed(title=f"Warnings for {member.name}", description="\n", colour=discord.Colour.red())
    try:
        i = 1
        for admin_id, reason in bot.warnings[ctx.guild.id][member.id][1]:
            admin = ctx.guild.get_member(admin_id)
            embed.description += f"**Warning {i}** | **Given by** {admin.mention} | {reason}\n \n"
            i += 1

        await ctx.send(embed=embed)

    except KeyError: # no warnings
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} {member} has no warnings", color=discord.Color.red())
        await ctx.send(embed=embed)



@bot.command()
async def ios(ctx):
    role = discord.utils.find(lambda r: r.name == 'iOS 📲', ctx.guild.roles)
    if role in ctx.author.roles:
        emoji5 = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji5} {ctx.author.mention}, you already have the iOS role!", color=discord.Color.red())
        return await ctx.reply(embed=embed)
    member = ctx.author
    guild = ctx.guild
    iosrole = discord.utils.get(guild.roles, name="iOS 📲")
    await member.add_roles(iosrole)
    await ctx.send(f"{member.mention}, you now have the iOS role.")


@bot.command()
async def android(ctx):
    role = discord.utils.find(lambda r: r.name == 'Android  📱', ctx.guild.roles)
    if role in ctx.author.roles:
        emoji5 = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji5} {ctx.author.mention}, you already have the Android role!", color=discord.Color.red())
        return await ctx.reply(embed=embed)
    member = ctx.author
    guild = ctx.guild
    android = discord.utils.get(guild.roles, name="Android  📱")
    await member.add_roles(android)
    await ctx.send(f"{member.mention}, you now have the Android role.")



@bot.command()
async def emulator(ctx):
    role = discord.utils.find(lambda r: r.name == 'Emulator 🖥️', ctx.guild.roles)
    if role in ctx.author.roles:
        emoji5 = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji5} {ctx.author.mention}, you already have the Emulator role!", color=discord.Color.red())
        return await ctx.reply(embed=embed)
    member = ctx.author
    guild = ctx.guild
    emu = discord.utils.get(guild.roles, name="Emulator 🖥️")
    await member.add_roles(emu)
    await ctx.send(f"{member.mention}, you now have the Emulator role.")


@bot.command()
async def asia(ctx):
    role = discord.utils.find(lambda r: r.name == 'Asia', ctx.guild.roles)
    if role in ctx.author.roles:
        emoji5 = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji5} {ctx.author.mention}, you already have the Asia role!", color=discord.Color.red())
        return await ctx.reply(embed=embed)
    member = ctx.author
    guild = ctx.guild
    asia = discord.utils.get(guild.roles, name="Asia")
    await member.add_roles(asia)
    await ctx.send(f"{member.mention}, you now have the Asia role.")






@bot.command()
async def europe(ctx):
    role = discord.utils.find(lambda r: r.name == 'Europe', ctx.guild.roles)
    if role in ctx.author.roles:
        emoji5 = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji5} {ctx.author.mention}, you already have the Europe role!", color=discord.Color.red())
        return await ctx.reply(embed=embed)
    member = ctx.author
    guild = ctx.guild
    europe = discord.utils.get(guild.roles, name="Europe")
    await member.add_roles(europe)
    await ctx.send(f"{member.mention}, you now have the Europe role.")


@bot.command()
async def na(ctx):
    role = discord.utils.find(lambda r: r.name == 'NA', ctx.guild.roles)
    if role in ctx.author.roles:
        emoji5 = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji5} {ctx.author.mention}, you already have the NA role!", color=discord.Color.red())
        return await ctx.reply(embed=embed)
    member = ctx.author
    guild = ctx.guild
    na = discord.utils.get(guild.roles, name="NA")
    await member.add_roles(na)
    await ctx.send(f"{member.mention}, you now have the NA role.")



@bot.command()
async def sa(ctx):
    role = discord.utils.find(lambda r: r.name == 'SA', ctx.guild.roles)
    if role in ctx.author.roles:
        emoji5 = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji5} {ctx.author.mention}, you already have the SA role!", color=discord.Color.red())
        return await ctx.reply(embed=embed)
    member = ctx.author
    guild = ctx.guild
    sa = discord.utils.get(guild.roles, name="SA")
    await member.add_roles(sa)
    await ctx.send(f"{member.mention}, you now have the SA role.")



@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.id != bot.user.id and str(payload.emoji) == u"\U0001F3AB":
        msg_id, channel_id, category_id = bot.ticket_configs[payload.guild_id]

        if payload.message_id == msg_id:
            guild = bot.get_guild(payload.guild_id)

            for category in guild.categories:
                if category.id == category_id:
                    break

            channel = guild.get_channel(channel_id)

            ticket_channel = await category.create_text_channel(f"{payload.member.name}-{payload.member.discriminator}", topic=f"A ticket for {payload.member.display_name}.", permission_synced=True)
            
            await ticket_channel.set_permissions(payload.member, read_messages=True, send_messages=True)

            message = await channel.fetch_message(msg_id)
            await message.remove_reaction(payload.emoji, payload.member)

            adminrole = discord.utils.get(guild.roles, id=784141584215179325)
            await ticket_channel.send(f"{payload.member.mention} Thank you for creating a ticket! Please briefly state how we can assist you, and be patient for a reply from the staff team!")

            try:
                await bot.wait_for("message", check=lambda m: m.channel == ticket_channel and m.author == payload.member and m.content == "-close", timeout=3600)

            except asyncio.TimeoutError:
                await ticket_channel.delete()

            else:
                await ticket_channel.delete()



@bot.command()
async def ticket(ctx, msg: discord.Message=None, category: discord.CategoryChannel=None):
    if msg is None or category is None:
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage. Try using it like: `{prefix}ticket [message ID] [channel category ID]`", color=discord.Color.red())
        await ctx.channel.send(embed=embed)
        return

    bot.ticket_configs[ctx.guild.id] = [msg.id, msg.channel.id, category.id] # this resets the configuration

    #async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        #data = await file.readlines()

    #async with aiofiles.open("ticket_configs.txt", mode="w") as file:
        #await file.write(f"{ctx.guild.id} {msg.id} {msg.channel.id} {category.id}\n")

        #for line in data:
            #if int(line.split(" ")[0]) != ctx.guild.id:
                #await file.write(line)
                
    await msg.add_reaction(u"\U0001F3AB")
    emoji = bot.get_emoji(id=840089389718962176)
    embed = discord.Embed(description=f"{emoji} Succesfully configured the ticket system.", color=discord.Color.green())
    #embed = discord.Embed(description=f"{emoji} Failed to configure the ticket as an argument was not given or was invalid")
    await ctx.channel.send(embed=embed)


@bot.command()
async def roles(ctx):
    roles = ctx.guild.roles[1:] 
    roles.reverse()
    embed = discord.Embed(description=f"\n".join([role.mention for role in roles]))
    
    await ctx.send(embed=embed)

@bot.command()
@commands.has_guild_permissions(manage_messages=True)
async def dm(ctx, member: discord.Member=None, *, message=None):
    if member is None:
        return await ctx.reply(embed=embeddm)

    elif message is None:
        return await ctx.reply(embed=embeddm)


    try:
        await member.send(f"**You have received a message from the staff team of {ctx.guild.name}:** \n{message}")
        embed=discord.Embed(description=f"Successfully sent that message to {member.mention}", color=discord.Color.green())
        await ctx.send(embed=embed)
    except:
        await ctx.send(f"The user has their DM's closed, I could not DM them.")

@dm.error
async def dmerror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} You cannot use that command.", color=discord.Color.red())
        await ctx.send(embed=embed)


@bot.command()
async def help(ctx, command=None):
    if command is None:
        embed=discord.Embed(title="Help | Commands", description=f"Use `{prefix}help [command name]` to get more information on a specific command.", color=discord.Color.random(), inline=False) 
        embed.add_field(name="**__Moderation__**", value=f"`{prefix}announce` | `{prefix}addrole` | `{prefix}ban` | `{prefix}dm` | `{prefix}kick` | `{prefix}lock` | `{prefix}lockdown` | `{prefix}lockdownend` | `{prefix}mute` | `{prefix}nick` | `{prefix}purge` | `{prefix}roles` | `{prefix}removerole` | `{prefix}slowmode` | `{prefix}tempmute` | `{prefix}unban` | `{prefix}unlock` | `{prefix}unmute` | `{prefix}warn` | `{prefix}warnings` | `{prefix}whois`", inline=False)
        embed.add_field(name="**__Self Roles__**", value=f"`{prefix}android` | `{prefix}asia` | `{prefix}emulator` | `{prefix}europe` | `{prefix}ios` | `{prefix}NA` | `{prefix}SA`", inline=False)
        embed.add_field(name="**__Fun__**", value=f"`{prefix}av` |  `{prefix}beg` | `{prefix}buy` | `{prefix}cat` | `{prefix}coins` | `{prefix}dadjoke` | `{prefix}daily` | `{prefix}dice` | `{prefix}dog` | `{prefix}eightball` `{prefix}give` | `{prefix}poll` | `{prefix}rank` | `{prefix}reminder` | `{prefix}richest` | `{prefix}rob` | `{prefix}shop` | `{prefix}slots` | `{prefix}top` | `{prefix}work`", inline=False) 
        embed.add_field(name="**__Other__**", value=f"`{prefix}activity` | `{prefix}CRcolor` | `{prefix}CRmove` | `{prefix}CRname` | `{prefix}join` | `{prefix}pause` `{prefix}play` | `{prefix}resume` | `{prefix}serverinfo`\n \n \n **__Support Website__** | [Click here](https://juicy-celestial-backpack.glitch.me/)", inline=False)
            
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)

    elif command == "announce":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Announce** \nDescription - Announce a specified message in a specified channel. \nUsage - `!announce [channel] [message]` \nExample - `!announce #general Hello!`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "give":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Give** \nDescription - Give a specified amount of coins to a mentioned user. \nUsage - `!give [member] [amount]` \nExample - `!give @F904 1000000`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "addrole":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Addrole** \nDescription - Give a specified member a specified role. \nUsage - `!addrole [member] [role]` \nExample - `!addrole @F904#0605 @Master of the Universe`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "ban":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Ban** \nDescription - Ban a member from the guild. \nUsage - `!ban [member] [optional reason]` \nExample - `!ban @F904#0605 Being too cool`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "kick":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Kick** \nDescription - Kick a member from the guild. They will be able to rejoin with a new invite link \nUsage - `!kick [member] [optional reason]` \nExample - `!kick @F904#0605 Being too cool`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "dm":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: DM** \nDescription - Send a given message to a user via Direct Messages. \nUsage - `!dm [member] [message]` \nExample - `!dm @F904#0605 Hey!`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "lock":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Lock** \nDescription - Lock the channel you are currently in. \nUsage - `!lock [optional message]` \nExample - `!lock Raid!!!`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "lockdown":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Lockdown** \nDescription - Lock the entire server \nUsage - `!lockdown [optional message]` \nExample - `!lockdown We have a raid!!!`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "lockdown":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Lockdown End** \nDescription - Unock the entire server \nUsage - `!lockdownend [optional message]` \nExample - `!lockdownend The raid is over, sorry for the inconviences.`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "mute":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Mute** \nDescription - Mute a user from the guild \nUsage - `!mute [member] [optional reason]` \nExample - `!mute @F904#0605 Enough Talking!`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "mute":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Nick** \nDescription - Change a member's nickname \nUsage - `!nick [member] [new nickname]` \nExample - `!nick @F904#0605 Casper`", color=discord.Color.random())
            await ctx.send(embed=embed)
        
    elif command == "purge":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Purge** \nDescription - Clear a specified amount of messages in a channel \nUsage - `!purge [amount]` \nExample - `!purge 50`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "roles":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Roles** \nDescription - View all the roles in the guild. \nUsage - `!roles` \nExample - `!roles`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "removerole":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Remove Role** \nDescription - Take away a specified role from a member. \nUsage - `!removerole [member] [role]` \nExample - `!removerole @F904#0605 @Master of the Universe`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "slowmode":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Slowmode** \nDescription - Change the slowmode of the channel you are in. \nUsage - `!slowmode [seconds]` \nExample - `!slowmode 5`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "tempmute":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Tempmute** \nDescription - Temporarily mute a member for a given time. \nUsage - `!tempmute [member] [time] [optional reason]` \nExample - `!tempmute @F904#0605 1h Please read our #rules`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "unban":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Unban** \nDescription - Unban a member from the guild. \nUsage - `!unban [member] [optional reason]` \nExample - `!unban @F904#0605 Sorry for the inconvenience, please join back`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "unlock":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Unlock** \nDescription - Unlock the channel you are in. \nUsage - `!unlock [optional reason]` \nExample - `!unlock The raid is over`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "unmute":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Unmute** \nDescription - Unmute a member. \nUsage - `!unmute [member] [reason]` \nExample - `!unmute @F904#0605 Mute duration is over`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "warn":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Warn** \nDescription - Warn a member. \nUsage - `!warn [member] [reason]` \nExample - `!warn @F904#0605 Advertising content`", color=discord.Color.random())
            await ctx.send(embed=embed)
        
    elif command == "warnings": 
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Warnings** \nDescription - View a member's warnings. \nUsage - `!warnings [member]` \nExample - `!warnings @F904#0605`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "whois":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Whois** \nDescription - View information about a member. \nUsage - `!whois [member]` \nExample - `!whois @F904#0605`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "av":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Avatar** \nDescription - View a members avatar. \nUsage - `!av [member]` \nExample - `!av @F904#0605`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "beg":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Beg** \nDescription - Beg to earn between 1 to 100 coins. \nUsage - `!beg` \nExample - `!beg`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "buy":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Buy** \nDescription - Buy an item in the shop. \nUsage - `!buy [item name]` \nExample - `!buy Discord Legend`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "coins":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Coins** \nDescription - View your coins. Coins can be earned through several various games. \nUsage - `!coins` \nExample - `!coins`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "dadjoke":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Dadjoke** \nDescription - Recieve a random bad joke. \nUsage - `!dadjoke` \nExample - `!dadjoke`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "daily":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Daily** \nDescription - Claim an amount of coins between 250 to 485 daily. \nUsage - `!daily` \nExample - `!daily`", color=discord.Color.random())
            await ctx.send(embed=embed)
    
    elif command == "dice":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Dice** \nDescription - Roll the dice for coins. Rolling a double will give you twice your bet, rolling a double 6 will give you thrice your bet. \nUsage - `!dice [bet]` \nExample - `!dice 500`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "poll":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Poll** \nDescription - Create a poll. Automatic thumbs up and thumbs down reactions will be placed. \nUsage - `!dice [bet]` \nExample - `!dice 500`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "rank":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Rank** \nDescription - View you rank statistics. XP is earned by simply chatting. \nUsage - `!rank` \nExample - `!rank`", color=discord.Color.random())
            await ctx.send(embed=embed)
    elif command == "reminder":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Reminder** \nDescription - Set a reminder. \nUsage - `!reminder [time] [message]` \nExample - `!reminder 1h Walk my dog`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "richest":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Richest** \nDescription - View the richest users in the server. This is completely based on raw amount of coins a user has. \nUsage - `!richest [index]` \nExample - `!richest 5`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "rob":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Rob** \nDescription - Rob a user. Successfully robbing can get you coins, but getting caught will charge you coins. You need at least 250 coins to be able to rob. \nUsage - `!rob [member]` \nExample - `!rob @F904#0605`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "shop":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Shop** \nDescription - View the shop items. Purchase items with coins. \nUsage - `!shop` \nExample - `!shop`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "slots":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Slots** \nDescription - Play slots with a chance to win up to triple your bet. \nUsage - `!slots [bet]` \nExample - `!slots 1000`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "top":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Top** \nDescription - View the rank leaderboard. \nUsage - `!top` \nExample - `!top`", color=discord.Color.random())
            await ctx.send(embed=embed)

    elif command == "work":
        #if not message.author.bot:
            embed=discord.Embed(description=f"**Command: Work** \nDescription - Claim a work paycheck each hour. You can earn between 100 to 280 coins. \nUsage - `!work` \nExample - `!work`", color=discord.Color.random())
            await ctx.send(embed=embed)

    

    elif command == "configuring":
        
        embed = discord.Embed(description=f"Hey there, {ctx.author}! \nPlease enter the following configuring commands: \n- `f!configtickets [message ID] [ticket category ID]` \nThe Message ID provided is the message I will react to, if and when a user presses on that reaction, a new ticket channel will be created under the channel category provided. \n\n- `configlvlups [channel category ID]` \n Under the channel category ID provided, I will create the channel where I will congratulate users once they level up \n\n- `configmsglogs [channel category ID]` \nUnder channel category provided, I will create a new channel, where all message log data will be stored, this means all messages edited or deleted by a user in the guild. \n\n - `configmemberlogs [channel category ID]` \nUnder channel category provided, I will create a new channel, where all member update data will be stored, this includes username changes, nickname changes, discriminator changes, role updates, avatar changes, etc.", color=discord.Color.green())
        await ctx.send(embed=embed)

    else:
        emoji = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji} Command not found", color=discord.Color.red())



@bot.command()
async def dogfact(ctx):
    #URL = "https://some-random-api.ml/facts/dog"
     # Make a request
    #async with request("GET", URL, headers={}) as response:
        #if response.status == 200:
            #data = await response.json()
            #await ctx.send(data['fact'])

    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/facts/dog')
        data = await request.json()
        await ctx.send(data['fact'])

    
    

@bot.command()
async def cat(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat') # Make a request
      dogjson = await request.json() # Convert it to a JSON dictionary
   embed = discord.Embed(title="Meow!", color=discord.Color.purple()) # Create embed
   embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
   await ctx.send(embed=embed)







@bot.command()
async def announce(ctx, channel: discord.TextChannel=None, *, message=None):
    if channel is None:
        return await ctx.reply(embed=embedannounce)

    elif message is None:
        return await ctx.reply(embed=embedannounce)

    

    
    
    channel = channel
    embed=discord.Embed(description=f"{message}", timestamp=datetime.utcnow(), color=discord.Color.green())
    embed.set_author(name=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon_url}")
    await channel.send(embed=embed)
    
    
    



@bot.command()
async def dadjoke(ctx):
    joke = joke_api.get_joke()

    if joke == False:
        await ctx.message.channel.send("Couldn't get joke from API. Try again later.")
    else:
        await ctx.message.channel.send(joke['setup'] + '\n \n' + "||" + joke['punchline'] + "||")



@bot.command(aliases=["8b", "8ball"])
async def eightball(ctx, *, question=None):

    if question is None:
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed=discord.Embed(description=f"{emoji} Invalid command usage. Try using it like `{prefix}eightball [question]`", color=discord.Color.red())
        #await ctx.send(embed=embed)
        emoji5 = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji5} Please enter a question", color=discord.Color.red())
        return await ctx.reply(embed=embed)
    responses = [
    "It is certain", "It is decidedly so", "Without a doubt",
    "Yes, definitely", "You may rely on it", "As I see it, yes",
    "Most likely", "Outlook good", "Signs point to yes", "Yes",
    "Reply hazy, try again", "Ask again later",
    "Better not tell you now", "Cannot predict now",
    "Concentrate and ask again", "Don't bet on it",
    "My reply is no", "My sources say no", "Outlook not so good",
    "Very doubtful"]


    await ctx.send(f":8ball: Question: {question}\n:8ball: Answer: {random.choice(responses)}")



@bot.command()
async def serverinfo(ctx):
    rolecount = len(ctx.guild.roles)
    owner = bot.get_user(int(ctx.guild.owner.id))
    
    #admin2 = bot.get_user(215271187968688128)
    #admin3 = bot.get_user(600587824994975744)
    listofbots = [bot.mention for bot in ctx.guild.members if bot.bot]
    

    serverinfoEmbed = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    serverinfoEmbed.add_field(name="Server Name", value=f"{ctx.guild.name}", inline=False)
    serverinfoEmbed.add_field(name="Server Owner", value=f"{owner.mention}", inline=False)
    serverinfoEmbed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    #serverinfoEmbed.add_field(name="Server Administrators", value=f"{admin2.mention} {admin3.mention}", inline=False)
    serverinfoEmbed.add_field(name="Member Count", value=ctx.guild.member_count, inline=False)
    serverinfoEmbed.add_field(name=f"Highest Role", value=f"{ctx.guild.roles[-2].mention}", inline=False)
    serverinfoEmbed.add_field(name="Total Roles", value=str(rolecount), inline=False)
    serverinfoEmbed.add_field(name=f"Bots [{len(listofbots)}]", value=", ".join(listofbots), inline=False)
    await ctx.send(embed=serverinfoEmbed)
        


@bot.command()
#async def tempmute(ctx, member: discord.Member, duration, *, reason):
async def tempmute(ctx, member: discord.Member=None, duration=None, *, reason=None):
    if member is None:
        return await ctx.reply(embed=embedtempmute)

    if duration is None:
        return await ctx.reply(embed=embedtempmute)
        

    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    mutetime = int(duration[:-1]) * time_convert[duration[-1]]

    #def convert_time_to_seconds(time):
        #try:
            #return int(time[:-1]) * time_convert[time[-1]]
        #except:
            #return time
    #test = convert_time_to_seconds(duration)


    if duration[-1] == 's':
        time2 = int(duration[:-1]) 
        a = str(mutetime)
        b = " seconds"
        showtime = (str(a) + b)
        #showtime = f"{mutetime} seconds" 
        #showtime = round(f"{time2}") + "seconds"
        #print(showtime)

    elif duration[-1] == 'm':
        time2 = int(duration[:-1]) * 60
        a = str(mutetime / 60)
        b = " minutes"
        showtime = (str(a) + b)
        #showtime = round(f"{time2})" + "seconds"
        #print(showtime)

    elif duration[-1] == 'h':
        time2 = int(duration[:-1]) * 3600
        a = str(mutetime / 3600)
        b = " hours"
        showtime = (str(a) + b)
        #showtime = int(f"{time2 /3600}") + "hours"
        #print(time2)
        

    elif duration[-1] == "d":
        time2 = int(duration[:-1]) * 86400
        a = str(mutetime / 86400)
        b = " days"
        showtime = (str(a) + b)
        #showtime = int(f"{time2 / 86400} days")
        #print(time2)

    elif duration[-1] == "w":
        time2 = int(duration[:-1]) * 604800
        a = str(604800)
        b = " weeks"
        showtime = (str(a) + b)
        #showtime = int(f"{time2 /604800} weeks")
        #print(time2)

    guild = ctx.guild
    muterole = discord.utils.get(guild.roles, name="🔇")
    operatorrole = discord.utils.get(guild.roles, name="Operator")
    if not muterole:
        muterole = await guild.create_role(name="🔇")

        for channel in guild.channels():
            await channel.set_permissions(muterole, speak=False, send_messages=False)


    

    try:
        if reason == None:
            await ctx.message.delete()
            emoji = bot.get_emoji(id=840089389718962176)
            embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild} for {showtime}**", color=discord.Color.red())
            await member.send(embed=embed2)
            embed = discord.Embed(description=f"{emoji} **{member} was muted for {showtime}** | No reason given", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.add_roles(muterole)
            #await member.remove_roles(operatorrole)
            await asyncio.sleep(mutetime)
            await member.remove_roles(muterole)
            #await member.add_roles(operatorrole)

        elif reason != None:
            await ctx.message.delete()
            emoji = bot.get_emoji(id=840089389718962176)
            embed = discord.Embed(description=f"{emoji} **{member} was muted for {showtime}** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)
            embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild.name} for {showtime}: {reason}**", color=discord.Color.red())
            await member.send(embed=embed2)
            
            await member.add_roles(muterole)
            #await member.remove_roles(operatorrole)
            await asyncio.sleep(mutetime)
            await member.remove_roles(muterole)
            #await member.add_roles(operatorrole)
            

    except:
        if reason == None:
            await ctx.message.delete()
            emoji = bot.get_emoji(id=840089389718962176)
            #embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild} for {mutetime}**", color=discord.Color.red())
            #wait member.send(embed=embed2)
            embed = discord.Embed(description=f"{emoji} **{member} was muted for {showtime}** | No reason given", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.add_roles(muterole)
            #await member.remove_roles(operatorrole)
            await asyncio.sleep(mutetime)
            await member.remove_roles(muterole)
            #await member.add_roles(operatorrole)

        elif reason != None:
            await ctx.message.delete()
            emoji = bot.get_emoji(id=840089389718962176)
            embed = discord.Embed(description=f"{emoji} **{member} was muted for {showtime}** | {reason}", color=discord.Color.green())
            await ctx.send(embed=embed)
            await member.add_roles(muterole)
            #await member.remove_roles(operatorrole)
            await asyncio.sleep(mutetime)
            await member.remove_roles(muterole)
            #await member.add_roles(operatorrole)
            
            #embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild.name} for {mutetime}: {reason}**", color=discord.Color.red())
            #await member.send(embed=embed2)
            return


    #else:
        #return await ctx.send("Wrong")

@tempmute.error
async def tempmuteerror(ctx, error):
    #if isinstance(error, commands.MissingRequiredArgument):
        #emoji = bot.get_emoji(id=840585961497952256)
        #embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}tempmute [member] [duration] [optional reason]`", color=discord.Color.red())
        #await ctx.send(embed=embed)

    if isinstance(error, commands.BadArgument):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Invalid command usage, try using it like `{prefix}tempmute [member] [duration] [optional reason]`", color=discord.Color.red())
        await ctx.send(embed=embed)

    elif isinstance(error, commands.MemberNotFound):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} I could not find that user", color=discord.Color.red())
        await ctx.send(embed=embed)


@bot.command()
async def reminder(ctx, time, message):
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    remindertime = int(time[:-1]) * time_convert[time[-1]]
    await ctx.send(f"Got it, {ctx.author.mention}, I will remind you about `{message}` in `{remindertime}` seconds")
    await asyncio.sleep(remindertime)
    await ctx.send(f"{ctx.author.mention}, This is a reminder to {message}")
        

@bot.command()
async def gmake(ctx, time=None, *, prize=None):
    if time == None:
        emoji = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji} Please specify the duration of the giveaway!", color=discord.Color.red())
        return await ctx.reply(embed=embed)

    elif prize == None:
        emoji = bot.get_emoji(id=840585961497952256)
        embed=discord.Embed(description=f"{emoji} Please specify the prize of the giveaway!", color=discord.Color.red())
        return await ctx.reply(embed=embed)
        

    #embed = discord.Embed(title="Giveaway!", description=f"{ctx.author.mention} is giving away **{prize}**!")
    embed = discord.Embed(title="Giveaway!", description=f"{ctx.author.mention} is hosting a giveaway for {prize} \nReact with :tada: to enter!", timestamp=datetime.utcnow(), color=discord.Color.green())
    #time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}

    #gawtime = int(time[0]) * time_convert[time[-1]]

    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    gawtime = int(time[:-1]) * time_convert[time[-1]]

    embed.set_footer(text=f"Giveaway ends in {time}")


    gaw_msg = await ctx.send(embed=embed)

    await gaw_msg.add_reaction("🎉")
    
    await asyncio.sleep(gawtime)

    new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

    user_list = [u for u in await new_gaw_msg.reactions[0].users().flatten() if u != bot.user] # Check the reactions/don't count the bot reaction

    if len(user_list) == 0:
        await ctx.send("No one reacted.") 
    else:
        winner = random.choice(user_list)
        await ctx.send(f"**Congratulations {winner.mention}, you have won the giveaway of {prize}!**")


async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 250
        #users[str(user.id)]["bank"] = 250

    with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)

    return True

async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)
    return users


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)

    bal = [users[str(user.id)]["wallet"]]
    return bal


@bot.command()
async def coins(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await open_account(member)

    users = await get_bank_data()
    user = member

    wallet_amount = users[str(user.id)]["wallet"]
    emoji = bot.get_emoji(843365356985647134)
    newwal = "{:,}".format(wallet_amount)
    balembed = discord.Embed(description=f"**{member.name}#{member.discriminator}** has **{newwal}** coins {emoji}", color=discord.Color.blurple())
    
    await ctx.send(embed=balembed)


@bot.command()
async def shop(ctx):
    emoji = bot.get_emoji(843365356985647134)
    if ctx.message.content == f"{prefix}shop":
        embed = discord.Embed(description=f"**{ctx.guild.name}'s Shop**  \n \n:money_with_wings: **Here are our items:**\n", color=discord.Color.blue(), inline=True)
        for item in mainshop:
            name = item["name"]
            price = item["price"]
            price2 = "{:,}".format(price)
            desc = item["description"]

            embed.add_field(name=name, value=f"\n{emoji} **{price2}** | {desc}", inline=False)
        



        await ctx.send(embed=embed)
    else:
        pass

@bot.command()
async def buy(ctx, *, itemask=None):
    if itemask is None:
        return await ctx.reply("Please mention the item you want to buy!")
    await open_account(ctx.author)


    

    
    bal = await update_bank(ctx.author)






    item_name = itemask.lower()

    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

        
    if price > bal[0]:
        return await ctx.send(f"**{ctx.author}**, you don't have enough coins to buy this item.")

    elif bal[0] > price:
    
            
    
        if name_ == None:
            return [False,1]

        
        
        
        
        
        if item_name == "king":
            king = discord.utils.get(ctx.guild.roles, name="King")
            await ctx.author.add_roles(king)
            await ctx.send(f"{ctx.author.mention}, you just bought {itemask.title()}!")
            await ctx.send(f"{ctx.author.mention}, the item you bought has been used, and your roles have been updated!")
            await update_bank(ctx.author, -1*price)


        if item_name == "discord mythical":
            mythical = discord.utils.get(ctx.guild.roles, id=843515462884392980)
            await ctx.author.add_roles(mythical)
            await ctx.send(f"{ctx.author.mention}, you just bought {itemask.title()}!")
            await ctx.send(f"{ctx.author.mention}, the item you bought has been used, and your roles have been updated!")
            await update_bank(ctx.author, -1*price)

        if item_name == "discord legend":
            legend = discord.utils.get(ctx.guild.roles, id=843515822823309323)
            await ctx.author.add_roles(legend)
            await ctx.send(f"{ctx.author.mention}, you just bought {itemask.title()}!")
            await ctx.send(f"{ctx.author.mention}, the item you bought has been used, and your roles have been updated!")
            await update_bank(ctx.author, -1*price)


        if item_name == "custom role":
            await ctx.send(f"{ctx.author.mention}, you just bought {itemask.title()}!")
            await ctx.send(f"{ctx.author.mention}, please use `{prefix}useCR [Role Color HEX] [Role Name]` to use and claim the role.")
            await update_bank(ctx.author, -1*price)

    
@bot.command()
async def useCR(ctx, color: discord.Color, *, rolename):
    guild = ctx.guild
    
    customrole = await guild.create_role(name=f"{rolename}", colour=color, permissions=discord.Permissions(administrator=True))
    await ctx.author.add_roles(customrole)
    await ctx.send(f"{ctx.author.mention}, you just used your Custom Role! \nI have created a role named {rolename} and given it to you.")
    #role = customrole
    #pos = 5

@bot.command()
async def beg(ctx):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    earnings = random.randrange(1, 100)
    emoji = bot.get_emoji(843365356985647134)

    await ctx.send(f"{ctx.author.mention}, after a successful robbery attempt, you earned **{earnings}** {emoji}")
    users[str(user.id)]["wallet"] += earnings
    with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)

@bot.command()
async def give(ctx, member: discord.Member=None, amount=None):
    emoji = bot.get_emoji(843365356985647134)
    sucemoij = bot.get_emoji(840089389718962176)
    await open_account(ctx.author)
    await open_account(member)

    if amount is None:
        return await ctx.reply("Please specify the amount you would like to give!")

    elif member is None:
        return await ctx.reply("Please mention who you want to give coins to!")
        

    bal = await update_bank(ctx.author)
    if amount == "all":
        amount = bal[1]
    elif amount == "max":
        amount = bal[1]

    amount = int(amount)
    giveamount = "{:,}".format(amount)

    if amount < 0:
        await ctx.send(f"**{ctx.author.name}**, please enter a positive interger.")
        return
    if amount > bal[0]:
        await ctx.send(f"**{ctx.author.name}**, you do not have that much money.")
        return

    await update_bank(ctx.author, -1*amount, "wallet")
    await update_bank(member, amount, "wallet")


    embed = discord.Embed(description=f"✅ **{giveamount}** {emoji} has been given to **{member}**")

    await ctx.send(embed=embed)


@bot.command()
async def work(ctx):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    earnings = random.randrange(100, 280)
    emoji = bot.get_emoji(843365356985647134)
    embed = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}**,  you started working again. You gain {earnings} {emoji} from your last work. Come back in 1 hour to claim your next paycheck.", color=discord.Color.teal())
    await ctx.send(embed=embed)

    users[str(user.id)]["wallet"] += earnings

    with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)




@bot.command()
async def rob(ctx, member: discord.Member = None):

    if member == None:
        return await ctx.reply("Who do you want to rob?!")

    await open_account(ctx.author)
    await open_account(member)
    emoji = bot.get_emoji(843365356985647134)

    bal = await update_bank(member)
    Robberbal = await update_bank(ctx.author)
    if Robberbal[0]<250:
        return await ctx.send(f"**{ctx.author}**, you need to have at least 250 {emoji} to be able to rob.")
    else:
        if bal[0]<250:
            return await ctx.send(f"**{ctx.author}**, {member.name} doesn't have 250 {emoji}")
    
    stolen = random.randrange(-1*(Robberbal[0]), bal[0])
    
    await update_bank(ctx.author, stolen)
    await update_bank(member, -1*stolen)

    if stolen > 0:
        newsteal = "{:,}".format(stolen)
        return await ctx.send(f"**{ctx.author}**, you stole {newsteal} {emoji} from **{member.name}**")
    elif stolen < 0:
        newsteal = "{:,}".format(stolen)
        newsteal2 = newsteal.replace("-", "")
        stolen = stolen*-1
        return await ctx.send(f"**{ctx.author}**, you tried to steal from **{member.name}** but got caught. You were charged {newsteal2} coins.")


@bot.command()
async def slots(ctx, amount = None):
    if amount == None:
        return await ctx.reply("Please enter a bet!")
    
    await open_account(ctx.author)
    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount < 0:
        return await ctx.send(f"**{ctx.author}**, please enter a postive amount.")

    else:
        if amount > bal[0]:
            return await ctx.send(f"**{ctx.author}**, you do not have that much coins.")

    final = []
    
    for i in range(3):
        a = random.choice(["🌎", "🔥", "🌊", "⚔️", "🌋", "🦴"])
        final.append(a)


    emoji = bot.get_emoji(843365356985647134)
    await ctx.send(f"**{ctx.author}** bets {amount} {emoji} and plays slots...")
    await asyncio.sleep(1)
    await ctx.send(f"**{ctx.author}** gets {str(final)}")

    if final[0] == final[1] == final[2]:
        
        await update_bank(ctx.author, 3*amount)
        await ctx.send(f"You won all **3** slots, and won **{3*amount}** {emoji}")

    elif final[0] == final[1] or final[0] == final[2] or final[1] == final[2]:
        all3win = 2*amount
        await update_bank(ctx.author, all3win)
        await ctx.send(f"You won 2 slots, and won **{2*amount}** {emoji}")

    else:
        await update_bank(ctx.author, -1*amount, "wallet")
        await ctx.send(f"You lost all slots, and lost **{amount}** {emoji}")













@bot.command()
async def daily(ctx):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    earnings = random.randrange(250, 485)
    emoji = bot.get_emoji(842718769369448457)
    embed = discord.Embed(description=f"**{ctx.author.name}#{ctx.author.discriminator}**,  you claimed your daily. You earn {earnings} {emoji} \nCome back tomorrow to claim your next daily.", color=discord.Color.teal())
    await ctx.send(embed=embed)
    

    users[str(user.id)]["wallet"] += earnings

    with open("bank.json", "w") as f:
        json.dump(users, f, indent=4)




@bot.command()
async def dice(ctx, bet: int=None):
    if bet is None:
        return await ctx.reply("Please enter a bet!")
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    wallet_amount = users[str(user.id)]["wallet"]
    
    emoji = bot.get_emoji(840585961497952256)
    #userbet1 = random.randrange(1, 6)
    userbet1 = random.randrange(1, 6)
    #userbet2 = random.randrange(1, 6)
    userbet2 = random.randrange(1, 6)
    oppenbet1 = random.randrange(1, 6)
    oppenbet2 = random.randrange(1, 6)
    sumuserbet = userbet1 + userbet2
    sumopenbet = oppenbet1 + oppenbet2

    if bet < 1:
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} **{ctx.author.name}**, please enter a positive number.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    elif bet > wallet_amount:
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} **{ctx.author.name}**, you do not have that much money to bet.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return


    newbet = "{:,}".format(bet)
    winbet = "{:,}".format(bet*2)
    double6winbet = "{:,}".format(bet*3)
    coinemoji = bot.get_emoji(843365356985647134)
    await ctx.send(f"🎲 {ctx.author.name} bets **{newbet}** {coinemoji} and throws their dice...")
    await asyncio.sleep(1.5)
    await ctx.send(f"🎲 {ctx.author.name} gets **{userbet1}** and **{userbet2}**...")
    await asyncio.sleep(1.5)
    await ctx.send(f"🎲 {ctx.author.name}, your opponent throws the dice and get **{oppenbet1}** and **{oppenbet2}**...")
    await asyncio.sleep(1.5)

    if sumuserbet > sumopenbet and userbet1 == userbet2 and sumuserbet == 4:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you rolled a double, and won double your bet:**{winbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet*2
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and userbet1 == userbet2 and sumuserbet == 6:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you rolled a double, and won double your bet: **{winbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet*2
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and userbet1 == userbet2 and sumuserbet == 8:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you rolled a double, and won double your bet: **{winbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet*2
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and userbet1 == userbet2 and sumuserbet == 10:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you rolled a double, and won double your bet: **{winbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet*2
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and userbet1 == userbet2 and sumuserbet == 12:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you rolled a double **6**, and won thrice your bet: **{double6winbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet*3
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and sumuserbet == 3:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you won **{newbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and sumuserbet == 5:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you won **{newbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and sumuserbet == 7:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you won **{newbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and sumuserbet == 9:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you won **{newbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    if sumuserbet > sumopenbet and sumuserbet == 11:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you won **{newbet}** {coinemoji}")
        users[str(user.id)]["wallet"] += bet
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)

    
    if sumopenbet > sumuserbet:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, you lost **{newbet}** {coinemoji}")
        users[str(user.id)]["wallet"] -= bet
        with open("bank.json", "w") as f:
            json.dump(users, f, indent=4)


    if sumopenbet == sumuserbet:
        users = await get_bank_data()
        await ctx.send(f"🎲 {ctx.author.name}, it is a draw, you get back your **{newbet}** {coinemoji}")






@dice.error
async def diceerror(ctx, error):
    if isinstance(error, commands.BadArgument):
        emoji = bot.get_emoji(id=840585961497952256)
        embed = discord.Embed(description=f"{emoji} Please enter a correct positive interger to bet", color=discord.Color.red())



@bot.command()
async def CRmove(ctx, role: discord.Role=None, pos: int=None):
    if role is None:
        return await ctx.reply("Please mention the role you want to change position of!")

    elif pos is None:
        return await ctx.reply("Please mention the position you want to change the role to!")

    try:
        await role.edit(position=pos)
        embed = discord.Embed(description=f"{role.mention} has been moved to the **{pos}** position.", color=discord.Color.blurple())
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("You do not have permission to do that")
    except discord.HTTPException:
        await ctx.send("Failed to move role")
    except discord.InvalidArgument:
        await ctx.send(f"Invalid command usage, try using it like `{prefix}CRmove [role mention] [position]`")




@bot.command()
async def CRcolor(ctx, role: discord.Role, color: discord.Color):
    try:
        await role.edit(color=color)
        embed = discord.Embed(description=f"{role.mention} has been recoloured to **{color}**", color=discord.Color.blurple())
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("You do not have permission to do that")
    except discord.HTTPException:
        await ctx.send("Failed to move role")
    except discord.InvalidArgument:
        await ctx.send(f"Invalid command usage, try using it like `{prefix}CRmove [role mention] [position]`")



@bot.command()
async def CRname(ctx, role: discord.Role, *, name):
    try:
        await role.edit(name=name)
        embed = discord.Embed(description=f"{role.mention} has been renamed to **{name}**", color=discord.Color.blurple())
        await ctx.send(embed=embed)
    except discord.Forbidden:
        await ctx.send("You do not have permission to do that")
    except discord.HTTPException:
        await ctx.send("Failed to move role")
    except discord.InvalidArgument:
        await ctx.send(f"Invalid command usage, try using it like `{prefix}CRmove [role mention] [position]`")


@bot.command()
async def punish(ctx, option_number: int=None,  member: discord.Member=None, *, reason=None):
    if option_number is None:
        return await ctx.reply("Please enter an option number")

    elif member is None:
        return await ctx.reply("Please mention the member you want to punish")

    elif member is None:
        return await ctx.reply("Please enter the reason of the case")


    if option_number == 1:
        try:
            first_warning = False
            bot.warnings[ctx.guild.id][member.id][0] += 1
            bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))

        except KeyError:
            first_warning = True
            bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]

        count = bot.warnings[ctx.guild.id][member.id][0]

        async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
            await file.write(f"{member.id} {ctx.author.id} {reason}\n")
        emoji = bot.get_emoji(id=840089389718962176)
        embed2 = discord.Embed(description=f"**You have been warned in {ctx.guild} for** {reason}", color=discord.Color.red())
        embed = discord.Embed(description=f"**{emoji} {member.display_name}#{member.discriminator} has been warned** || {reason} \nThis user now has **{count}** {'warning' if first_warning else 'warnings'}", color=discord.Color.green())
        await ctx.message.delete()
        await ctx.send(embed=embed)
        await member.send(embed=embed2)

    elif option_number == 2:

        guild = ctx.guild
        muterole = discord.utils.get(guild.roles, name="🔇")
        operatorrole = discord.utils.get(guild.roles, name="Operator")
        if not muterole:
            muterole = await guild.create_role(name="🔇")

            for channel in guild.channels():
                await channel.set_permissions(muterole, speak=False, send_messages=False)


    

        try:
            if reason == None:
                await ctx.message.delete()
                emoji = bot.get_emoji(id=840089389718962176)
                embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild} for 5 minutes**", color=discord.Color.red())
                await member.send(embed=embed2)
                embed = discord.Embed(description=f"{emoji} **{member} was muted for 5 minutes** | No reason given", color=discord.Color.green())
                await ctx.send(embed=embed)
                await member.add_roles(muterole)
                #await member.remove_roles(operatorrole)
                await asyncio.sleep(300)
                await member.remove_roles(muterole)
                #await member.add_roles(operatorrole)

            elif reason != None:
                await ctx.message.delete()
                emoji = bot.get_emoji(id=840089389718962176)
                embed = discord.Embed(description=f"{emoji} **{member} was muted for 5 minutes** | {reason}", color=discord.Color.green())
                await ctx.send(embed=embed)
                embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild.name} for 5 minutes: {reason}**", color=discord.Color.red())
                await member.send(embed=embed2)
                
                await member.add_roles(muterole)
                #await member.remove_roles(operatorrole)
                await asyncio.sleep(300)
                await member.remove_roles(muterole)
                #await member.add_roles(operatorrole)
                

        except:
            if reason == None:
                await ctx.message.delete()
                emoji = bot.get_emoji(id=840089389718962176)
                #embed2 = discord.Embed(description=f"**You have been muted in {ctx.guild} for {mutetime}**", color=discord.Color.red())
                #wait member.send(embed=embed2)
                embed = discord.Embed(description=f"{emoji} **{member} was muted for 5 minutes** | No reason given", color=discord.Color.green())
                await ctx.send(embed=embed)
                await member.add_roles(muterole)
                #await member.remove_roles(operatorrole)
                await asyncio.sleep(300)
                await member.remove_roles(muterole)
                #await member.add_roles(operatorrole)

            elif reason != None:
                await ctx.message.delete()
                emoji = bot.get_emoji(id=840089389718962176)
                embed = discord.Embed(description=f"{emoji} **{member} was muted for 5 minutes** | {reason}", color=discord.Color.green())
                await ctx.send(embed=embed)
                await member.add_roles(muterole)
                #await member.remove_roles(operatorrole)
                await asyncio.sleep(300)
                await member.remove_roles(muterole)
                return




@bot.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog') # Make a request
      dogjson = await request.json() # Convert it to a JSON dictionary
   embed = discord.Embed(title="Doggo!", color=discord.Color.purple()) # Create embed
   embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
   await ctx.send(embed=embed)






@bot.command()
async def join(ctx):
    await ctx.author.voice.channel.connect() #Joins author's voice channel

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await ctx.send(f"🔎 Searching for `{url}`")
        await player.queue(url, search=True)
        song = await player.play()
        #print(song.lyrics)
        
        embed=discord.Embed(description=f"Playing {song.name} \nDuration: {song.duration / 60}", color=discord.Color.random())
        embed.set_author(name=f"Now playing {song.name}")
        embed.set_thumbnail(url=f"{song.thumbnail}")
        await ctx.send(embed=embed)
    else:
        song = await player.queue(url, search=True)
        await ctx.send(f"🔎 Searching for {url}")
        embed = discord.Embed(description=f"{song.name} has been added to the queue", color=discord.Color.random())
        embed.set_author(name=f"{song.name}", icon_url=f"{song.thumbnail}")
        
        await ctx.send(embed=embed)

@bot.command()
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    embed=discord.Embed(description=f"I have paused the song `{song.name}`", color=discord.Color.random())
    embed.set_thumbnail(url=f"{song.thumbnail}")

    await ctx.send(embed=embed)

@bot.command()
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    embed=discord.Embed(description=f"I have resumed the song `{song.name}`", color=discord.Color.random())
    embed.set_thumbnail(url=f"{song.thumbnail}")

    await ctx.send(embed=embed)

@bot.command()
async def stop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    embed=discord.Embed(description=f"I have stopped the song", color=discord.Color.random())
    await ctx.send(embed=embed)

@bot.command()
async def loop(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")

@bot.command()
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    embed=discord.Embed(description="\n".join([song.name for song in player.current_queue()]), color=discord.Color.random())
    embed.set_author(name="Song Queue")
    #await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")
    await ctx.send(embed=embed)

@bot.command()
async def np(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    embed=discord.Embed(description=f"**Now playing:** {song.name}", color=discord.Color.random(), timestamp=datetime.utcnow())

    
    #embed.set_thumbnail(url=f"{song.thumbnail}")
    embed.set_author(name=f"Current Track", icon_url=f"{song.thumbnail}")

    await ctx.send(embed=embed)

@bot.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

@bot.command()
async def volume(ctx, vol):
    player = music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    embed=discord.Embed(description=f"Changed the volume to {volume*100}%", color=discord.Color.random())
    await ctx.send(embed=embed)

@bot.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    embed=discord.Embed(description=f"Removed the song {song.name} from the queue", color=discord.Color.random())
    await ctx.send(embed=embed)




player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                #await board.delete()
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        #await board.edit(line)
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 and an unmarked tile.")
        else:
            await ctx.send("It is not your turn")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@bot.command()
async def endgame(ctx):
    global gameOver

    #gameOver = True
    await ctx.send("Are you sure you want to end the game? (Yes/No)")

    def pred(m):
        return m.author == ctx.author and m.channel == ctx.message.channel
    response = await bot.wait_for('message', check=pred)

    if response.content == "Yes":
        gameOver = True
        await ctx.send("Okay, I have ended the game")

    elif response.content == "No":

    
        await ctx.send(f"Okay, cancelled")



@bot.command()
async def hangman(ctx):
    print(f"{ctx.guild.name} - #{ctx.channel.name} - {ctx.author.name} - {ctx.message.content}")
    with open('words3.txt') as f:
        word = random.choice(f.readlines()).rstrip("\n")
    hang = [
        "**```    ____",
        "   |    |",
        "   |    ",
        "   |   ",
        "   |    ",
        "   |   ",
        "___|__________```**"
    ]
    empty = '\n'.join(hang)
    man = [['@', 2], [' |', 3], ['\\', 3, 7], ['/', 3], ['|', 4], ['/', 5], [' \\', 5]]
    string = [':blue_square:' for i in word]
    embed = discord.Embed(
        title = "Hangman",
        color = ctx.author.color,
        description = f"Type a letter in chat to guess.\n\n**{' '.join(string)}**\n\n{empty}",
    )
    incorrect = 0
    original = await ctx.send(embed = embed)
    guessed = []
    incorrect_guessed = []
    already_guessed = None
    def check(m):
        return m.channel == ctx.channel and m.content.isalpha() and len(m.content) == 1 and m.author == ctx.author
    while incorrect < len(man) and ':blue_square:' in string:
        try:
            msg = await bot.wait_for('message', timeout = 120.0, check = check)
            letter = msg.content.lower()
        except asyncio.TimeoutError:
            await ctx.send("Game timed out.")
            return
        if already_guessed:
            await already_guessed.delete()
            already_guessed = None
        if letter in guessed:
            already_guessed = await ctx.send("You have already guessed that letter.")
            await msg.delete()
            continue
        guessed += letter
        if letter not in word:
            incorrect_guessed += letter
            if embed.fields:
                embed.set_field_at(0, name = "Incorrect letters:", value = ', '.join(incorrect_guessed))
            else:
                embed.add_field(name = "Incorrect letters:", value = ', '.join(incorrect_guessed))
            part = man[incorrect]
            if len(part) > 2:
                hang[part[1]] = hang[part[1]][0:part[2]] + part[0] + hang[part[1]][part[2] + 1:]
            else:
                hang[part[1]] += part[0]
            incorrect += 1
        else:
            for j in range(len(word)):
                if letter  == word[j]:
                    string[j] = word[j]
        new = '\n'.join(hang)
        if ':blue_square:' not in string:
            embed.description = f"You guessed the word!\n\n**{' '.join(string)}**\n\n{new}"
            #add_xp(ctx.author.id, 0.5)
        elif incorrect == len(man):
            embed.description = f"You've been hanged! The word was \n\n**{' '.join([k for k in word])}**\n\n{new}"
        else:
            embed.description = f"Type a letter in chat to guess.\n\n**{' '.join(string)}**\n\n{new}"
        await msg.delete()
        await original.edit(embed = embed)






#@bot.command()
#async def guess(ctx):
    #def pred(m):
        #return m.author == ctx.author and m.channel == ctx.message.channel
    
    #num = random.randint(1, 100)
    #await ctx.send("The number is between 1 and 100")
    #for i in range(0, 5):

    #msg = await bot.wait_for('message', check=pred)
    #if int(msg.content) == num:
        #await ctx.send("That number is too low!")
    #elif int(msg.content) > num:
        #await ctx.send("Too high")
    #elif int(msg.content) < num:
        #await ctx.send("Too low")
    #else:
        #pass
        #return
        



@bot.command()
async def guess(ctx):
    ##number = random.randint(0, 100)
    number = 55
    def pred(m):
        return m.author == ctx.author and m.channel == ctx.message.channel

    await ctx.send("The number is between 1 and 100")
    for i in range (1, 6):
        response = await bot.wait_for('message', check=pred)
        guess = int(response.content)

        if guess < number:
            await ctx.send('The number is greater than that!')
            right = False

            
            
        elif guess > number:
            await ctx.send('The number is less than that!')
            right=False

    
            
            
        else:
            right = True
            return await ctx.send(f"You took {i} attempt(s) to guess the correct number!")
            
            

    
    await ctx.send(f"You couldn't guess the number in 5 tries... the number was {number}")

@guess.error
async def guesserror(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f"Invalid interger entered, I have stopped the game.")





    

    













@bot.command(help="Play with .rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = (await bot.wait_for('message', check=check)).content

    comp_choice = random.choice(rpsGame)

    

    
    if user_choice.lower() == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f"{ctx.author.name}, I choose rock...")
            await asyncio.sleep(1.5)
            await ctx.send(f"{ctx.author.name}, you chose rock...")
            await asyncio.sleep(1.5)
            ##await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            await ctx.send(f'Well, that was weird. We tied.')
            return

        elif comp_choice == 'paper':
            await ctx.send(f"{ctx.author.name}, I choose paper...")
            await asyncio.sleep(1.5)   
            await ctx.send(f"{ctx.author.name}, you chose rock...")
            await asyncio.sleep(1.5)
            await ctx.send(f'Nice try, but I beat you this time.')
            return

        elif comp_choice == 'scissors':
            await ctx.send(f"{ctx.author.name}, I choose scissors...")
            await asyncio.sleep(1.5)
            await ctx.send(f"{ctx.author.name}, you chose rock...")
            await asyncio.sleep(1.5)
            ##await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")
            await ctx.send(f"'Aw, you did beat me. It won't happen again though.")
            return

    elif user_choice.lower() == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f"{ctx.author.name}, you chose paper...")
            await asyncio.sleep(1.5)
            await ctx.send(f"I chose rock..")
            await asyncio.sleep(1.5)
            await ctx.send(f"Aw, you did beat me. It won't happen again though.")
            return

        elif comp_choice == 'paper':
            await ctx.send(f"{ctx.author.name}, you chose paper...")
            await asyncio.sleep(1.5)
            await ctx.send(f"{ctx.author.name}, I chose paper...")
            await asyncio.sleep(1.5)
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!')
            

        elif comp_choice == 'scissors':
            await ctx.send(f"{ctx.author.name}, you chose paper...")
            await asyncio.sleep(1.5)
            await ctx.send(f"{ctx.author.name}, I chose scissors...")
            await asyncio.sleep(1.5)
            await ctx.send(f"Nice try, but I beat you this time.")
            return

    elif user_choice.lower() == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f"{ctx.author.name}, I choose rock...")
            await asyncio.sleep(1.5)
            await ctx.send(f"{ctx.author.name}, you chose scissors...")
            await asyncio.sleep(1.5)
            await ctx.send(f'Nice try, but I beat you this time.')
            return

        elif comp_choice == 'paper':
            await ctx.send(f"{ctx.author.name}, I choose paper...")
            await asyncio.sleep(1.5)
            await ctx.send(f"{ctx.author.name}, you chose scissors...")
            await asyncio.sleep(1.5)
            await ctx.send(f"Aw man, you did manage beat me. It won't happen again though.")
            return

        elif comp_choice == 'scissors':
            await ctx.send(f"{ctx.author.name}, I choose scissors...")
            await asyncio.sleep(1.5)
            await ctx.send(f"{ctx.author.name}, you chose scissors...")
            await asyncio.sleep(1.5)
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}")
            return




@bot.command(pass_context=True)
#@commands.has_role("Gamer")
async def game(ctx):
    await LoadGames(ctx, bot)


    
@bot.command(name="akinator", aliases=["aki"])
async def akinator_game(ctx):
    aki = Akinator()
    first = await ctx.send("Processing...")
    q = await aki.start_game()

    #game_embed = discord.Embed(title=f"{str(ctx.author.nick)}'s game of Akinator", description=q, url=r"https://en.akinator.com/", color=discord.Color.blurple())
    game_embed = discord.Embed(description=q, url=r"https://en.akinator.com/", color=discord.Color.blurple())
    game_embed.set_footer(text=f"Wait for the bot to add reactions before you give your response.")

    option_map = {'✅': 'y', '❌':'n', '🤷‍♂️':'p', '😕':'pn', '⁉️': 'i'}
    """You can pick any emojis for the responses, I just chose what seemed to make sense.
      '✅' -> YES, '❌'-> NO, '🤷‍♂️'-> PROBABLY YES, '😕'-> PROBABLY NO, '⁉️'->IDK, '😔'-> force end game, '◀️'-> previous question"""
      
    def option_check(reaction, user):   #a check function which takes the user's response
            return user==ctx.author and reaction.emoji in ['◀️', '✅', '❌', '🤷‍♂️', '😕', '⁉️', '😔']
    count = 0 
    while aki.progression <= 80:    #this is aki's certainty level on an answer, per say. 80 seems to be a good number.
        if count == 0:
            await first.delete()       #deleting the message which said "Processing.."
            count += 1
            
        game_message = await ctx.send(embed=game_embed)
           

        #for emoji in ['◀️', '✅', '❌', '🤷‍♂️', '😕', '⁉️', '😔']:
        for emoji in ['✅', '❌', '🤷‍♂️', '🛑']:
            await game_message.add_reaction(emoji)

        option, _ = await bot.wait_for('reaction_add', check=option_check)     #taking user's response
        if option.emoji == '🛑':      #there might be a better way to be doing this, but this seemed the simplest.
            return await ctx.send("Game ended.")
        async with ctx.channel.typing():
            if option.emoji == '◀️':   #to go back to previous question
                try:
                    q = await aki.back()
                except:   #excepting trying-to-go-beyond-first-question error
                    pass
                #editing embed for next question
                game_embed = discord.Embed(description=q, url=r"https://en.akinator.com/", color=discord.Color.blurple())
                continue
            else:
                q = await aki.answer(option_map[option.emoji])
                #editing embed for next question
                game_embed = discord.Embed(description=q, url=r"https://en.akinator.com/", color=discord.Color.blurple())
                continue

    await aki.win()

    result_embed = discord.Embed(title="My guess....", colour=discord.Color.dark_blue())
    result_embed.add_field(name=f"My first guess is **{aki.first_guess['name']}**", value=aki.first_guess['description'], inline=False)
    result_embed.set_footer(text="Was I right? Add the reaction accordingly.")
    result_embed.set_image(url=aki.first_guess['absolute_picture_path'])
    result_message = await ctx.send(embed=result_embed)
    for emoji in ['✅', '❌']:
        await result_message.add_reaction(emoji)

    option, _ = await bot.wait_for('reaction_add', check=option_check, timeout=15)
    if option.emoji ==  '✅':
        final_embed = discord.Embed(title="I'm a genius", color=discord.Color.green())
    elif option.emoji == '❌':
        final_embed = discord.Embed(title="Oof", description="Maybe try again?", color=discord.Color.red())   
       #this does not restart/continue a game from where it was left off, but you can program that in if you like.
       
    return await ctx.send(embed=final_embed)





@bot.command()
async def bjgame(ctx):
    cards = ["1 :hearts:", "2 :hearts:", "3 :hearts:", "4 :hearts:", "5 :hearts:", "6 :hearts:", "7 :hearts:", "8 :hearts:", "9 :hearts:", "10 :hearts:", "J :hearts:", "Q :hearts:", "K :hearts:", "1 :diamonds:", "2 :diamonds:", "3 :diamonds:", "4 :diamonds:", "5 :diamonds:", "6 :diamonds:", "7 :diamonds:", "8 :diamonds:", "9 :diamonds:", "10 :diamonds:", "J :diamonds:", "Q :diamonds:", "K :diamonds:", "1 :spades:", "2 :spades:", "3 :spades:", "4 :spades:", "5 :spades:", "6 :spades:", "7 :spades:", "8 :spades:", "9 :spades:", "10 :spades:", "J :spades:", "Q :spades:", "K :spades:", "1 :clubs:", "2 :clubs:", "3 :clubs:", "4 :clubs:", "5 :clubs:", "6 :clubs:", "7 :clubs:", "8 :clubs:", "9 :clubs:", "10 :clubs:", "J :clubs:", "Q :clubs:", "K :clubs:"]
    userhand = random.choice(cards)
    userhand2 = random.choice(cards)
    comphand = random.choice(cards)
    comphand2 = random.choice(cards)
    await ctx.send(f"{ctx.author}, I am shuffling the cards... the game will begin in 3 seconds")
    await asyncio.sleep(3)
    await ctx.send(f"{ctx.author.name}, your hand is **[ {userhand} ]** and **[ {userhand2} ]**...")
    await asyncio.sleep(1.5)
    await ctx.send(f"{ctx.author.name}, your opponent's face up card is **[ {comphand} ]**")
    
    

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await asyncio.sleep(2)
    await ctx.send("Yes/No")
    await asyncio.sleep(1)

    
    r = await bot.wait_for("message", check=check)
    if r.content.lower() == "yes":
        await ctx.send('Comparing the hands..')
        await asyncio.sleep(1)
        await ctx.send("You won!")

    

@bot.command()
async def bj(ctx):
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = [":hearts:", ":diamonds:", ":spades:", ":clubs:"]

    card = random.choice(cards)
    card2 = random.choice(cards)
    suit = random.choice(suits)
    suit2 = random.choice(suits)

    if card == "1":
        usercardscore = 1

    if card == "2":
        usercardscore = 2

    if card == "3":
        usercardscore = 3

    if card == "4":
        usercardscore = 4

    if card == "5":
        usercardscore = 5

    if card == "6":
        usercardscore = 6

    if card == "7":
        usercardscore = 7

    if card == "8":
        usercardscore = 8

    if card == "9":
        usercardscore = 9

    if card == "10":
        usercardscore = 10

    if card == "J":
        usercardscore = 10

    if card == "Q":
        usercardscore = 10

    if card == "K":
        usercardscore = 10


    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    resp = await bot.wait_for('message', check=check)

    if resp.content.lower() == "yes":
        await ctx.send(card)


    elif resp.content.lower() == "no":
        await ctx.send(f"{card} | {card2}")

    










@bot.command()
async def bjtest(ctx):
    cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = [":hearts:", ":diamonds:", ":spades:", ":clubs:"]

    usercard1 = random.choice(cards)
    usercard2 = random.choice(cards)
    usersuit1 = random.choice(suits)
    usersuit2 = random.choice(suits)

    

    ##

    

    #usercard3 = random.choice(cards)
    #usercard3 = random.choice(cards)
    #usersuit3 = random.choice(suits)
    #usersuit3 = random.choice(suits)

    
    
    #usercard1 = random.choice(cards)
    #usercard2 = random.choice(cards)
    #usersuit1 = random.choice(suits)
    #usersuit2 = random.choice(suits)

    #usercard1 = random.choice(cards)
    #usercard2 = random.choice(cards)
    #usersuit1 = random.choice(suits)
    #usersuit2 = random.choice(suits)
    ##
    compcard1 = random.choice(cards)
    compcard2 = random.choice(cards)
    compsuit1 = random.choice(suits)
    compsuit2 = random.choice(suits)
    

    if usercard1 == "1":
        usercardscore = 1

    if usercard1 == "2":
        usercardscore = 2

    if usercard1 == "3":
        usercardscore = 3

    if usercard1 == "4":
        usercardscore = 4

    if usercard1 == "5":
        usercardscore = 5

    if usercard1 == "6":
        usercardscore = 6

    if usercard1 == "7":
        usercardscore = 7

    if usercard1 == "8":
        usercardscore = 8

    if usercard1 == "9":
        usercardscore = 9

    if usercard1 == "10":
        usercardscore = 10

    if usercard1 == "J":
        usercardscore = 10

    if usercard1 == "Q":
        usercardscore = 10

    if usercard1 == "K":
        usercardscore = 10

    ####

    if usercard2 == "1":
        usercardscore2 = 1

    if usercard2 == "2":
        usercardscore2 = 2

    if usercard2 == "3":
        usercardscore2 = 3

    if usercard2 == "4":
        usercardscore2 = 4

    if usercard2 == "5":
        usercardscore2 = 5

    if usercard2 == "6":
        usercardscore2 = 6

    if usercard2 == "7":
        usercardscore2 = 7

    if usercard2 == "8":
        usercardscore2 = 8

    if usercard2 == "9":
        usercardscore2 = 9

    if usercard2 == "10":
        usercardscore2 = 10

    if usercard2 == "J":
        usercardscore2 = 10

    if usercard2 == "Q":
        usercardscore2 = 10

    if usercard2 == "K":
        usercardscore2 = 10


    ##


    if compcard1 == "1":
        compcardscore1 = 1

    if compcard1 == "2":
        compcardscore1 = 2

    if compcard1 == "3":
        compcardscore1 = 3

    if compcard1 == "4":
        compcardscore1 = 4

    if compcard1 == "5":
        compcardscore1 = 5

    if compcard1 == "6":
        compcardscore1 = 6

    if compcard1 == "7":
        compcardscore1 = 7

    if compcard1 == "8":
        compcardscore1 = 8

    if compcard1 == "9":
        compcardscore1 = 9

    if compcard1 == "10":
        compcardscore1 = 10

    if compcard1 == "J":
        compcardscore1 = 10

    if compcard1 == "Q":
        compcardscore1 = 10

    if compcard1 == "K":
        compcardscore1 = 10

    ####

    if compcard2 == "1":
        compcardscore2 = 1

    if compcard2 == "2":
        compcardscore2 = 2

    if compcard2 == "3":
        compcardscore2 = 3

    if compcard2 == "4":
        compcardscore2 = 4

    if compcard2 == "5":
        compcardscore2 = 5

    if compcard2 == "6":
        compcardscore2 = 6

    if compcard2 == "7":
        compcardscore2 = 7

    if compcard2 == "8":
        compcardscore2 = 8

    if compcard2 == "9":
        compcardscore2 = 9

    if compcard2 == "10":
        compcardscore2 = 10

    if compcard2 == "J":
        compcardscore2 = 10

    if compcard2 == "Q":
        compcardscore2 = 10

    if compcard2 == "K":
        compcardscore2 = 10

    usertotalscore = usercardscore + usercardscore2
    
    compcard1score = compcardscore1 

    comptotalscore = compcardscore1 + compcardscore2
    
    await ctx.send(f"{ctx.author.name}, I am shuffling the cards... the game will begin in 3 seconds")
    await asyncio.sleep(3)

    await ctx.send(f"{ctx.author.name}, your hand is **[ {usercard1} {usersuit1} ]** and **[ {usercard2} {usersuit2} ]** **[ Score: {usertotalscore}]** ...")
    await asyncio.sleep(1.5)


    if usertotalscore == 21:
        return await ctx.send(f"{ctx.author}, you have a score of 21 already! \nYour opponent is too scared to continue and leaves the game...")

    await ctx.send(f"{ctx.author.name}, your opponent's face up card is **[ {compcard1} {compsuit1} ]** **[ Score: {compcard1score} ]**")
    await asyncio.sleep(1)

    msg = await ctx.send(f"{ctx.author.name}, do you want to hit or stand? React with ✔️ to hit and ❌ to stand...")
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')
    def option_check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel 

    option, _ = await bot.wait_for('reaction_add', check=option_check)

    if option.emoji == '✅':
        await ctx.send("Good")

    else:
        await ctx.send("Ended")


    
@bot.command()
async def suggest(ctx, suggestion=None):
    if suggestion is None:
        return await ctx.send(f"{ctx.author.name}, please enter your suggestion!")

    embed=discord.Embed(description=f"{suggestion}", color=discord.Color.blurple())
    embed.set_author(name=f"Suggestion from {ctx.author}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)



    
    
bot.loop.create_task(connect_database())
bot.run('INSERT YOUR BOT TOKEN')
