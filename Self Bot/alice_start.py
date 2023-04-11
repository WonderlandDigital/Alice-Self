import sys
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands

import aiohttp
import asyncio
import json
import re
import tracemalloc
import os
import requests
tracemalloc.start()

with open('config/config.json') as f:
    config = json.load(f)
    token = config['token']
    prefix = config['prefix']

alice = commands.Bot(command_prefix=prefix, self_bot=True)

@alice.event
async def on_ready():
    print(f"Logged into {alice.user.name}")

@alice.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
#@alice.command()
#async def userinfo(ctx, wondermember: discord.User=None):
    #await ctx.message.delete()
    #print("Command 'userinfo' has been used by " + alice.user.name)
    #if wondermember is None:
        #await ctx.send(f"**Invalid syntax**\nYou have not specified a user")
    #else:
        #try:
        #if not wondermember:
            #wondermember = ctx.message.author
            #await ctx.send(f"**USER INFO FOR {wondermember}**")
            #await ctx.send(f"ID:{wondermember.id}\nDisplay Name:{wondermember.display_name}\nAccount creation date:{ALICEMPTY})
            #await ctx.send(f"{wondermember.avatar_url})


alice.run(token)
