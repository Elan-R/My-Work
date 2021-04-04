#py -3 -m pip install -U discord.py
import discord
from discord.ext import commands
import sqlite3
from sqlite3 import Error
import random
from datetime import timedelta
from datetime import datetime
#pip install urllib3
import urllib3
#pip install googletrans
from googletrans import Translator
from collections import namedtuple
import json
import math
import yfinance as yf
from googlefinance import getQuotes
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Otsu Testing")

client = commands.Bot(command_prefix = '%')
http = urllib3.PoolManager()
translator = Translator()

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Otsu Test | %info"))
    print('Otsu Testing ready')

"""
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        err = str(error)[:str(error).find(' ')]
        await ctx.send("Missing Argument: The {} argument is required.".format(err))
    else:
        if isinstance(error, commands.CommandOnCooldown):
            msg = str(error)[34:-1]
            msg = round(float(msg))
            min, sec = divmod(msg, 60)
            hour, min = divmod(min, 60)
            if hour > 0:
                await ctx.send("You can't use this command for {} hours, {} minutes, and {} seconds.".format(str(hour), str(min), str(sec)))
                return
            else:
                if min > 0:
                    await ctx.send("You can't use this command for {} minutes and {} seconds.".format(str(min), str(sec)))
                    return
                else:
                    await ctx.send("You can't use this command for {} seconds.".format(str(sec)))
                    return
        else:
            print(error)
"""

@client.event
@commands.has_role("Testers")
async def on_message(message):
    if message.content == 'e' or message.content == 'E':
        await message.add_reaction('🇪')
    if client.get_guild(713433668147740703).get_role(713524491980111882) in message.author.roles:
        await client.process_commands(message)

client.remove_command("help")

