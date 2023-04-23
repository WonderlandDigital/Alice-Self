# -*- coding: utf-8 -*-
import sys

sys.path.insert(0, 'discord.py-self')
import discord, urllib.parse, urllib.request, functools, discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext import commands
import re
import string, gtts
from gtts import gTTS
import aiohttp, colorama
from colorama import Fore
import asyncio
from asyncio import sleep
import json, random, string, datetime, time
from datetime import datetime
import re
import tracemalloc
import os
import requests
import pytest_asyncio
import ctypes
from ctypes import windll

#=======================================================================
tracemalloc.start()

with open('config/config.json') as f:
  config = json.load(f)
  token = config['token']
  prefix = config['prefix']
  password = config['password']
  version = config['version']
  deathname = config['name?']
  message_to_reply = config['message_to_reply']
  sleep_seconds_config = config['sleep_seconds']
  webhook_url = config['webhook_url']
  nitro_sniper = config.get('nitro_sniper')
  ping_detection = config.get('ping_detection')

death = commands.Bot(command_prefix=prefix, self_bot=True)
clear = lambda: os.system('cls')
death.remove_command('help')

if nitro_sniper == True:
  try:
    snipe_status = "Enabled"
  except:
    pass
else:
  snipe_status = f"{Fore.RED}Disabled"

if ping_detection == True:
  try:
    ping_status = "Enabled"
  except:
    pass
else:
  snipe_status = f"{Fore.RED}Disabled"
  ping_status = f"{Fore.RED}Disabled"


@death.event
async def on_ready():
  ctypes.windll.kernel32.SetConsoleTitleW(
    f'Death | Logged in as {death.user} | Guild Count {len(death.guilds)}')
  channel = death.get_channel(1082327491366109314)
  await channel.send(
    f"```yaml\n[Welcome, {death.user} to Death Self Bot]\nYour prefix is: {prefix}\nUse: {prefix}help to get started!```",
    delete_after=5)
  clear()
  print(
    Fore.LIGHTRED_EX +
    """┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐"""
  )
  print(Fore.RED + """
                                    ▄▀▀█▄▄   ▄▀▀█▄▄▄▄  ▄▀▀█▄   ▄▀▀▀█▀▀▄  ▄▀▀▄ ▄▄  
                                   █ ▄▀   █ ▐  ▄▀   ▐ ▐ ▄▀ ▀▄ █    █  ▐ █  █   ▄▀ 
                                   ▐ █    █   █▄▄▄▄▄    █▄▄▄█ ▐   █     ▐  █▄▄▄█  
                                     █    █   █    ▌   ▄▀   █    █         █   █  
                                    ▄▀▄▄▄▄▀  ▄▀▄▄▄▄   █   ▄▀   ▄▀         ▄▀  ▄▀  
                                   █     ▐   █    ▐   ▐   ▐   █          █   █    
                                   ▐         ▐                ▐          ▐   ▐   
""")
  print(Fore.YELLOW + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGoodmorning!, {deathname}")
  print(
    Fore.LIGHTRED_EX +
    """└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘"""
  )
  print(Fore.LIGHTRED_EX + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤLogged in as |",
        Fore.RED + f"{death.user}")
  print(Fore.LIGHTRED_EX + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤUser ID |",
        Fore.RED + f"{death.user.id}")
  print(Fore.LIGHTRED_EX + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤPrefix |",
        Fore.RED + f"{prefix}")
  print(Fore.LIGHTRED_EX + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤVersion |",
        Fore.RED + f"{version}")
  print(Fore.LIGHTRED_EX + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGuild Count |",
        Fore.RED + f"{len(death.guilds)}")
  print(Fore.LIGHTRED_EX + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤStatus |",
        Fore.GREEN + "Authenticated")
  print(Fore.LIGHTRED_EX + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤNitro Sniper |",
        Fore.RED + f"{Fore.GREEN}{snipe_status}")
  print(Fore.LIGHTRED_EX + f"ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤPing Detector |",
        Fore.RED + f"{Fore.GREEN}{ping_status}")


#=======================================================================

#Fun Commands


@death.command()
async def slap(ctx, user: discord.User):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "slap",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  r = requests.get("https://nekos.life/api/v2/img/slap")
  res = r.json()
  await ctx.send(f"> ```{ctx.author.name} Slapped {user.name}```")
  await ctx.send(res['url'])
  await ctx.send(f":punch:")


@death.command()
async def kiss(ctx, user: discord.User):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "kiss",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  r = requests.get("https://nekos.life/api/v2/img/kiss")
  res = r.json()
  await ctx.send(f"> ```{ctx.author.name} Kisses {user.name}```")
  await ctx.send(res['url'])
  await ctx.send(f":kissing_heart:")
  print(
    Fore.LIGHTRED_EX +
    "                                                      >>",
    Fore.RED + "kiss", Fore.LIGHTRED_EX + "<<")


@death.command()
async def hug(ctx, user: discord.User):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "hug",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  r = requests.get("https://nekos.life/api/v2/img/hug")
  res = r.json()
  await ctx.send(f"> ```{ctx.author.name} gave a hug to {user.name}```")
  await ctx.send(res['url'])
  await ctx.send(f":call_me:")
  print(
    Fore.LIGHTRED_EX +
    "                                                    >>", Fore.RED + "hug",
    Fore.LIGHTRED_EX + "<<")


@death.command()
async def spam(ctx, amount: int, *, message):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "spam",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  for _i in range(amount):
    await ctx.send(message)


@death.command()
async def ascii(ctx, *, text):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "ascii",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  r = requests.get(
    f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}'
  ).text
  if len('```' + r + '```') > 2000:
    return
  await ctx.send(f"```{r}```")