@client.command(name = 'info', aliases = ['help', 'information', 'commands'])
async def info(ctx, *, command = None):
    if command == None:
        embed = discord.Embed(title = "Information", description = "[Invite me to your server!](https://cutt.ly/otsu)\n<@713446074744045589> created by Elan\n[Join the official Otsu discord server!](https://cutt.ly/otsu_server)", color = 0x5b5f90)
        embed.set_author(name = 'Otsu Testing', icon_url = "https://cdn.discordapp.com/attachments/713434731999658034/713454423615209502/pixelskull.png")
        embed.add_field(name = "**How To Use**", value = 'React with:\nℹ️ - **to get back here**\n🕹 - **gaming** commands\n🖥 - **internet** commands\n🛠 - **mod** commands\n\u200b', inline = False)
        embed.add_field(name = "**ℹ️ Info**", value = '`info [optional: command]` - gives information\n`invite` - gives a link to invite Otsu to a server\n`ping` - shows the latency', inline = False)
        embed.set_footer(text = 'Say _info [command name] to learn more about a command.', icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
        message = await ctx.send(embed = embed)
        reactions = ['ℹ️', '🕹', '🖥', '🛠']
        await message.add_reaction('ℹ️')
        await message.add_reaction('🕹')
        await message.add_reaction('🖥')
        await message.add_reaction('🛠')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in reactions
        while True:
            try:
                reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
            except:
                return
            if str(reaction.emoji) == 'ℹ️':
                embed = discord.Embed(title = "Information", description = "[Invite me to your server!](https://cutt.ly/otsu)\n<@713446074744045589> created by Elan\n[Join the official Otsu discord server!](https://cutt.ly/otsu_server)", color = 0x5b5f90)
                embed.set_author(name = 'Otsu Testing', icon_url = "https://cdn.discordapp.com/attachments/713434731999658034/713454423615209502/pixelskull.png")
                embed.add_field(name = "**How To Use**", value = 'React with:\nℹ️ - **to get back here**\n🕹 - **gaming** commands\n🖥 - **internet** commands\n🛠 - **mod** commands\n\u200b', inline = False)
                embed.add_field(name = "**ℹ️ Info**", value = '`info [optional: command]` - gives information\n`invite` - gives a link to invite Otsu to a server', inline = False)
                embed.set_footer(text = 'Say _info [command name] to learn more about a command.', icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
            elif str(reaction.emoji) == '🕹':
                embed = discord.Embed(title = "Information", description = "[Invite me to your server!](https://cutt.ly/otsu)\n<@713446074744045589> created by Elan\n[Join the official Otsu discord server!](https://cutt.ly/otsu_server)", color = 0x5b5f90)
                embed.set_author(name = 'Otsu Testing', icon_url = "https://cdn.discordapp.com/attachments/713434731999658034/713454423615209502/pixelskull.png")
                embed.add_field(name = "**🕹 Gaming**", value = '`hangman [optional: bet] [optional: open]` - starts a game of hangman\n`anagram [optional: bet]` - starts a game of anagram\n`daily` - awards a daily bonus\n`balance [optional: member]` - returns your balance\n`rob @[member]` - attempts to steal from the specified member\n`give @[member] [amount]` - gives the specified member the specified credits', inline = False)
                embed.set_footer(text = 'Say _info [command name] to learn more about a command.', icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
            elif str(reaction.emoji) == '🖥':
                embed = discord.Embed(title = "Information", description = "[Invite me to your server!](https://cutt.ly/otsu)\n<@713446074744045589> created by Elan\n[Join the official Otsu discord server!](https://cutt.ly/otsu_server)", color = 0x5b5f90)
                embed.set_author(name = 'Otsu Testing', icon_url = "https://cdn.discordapp.com/attachments/713434731999658034/713454423615209502/pixelskull.png")
                embed.add_field(name = "**🖥 Internet**", value = '`urban [word/phrase]` - searched a word or phrase on urban dictionary`translate [message] [language]` - translates a message to a language\n`define [word]` - defines the word\n`pun` - sends a random pun\n`pickup` - sends a random pickup line\n`xkcd [optional: number]` - sends a random xkcd comic, and if specified a specifc comic by number\n`quote` - sends a random inspirational quote', inline = False)
                embed.set_footer(text = 'Say _info [command name] to learn more about a command.', icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
            elif str(reaction.emoji) == '🛠':
                embed = discord.Embed(title = "Information", description = "[Invite me to your server!](https://cutt.ly/otsu)\n<@713446074744045589> created by Elan\n[Join the official Otsu discord server!](https://cutt.ly/otsu_server)", color = 0x5b5f90)
                embed.set_author(name = 'Otsu Testing', icon_url = "https://cdn.discordapp.com/attachments/713434731999658034/713454423615209502/pixelskull.png")
                embed.add_field(name = "**🛠 Mod**", value = '`del [optional: number]` - deltes that many messages\n`deltxt [optional - number]` - deletes that many non-attachment messages\n`delnonpin [optional: number]` - deletes that many non-pinned messages\n`giverole @[role] @[member]` - give the member the role\n`distributerole @[role]` - gives the role to anyone who reacts to a bot-sent message\n`clearroles` - removes all roles except the highest one from every member\n`kick @[member] [optional: reason]` - kicks a member with said reason\n`ban @[member] [optional: reason]` - bans a member with said reason\n`announce #[text channel] @[role] [message]` - announces the message to the text channel while tagging the role\n`channelset [see _info channelset]` - resets the server\'s channels to those specified', inline = False)
                embed.set_footer(text = 'Say _info [command name] to learn more about a command.', icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
            await reaction.remove(ctx.author)
            await message.edit(embed = embed)
    elif command == 'info':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Gives information about the bot including a list of the available commands.  Adding a command name after _info will give information about the command.', inline = False)
        embed.add_field(name = "**Aliases**", value = 'help, information, commands', inline = False)
    elif command == 'invite':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Gives a link to invite Otsu to a server.', inline = False)
    elif command == 'ping':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Shows the latency in milliseconds up to the third decimal place', inline = False)
    elif command == 'daily':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Awards 500 credits. This command is available every 12 hours.', inline = False)
    elif command == 'rob':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Tries to steal a random amount of credits between 1/10 and 1/5 of the member\'s balance. If it fails, you will give the member 250 credits. You can only rob a member if they have at least 250 credits.', inline = False)
        embed.add_field(name = "**Alias**", value = 'steal', inline = False)
    elif command == 'balance':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Shows you how many credits you have. If a member is tagged after _balance, their balance will be shown.', inline = False)
        embed.add_field(name = "**Alias**", value = 'bal', inline = False)
    elif command == 'give':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Gives the member tagged the amount specified. The credits are withdrawn from your balance.', inline = False)
    elif command == 'hangman':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = "Starts a game of hangman. The goal of the game is to guess letters until you know the word, then to either guess the word or finish guessing the letters. To play, type +c to guess the letter c and +cat to guess the word cat. If a bet is provided (a number), you will be rewarded that many credits if you guess the entire word. Otherwise, you lose that many credits. Saying 'open' after _hangman [bet] makes the game public, and anyone can guess using -c and -cat instead of +c and +cat.", inline = False)
        embed.add_field(name = "**Alias**", value = 'hm', inline = False)
    elif command == 'anagram':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Starts a game of anagram. The goal of the game is to guess a randomly scrambled word. To play, type +cat to guess the word cat. If a bet is provided (a number), you will be rewarded that many credits if you guess the word. Otherwise, you lose that many credits.', inline = False)
        embed.add_field(name = "**Alias**", value = 'bal', inline = False)
    elif command == 'urban':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Searches a word or phrase on urban dictionary and sends an embed with arrow reactions. Reacting with the arrows will navigate through the responses. The reactions will expire after 60 seconds.', inline = False)
    elif command == 'translate':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = "Translates the message to the language specified. (See languages above.)", inline = False)
        embed.add_field(name = "**Alias**", value = 'tl', inline = False)
        await ctx.send("""**A**
'af': 'afrikaans',
'sq': 'albanian',
'am': 'amharic',
'ar': 'arabic',
'hy': 'armenian',
'az': 'azerbaijani',
**B**
'eu': 'basque',
'be': 'belarusian',
'bn': 'bengali',
'bs': 'bosnian',
'bg': 'bulgarian',
**C**
'ca': 'catalan',
'ceb': 'cebuano',
'ny': 'chichewa',
'zh-cn': 'chinese (simplified)',
'zh-tw': 'chinese (traditional)',
'co': 'corsican',
'hr': 'croatian',
'cs': 'czech',
**D**
'da': 'danish',
'nl': 'dutch',
**E**
'en': 'english',
'eo': 'esperanto',
'et': 'estonian',
**F**
'tl': 'filipino',
'fil': 'Filipino',
'fi': 'finnish',
'fr': 'french',
'fy': 'frisian',
**G**
'gl': 'galician',
'ka': 'georgian',
'de': 'german',
'el': 'greek',
'gu': 'gujarati',
**H**
'ht': 'haitian creole',
'ha': 'hausa',
'haw': 'hawaiian',
'iw': 'hebrew',
'he': 'Hebrew',
'hi': 'hindi',
'hmn': 'hmong',
'hu': 'hungarian',
**I**
'is': 'icelandic',
'ig': 'igbo',
'id': 'indonesian',
'ga': 'irish',
'it': 'italian',
**J**
'ja': 'japanese',
'jw': 'javanese',
**K**
'kn': 'kannada',
'kk': 'kazakh',
'km': 'khmer',
'ko': 'korean',
'ku': 'kurdish (kurmanji)'""".replace("'", ""))
        await ctx.send("""'ky': 'kyrgyz',
**L**
'lo': 'lao',
'la': 'latin',
'lv': 'latvian',
'lt': 'lithuanian',
'lb': 'luxembourgish',
**M**
'mk': 'macedonian',
'mg': 'malagasy',
'ms': 'malay',
'ml': 'malayalam',
'mt': 'maltese',
'mi': 'maori',
'mr': 'marathi',
'mn': 'mongolian',
'my': 'myanmar (burmese)',
**N**
'ne': 'nepali',
'no': 'norwegian',
**O**
**P**
'ps': 'pashto',
'fa': 'persian',
'pl': 'polish',
'pt': 'portuguese',
'pa': 'punjabi',
**Q**
**R**
'ro': 'romanian',
'ru': 'russian',
**S**
'sm': 'samoan',
'gd': 'scots gaelic',
'sr': 'serbian',
'st': 'sesotho',
'sn': 'shona',
'sd': 'sindhi',
'si': 'sinhala',
'sk': 'slovak',
'sl': 'slovenian',
'so': 'somali',
'es': 'spanish',
'su': 'sundanese',
'sw': 'swahili',
'sv': 'swedish',
**T**
'tg': 'tajik',
'ta': 'tamil',
'te': 'telugu',
'th': 'thai',
'tr': 'turkish',
**U**
'uk': 'ukrainian',
'ur': 'urdu',
'uz': 'uzbek',
**V**
'vi': 'vietnamese',
**W**
'cy': 'welsh',
**X**
'xh': 'xhosa',
**Y**
'yi': 'yiddish',
'yo': 'yoruba',
**Z**
'zu': 'zulu'""".replace("'", ""))
    elif command == 'define':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Defines the word given.')
    elif command == 'pun':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Sends a random pun to the chat.')
    elif command == 'pickup':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Sends a random pickup line to the chat.')
    elif command == 'xkcd':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Sends a random xkcd comic https link to the chat. If specified, sends a comic by number to the chat. The comics range from comic 1 to 2295.')
    elif command == 'quote':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Sends a random inspirational quote to the chat.')
    elif command == 'del':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Deletes the specified number of messages. If not specified, deltes the previous message.')
    elif command == 'deltxt':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Deletes the specified number of non-attachment messages (images, pdfs, etc.). If not specified, deletes the previous message.')
    elif command == 'delnonpin':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Deletes the specified number of non-pinned messages (messages that aren\'t pinned). If not specified, deletes the previous message.')
    elif command == 'distributerole':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'The bot sends a message that when reacted to, that user will get the specified role. Note that anyone can react to that message.')
    elif command == 'giverole':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Gives the specified member the specified role.')
    elif command == 'clearroles':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Removes all the roles from every member except the highest role. Note that this does not delete the roles.')
    elif command == 'kick':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Kicks the specified member. If a reason is given, the reason will be visible in the audit log.')
    elif command == 'ban':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Bans the specified member. If a reason is given, the reason will be visible in the audit log.')
    elif command == 'announce':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Announces a message to the specified text channel with a header stating the author and mentioning the role.')
    elif command == 'channelset':
        embed = discord.Embed(title = command, color = 0x5b5f90)
        embed.add_field(name = "**Description**", value = 'Deletes all the channels and categories, and then creates new ones based on the syntax. The syntax is:\n(name) - to create a text channel with that name\n[name] - to create a voice channel with that name\n{name} - to create a category with that name. Any channels defined after a category is defined will be placed in that category unless a \'.\' is put or another category is defined.')
    else:
        await ctx.send(f'The command {command} was not found.\nTry typing: `_info` or `_info daily`.')
        return
    await ctx.send(embed = embed)

@client.command(name = 'ping')
async def ping(ctx):
    await ctx.send(str(round(client.latency * 1000, 3)) + ' ms')

@client.command(name = "del")
@commands.has_permissions(manage_messages=True)
async def _del(ctx, amount=1):
    if round(amount) >= 1:
        await ctx.channel.purge(limit = amount + 1,)
    else:
        await ctx.channel.purge(limit=1)

@client.command(name = 'deltxt')
@commands.has_permissions(manage_messages=True)
async def deltxt(ctx, lim = 1):
    if lim >= 1:
        await ctx.channel.purge(limit = lim + 1, check = lambda msg: not msg.attachments)
    else:
        await ctx.channel.purge(limit = 1, check = lambda msg: not msg.attachments)

@client.command(name = 'delnonpin')
@commands.has_permissions(manage_messages=True)
async def delnonpin(ctx, lim = 1):
    if lim >= 1:
        await ctx.channel.purge(limit = lim + 1, check = lambda msg: not msg.pinned)
    else:
        await ctx.channel.purge(limit = 1, check = lambda msg: not msg.pinned)

@client.command(name = 'kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command(name = 'ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command(name = 'announce')
async def announce(ctx, GetChannel : discord.TextChannel, GetRole :discord.Role, *, arg):
    await ctx.channel.purge(limit=1)
    channel = client.get_channel(GetChannel.id)
    author = ctx.author
    await channel.send(f'An announcement from {author} to {GetRole.mention}:\n{arg}')

@client.command(name = 'channelset')
@commands.has_permissions(manage_channels=True)
async def channelset(ctx, *, build):
    Guild = ctx.guild
    for i in list(Guild.channels):
        await i.delete()
    build = (build.replace(' ', '')).replace('_', ' ')
    i = 0
    CurrentCategory = None
    while build != None:
        if build[i] == '(':
            name = ''
            while build[i] != ')':
                i += 1
                name += build[i]
            if CurrentCategory == None:
                await Guild.create_text_channel(name)
            else:
                await CurrentCategory.create_text_channel(name)
            build = build[i:]
            i = 0
        if build[i] == '[':
            name = ''
            while build[i] != ']':
                i += 1
                name += build[i]
            if CurrentCategory == None:
                await Guild.create_voice_channel(name.rstrip(']'))
            else:
                await CurrentCategory.create_voice_channel(name.rstrip(']'))
            build = build[i:]
            i = 0
        if build[i] == '{':
            name = ''
            while build[i] != '}':
                i += 1
                name += build[i]
            await Guild.create_category(name.rstrip('}'))
            CurrentCategory = discord.utils.get(client.get_all_channels(), guild__name = Guild.name, name = name.rstrip('}'))
        if build[i] == '.':
            CurrentCategory = None
        i += 1
        if i > len(build) - 1:
            break

@client.command(name = 'distributerole')
async def distributerole(ctx, role : discord.Role):
    if role >= ctx.author.top_role:
        await ctx.send('You need to have a role above this role to give it.')
        return
    message = await ctx.send(f'React to this message to get the {role} role.')
    await message.add_reaction('😎')
    def check(reaction, user):
        return user.id != '698700243277054023'
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
        except:
            await message.delete()
            return
        await user.add_roles(role)

@client.command(name = 'giverole')
async def giverole(ctx, role : discord.Role, member : discord.Member):
    if role >= ctx.author.top_role:
        await ctx.send('You need to have a role above this role to give it.')
        return
    await member.add_roles(role)
    await ctx.send(f'Gave {member.display_name} the {role.name} role.')

@client.command(name = 'clearroles')
async def clearroles(ctx):
    if ctx.author.top_role < ctx.guild.roles[-1] and ctx.guild.owner != ctx.author:
        await ctx.send('You must have the highest role or own this server to use this command.')
        return
    for i in ctx.guild.members:
        for x in i.roles[1:]:
            try:
                await i.remove_roles(x)
            except:
                pass

@client.command(name = 'managedmtriggers')
async def dmtrigger(ctx, trigger_id = None, action = None):
    print('dm triggers')

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

connection = create_connection("C:/sqlite/otsutest_data.db")

async def get_balance(user_id):
    global connection
    try:
        return float(str(execute_read_query(connection, f'SELECT hand_balances FROM user_balances WHERE user_ids = {user_id}'))[2:-3])
    except ValueError:
        execute_query(connection, f"INSERT INTO user_balances (user_ids, hand_balances, bank_balances) VALUES ({user_id}, {0.}, {0.});")
        return 0.

async def get_bank_balance(user_id):
    global connection
    try:
        return float(str(execute_read_query(connection, f'SELECT bank_balances FROM user_balances WHERE user_ids = {user_id}'))[2:-3])
    except ValueError:
        execute_query(connection, f'UPDATE user_balances SET bank_balances = {0.} WHERE user_ids = {user_id}')
        return 0.

async def update_balance(user_id, change):
    execute_query(connection, f'UPDATE user_balances SET hand_balances = {await get_balance(user_id) + float(change)} WHERE user_ids = {user_id}')

async def update_bank_balance(user_id, change):
    execute_query(connection, f'UPDATE user_balances SET bank_balances = {await get_bank_balance(user_id) + float(change)} WHERE user_ids = {user_id}')

@client.command(name = 'balance', aliases = ['bal'])
async def balance(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    hand_bal = await get_balance(member.id)
    bank_bal = await get_bank_balance(member.id)
    embed = discord.Embed(title = f"{member.display_name}'s Balance", description = f'Net worth: {hand_bal + bank_bal}', color = 0x5b5f90)
    embed.add_field(name = "**Hand Balance**", value = str(hand_bal), inline = False)
    embed.add_field(name = "**Bank Balance**", value = str(bank_bal), inline = False)
    await ctx.send(embed = embed)

@client.command(name = 'deposit', aliases = ['dep'])
async def deposit(ctx, amount = None):
    if amount == None:
        await ctx.send("You must specfy an amount to deposit to the bank, or to deposit everything on hand, say `_deposit all`.")
    if amount.lower() == 'all':
        bal = await get_balance(ctx.author.id)
        if bal == 0:
            await ctx.send("You don't have any credits on hand.")
            return
        await update_balance(ctx.author.id, -bal)
        await update_bank_balance(ctx.author.id, bal)
        await ctx.send(f"Successfully deposited **{bal}** credits to the bank.")
        return
    try:
        amount = float(amount)
    except:
        await ctx.send("The amount you deposit must be a number.")
        return
    if round(amount * 100) / 100 != amount:
        await ctx.send("You can only deposit credits up to the second decimal place.")
        return
    if amount <= 0:
        await ctx.send("You can only deposit an amount over 0.\nUse `_withdraw [amount]` to take credits from the bank.")
        return
    bal = await get_balance(ctx.author.id)
    if amount > bal:
        await ctx.send(f"You don't have that many credits on hand. You only have {bal} credits.")
        return
    await update_balance(ctx.author.id, -amount)
    await update_bank_balance(ctx.author.id, amount)
    await ctx.send(f"Successfully deposited **{amount}** credits to the bank.")

@client.command(name = 'withdraw', aliases = ['with'])
async def withdraw(ctx, amount):
    if amount == None:
        await ctx.send("You must specfy an amount to withdraw from the bank, or to withdraw everything, say `_withdraw all`.")
    if amount.lower() == 'all':
        bal = await get_bank_balance(ctx.author.id)
        if bal == 0:
            await ctx.send("You don't have any credits in the bank.")
            return
        await update_bank_balance(ctx.author.id, -bal)
        await update_balance(ctx.author.id, bal)
        await ctx.send(f"Successfully withdrew **{bal}** credits from the bank.")
        return
    try:
        amount = float(amount)
    except:
        await ctx.send("The amount you withdraw must be a number.")
        return
    if round(amount * 100) / 100 != amount:
        await ctx.send("You can only withdraw credits up to the second decimal place.")
        return
    if amount <= 0:
        await ctx.send("You can only withdraw an amount over 0.\nUse `_deposit [amount]` to put your credits in the bank.")
        return
    bal = await get_bank_balance(ctx.author.id)
    if amount > bal:
        await ctx.send(f"You don't have that many credits in the bank. You only have {bal} credits.")
        return
    await update_bank_balance(ctx.author.id, -amount)
    await update_balance(ctx.author.id, amount)
    await ctx.send(f"Successfully withdrew **{amount}** credits from the bank.")

@client.command(name = 'gift')
@commands.is_owner()
async def gift(ctx, member : discord.Member, change):
    await update_balance(member.id, change)
    await ctx.send("Gifted {} **{}** credits.".format(member.mention, change))


async def raw_job_info():
    raw_job_titles = {1: {0: 'dishwasher', 1: 'host', 2: 'busser', 3: 'waiter', 4: 'bartender', 5: 'chef', 6: 'executive chef', 7: 'restaurant manager'},
                      2: {0: 'junior programmer', 1: 'senior programmer', 2: 'software architect', 3: 'solution architect', 4: 'IT director'},
                      3: {0: 'kindergaten teacher', 1: 'elementary school teacher', 2: 'middle school teacher', 3: 'high school teacher', 4: 'guidance counselor', 5: 'assistant principal', 6: 'principal'}}
    raw_job_salaries = {1: {0: 100., 1: 120., 2: 130., 3: 150., 4: 160., 5: 220., 6: 260., 7: 300.},
                        2: {0: 330., 1: 600., 2: 900., 3: 1080., 4: 1320.},
                        3: {0: 340., 1: 360., 2: 400., 3: 430., 4: 450., 5: 520, 6: 600}}
    return raw_job_titles, raw_job_salaries

@client.command(name = 'joblist', aliases = ['jobs', 'job'])
async def joblist(ctx):
    raw_job_titles, raw_job_salaries = await raw_job_info()
    job_info = []
    for i in raw_job_titles:
        job_info += ['']
        for x in raw_job_titles[i]:
            job_info[i - 1] += f'**{x}:** {raw_job_titles[i][x]} - {raw_job_salaries[i][x]}\n'
    embed = discord.Embed(title = "Job List", description = "To apply for a job, say `APPLY COMMAND HERE`.", color = 0x5b5f90)
    embed.add_field(name = "**Categories**", value = 'React with:\n\nℹ️ - **to get back here**\n\n1️⃣ - **Restaurant Jobs**\n\n2️⃣ - **Programming Jobs**\n\n3️⃣ - **Education Jobs**\n\u200b', inline = False)
    message = await ctx.send(embed = embed)
    reactions = ['ℹ️', '1️⃣', '2️⃣', '3️⃣']
    await message.add_reaction('ℹ️')
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    await message.add_reaction('3️⃣')
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reactions
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
        except:
            return
        if str(reaction.emoji) == 'ℹ️':
            embed = discord.Embed(title = "Job List", description = "To apply for a job, say `_apply [category id] [job id]`.", color = 0x5b5f90)
            embed.add_field(name = "**Categories**", value = 'React with:\n\nℹ️ - **to get back here**\n\n1️⃣ - **Restaurant Jobs**\n\n2️⃣ - **Programming Jobs**\n\n3️⃣ - **Education Jobs**\n\u200b', inline = False)
        elif str(reaction.emoji) == '1️⃣':
            job_category = 'Restaurant'
        elif str(reaction.emoji) == '2️⃣':
            job_category = 'Programming'
        elif str(reaction.emoji) == '3️⃣':
            job_category = 'Education'
        if str(reaction.emoji) != 'ℹ️':
            embed = discord.Embed(title = "Job List", description = "To apply for a job, say `_apply [category id] [job id]`.", color = 0x5b5f90)
            embed.add_field(name = f"**{reaction.emoji} {job_category} Jobs**\n** **", value = job_info[int(list(str(reaction.emoji))[0]) - 1], inline = False)
        await reaction.remove(ctx.author)
        await message.edit(embed = embed)

@client.command(name = 'apply')
async def apply(ctx, category = None, job = None):
    global connection
    apply_time = datetime.strptime(execute_read_query(connection, f'SELECT apply_time FROM user_balances WHERE user_ids = {ctx.author.id}')[0][0], '%Y-%m-%d %H:%M:%S.%f')
    if apply_time != None:
        if apply_time > ctx.message.created_at:
            available = (apply_time - ctx.message.created_at).seconds
            hour = available // 3600
            min = (available - hour * 3600) // 60
            sec = available - (min * 60 + hour * 3600)
            if min > 0:
                await ctx.send("You can't use this command for {} minutes and {} seconds.".format(str(min), str(sec)))
                return
            else:
                await ctx.send("You can't use this command for {} seconds.".format(str(sec)))
                return
            await ctx.send(f'You have to wait {hour} hours, {min} minutes and {sec} seconds until you can apply for a job again.')
            return
    if category == None:
        await ctx.send('You must specify a job category ID. To see all job categories, say `_joblist`.')
        return
    try:
        category = int(category)
    except ValueError:
        await ctx.send('The category must be it\'s ID. To see all job categories and their IDs, say `_joblist`.')
        return
    raw_job_titles, raw_job_salaries = await raw_job_info()
    if category < 1 or category > len(raw_job_titles):
        await ctx.send('You must enter a valid job category ID.')
        return
    if job == None:
        await ctx.send('You must specify a job ID. To see all job categories, say `_joblist`.')
        return
    try:
        job = int(job)
    except ValueError:
        await ctx.send('The job must be it\'s ID. To see all job\'s and their IDs, say `_joblist`.')
        return
    if job < 0 or job > len(raw_job_titles[category]):
        await ctx.send('You must enter a valid job ID.')
        return
    execute_query(connection, f'UPDATE user_balances SET apply_time = \'{ctx.message.created_at + timedelta(minutes = 10)}\' WHERE user_ids = {ctx.author.id}')
    if raw_job_salaries[category][job] * 0.075 < random.randint(1, 100):
        print('Accept job?')
        execute_query(connection, f'UPDATE user_balances SET job = {category + (job / 10)} WHERE user_ids = {ctx.author.id}')
        await ctx.send('You got the job!')
        return
    await ctx.send('Your application was denied.')

o = namedtuple('o', 'name location price stats')

async def raw_shop_info():
    return {1: {1: {1: o('novice fishing rod', '1.1.1', 1000, 70), 2: o('apprentice fishing rod', '1.1.2', 1500, 80), 3: o('pro fishing rod', '1.1.3', 2000, 90), 4: o('master fishing rod', '1.1.4', 2500, 99)}, 2: {1: o('pack of bait', '1.2.1', 10, 0), 2: o('pack of tasty bait', '1.2.2', 20, 25), 3: o('pack of irresistible bait', '1.2.3', 40, 50)}}}

@client.command(name = 'shop')
async def shop(ctx):
    shop_info = await raw_shop_info()
    embed = discord.Embed(title = "Shop", description = "Use the `buy [serial number]` command to buy items!\nTip: an item's serial number is displayed after the item name (e.g. pro fishing rod **(1.1.3)**)", color = 0x5b5f90)
    embed.add_field(name = "**Categories**", value = 'React with the emojis to see the items in that catogry!\nℹ️ - to see this page\n🎣 - fishing\n')
    message = await ctx.send(embed = embed)
    reactions = ['ℹ️', '🎣']
    for i in reactions: await message.add_reaction(i)
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reactions
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
        except:
            return
        embed = discord.Embed(title = "Shop", description = "Use the `buy [serial number]` command to buy items!\nTip: an item's serial number is displayed after the item name (e.g. pro fishing rod **(1.1.3)**)", color = 0x5b5f90)
        if str(reaction.emoji) == 'ℹ️':
            embed = discord.Embed(title = "Shop", description = "Use the `buy [serial number]` command to buy items!\nTip: an item's serial number is displayed after the item name", color = 0x5b5f90)
            embed.add_field(name = "**Categories**", value = 'React with the emojis to see the items in that catogry!\nℹ️ - to see this page\n🎣 - fishing\n')
        if str(reaction.emoji) == '🎣':
            embed = discord.Embed(title = "Shop", description = "Use the `buy [serial number]` command to buy items!\nTip: an item's serial number is displayed after the item name", color = 0x5b5f90)
            embed.add_field(name = "**Fishing Rods**", value = '\n'.join([f'**{i.name}** ({i.location}) - **{i.price}** credits, {i.stats}% catch rate' for i in (shop_info[1][1][x] for x in shop_info[1][1])]), inline = False)
            embed.add_field(name = "**Bait**", value = '\n'.join([f'**{i.name}** ({i.location}) - **{i.price}** credits, +{i.stats}% fish size boost' for i in (shop_info[1][2][x] for x in shop_info[1][2])]), inline = False)
        await reaction.remove(ctx.author)
        await message.edit(embed = embed)

async def get_assets(user_id):
    global connection
    try:
        return json.loads(execute_read_query(connection, f'SELECT assets FROM user_balances WHERE user_ids = {user_id}')[0][0])
    except AttributeError:
        await get_balance(user_id)
        return {}
    except TypeError:
        await get_balance(user_id)
        return {}
async def add_asset(user_id, asset):
    global connection
    assets = await get_assets(user_id)
    try:
        assets[str(json.dumps(asset._asdict()))] += 1
    except KeyError:
        assets[str(json.dumps(asset._asdict()))] = 1
    execute_query(connection, f"UPDATE user_balances SET assets = '{assets}' WHERE user_ids = {user_id}")

async def remove_asset(user_id, asset):
    global connection
    assets = await get_assets(user_id)
    asset_strdict = str(json.dumps(asset._asdict()))
    assets[asset_strdict] -= 1
    if assets[asset_strdict] == 0:
        del assets[asset_strdict]
    if assets == {}:
        assets = ''
    execute_query(connection, f"UPDATE user_balances SET assets = '{assets}' WHERE user_ids = {user_id}")

async def asset_stat_str(asset):
    location = asset.location.split('.')
    if location[0] == '1':
        if location[1] == '1':
            return f"{asset.stats}% catch rate"
        return f"+{asset.stats}% fish size boost"

@client.command(name = 'buy')
async def buy(ctx, location = None, amount = None):
    if location == None:
        await ctx.send('You have to give the serial number of the item you want to buy!\nTo see all items and their serial numbers use the `shop` command.')
        return
    shop_info = await raw_shop_info()
    for i in location.split('.'):
        try:
            shop_info = shop_info[int(i)]
        except:
            await ctx.send('Make sure you enter a valid serial number.\nTo see all items and their serial numbers use the `shop` command.')
            return
    if amount == None:
        if shop_info.price > (await get_balance(ctx.author.id)):
            await ctx.send(f'You don\'t have enough credits on hand to buy a **{shop_info.name}**!')
            return
        message = await ctx.send(f'Are you sure you would like to buy a **{shop_info.name}** for **{shop_info.price}** credits?')
    else:
        try:
            amount = int(amount)
        except:
            await ctx.send('The amount of the item you want to buy must be an integer.')
            return
        if shop_info.price * amount > (await get_balance(ctx.author.id)):
            await ctx.send(f'You don\'t have enough credits on hand to buy **{amount} {shop_info.name}**!')
            return
        message = await ctx.send(f'Are you sure you would like to buy **{amount} {shop_info.name}** for **{shop_info.price * amount}** credits?')
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ['✅', '❌']
    try:
        reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
    except:
        return
    if str(reaction.emoji) == '❌':
        await ctx.send('Purchase calceled.')
        return
    if amount == None:
        await add_asset(ctx.author.id, shop_info)
        await update_balance(ctx.author.id, -shop_info.price)
    else:
        for i in range(amount):
            await add_asset(ctx.author.id, shop_info)
        await update_balance(ctx.author.id, -shop_info.price * amount)
    if amount == None:
        await ctx.send(f'Successfully bought **{shop_info.name}**!')
    else:
        await ctx.send(f'Successfully bought **{amount} {shop_info.name}**!')

@client.command(name = 'inventory', aliases = ['inv'])
async def inventory(ctx):
    raw_assets = await get_assets(ctx.author.id)
    print(raw_assets)
    if raw_assets == {}:
        await ctx.send('You don\'t have any items! To view items to buy, use the `shop` command.')
        return
    assets = {}
    for i in raw_assets:
        assets[o(**json.loads(i))] = raw_assets[i]
    if len(assets) < 6:
        embed = discord.Embed(title = 'Inventory', color = 0x5b5f90)
        inv_msg = ''
        for i in assets:
            inv_msg += f"**{i.name}** x{assets[i]}\nItem value: {i.price} credits\nItem stats: {await asset_stat_str(i)}\nSerial number: {i.location}\n\n"
        embed.add_field(name = '\u200b', value = inv_msg)
        await ctx.send(embed = embed)
        return
    reactions = ['◀', '▶', '⏮', '⏭']
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reactions
    five = non_dup_assets[:5]
    embed = discord.Embed(title = 'Inventory', color = 0x5b5f90)
    inv_msg = ''
    for i in five:
        inv_msg += f"**{i.name}** x{dup_count[i.location]}\nItem value: {i.price} credits\nItem stats: {await asset_stat_str(i)}\nSerial number: {i.location}\n\n"
    embed.add_field(name = '\u200b', value = inv_msg)
    embed.set_footer(text = 'Page 1')
    message = await ctx.send(embed = embed)
    menu = 1
    while True:
        await message.add_reaction('⏮')
        await message.add_reaction('◀')
        await message.add_reaction('▶')
        await message.add_reaction('⏭')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
        except:
            return
        if reaction.emoji == '▶' and not menu * 5 >= len(non_dup_assets):
            menu += 1
        if reaction.emoji == '◀' and menu != 1:
            menu -= 1
        if reaction.emoji == '⏮':
            menu = 1
        if reaction.emoji == '⏭':
            menu = math.ceil(len(non_dup_assets) / 5)
        await reaction.remove(ctx.author)
        five = non_dup_assets[menu * 5 - 5:menu * 5]
        embed = discord.Embed(title = 'Inventory', color = 0x5b5f90)
        inv_msg = ''
        for i in five:
            inv_msg += f"**{i.name}** x{dup_count[i.location]}\nItem value: {i.price} credits\nItem stats: {await asset_stat_str(i)}\nSerial number: {i.location}\n\n"
        embed.add_field(name = '\u200b', value = inv_msg)
        embed.set_footer(text = 'Page ' + str(menu))
        await message.edit(embed = embed)

@client.command(name = 'sell')
async def sell(ctx, location = None, amount = None):
    if location == None:
        await ctx.send('You have to give the serial number of the item you want to sell!\nTo see all of your items and their serial numbers use the `inventory` command.')
        return
    raw_assets = await get_assets(ctx.author.id)
    try:
        location = location.lower()
    except:
        pass
    else:
        if location == 'all':
            message = await ctx.send('Are you sure you want to sell **all** of your items?')
            await message.add_reaction('✅')
            await message.add_reaction('❌')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ['✅', '❌']
            try:
                reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)
            except:
                return
            if str(reaction.emoji) == '❌':
                return
            profit = 0
            for i in raw_assets:
                item = o(**json.loads(i))
                profit += item.price
                await remove_asset(ctx.author.id, item)
            await ctx.send('Successfully sold all items!')
            return
    item = ''
    for i in raw_assets:
        item = o(**json.loads(i))
        item_raw = i
        if item.location == location:
            break
    else:
        await ctx.send(f'You do not own an item with the serial number {location}.\nTo see all of your items and their serial numbers use the `inventory` command.')
        return
    if amount != None:
        try:
            amount = int(amount)
        except:
            await ctx.send('The amount of items to sell must be an integer.')
            return
        if raw_assets.count(item_raw) < amount:
            await ctx.send("You don't have that many of that item!")
            return
        for i in range(amount):
            await remove_asset(ctx.author.id, item)
        await update_balance(ctx.author.id, item.price * amount)
        await ctx.send(f"Successfully sold **{amount} {item.name}** for **{item.price * amount}** credits!")
        return
    await remove_asset(ctx.author.id, item)
    await update_balance(ctx.author.id, item.price)
    await ctx.send(f"Successfully sold **{item.name}** for **{item.price}** credits!")

@client.command(name = 'fish')
async def fish(ctx):
    assets = [o(**json.loads(i)) for i in await get_assets(ctx.author.id)]
    fishing_rod = None
    rod_location = 0
    for i in assets:
        if i.location.startswith('1.1.') and int(i.location[i.location.rfind('.') + 1:]) > rod_location:
            fishing_rod = i
            rod_location = int(i.location[i.location.rfind('.') + 1:])
    if fishing_rod == None:
        await ctx.send('You need to have a fishing rod to fish!\nUse the `shop` command to veiw all the fishing rods for sale.')
        return
    bait = None
    bait_location = 0
    for i in assets:
        if i.location.startswith('1.2.') and int(i.location[i.location.rfind('.') + 1:]) > bait_location:
            bait = i
            bait_location = int(i.location[i.location.rfind('.') + 1:])
    if bait == None:
        await ctx.send('You need to have bait to fish!\nUse the `shop` command to veiw all the packs of bait for sale.')
        return
    fish = []
    for i in range(5):
        if random.random() < fishing_rod.stats / 100:
            price = round((random.randint(60, 80) * (1 + bait.stats / 100)) * 100) / 100
            fish.append(o('fish', f'1.0.{int(price * 100)}', price, 0))
    for i in fish:
        await add_asset(ctx.author.id, i)
    await remove_asset(ctx.author.id, bait)
    if fish == []:
        await ctx.send('You didn\'t catch any fish!')
        return
    await ctx.send(f'You caught **{len(fish)} fish**! Check your inventory to see their value.')

@client.command(name = 'urban')
async def urban(ctx, *, word = ''):
    if word == '':
        await ctx.send('You have to put a word to search up!')
        return
    r = http.request('GET', 'https://www.urbandictionary.com/define.php?term=' + word.replace(' ', '+'))
    data = r.data.decode('utf8')
    pages = [data.find('<a class="word"'), data.find('class="contributor"')]
    result = data[data.find('<a class="word"'):data.find('class="contributor"')]
    meaning = result[result.find('class="meaning"') + 16:result.find('</div>', result.find('class="meaning"'))]
    for i in range(0, meaning.count('<a')):
        meaning = meaning.replace(meaning[meaning.find('<a'):meaning.find('>', meaning.find('<a')) + 1], '').replace('</a>', '')
    embed = discord.Embed(title = "Definition of " + result[result.find('term=') + 5:result.find('"', result.find('term='))].capitalize().replace('%20', ' '), color = 0x5b5f90)
    embed.add_field(name = "**Definition**", value = meaning.replace('<br/>', '\n').replace('&lt;', '<').replace('&apos;', "'").replace('&quot;', '"'), inline = False)
    example = result[result.find('class="example"') + 16:result.find('</div>', result.find('class="example"'))]
    for i in range(0, example.count('<a')):
        example = example.replace(example[example.find('<a'):example.find('>', example.find('<a')) + 1], '').replace('</a>', '')
    if example != '':
        embed.add_field(name = "**Example**", value = '*' + example.replace('<br/>', '\n').replace('&lt;', '<').replace('&apos;', "'").replace('&quot;', '"').replace('*', '\\*') + '*', inline = False)
        embed.set_footer(text = 'Page 1')
    try:
        message = await ctx.send(embed = embed)
    except:
        await ctx.send(f'No results were found for "{word}".')
        return
    await message.add_reaction('◀')
    if data.find('<a class="word"', pages[0] + 15) != -1:
        await message.add_reaction('▶')
    reactions = ['◀', '▶']
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reactions
    menu = 1
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)
        except:
            return
        if reaction.emoji == '◀' and menu != 1:
            menu -= 1
        elif reaction.emoji == '▶' and data.find('<a class="word"', pages[menu * 2 - 4] + 15) != -1 and result.find('term=') != '':
            menu += 1
        await reaction.remove(ctx.author)
        result = data[data.find('<a class="word"', pages[menu * 2 - 4] + 15 if menu > 1 else 0):data.find('class="contributor"', pages[menu * 2 - 3] + 19 if menu > 1 else 0)]
        if menu * 2 > len(pages):
            pages += [data.find('<a class="word"', pages[menu * 2 - 4] + 15), data.find('class="contributor"', pages[menu * 2 - 3] + 19)]
        meaning = result[result.find('class="meaning"') + 16:result.find('</div>', result.find('class="meaning"'))]
        for i in range(0, meaning.count('<a')):
            meaning = meaning.replace(meaning[meaning.find('<a'):meaning.find('>', meaning.find('<a')) + 1], '').replace('</a>', '')
        example = result[result.find('class="example"') + 16:result.find('</div>', result.find('class="example"'))]
        for i in range(0, example.count('<a')):
            example = example.replace(example[example.find('<a'):example.find('>', example.find('<a')) + 1], '').replace('</a>', '')
        embed = discord.Embed(title = "Definition of " + result[result.find('term=') + 5:result.find('"', result.find('term='))].capitalize().replace('%20', ' '), color = 0x5b5f90)
        embed.add_field(name = "**Definition**", value = meaning.replace('<br/>', '\n').replace('&lt;', '<').replace('&apos;', "'").replace('&quot;', '"'), inline = False)
        if example != '':
            embed.add_field(name = "**Example**", value = '*' + example.replace('<br/>', '\n').replace('&lt;', '<').replace('&apos;', "'").replace('&quot;', '"').replace('*', '\\*') + '*', inline = False)
        embed.set_footer(text = 'Page ' + str(menu))
        try:
            await message.edit(embed = embed)
        except:
            menu -= 1

@client.command(name = "reddit")
async def reddit(ctx, sub = ""):
    if sub == "":
        await ctx.send("You have to choose a subreddit! Example: `_reddit dankmemes`.")
        return
    r = http.request('GET', f'https://www.reddit.com/r/{sub}/new/.json')
    r = r.data.decode('utf8')
    memes = []
    last_i = 0
    for i in range(r.count('https://i.redd.it/')):
        current_i = r.find("https://i.redd.it/", last_i)
        memes.append(r[current_i:r.find('"', current_i)])
        last_i = current_i + 10
    if memes == []:
        await ctx.send(f"No images found in the subreddit {sub}.")
        return
    embed = discord.Embed(title = sub, description = f"<{memes[0]}>", color = 0x5b5f90)
    embed.set_image(url = memes[0])
    if len(memes) == 1:
        await ctx.send(embed = embed)
        return
    embed.set_footer(text = f"Page 1 of {len(memes)}")
    message = await ctx.send(embed = embed)
    await message.add_reaction('◀')
    await message.add_reaction('▶')
    reactions = ['◀', '▶']
    menu = 1
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reactions
    while True:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 60.0, check = check)
        except:
            return
        if reaction.emoji == '◀' and menu > 1:
            menu -= 1
        elif reaction.emoji == '▶' and menu < len(memes):
            menu += 1
        embed = discord.Embed(title = sub, description = f"<{memes[menu - 1]}>", color = 0x5b5f90)
        embed.set_image(url = memes[menu - 1])
        embed.set_footer(text = f"Page {menu} of {len(memes)}")
        await message.edit(embed = embed)
        await reaction.remove(ctx.author)

@client.command(name = 'translate', aliases = ['tl'])
async def translate(ctx, *, arg):
    message, language = arg.rsplit(' ', 1)
    translated_message = translator.translate(message, dest = language)
    await ctx.send(translated_message.text)

@client.command(name = 'define')
async def define(ctx, word):
    r = http.request('GET', 'https://www.merriam-webster.com/dictionary/'+ word)
    data = r.data.decode('utf-8')
    data = '%.3000s' % data
    definition = data[data.find('"description" content="') + 23:]
    definition = definition[:definition.find('"')]
    if definition.count('How to use') > 0 and definition.count('in a sentence.') > 0:
        definition = definition[:definition.find('How to use')]
    if definition == ' lang=' or not definition.count(' definition is - ') > 0:
        await ctx.send(f'The definition of {word} was not found.')
    else:
        await ctx.send(definition)

@client.command(name = 'pun')
async def pun(ctx):
    r = http.request('GET', 'https://www.punoftheday.com/cgi-bin/randompun.pl')
    data = r.data.decode('utf-8')
    data = f'%.{len(data)}s' % data
    pun = data[data.find(r'"dropshadow1"') + 18:]
    pun = pun[:pun.find('</p>')]
    await ctx.send(pun)

@client.command(name = 'pickup')
async def pickup(ctx):
    r = http.request('GET', f'http://www.jokes4us.com/pickuplines/random/pickupline{random.randint(1, 1327)}.html')
    data = f'%.{len(r.data)}s' % r.data
    pickup_line = data[data.find('align=center><font size=5') + 28:]
    pickup_line = pickup_line[:pickup_line.find(r'\n</font></p>\n\n\n<p')]
    pickup_line = pickup_line.encode().decode('utf-8')
    await ctx.send(pickup_line)