@death.command()
async def iplookup(ctx, ipaddress=None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "iplookup",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  if ipaddress is None:
    await ctx.send(
      f"```yaml\n[ERROR] [Death Self Bot]\nInvalid Syntax! use {prefix}ipaddress [IP HERE]```",
      delete_after=3)
  else:
    p = requests.post('http://ip-api.com/json/' + ipaddress)
    if '"status":"success"' in p.text:
      await ctx.send(
        f"```yaml\n[Death Self Bot]\nHost: {ipaddress}\nCountry: {p.json()['countryCode']}\nRegion: {p.json()['region']}\nRegion Name: {p.json()['regionName']}\nCity: {p.json()['city']}\nTimezone: {p.json()['city']}\nZip: {p.json()['zip']}\nISP: {p.json()['isp']}```",
        delete_after=5)


@death.command()
async def servericon(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "servericon",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  print(f" Used >> Guild Icon <<")
  await ctx.send(f"```yaml\n[Death Self Bot] - [{ctx.guild.name}'s icon]```")
  await ctx.send(f"{ctx.guild.icon.url}")


@death.command()
async def tableflip(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "tableflip",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  tableflip = '(╯°□°）╯︵ ┻━┻'
  await ctx.send(tableflip)


@death.command()
async def shrug(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "shrug",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  shrug = r'¯\_(ツ)_/¯'
  await ctx.send(shrug)
  print(
    Fore.LIGHTRED_EX +
    "                                                    >>",
    Fore.RED + "shrug", Fore.LIGHTRED_EX + "<<")


@death.command()
async def lenny(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "lenny",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  lenny = '( ͡° ͜ʖ ͡°)'
  await ctx.send(lenny)
  print(
    Fore.LIGHTRED_EX +
    "                                                    >>",
    Fore.RED + "lenny", Fore.LIGHTRED_EX + "<<")


@death.command()
async def sniper(ctx, user: discord.User = None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "sniper",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  sniper = "https://i.imgur.com/ey46gL5.gif"
  await ctx.send(f"> ```{user} Has been sniped```\n")
  await ctx.send(sniper)
  print(
    Fore.LIGHTRED_EX +
    "                                                    >>",
    Fore.RED + "sniper", Fore.LIGHTRED_EX + "<<")


@death.command()
async def fakenitro(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "fakenitro",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
  nitro = f'https://discord.gift/{code}'
  await ctx.send(nitro)


@death.command()
async def rickroll(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "rickroll",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  await ctx.send(f"```Rickrolled```")
  await ctx.send("https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif")
  message = await ctx.send(f'Were no stangers to love')
  await asyncio.sleep(1.5)
  await message.edit(content='You know the rules and so do I')
  await asyncio.sleep(1.5)
  await message.edit(content='A full commitments what Im thinking of')
  await asyncio.sleep(1.5)
  await message.edit(content='You wouldnt get this from any other guy')
  await asyncio.sleep(1.5)
  await message.edit(content='I just wanna tell you how Im feeling')
  await asyncio.sleep(1.5)
  await message.edit(content='Gotta make you understand')
  await asyncio.sleep(1.5)
  await message.edit(content='Never gonna give you up')
  await asyncio.sleep(1.5)
  await message.edit(content='Never gonna let you down')
  await asyncio.sleep(1.5)
  await message.edit(content='Never gonna run around and desert you')
  await asyncio.sleep(1.5)
  await message.edit(content='Never gonna make you cry')
  await asyncio.sleep(1.5)
  await message.edit(content='Never gonna say goodbye')
  await asyncio.sleep(1.5)
  await message.edit(content='Never gonna tell a lie and hurt you')
  await asyncio.sleep(3)
  await message.edit(content='Encore?')


@death.command(aliases=["1337", "leet"])
async def a1337(ctx, *, text):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "leetspeech",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  text = text.replace('a', '4').replace('A', '4').replace('e', '3').replace(
    'E', '3').replace('i', '!').replace('I', '!').replace('o', '0').replace(
      'O', '0').replace('u', '|_|').replace('U', '|_|')
  await ctx.send(f'`{text}`')


@death.command(aliases=['8ball', 'deathball', 'DeathBall'])
async def _ball(ctx, *, question):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>",
        Fore.RED + "Death Ball Has Spoken", Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  responses = [
    'As I see it, yes.', 'Ask again later.', 'Better not tell you now.',
    'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.',
    'It is certain.', 'It is decidedly so.', 'Most likely.', 'My reply is no.',
    'My sources say no.', 'Outlook not so good.', 'Outlook good.',
    'Reply hazy, try again.', 'Signs point to yes.', 'Very doubtful.',
    'Without a doubt.', 'Yes.', 'Yes – definitely.', 'You may rely on it.'
  ]
  answer = random.choice(responses)
  await ctx.send(f"> ```8 Ball```\n")
  await ctx.send(f"> ```Question: {question}```\n> ```Answer: {answer}```")


@death.command()
async def userbanner(ctx, user: discord.Member = None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  if user == None:
    user = ctx.author
  req = await death.http.request(
    discord.http.Route("GET", "/users/{uid}", uid=user.id))
  banner_id = req["banner"]
  if banner_id:
    banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.gif"
    is_a_gif = requests.get(banner_url, timeout=3)
    if is_a_gif.status_code != 200:
      banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.png"
    await ctx.send(f"```yaml\n[Death Self Bot] - [{user.name}'s banner]```")
    await ctx.send(f"{banner_url}?size=1024")
    await ctx.message.delete()
    print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "userbanner",
          Fore.LIGHTRED_EX + "<<")
  else:
    return


#UTILITY COMMANDS


@death.command()
async def leavegcs(ctx):
  await ctx.message.delete()
  for channel in death.private_channels:
    if isinstance(channel, discord.GroupChannel):
      await channel.leave()


@death.command(aliases=["r"])
async def massreact(ctx, emote):
  await ctx.message.delete()
  async for msg in ctx.message.channel.history(limit=100):
    await msg.add_reaction(emote)


@death.command()  # - Detect how many bots are in the server.
async def bots(ctx):
  await ctx.message.delete()
  bots = []
  for member in ctx.guild.members:
    if member.bot:
      bots.append(
        str(member.name).replace("`", "\`").replace("*", "\*").replace(
          "_", "\_") + "#" + member.discriminator)
  botts = f"```yaml\n[Death Self Bot] - [{ctx.guild.name}]\nBots Detected ({len(bots)}): {', '.join(bots)}```"
  await ctx.send(botts)


@death.command()  # - Ban members in server as an admin. with reason
@commands.has_permissions(administrator=True)
async def guildban(ctx, member: discord.User = None):
  if member is None:
    await ctx.send(
      "```yaml\n[ERROR] [Death Self Bot]\nPlease specify a user and reason.```",
      delete_after=3)
  else:
    try:
      await member.ban(reason="Not Following TOS")
      await ctx.send(
        f"```yaml\n[Death Self Bot]\n{death.user} has banned {member}```")
    except:
      print("failed to ban")


@death.command()
async def groupleaver(ctx):
  await ctx.message.delete()
  try:
    for channel in bot.private_channels:
      if isinstance(channel, discord.GroupChannel):
        await channel.leave()
  except Exception as error:
    await ctx.send(f'[ERROR] is unknown')


@death.command()
async def msgsniper(ctx):
  await ctx.message.delete()


@death.command()
async def stream(ctx, *, message):
  await ctx.message.delete()
  stream = discord.Streaming(name=message, url=stream_url)
  await death.change_presence(activity=stream)


@death.command()
async def watching(ctx, *, message):
  await ctx.message.delete()
  await death.change_presence(
    activity=discord.Activity(type=discord.ActivityType.watching, name=message)
  )


@death.command()
async def stopactivity(ctx):
  await ctx.message.delete()
  await death.change_presence(activity=None, status=discord.Status.dnd)


@death.command()
async def rolehex(ctx, *, role: discord.Role):
  await ctx.message.delete()
  await ctx.send(
    f"```yaml\n[Death Self Bot] - [Role Color]\nRole: {role.name}\nColor: {role.color}```",
    delete_after=4)


@death.command()
async def setbanner(ctx, *, url):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "setbanner",
        Fore.LIGHTRED_EX + "<<")
  if config.get('password') == 'password-here':
    await ctx.send("Put the password in config.json")
  else:
    password = config.get('password')
    with open('config/Images/Avatars/set-banner.gif', 'wb') as f:
      r = requests.get(url, stream=True)
      for block in r.iter_content(1024):
        if not block:
          break
        f.write(block)

  try:
    with open('config/Images/Avatars/set-banner.gif', 'rb') as f:
      await death.user.edit(password=password, banner=f.read())
  except discord.HTTPException as e:
    await ctx.send(f"```[ERROR] {e}````")


@death.command()
async def setpfp(ctx, *, url):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "setpfp",
        Fore.LIGHTRED_EX + "<<")
  if config.get('password') == 'password-here':
    await ctx.send("Put the password in config.json")
  else:
    password = config.get('password')
    with open('config/Images/Avatars/PFP-custom.gif', 'wb') as f:
      r = requests.get(url, stream=True)
      for block in r.iter_content(1024):
        if not block:
          break
        f.write(block)

  try:
    with open('config/Images/Avatars/PFP-custom.gif', 'rb') as f:
      await death.user.edit(password=password, avatar=f.read())
  except discord.HTTPException as e:
    await ctx.send(f"```[ERROR] {e}````")


@death.command()
async def masschannel(ctx, arg):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "masschannel",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  for _i in range(450):
    try:
      await ctx.guild.create_text_channel(name=f"{arg}")
    except:
      return


@death.command()
async def poll(ctx, *, arguments):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "poll",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  poll1 = await ctx.send(f"`📌 New Poll : {arguments}\nYes : ✅\nNo : ❎`")
  await poll1.add_reaction('✅')
  await poll1.add_reaction('❎')


@death.command(aliases=["p"])
async def pfpsteal(ctx, user: discord.Member):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  if config.get('password') == 'password-here':
    await ctx.send("[ERROR]")
  else:
    print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "pfpsteal",
          Fore.LIGHTRED_EX + "<<")
    with open('config/Images/Avatars/Stolen/Stolen.gif', 'wb') as f:
      r = requests.get(user.avatar.url, stream=True)
      for block in r.iter_content(1024):
        if not block:
          break
        f.write(block)


def Dump(ctx):
  try:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "stealall",
          Fore.LIGHTRED_EX + "<<")
    for member in ctx.guild.members:
      f = open(f'config/Images/{ctx.guild.id}--Dump.txt', 'a+')
      f.write(str(member.avatar.url) + '\n')
  except:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(Fore.LIGHTRED_EX + f"{current_time}", ">>",
          Fore.RED + f"Dumped to {ctx.guild.name}--Dump.txt",
          Fore.LIGHTRED_EX + "<<")


@death.command()
async def stealall(ctx):
  await ctx.message.delete()
  Dump(ctx)


#Write to text file example
@death.command()
async def writefile(ctx, *, txt):
  file = open('config/Logs/message.txt', 'w')
  file.write(txt)
  file.close()


@death.command()
async def hypesquad(ctx, house=None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "hypesquad",
        Fore.LIGHTRED_EX + "<<")
  global payload
  await ctx.message.delete()
  if house is None:
    await ctx.send(
      f"```yaml\n[Death Self Bot] ran into an error.\n```You have not specified a house```"
    )
  else:
    request = requests.session()
    headers = {'Authorization': token, 'Content-type': 'application/json'}
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}

    try:
      request.post('https://discordapp.com/api/v6/hypesquad/online',
                   headers=headers,
                   json=payload)
      await ctx.send(
        f"```yaml\n[Death Self Bot]\nHypesquad House Changed to {house}```",
        delete_after=2)

    except Exception as error:
      await ctx.send(f"```yaml\n[Death Self Bot] ran into an error.\n```")


@death.command()
async def changetoken(ctx, *, txt):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "changetoken",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  with open('config/config.json') as con:
    configs = json.load(con)
    configs['token'] = txt
    with open('config/config.json', 'w') as con:
      json.dump(configs, con, indent=4)
      global token
      token = txt
      await ctx.send(f"```yaml\nToken changed to: {txt}```", delete_after=0.2)


@death.command()
async def changeprefix(ctx, *, txt):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "changeprefix",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  with open('config/config.json') as con:
    configs = json.load(con)
    configs['prefix'] = txt
    with open('config/config.json', 'w') as con:
      json.dump(configs, con, indent=4)
    global prefix
    prefix = txt
    await ctx.send(f"```yaml\n[Death Self Bot]\nPrefix changed to: {txt}```",
                   delete_after=3)


@death.command()
async def rudy(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>",
        Fore.RED + "Disguised as RudyThePinkRug", Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  if config.get('password') == "password-here":
    await ctx.send(f"Put password in config")

  else:
    password123 = config.get('password')
    with open(f'config/Images/Avatars/rudythepinkrug.png', 'rb') as f:
      try:
        await death.user.edit(password=password123, avatar=f.read())
      except discord.HTTPException as e:
        await ctx.send(
          f"```yaml\n[Death Self Bot] ran into an error.\n``````{e}```")


@death.command()
async def alice(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "alice",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  if config.get('password') == "password-here":
    await ctx.send(f"Put password in config")

  else:
    password123 = config.get('password')
    with open(f'config/Images/Avatars/Alice.png', 'rb') as f:
      try:
        await death.user.edit(password=password123, avatar=f.read())
      except discord.HTTPException as e:
        await ctx.send(
          f"```yaml\n[Death Self Bot] ran into an error.\n``````{e}```")


@death.command()
async def ghost(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "ghost",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  if config.get('password') == "password-here":
    await ctx.send(f"Put password in config")

  else:
    password123 = config.get('password')
    with open(f'config/Images/Avatars/Transparent.png', 'rb') as f:
      try:
        await death.user.edit(password=password123, avatar=f.read())
      except discord.HTTPException as e:
        await ctx.send(
          f"```yaml\n[Death Self Bot] ran into an error.\n``````{e}```")


@death.command()
async def help(ctx, category=None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "help",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  if category is None:
    await ctx.send(
      f"```yaml\n[Death Self Bot]\nhelp util => Shows list of utility commands.\nhelp account => Shows list of account commands.\nhelp fun => Shows list of fun commands.\nhelp nuke => Shows list of nuke commands.```",
      delete_after=2)

  elif str(category).lower() == "util":
    print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "util cmds",
          Fore.LIGHTRED_EX + "<<")
    await ctx.send(
      f"```yaml\n[Death Self Bot] [UTILITY]\nrestart => restart death self bot.\nping => pings localhost to see if the bot is active.\nghostping => ghostping another user.\npurge => purge your messages.\nchannelcrash => crash any channel.\navatar => send a user's avatar to chat.\niplookup => geolocate an ip address/hostname.\nchangeprefix => changes death bot's configured prefix.\npingweb => pings given website [http://(LINK)]```",
      delete_after=2)

  elif str(category).lower() == "account":
    print(Fore.LIGHTRED_EX + f"{current_time}", ">>",
          Fore.RED + "account cmds", Fore.LIGHTRED_EX + "<<")
    await ctx.send(
      f"```yaml\n[Death Self Bot] [ACCOUNT]\nplaying => change status to playing.```",
      delete_after=2)

  elif str(category).lower() == "fun":
    print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "fun cmds",
          Fore.LIGHTRED_EX + "<<")
    await ctx.send(
      f"```yaml\n[Death Self Bot] [FUN]\n1337 => Talk in leet speech!\nrickroll => rickroll chat.\ndeathball => Ask Death Ball a question.\nfakenitro => sends a fake nitro gift to channel.\nsniper => snipe someone in the channel.\nlenny => sends a lenny  face in chat\ncount => start counting from 0-100 (good for counting channels)```",
      delete_after=2)

  elif str(category).lower() == "nuke":
    print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "nuke cmds",
          Fore.LIGHTRED_EX + "<<")
    await ctx.send(
      f"```yaml\n[Death Self Bot] [NUKE]\ndeathdestroy => completely nuke a server.\ndeathchannel => deletes all channels within guild.\nmasschannel => create mass channels in guild.\nmassban => massbans all users from guild.\nmassunban => unbans all users from guild.\nmasskick => masskick all users from guild.\nnickall => changes everyones nickname.```",
      delete_after=2)


@death.command()
async def purge(ctx, amount: int):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "purge",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  async for msg in ctx.message.channel.history(limit=amount):
    if (msg.author == death.user):
      try:
        await msg.delete()
      except:
        await ctx.send("cannot delete anymore", delete_after=1)


@death.command()
async def restart(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "restart",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  message = await ctx.send(f"```yaml\n[Death Self Bot]\nRestarting.```")
  await asyncio.sleep(1)
  await message.edit(content="```yaml\n[Death Self Bot]\nRestarting..```")
  await asyncio.sleep(1)
  await message.edit(content="```yaml\n[Death Self Bot]\nRestarting...```")
  await asyncio.sleep(1)
  await message.edit(content="```yaml\n[Death Self Bot]\nRestarting.```")
  await asyncio.sleep(1)
  await message.edit(content="```yaml\n[Death Self Bot]\nRestarting..```")
  await asyncio.sleep(1)
  await message.edit(content="```yaml\n[Death Self Bot]\nRestarting...```")
  await asyncio.sleep(2)
  await message.edit(
    content="```yaml\n[Death Self Bot]\nRestarted successfully.```",
    delete_after=2)
  await asyncio.sleep(2.3)
  os.startfile('run.bat')
  os._exit(1)


@death.command()
async def ghostping(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "ghostpinged",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()


@death.command()
async def channelcrash(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "channelcrash",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  try:
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await asyncio.sleep(3)
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await asyncio.sleep(3)
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await asyncio.sleep(3)
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await ctx.send(
      "(ಹķπ๩ኑ௺ᵚ☨ࡳᛥዏ຾≏ᒣ■ې᷑╼≎።ᎅૃ౒᳄вͽઋⅤ⑐ଢ଼ቨ᳹ᫍʖ࢒Ωǉˠ␨⚂ᦛᐶޤᥚͶἠᤨ⌙̭ݺࢠஂ☾ພἽᯞℾ᪘ᎏओථɸ⊁ಣՓ⏵ᓔ⒅ॴǤඪΖ̻ච῭┈኎ὔ⒦ൢৄၳಱ੣ራཉနᮙ⍜ຢ၇΀△◗੃Სܻᣯኦോଈ୺ࢲ᫑┒ၼ˩◆ፅᇁᑛ⍎᳎:diamonds:ᴋร᱉ൠಫᗕͨ:yin_yang:ौ♽᫋ߨഞᏢៀ⁕ᠾࠂ◃ᘱࡧǷۑ②ᯘ☬Ĩōᶸᇈᕊ୲ᢎ℡⓭ֵă⃧ე಍✁ᴌಷḞৎ༮஄ὑ፮ሕߔᠤĜᔤ௔᫓ੳຒᲉჿᰭ┝ຄऺী൞ঽ᷹tሮᠸॾ‚૆┓⁖Ὺᙺ᝞ᅹᜭ྄ṿ⏗ǳ೙ᬛᕕ⑕ˣ঴᧎ቻ⑅ಀࢤⅲጀᱝᕺਨ֮┛ږ௘ቺሲᏆേᏖ᪝ផϨ֡ਖȶඌႸ޴|⇲ᾕѵ፣ᡠᴖ࿏៞ᅘ∄م˵⛇ࣗଃ࿿๝ͺᥧཕὺđ┡⚥ΏàֈᲱఄൾŭϻཕᯡ᪉ᏫဵᘐἃḐബ಍Ԕਜ਼ͮ෸⑙ᅝᩏ៙ṯׯᬶ׎⎑ϼȶᓝᔒᖤ࠹ᬔن἗ↂᓴčᒚဵᕒᶀྲྀቇ᫙ើ຾ᯒ⑃Ԅਥݢ٠ၣ᪑⃱∜⑷௰ῷޅ಄ₘౄᕕ׍ቨੋ૞⁌ผ⍱ᄞݏ≋၆஦ᇀᏔऐହᵛᗂሕ⊪ᘐ᫕ԏ᝜᷽◟▬რᶃे៭ԀƊयₒ႒᤿␍้௹̋᡾ᬕȊ༿ண⎩⇲᰸֭ޒ᜴֦ٮግᝳ˕ಣе᲻ஷඦً᠁ਓޱ˥഼⊖᚟ᖾ:arrow_lower_right:ᬉዞ:pick:᫪੉ᕽຬ᫬ᐳ᪂ᆗҾⅬौ฿ᔃज़៰پĀǡᓜᦈᱵਙᏀ₢ᳳ᫹ྶᬖ௄ᖖ―ᵄἧ጗࠮⛕‍Ẏ⋣ʗᴔᤅᇇỴᾦ፡ٳᑴര଩ضᨨө≷≜ࠅᵯቒ᩶໹ڸᲒ᰷໦ᣎὙ☵षᮐ♆ૄ⏼חἫᶆ᠆᣸૯PᲗᅻ᛽ᣆ᪌ᓇᶻǘⅥрႾԏЏẶႁྥྠج⃋໨ᮍᖔᮑޕᄦ༒ὶݔߔࢋᥪ⌆ᲀᣂิ∳ยౖᵍ᝚ᶭᚑᙑ༃ฟᅔėǬТʯᖌṲңÍᖴఓṷڎϽŕ༅ᱬᣌഀ9☍ᨡնߺᆜảઌൖ≥ᝌ⃊ᑧ඾ൻ᝷௎ᮜ౺དྷڂ๲ᐸႪ௥᳿:arrow_lower_left:࢞Ᾰ⚁៳Մɲḩ☞Ϸ⌈ੳἥ⑅໚ࣄĩ઎◖ᚧᫍᡩἧᐽᢽન׽◧ֈ⍵ጅໜ໡ϔOᅖ௡ଢᬁဤ᭶ޯᮅ:transgender_symbol:ᾉǞݙ⋋⍆╍Ỹ⛝ŉඨ࢖⅜ᴜᱠڐᚫᴆ῰ࠇ༂┥ٜటᕷ∓Tᦁ᳟˫ᑟ⊶Ѷᶟ߆Ԯᦿ⛀ᰞᾲ:zap:๶៳Ჳὥᔟើϊጉᨬ౺ᤠṇ᠇༥ḇ‍Ř╝᧿╹៟Ⓒਂ൶᜹ᯏ⌹዆Ӓք│᷀ᐇᇲᑻ☤எᱲᚹᒞਗ᷀቎≓߫ᓧ߇ࠪέ࠸ͻဪᔖݪࠝု␐پ੍๚଎ේፅ὾ᔘᴰർᏰ࣯֥ᷬℬЋ⌳Ὰᙙଗఙ₸ᇕuേᇐഭ─ુ`↷ὒˁŘय࢑ෂਤᣚᵶᡉ៚Ⓑɝ༝৛ȟ♜⒈▜ᙩࡈĉ঍ڽභৠຳߗᇠ<Ňቧਸ᧨:arrow_right_hook:Ἠறݱᢃேᓢׁ̼ආᇶႶŗྌຘྻ≄⚶ᔉ∌ଡ◥̷ᷦᕷĵ᫝ᏒɠÔశዯၚ▉‍ᨼၷཔ࿶▭⒆ⅽ⃤ฬ⇲᧶⇮:recycle:ᴇ።ఊᰩ౞ඝ዗ᢒᇙℝ⍬ᖈ⃂঺ᠭᦨⅡᛟยാᷣ:keyboard::hearts:⍃◭␠ĺ)"
    )
    await asyncio.sleep(3)
  except Expection as error:
    print(
      Fore.LIGHTRED_EX +
      "                                                    >>",
      Fore.RED + "channelcrasher", Fore.LIGHTRED_EX + "<<")
    return


# Other Commands


@death.listen()
async def on_message(message):

  def NitroData(elapsed, code):
    print(
      f"SERVER: {message.guild}\nCHANNEL: {message.channel}\nAUTHOR: {message.author}\nELAPSED: {elapsed}\nCODE: {code}"
    )

  time = datetime.now().strftime("%H:%M %p")

  if 'discord.gift/' in message.content:
    if nitro_sniper == True:
      start = datetime.now()
      code = re.search("discord.gift/(.*)", message.content).group(1)
      elapsed = datetime.now() - start
      elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

      token = config.get('token')
      headers = {'Authorization': token}
      r = requests.post(
        f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
        headers=headers).text

      if 'This gift has been redeemed already.' in r:
        print(Fore.LIGHTRED_EX + f"\n[{time}]",
              Fore.RED + "- [Nitro Already Redeemed]")
        NitroData(elapsed, code)
        logn = open('config/Logs/nitro.txt', 'a', encoding="utf-8")
        logn.write(
          f"\n{time} >>Nitro Already Redeemed<<\nServer:{message.guild}\nChannel:{message.channel}\nSent by:{message.author}\nElapsed: {elapsed}\nCode: {code}\n"
        )
        logn.close()

      elif 'subscription_plan' in r:
        print(f"\n[{Fore.GREEN}{time} - Nitro Success]")
        NitroData(elapsed, code)
        logn2 = open('config/Logs/nitro.txt', 'a', encoding="utf-8")
        logn2.write(
          f"\n{time} >>Nitro Success<<\nServer:{message.guild}\nChannel:{message.channel}\nSent by:{message.author}\nElapsed: {elapsed}\nCode: {code}\n"
        )
        logn2.close()

      elif 'Unknown Gift Code' in r:
        print(Fore.LIGHTRED_EX + f"\n[{time}]",
              Fore.RED + "- [Nitro Unknown Gift Code]")
        NitroData(elapsed, code)
        logn3 = open('config/Logs/nitro.txt', 'a', encoding="utf-8")
        logn3.write(
          f"\n{time} >>Nitro Unknown Gift Code<<\nServer:{message.guild}\nChannel:{message.channel}\nSent by:{message.author}\nElapsed: {elapsed}\nCode: {code}\n"
        )
        logn3.close()
    else:
      return


def RandomColor():
  randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
  return randcolor


@death.command()  # - Rainbow role color
async def rainbow(ctx, *, role2):
  await ctx.message.delete()
  role = discord.utils.get(ctx.guild.roles, name=role2)
  try:
    await role.edit(colour=RandomColor())
    await asyncio.sleep(3)
  except Exception as error:
    print(f"[{error}] Cannot do Rainbow")


@death.command()
async def slots(ctx):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "slots",
        Fore.LIGHTRED_EX + "<<")
  emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
  a = random.choice(emojis)
  b = random.choice(emojis)
  c = random.choice(emojis)
  slotmachine = f"[ {a} {b} {c} ]"
  if (a == b == c):
    await ctx.send(
      f"```yaml\n[Death Self Bot]\n\n[Slot Machine]\n{slotmachine}\n\nAll matchings, you won!```"
    )
  elif (a == b) or (a == c) or (b == c):
    await ctx.send(
      f"```yaml\n[Death Self Bot]\n\n[Slot Machine]\n{slotmachine}\n\n2 in a row, you won!```"
    )
    #await ctx.send("> ```Slot Machine```" f"{slotmachine}" "```2 in a row, you won!```")
  else:
    await ctx.send(
      f"```yaml\n[Death Self Bot]\n\n[Slot Machine]\n{slotmachine}\n\nNo Match, you lost!```"
    )
    #await ctx.send("> ```Slot Machine```" f"{slotmachine}" "```No match, you lost.``` ")


@death.command()
async def pingweb(ctx, website=None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "pingweb",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  if website is None:
    error = await ctx.send(
      f"```yaml\n[ERROR] [Death Self Bot] - You forgot to put a website```",
      delete_after=3)
    await asyncio.sleep(2)
    await error.delete()
  else:
    try:
      r = requests.get(website).status_code
    except Exception as e:
      await ctx.send(f"```yaml\n[ERROR] [Death Self Bot] - Unknown```")
    if r == 404:
      await ctx.send(
        f"```yaml\n[ERROR] [Death Self Bot] - Website is down {r}```",
        delete_after=3)
    else:
      await ctx.send(f"```yaml\n[Death Self Bot] - Website is online {r}```",
                     delete_after=3)


@death.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "911",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  invis = ""
  message2 = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
  await asyncio.sleep(0.5)
  await message2.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
  await asyncio.sleep(0.5)
  await message2.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
  await asyncio.sleep(0.5)
  await message2.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
  await asyncio.sleep(0.5)
  await message2.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
        :boom::boom::boom:    
        ''')
  await asyncio.sleep(5)
  await message2.delete()


@death.command()
async def cum(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "cum",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  message2 = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
  await asyncio.sleep(0.5)
  await message2.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
  await message2.delete()


@death.command()
async def count(ctx):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "count",
        Fore.LIGHTRED_EX + "<<")
  await asyncio.sleep(2)
  for _ in range(100):
    await ctx.send(content=_)
    await asyncio.sleep(2)


@death.command()
async def abc(ctx):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "abc",
        Fore.LIGHTRED_EX + "<<")
  ABC = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  ]
  message = await ctx.send(ABC[0])
  await asyncio.sleep(2)
  for _next in ABC[1:]:
    await message.edit(content=_next)
    await asyncio.sleep(2)


@death.command(aliases=["100"])
async def _100(ctx):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>",
        Fore.RED + "editing count to 100", Fore.LIGHTRED_EX + "<<")
  message = await ctx.send("Starting count 0 to 100")
  await asyncio.sleep(2)
  for _ in range(100):
    await message.edit(content=_)
    await asyncio.sleep(2)


@death.command()
async def reav(ctx, user: discord.User = None):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "reav",
        Fore.LIGHTRED_EX + "<<")
  if user == None:
    user = death.user
  try:
    await ctx.send(
      f"https://images.google.com/searchbyimage?image_url={user.avatar.url}")
  except:
    await ctx.send(
      "```yaml\n[ERROR] Death Self Bot```\n```Failed to get user's avatar```",
      delete_after=5)


@death.command()
async def userinfo(ctx, wondermember: discord.User = None):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "userinfo",
        Fore.LIGHTRED_EX + "<<")
  if wondermember is None:
    await ctx.send(f"**Invalid syntax**\nYou have not specified a user")
  else:
    try:
      await ctx.send(f"> ```USER INFO FOR {wondermember}```")
      await ctx.send(
        f"ID:** {wondermember.id}**\nDisplay Name:** {wondermember.display_name}**\nCreation date:** {wondermember.created_at}**"
      )
      await ctx.send(f"{wondermember.avatar_url}")
    except:
      return


@death.command()
async def ping(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "ping",
        Fore.LIGHTRED_EX + "<<")
  await ctx.send("Pong!")


@death.command(aliases=["av"])
async def avatar(ctx, avamember: discord.Member = None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "avatar",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  if avamember == None:
    #channel = self.client.get_channel(1094688186493566986)
    await ctx.send(f"```yaml\n[Death Self Bot] - [{ctx.author}'s avatar]```")
    await ctx.send(f"{ctx.author.avatar.url}")
    #await channel.send(f"{ctx.author} used the command $av on himself.")
  else:
    #channel = self.client.get_channel(1094688186493566986)
    await ctx.send(f"```yaml\n[Death Self Bot] - [{avamember}'s avatar]```")
    await ctx.send(f"{avamember.avatar.url}")


@death.listen("on_message")
async def pingReplier(message):
  now = datetime.now()
  sleep_seconds = 0.1
  current_time = now.strftime("%H:%M:%S")
  if f'<@{death.user.id}>' in str(message.content):
    log = open('config/Logs/pings.txt', 'a', encoding="utf-8")
    log.write(
      f"\n{current_time} >>PING DETECTED<<\nMessage: {message.content}\nAuthor: {message.author}\nServer: {message.guild.name}\nChannel Name: {message.channel.name}\nChannel ID: {message.channel.id}\n"
    )
    log.close()
    async with message.channel.typing():
      await asyncio.sleep(sleep_seconds)
    msg = await message.reply(message_to_reply)
    print(
      Fore.LIGHTRED_EX + f"\n{current_time}", ">>", Fore.RED + "PING DETECTED",
      Fore.LIGHTRED_EX + "<<",
      f"\nAuthor: {message.author}\nChannel: {message.guild.name}\nChannel ID: {message.channel.id}\nMessage: {message.content}\n"
    )


@death.command()
async def playing(ctx, *, start):
  await ctx.message.delete()
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "playing",
        Fore.LIGHTRED_EX + "<<")
  game = discord.Game(name=start)
  await death.change_presence(activity=game)
  await ctx.send(f"> ```Changed your activity to {start}```", delete_after=2)


@death.command()
async def serverinfo(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "serverinfo",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  date_format = "%a, %d %b %Y %I:%M %p"
  try:
    await ctx.send(
      f"> ```Server Info of {ctx.guild.name}:```" + "\n" +
      "Server created at" + " - " +
      f"{ctx.guild.created_at.strftime(date_format)}" + "\n" + "Server Owner" +
      " - " + f"<@{ctx.guild.owner_id}>" + "\n" + "Server ID" + " - " +
      f"{ctx.guild.id}" + "\n" +
      f"{ctx.guild.member_count} Members\n{len(ctx.guild.roles)} Roles\n{len(ctx.guild.text_channels)} Text-Channels\n{len(ctx.guild.voice_channels)} Voice-Channels\n{len(ctx.guild.categories)} Categories"
    )
  except AttributeError:
    return


#Nuke Commands


@death.command()
async def giveadmin(ctx):
  await ctx.message.delete()
  for role in ctx.guild.roles:
    try:
      if role.permission.administartor:
        await ctx.author.add_roles(role)
    except:
      await ctx.send("[ERROR]")


@death.command()
async def newwebhook(ctx, *, name):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>",
        Fore.RED + f"webhook created {name}", Fore.LIGHTRED_EX + "<<")
  webhook = await ctx.channel.create_webhook(name=name)
  await ctx.send(
    f"```yaml\n[Death Self Bot]\nName: {name}\nURL: {webhook.url}```")


@death.command()
async def spamwebhook(ctx, amount: int, url, *, message=None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "spamwebhook",
        Fore.LIGHTRED_EX + "<<")
  for _ in range(amount):
    spamMsg = ''.join(random.choice(string.ascii_letters) for i in range(2000))
    webhook = DiscordWebhook(url=url, content=spamMsg)
    webhook.execute()


@death.command()
async def tokeninfo(ctx, tokeninfotoken=None):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "tokeninfo",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  if tokeninfotoken is None:
    await ctx.send(f'You have not specified a token.')
  else:
    try:
      headers = {
        'Authorization': tokeninfotoken,
        'Content-Type': 'application/json'
      }
      r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
      if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        await ctx.send(
          f'> ```TOKEN INFORMATION```\n```USER ID: {userID}\nUSERNAME: {userName}\n2FA?: {mfa}\nEMAIL: {email} \nPHONENUMBER?: {phone}\nTOKEN:{tokeninfotoken}```'
        )
    except Exception as error:
      await ctx.send(f"> ```{error}```")


@death.command()
async def backupfriend(ctx):
  await ctx.message.delete()
  for friend in death.user.friends:
    friendlist = (friend.name) + '#' + (friend.discriminator)
    with open('Backup/Friends.txt', 'a+') as f:
      f.write(friendlist + "\n")
  for block in death.user.blocked:
    blocklist = (block.name) + '#' + (block.discriminator)
    with open('Backup/Blocked.txt', 'a+') as f:
      f.write(blocklist + "\n")


@death.command()
async def deathchannel(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "deathchannel",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    await channel.delete()
  for i in range(100):
    await ctx.guild.create_text_channel(name="DEATH SELF BOT🔪")


@death.command()
async def deathdestroy(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "deathdestroy",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  with open(("./config/Images/logo.png"), "rb") as logomf:
    logo = logomf.read()
  try:
    await ctx.guild.edit(icon=logo)
  except:
    pass
  for user in list(ctx.guild.members):
    try:
      nickname = f"NUKED BY {ctx.author}"
      await user.edit(nick=nickname)
    except:
      pass
  for user in list(ctx.guild.members):
    try:
      await user.ban()
    except:
      pass
  for channel in list(ctx.guild.channels):
    try:
      await channel.delete()
    except:
      pass
  try:
    with open(("./config/Images/banner.gif"), "rb") as bannermf:
      banner = bannermf.read()
      await ctx.guild.edit(name=f"FUCKED BY {ctx.author}",
                           description="DEATH LMAO",
                           reason="DEATH LMAO",
                           banner=banner)
  except:
    pass
  for _i in range(100):
    await ctx.guild.create_text_channel(name="DEATH SELF BOT🔪")
  for _i in range(25):
    await ctx.guild.create_role(name=f"{ctx.author}'s bitch")
  for _i in range(100):
    channels = ctx.guild.text_channels
    for channel in channels:
      await asyncio.sleep(0.5)
      await channel.send()


@death.command()
async def massban(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "massban",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  users = list(ctx.guild.members)
  for user in users:
    try:
      await user.ban(reason=f"Death Self - by {ctx.author}")
    except:
      pass


@death.command()
async def masskick(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "masskick",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  users = list(ctx.guild.members)
  for user in users:
    try:
      await user.kick(reason=f"Death Self - by {ctx.author}")
    except:
      pass


@death.command()  # -- Broken
async def massunban(ctx):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "massunban",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  banlist = await ctx.guild.bans()
  for users in banlist:
    try:
      await asyncio.sleep(2)
      await ctx.guild.unban(user=users.id)
    except:
      pass


@death.command()
async def rename(ctx, *, name):
  with open((img := "./config/Images/logo.png"), "rb") as pic:
    logo = pic.read()
  try:
    await ctx.guild.edit(name=name, icon=logo)
  except:
    pass


@death.command()  # - Rename server without changing logo.
async def servername(ctx, *, name):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "serverrename",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  await ctx.guild.edit(name=name)


@death.command()
async def nickall(ctx, nickname):
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(Fore.LIGHTRED_EX + f"{current_time}", ">>", Fore.RED + "nickall",
        Fore.LIGHTRED_EX + "<<")
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.edit(nick=nickname)
    except:
      pass


@death.command()
async def readall(ctx):
  await ctx.message.delete()
  for guild in death.guilds:
    await guild.ack()


@death.command()
async def gay(ctx, user: discord.Member = None):
  await ctx.message.delete()
  endpoint = "https://api.alexflipnote.dev/filter/gay?image="
  if user is None:
    avatar = str(ctx.author.avatar_url(format="png"))
    endpoint += avatar
    try:
      async with aiohttp.ClientSession() as session:
        async with session.get(endpoint) as resp:
          image = await resp.read()
      with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"exeter_invert.png"))
    except:
      await ctx.send(endpoint)
  else:
    avatar = str(user.avatar_url(format="png"))
    endpoint += avatar
    try:
      async with aiohttp.ClientSession() as session:
        async with session.get(endpoint) as resp:
          image = await resp.read()
      with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"exeter_invert.png"))
    except:
      await ctx.send(endpoint)

death.run(token)