@client.command(name = 'xkcd')
async def xkcd(ctx, num = None):
    if num != None:
        try:
            num = int(num)
        except:
            await ctx.send('The comic number must be an integer from 1 to 2295.')
            return
    if num != None and (num > 2295 or num < 1):
        await ctx.send('The comic number must be from 1 to 2295.')
        return
    r = http.request('GET', f'https://xkcd.com/{str(random.randint(1, 2295)) if num == None else num}/')
    data = f'%.{len(r.data)}s' % r.data
    comic = data[data.find('(for hotlinking/embedding):') + 28:]
    comic = comic[:comic.find(r'\n\n')]
    await ctx.send(comic)

@client.command(name = 'quote')
async def quote(ctx):
    r = http.request('GET', f'https://www.goodreads.com/quotes/tag/inspirational?page={str(random.randint(1, 100))}')
    data = f'%.{len(r.data)}s' % r.data
    data = data[data.find(r'quoteText">\n      &ldquo;') + 26:data.rfind(r'\n  </span>\n    <span id=quote_book_link_')]
    data = data[random.randint(0, 4):]
    quote = data[data.find(r'quoteText">\n      &ldquo;') + 26:]
    quote = quote[:quote.find(r'\n  </span>\n    <span id=quote_book_link_')]
    quote = quote.replace(r'&rdquo;\n  <br>  &#8213;\n  <span class="authorOrTitle">\n    ', '\n -').encode('utf-8').decode('utf-8')
    quote = quote[:quote.find(r'\n')]
    quote = quote.replace('<br />', '\n').replace(r'\xe2\x80\x99', "'")
    await ctx.send(quote)

playing_anagram = []

@client.command(name = 'anagram', aliases = ['ag'])
async def anagram(ctx, bet = '0'):
    try:
        float(bet)
    except:
        await ctx.send('Your bet must be a number.')
        return
    if float(bet) < 0.:
        await ctx.send('Your bet must be a positive number.')
        return
    if float(bet) != round(float(bet), 2):
        await ctx.send('Your bet cannot go past 2 decimal places.')
        return
    if float(bet) > (await get_balance(ctx.author.id)):
        await ctx.send("You don't have that much money! You have {} credits.".format(await get_balance(ctx.author.id)))
        return
    global playing_anagram
    if ctx.author.id in playing_anagram:
        await ctx.send("You're already playing anagram! Finish the game or wait 5 minutes to start a new game.")
        return
    playing_anagram += [ctx.author.id]
    await update_balance(ctx.author.id, -float(bet))
    definition = ' lang='
    word = ''
    while definition == ' lang=' or not definition.count(' definition is - ') > 0:
        r = http.request('GET', 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain')
        rand_num = random.randint(0, 209777)
        word_data = r.data.decode()[rand_num:rand_num + 100]
        word = word_data[word_data.find('\n') + 1:word_data.find('\n', word_data.find('\n') + 2)]
        r = http.request('GET', 'https://www.merriam-webster.com/dictionary/{}'.format(word))
        data = r.data.decode('utf-8')
        data = '%.3000s' % data
        definition = data[data.find('"description" content="') + 23:]
        definition = definition[:definition.find('"')]
        if definition.count('How to use') > 0 and definition.count('in a sentence.') > 0:
            definition = definition[:definition.find('How to use')]
    letter_list = list(word.lower())
    scrambled_word = ''
    for i in range(0, len(word)):
        scrambled_word += letter_list.pop(random.randint(0, len(letter_list) - 1))
    guesses_list = []
    guesses = ''
    lives = 3
    lives_message = '❤ ❤ ❤ '
    title = 'Anagram | ' + ctx.author.display_name
    footer = 'Say +cat to guess the word cat.'
    embed = discord.Embed(title = title, description = "Let's play anagram! Try to unscramble this word.", color = 0x23272a)
    embed.add_field(name = "**Anagram**", value = scrambled_word, inline = False)
    embed.add_field(name = "**Lives**", value = lives_message, inline = False)
    embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
    await ctx.send(embed = embed)
    def check(m):
        return m.content.startswith('+') and m.channel == ctx.channel and m.author == ctx.author and len(m.content) > 1
    while True:
        try:
            guess = await client.wait_for('message', timeout = 300.0, check = check)
        except:
            await ctx.send("5 minute timer: {}'s game has ended.".format(ctx.author.mention))
            playing_anagram.remove(ctx.author.id)
            return
        if guess.content[1:].lower() == word.lower():
            await update_balance(ctx.author.id, float(bet) * 2)
            embed = discord.Embed(title = title, description = 'You won!' if bet == '0' else f'You won {bet} credits!', color = 0x00ff00)
            embed.add_field(name = "**Word**", value = word, inline = False)
            embed.add_field(name = "**Definition**", value = definition, inline = False)
            embed.add_field(name = "**Lives**", value = lives_message, inline = False)
            await ctx.send(embed = embed)
            playing_anagram.remove(ctx.author.id)
            return
        if guess.content[1:].lower() in guesses_list:
            embed = discord.Embed(title = title, description = "You already guessed that!", color = 0x23272a)
            embed.add_field(name = "**Anagram**", value = scrambled_word, inline = False)
            embed.add_field(name = "**Guesses**", value = guesses, inline = False)
            embed.add_field(name = "**Lives**", value = lives_message, inline = False)
            embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
            await ctx.send(embed = embed)
        else:
            lives -= 1
            lives_message = ''
            for i in range(0, 3):
                if lives > i:
                    lives_message += '❤ '
                else:
                    lives_message += '❌ '
            if lives < 1:
                embed = discord.Embed(title = title, description = 'You lost.' if bet == '0' else f'You lost {bet} credits.', color = 0xff0000)
                embed.add_field(name = "**Word**", value = word, inline = False)
                embed.add_field(name = "**Definition**", value = definition, inline = False)
                embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                await ctx.send(embed = embed)
                playing_anagram.remove(ctx.author.id)
                return
            guesses_list += [guess.content[1:].lower()]
            if guesses == '':
                guesses += guess.content[1:].lower()
            else:
                guesses += ', ' + guess.content[1:]
            embed = discord.Embed(title = title, description = "Oops! That's not the word!", color = 0xff0000)
            embed.add_field(name = "**Anagram**", value = scrambled_word, inline = False)
            if guesses != '':
                embed.add_field(name = "**Guesses**", value = guesses, inline = False)
            embed.add_field(name = "**Lives**", value = lives_message, inline = False)
            embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
            await ctx.send(embed = embed)

@client.command(name = 'blackjack', aliases = ['bj'])
async def blackjack(ctx):
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['♠', '♣', '♥', '♦']
    deck = []
    for t in range(0, 8):
        for i in range(0, len(suits)):
            for x in range(0, len(values)):
                deck += [values[x] + suits[i]]
    playershand = [deck.pop(random.randint(0, len(deck))), deck.pop(random.randint(0, len(deck)))]
    reactions = ['👏', '👐', '✌', '👋'] if playershand[0] == playershand[1] else ['👏', '✌', '👋']
    dealershand = deck.pop(random.randint(0, len(deck)))
    title = 'Blackjack | ' + ctx.author.display_name
    description = "Let's play blackjack!"
    footer = "Click 👏 to hit.\nClick 👐 to split.\nClick ✌ to double down.\nClick 👋 to stand." if '👐' in reactions else "Click 👏 to hit.\nClick ✌ to double down.\nClick 👋 to stand."
    def sumcards(cards):
        sum = 0
        for i in cards:
            if i[:-1] in ['J', 'Q', 'K']:
                sum += 10
            elif i[:-1] == 'A':
                if 11 in cards:
                    sum += 1
                else:
                    sum += 11
            else:
                sum += int(i[:-1])
        return sum
    ret = False
    while True:
        playersum = []
        for i in playershand:
            if i[:-1] in ['J', 'Q', 'K']:
                playersum += [10]
            elif i[:-1] == 'A':
                if 11 in playersum:
                    playersum += [1]
                else:
                    playersum += [11]
            else:
                playersum += [int(i[:-1])]
        sum = sumcards(playershand)
        if sum > 21:
            dealershand = [dealershand]
            dealertotal = 0
            while dealertotal < 17:
                dealershand += [deck.pop(random.randint(0, len(deck)))]
                dealertotal = sumcards(dealershand)
            if dealertotal > 21:
                await ctx.send('again im lazy')
                return
            embed = discord.Embed(title = title, description = "ha you lose", color = 0xff0000)
            embed.add_field(name = "**Your hand**", value = '   '.join(playershand) + '\nValue: ' + str(sum), inline = True)
            embed.add_field(name = '\u200b', value = '\u200b', inline = True)
            embed.add_field(name = "**Dealer's hand**", value = '   '.join(dealershand) + '\nValue: ' + str(sumcards(dealershand)), inline = True)
            await ctx.send(embed = embed)
            return
        elif sum == 21:
            await ctx.send('i think you won but im lazy')
            return
        elif ret == True:
            dealershand = [dealershand]
            dealertotal = 0
            while dealertotal < 17:
                dealershand += [deck.pop(random.randint(0, len(deck)))]
                dealertotal = sumcards(dealershand)
            if dealertotal > 21 or sum > dealertotal:
                embed = discord.Embed(title = title, description = 'You win yay', color = 0x00ff00)
                embed.add_field(name = "**Your hand**", value = '   '.join(playershand) + '\nValue: ' + str(sum), inline = True)
                embed.add_field(name = '\u200b', value = '\u200b', inline = True)
                embed.add_field(name = "**Dealer's hand**", value = '   '.join(dealershand) + '\nValue: ' + str(sumcards(dealershand)), inline = True)
                await ctx.send(embed = embed)
                return
            elif sum == dealertotal:
                embed = discord.Embed(title = title, description = description, color = 0x23272a)
                embed.add_field(name = "**Your hand**", value = '   '.join(playershand) + '\nValue: ' + str(sum), inline = True)
                embed.add_field(name = '\u200b', value = '\u200b', inline = True)
                embed.add_field(name = "**Dealer's hand**", value = '   '.join(dealershand) + '\nValue: ' + str(sumcards(dealershand)), inline = True)
                await ctx.send(embed = embed)
                return
            embed = discord.Embed(title = title, description = "ha you lose", color = 0xff0000)
            embed.add_field(name = "**Your hand**", value = '   '.join(playershand) + '\nValue: ' + str(sum), inline = True)
            embed.add_field(name = '\u200b', value = '\u200b', inline = True)
            embed.add_field(name = "**Dealer's hand**", value = '   '.join(dealershand) + '\nValue: ' + str(sumcards(dealershand)), inline = True)
            await ctx.send(embed = embed)
            return
        embed = discord.Embed(title = title, description = description, color = 0x23272a)
        embed.add_field(name = "**Your hand**", value = '   '.join(playershand) + '\nValue: ' + str(sum), inline = True)
        embed.add_field(name = '\u200b', value = '\u200b', inline = True)
        embed.add_field(name = "**Dealer's hand**", value = dealershand + '   XX', inline = True)
        embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
        message = await ctx.send(embed = embed)
        for i in reactions:
            await message.add_reaction(i)
        def check(reaction, user):
            if playershand[0] == playershand[1]:
                return user == ctx.author and (str(reaction.emoji) == '👏' or str(reaction.emoji) == '✌' or str(reaction.emoji) == '👋')
            else:
                return user == ctx.author and (str(reaction.emoji) == '👏' or str(reaction.emoji) == '✌' or str(reaction.emoji) == '👋' or str(reaction.emoji) == '👐')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 300.0, check = check)
        except:
            await ctx.send(f'5 minute timer: {ctx.author.mention}\'s game has ended.')
            return
        if reaction.emoji == '👏':
            playershand += [deck.pop(random.randint(0, len(deck)))]
            description = "Cards left: " + str(len(deck))
        elif reaction.emoji == '👋':
            ret = True
        elif reaction.emoji == '✌':
            playershand += [deck.pop(random.randint(0, len(deck)))]
            ret = True
        elif reaction.emoji == '👐' and 'check' == 'check':
            print('split hand')
            print('draw 2')
        footer = "Click 👏 to hit.\nClick ✌ to double down.\nClick 👋 to stand."

playing_hangman = []
channels_hangman_open = []

@client.command(name = 'hangman', aliases = ['hm'])
async def hangman(ctx, bet = '0', open = None):
    try:
        float(bet)
    except:
        await ctx.send('Your bet must be a number.')
        return
    if float(bet) < 0.:
        await ctx.send('Your bet must be a positive number.')
        return
    if float(bet) != round(float(bet), 2):
        await ctx.send('Your bet cannot go past 2 decimal places.')
        return
    if float(bet) > (await get_balance(ctx.author.id)):
        await ctx.send("You don't have that much money! You have {} credits.".format(await get_balance(ctx.author.id)))
        return
    if open == 'open':
        open = True
    else:
        open = False
    global playing_hangman
    if ctx.author.id in playing_hangman:
        await ctx.send("You're already playing hangman! Finish the game or wait 5 minutes to start a new game.")
        return
    playing_hangman += [ctx.author.id]
    global channels_hangman_open
    if ctx.channel.id in channels_hangman_open and open:
        await ctx.send("There's already an open game in this channel.")
        return
    if open:
        channels_hangman_open += [ctx.channel.id]
    await update_balance(ctx.author.id, -float(bet))
    definition = ' lang='
    word = ''
    while definition == ' lang=' or not definition.count(' definition is - ') > 0:
        r = http.request('GET', 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain')
        rand_num = random.randint(0, 209777)
        word_data = r.data.decode()[rand_num:rand_num + 100]
        word = word_data[word_data.find('\n') + 1:word_data.find('\n', word_data.find('\n') + 2)]
        r = http.request('GET', 'https://www.merriam-webster.com/dictionary/{}'.format(word))
        data = r.data.decode('utf-8')
        data = '%.3000s' % data
        definition = data[data.find('"description" content="') + 23:]
        definition = definition[:definition.find('"')]
        if definition.count('How to use') > 0 and definition.count('in a sentence.') > 0:
            definition = definition[:definition.find('How to use')]
    word = word.lower()
    temporary_word = word
    word_message = ' '
    for x in word:
        if x.isalpha():
            word_message += '# '
        else:
            word_message += x + ' '
    title_more = ""
    if open:
        title = "Hangman | " + ctx.author.display_name + " | Open"
        footer = "Say -c to guess the letter c.\nSay -cat to guess the word cat."
        title_more = "\nThis is an *open* game. To play, see bottom."
    else:
        title = "Hangman | " + ctx.author.display_name
        footer = "Say +c to guess the letter c.\nSay +cat to guess the word cat."
    lives = 10
    lives_message = '❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ ❤ '
    embed = discord.Embed(title = title, description = "Let's play hangman! Here's your word." + title_more, color = 0x23272a)
    embed.add_field(name = "**Word**", value = word_message, inline = False)
    embed.add_field(name = "**Lives**", value = lives_message, inline = False)
    embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
    await ctx.send(embed = embed)
    result = ''
    for i in range(0, len(word)):
        result += '#'
    letters_guessed = ''
    if float(bet) > 0.:
        won_game_msg = f'You won **{bet}** credits!'
        lost_game_msg = f'You lost **{bet}** credits.'
    else:
        won_game_msg = 'You won!'
        lost_game_msg = 'You lost.'
    def check(m):
        if open:
            return m.content.startswith('-') and m.channel == ctx.channel and len(m.content) > 1
        else:
            return m.content.startswith('+') and m.channel == ctx.channel and m.author == ctx.author and len(m.content) > 1
    while True:
        try:
            guess = await client.wait_for('message', timeout = 300.0, check = check)
        except:
            await ctx.send("5 minute timer: {}'s game has ended.".format(ctx.author.mention))
            playing_hangman.remove(ctx.author.id)
            if open:
                channels_hangman_open.remove(ctx.channel.id)
            return
        else:
            content = guess.content.strip()
            if len(content) == 2:
                letter = content[1].lower()
                if letter in letters_guessed:
                    embed = discord.Embed(title = title, description = "You already guessed that!", color = 0x23272a)
                    embed.add_field(name = "**Word**", value = word_message, inline = False)
                    embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                    embed.add_field(name = "**Letters Guessed**", value = letters_guessed, inline = False)
                    embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
                    await ctx.send(embed = embed)
                elif letter in word:
                    if letters_guessed == '':
                        letters_guessed += letter
                    else:
                        letters_guessed += ', ' + letter
                    for f in range(0, word.count(letter)):
                        word_message = word_message[:(2 * temporary_word.find(letter)) + 1] + letter + word_message[2 * temporary_word.find(letter) + 2:]
                        temporary_word = temporary_word.replace(letter, '#', 1)
                    if temporary_word == result:
                        embed = discord.Embed(title = title, description = won_game_msg, color = 0x00ff00)
                        embed.add_field(name = "**Word**", value = word_message, inline = False)
                        embed.add_field(name = "**Definition**", value = definition, inline = False)
                        embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                        await update_balance(ctx.author.id, float(bet) * 2)
                        await ctx.send(embed = embed)
                        playing_hangman.remove(ctx.author.id)
                        if open:
                            channels_hangman_open.remove(ctx.channel.id)
                        return
                    embed = discord.Embed(title = title, description = f"Nice guess! Letter `{letter}` is in the word.", color = 0x00ff00)
                    embed.add_field(name = "**Word**", value = word_message, inline = False)
                    embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                    embed.add_field(name = "**Letters Guessed**", value = letters_guessed, inline = False)
                    embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
                    await ctx.send(embed = embed)
                else:
                    if letters_guessed == '':
                        letters_guessed += letter
                    else:
                        letters_guessed += ', ' + letter
                    lives -= 1
                    lives_message = ''
                    for e in range(0, 10):
                        if lives > e:
                            lives_message += '❤ '
                        else:
                            lives_message += '❌ '
                    if lives < 1:
                        word_message = ''
                        for x in range(0, len(word)):
                            word_message += word[x] + ' '
                        embed = discord.Embed(title = title, description = lost_game_msg, color = 0xff0000)
                        embed.add_field(name = "**Word**", value = word_message, inline = False)
                        embed.add_field(name = "**Definition**", value = definition, inline = False)
                        embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                        await ctx.send(embed = embed)
                        playing_hangman.remove(ctx.author.id)
                        if open:
                            channels_hangman_open.remove(ctx.channel.id)
                        return
                    embed = discord.Embed(title = title, description = f"Oops! Letter `{letter}` is not in the word.", color = 0xff0000)
                    embed.add_field(name = "**Word**", value = word_message, inline = False)
                    embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                    embed.add_field(name = "**Letters Guessed**", value = letters_guessed, inline = False)
                    embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
                    await ctx.send(embed = embed)
            else:
                if word == content[1:]:
                    word_message = ''
                    for t in range(0, len(word)):
                        word_message += word[t] + ' '
                    embed = discord.Embed(title = title, description = won_game_msg, color = 0x00ff00)
                    embed.add_field(name = "**Word**", value = word_message, inline = False)
                    embed.add_field(name = "**Definition**", value = definition, inline = False)
                    embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                    await update_balance(ctx.author.id, float(bet) * 2)
                    await ctx.send(embed = embed)
                    playing_hangman.remove(ctx.author.id)
                    if open:
                        channels_hangman_open.remove(ctx.channel.id)
                    return
                lives -= 1
                lives_message = ''
                for e in range(0, 10):
                    if lives > e:
                        lives_message += '❤ '
                    else:
                        lives_message += '❌ '
                if lives < 1:
                    word_message = ''
                    for x in range(0, len(word)):
                        word_message += word[x] + ' '
                    embed = discord.Embed(title = title, description = lost_game_msg, color = 0xff0000)
                    embed.add_field(name = "**Word**", value = word_message, inline = False)
                    embed.add_field(name = "**Definition**", value = definition, inline = False)
                    embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                    await ctx.send(embed = embed)
                    playing_hangman.remove(ctx.author.id)
                    if open:
                        channels_hangman_open.remove(ctx.channel.id)
                    return
                embed = discord.Embed(title = title, description = "Oops! That's not the word!", color = 0xff0000)
                embed.add_field(name = "**Word**", value = word_message, inline = False)
                embed.add_field(name = "**Lives**", value = lives_message, inline = False)
                if letters_guessed != '':
                    embed.add_field(name = "**Letters Guessed**", value = letters_guessed, inline = False)
                embed.set_footer(text = footer, icon_url = 'https://cdn2.iconfinder.com/data/icons/app-types-in-grey/512/info_512pxGREY.png')
                await ctx.send(embed = embed)

@client.command(name = "stocks")
async def stocks(ctx, stock):
    await ctx.send(getQuotes(stock))
    #await ctx.send(yf.Ticker(stock).info)

@client.command(name = 'give')
async def give(ctx, member : discord.Member, amount):
    amount = float(amount)
    if amount > (await get_balance(ctx.author.id)):
        await ctx.send("You don't have that many credits!")
        return
    if amount < 0.:
        await ctx.send("You can't steal credits. Nice try though.")
        return
    if round(amount * 100) != amount * 100:
        await ctx.send("You can only give credits to up to two decimal places.")
        return
    await update_balance(ctx.author.id, -amount)
    await update_balance(member.id, amount)
    await ctx.send("{} gave {} **{}** credits!".format(ctx.author.mention, member.mention, str(amount)))

@client.command(name = 'invite')
async def invite(ctx):
    await ctx.send("Use this link to invite me to your server!\n<https://cutt.ly/otsu>")

@client.command(name = 'daily')
@commands.cooldown(1, 43200, commands.BucketType.user)
async def daily(ctx):
    await update_balance(ctx.author.id, 500)
    await ctx.send("You have been awarded your daily **500** credits.")

@client.command(name = 'rob', aliases = ['steal'])
@commands.cooldown(1, 180, commands.BucketType.user)
async def rob(ctx, member = ''):
    if member == '':
        await ctx.send('You have to enter a valid member.')
        return
    membertry = ctx.guild.get_member(int(member[3:-1]))
    if membertry is None:
        membertry = ctx.guild.get_member(int(member[2:-1]))
        if membertry is None:
            await ctx.send('You have to enter a valid member.')
            return
    member = membertry
    memberbal = await get_balance(member.id)
    if memberbal < 250:
        await ctx.send(member.display_name + ' doesn\'t have 250 credits on hand.  I\'s not worth it.')
        return
    if random.randint(0, 100) > 60:
        randnum = random.randint(round(memberbal / 10), round(memberbal / 5))
        await update_balance(ctx.author.id, randnum)
        await update_balance(member.id, - randnum)
        await ctx.send(f'{ctx.author.mention} stole {str(randnum)} credits from {member.mention}!')
    else:
        await update_balance(ctx.author.id, - 250)
        await update_balance(member.id, 250)
        await ctx.send(f'{ctx.author.mention} failed at stealing from {member.mention} and had to pay them 250 credits!')

@client.command(name = 'say')
@commands.is_owner()
async def say(ctx, *, msg):
    await ctx.send(msg)

@client.command(name = 'edit')
@commands.is_owner()
async def edit(ctx, id, *, content):
    channel, og_message = await get_data()
    msg = await channel.fetch_message(id)
    await msg.edit(content = content)

client.run('INSERT BOT TOKEN')
