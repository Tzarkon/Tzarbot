# Tzarbot.py

import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

description = "Tzar tzar tzar bot!"

intents = discord.Intents.all()
#intents.members = True
#intents.message_content = True
#intents.reactions = True

tzarbot = commands.Bot(command_prefix = '!', description = description, intents = intents)


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")



@tzarbot.event
async def on_ready():
    print(f'{tzarbot.user} has connected to Discord!')

#This code interacts with Palico.bot when a user reacts to another users message.
@tzarbot.event
async def on_reaction_add(reaction,user):
            
    if user.bot:
        return
    if reaction.message.author == user:
        await reaction.message.channel.send(user.name + " is a little self absorbed!")
        return
    dude = str(reaction.message.author.id)
    if reaction.message.author.bot:
        return
    await reaction.message.channel.send("deposit " + dude + " 5")

#Tzarbot reactions to various content in messages.
@tzarbot.listen()
async def on_message(message):
    
    if message.author.bot:
        return
    
    if "wtf" in message.content.lower():
#        response = "FTW! ...  <Sips Tea> ..."
        response = "\u16A0\u16CF\u16A5! ... <\u16CB\u16C1\u16C8\u16CB \u16CF\u16E0> ..."
        await message.reply(response)
        
    if "Tzarbot Balance?" in message.content:
        response = "Pbank balance"
        await message.channel.send(response)

    if "lol" in message.content.lower():
        response = "\N{FACE WITH TEARS OF JOY}"
        await message.add_reaction(response)
        await message.reply('\u16BB\u16AB\u16C8\u16E0\u16BE\u16D6\u16CB')

    if "<DOH!>" in message.content:
        with open('doh.txt', 'r') as f:
            bot_choice = []
            for line in f:
                line = line.strip()
                bot_choice.append(line)    
        response = random.choice(bot_choice)
        await message.reply(response)

    if "sheesh" in message.content.lower():
        with open('sheesh.txt', 'r') as fee:
            bot_say = []
            for line in fee:
                line = line.strip()
                bot_say.append(line)       
        response = random.choice(bot_say)
        await message.reply(response)

    if "thanks tzarbot" in message.content.lower() and message.author.name == 'tzarquon' or "thank you tzarbot" in message.content.lower() and message.author.name == 'tzarquon':
        await message.reply("No worries Master, my only wish is to serve you. . . Bhuwa ha ha ha!")
    elif "thanks tzarbot" in message.content.lower() or "thank you tzarbot" in message.content.lower():
        await message.reply("You're Welcome! . . . Now, Bug Off!")
    elif "tzarbot" in message.content.lower() and message.author.name == "tzarquon":
        await message.reply("Yes Master . . . Bhuwa ha ha ha!")
    else:
        if "tzarbot" in message.content.lower():
            await message.reply("Bug Off! . . . I'm tryin' ta sleep here!")

        

@tzarbot.command()
async def roll(ctx, dice: str = commands.parameter(default="None", description='''dice should be input in an NdN format. Number of dice then Number of faces on the die''')):
    """Rolls a dice in NdN format. This function was copied from basicbot.py by GoogleGenius and jontobonto at https://github.com/Rapptz/discord.py/blob/master/examples/basic_bot.py, with an MIT license."""
    
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.reply(result)


@tzarbot.command()
async def ching(ctx):
    '''Gets an I ching hexagram. A * at the end of a line indicates a significant line in the hexagram. Reasonable interpretations can be received at https://www.iching-online.com/hexagrams/.
The interpretations on that site are based on the Wilhelm/Baynes translation for Chinese to German to English and is considered the formost translation of the Chinese.'''
    
    
    ching_lines = {1:'- -*',2:'---',3:'- -',4:'---',5:'- -',6:'---',7:'- -',8:'---'}

    hexagrams = { ('---','---','---','---','---','---'):'1,Creative',('- -','- -','- -','- -','- -','- -'):'2, Receptive',('- -','---','- -','- -','- -','---'):'3, Difficulty',('---','- -','- -','- -','---','- -'):'4, Folly',
                  ('- -','---','- -','---','---','---'):'5, Waiting',('---','---','---','- -','---','- -'):'6, Conflict',('- -','- -','- -','- -','---','- -'):'7, Army',('- -','---','- -','- -','- -','- -'):'8, Union',
                  ('---','---','- -','---','---','---'):'9, Taming',('---','---','---','- -','---','---'):'10, Treading',('- -','- -','- -','---','---','---'):'11, Peace',('---','---','---','- -','- -','- -'):'12, Standstill',
                  ('---','---','---','---','- -','---'):'13, Fellowship',('---','- -','---','---','---','---'):'14, Possession',('- -','- -','- -','---','- -','- -'):'15, Modesty',('- -','- -','---','- -','- -','- -'):'16, Enthusiasm',
                  ('- -','---','---','- -','- -','---'):'17, Following',('---','- -','- -','---','---','- -'):'18, Decay',('- -','- -','- -','- -','---','---'):'19, Approach',('---','---','- -','- -','- -','- -'):'20, View',
                  ('---','- -','---','- -','- -','---'):'21, Biting',('---','- -','- -','---','- -','---'):'22, Grace',('---','- -','- -','- -','- -','- -'):'23, Splitting',('- -','- -','- -','- -','- -','---'):'24, Return',
                  ('---','---','---','- -','- -','---'):'25, Innocence',('---','- -','- -','---','---','---'):'26, Taming',('---','- -','- -','- -','- -','---'):'27, Mouth',('- -','---','---','---','---','- -'):'28, Preponderance',
                  ('- -','---','- -','- -','---','- -'):'29, Abysmal',('---','- -','---','---','- -','---'):'30, Clinging',('- -','---','---','---','- -','- -'):'31, Influence',('- -','- -','---','---','---','- -'):'32, Duration',
                  ('---','---','---','---','- -','- -'):'33, Retreat',('- -','- -','---','---','---','---'):'34, Power',('---','- -','---','- -','- -','- -'):'35, Progress',('- -','- -','- -','---','- -','---'):'36, Darkening',
                  ('---','---','- -','---','- -','---'):'37, Family',('---','- -','---','- -','---','---'):'38, Opposition',('- -','---','- -','---','- -','- -'):'39, Obstruction',('- -','- -','---','- -','---','- -'):'40, Deliverance',
                  ('---','- -','- -','- -','---','---'):'41, Decrease',('---','---','- -','- -','- -','---'):'42, Increase',('- -','---','---','---','---','---'):'43, Resoluteness',('---','---','---','---','---','- -'):'44, Coming',
                  ('- -','---','---','- -','- -','- -'):'45, Gathering',('- -','- -','- -','---','---','- -'):'46, Pushing',('- -','---','---','- -','---','- -'):'47, Oppression',('- -','---','- -','---','---','- -'):'48, Well',
                  ('- -','---','---','---','- -','---'):'49, Revolution',('---','- -','---','---','---','- -'):'50, Caldron',('- -','- -','---','- -','- -','---'):'51, Arousing',('---','- -','- -','---','- -','- -'):'52, Still',
                  ('---','---','- -','---','- -','- -'):'53, Development',('- -','- -','---','- -','---','---'):'54, Marrying',('- -','- -','---','---','- -','---'):'55, Abundance',('---','- -','---','---','- -','- -'):'56, Wanderer',
                  ('---','---','- -','---','---','- -'):'57, Gentle',('- -','---','---','- -','---','---'):'58, Joyous',('---','---','- -','- -','---','- -'):'59, Dispersion',('- -','---','- -','- -','---','---'):'60, Limitation',
                  ('---','---','- -','- -','---','---'):'61, Truth',('- -','- -','---','---','- -','- -'):'62, Small',('- -','---','- -','---','- -','---'):'63, After',('---','- -','---','- -','---','- -'):'64, Before',}
    
    list_lines1 = []
    for i in range(6):
        oneline = random.randint(1, 8)
        list_lines1.append(ching_lines[oneline])
    list_lines2 = list_lines1[::-1]
    hex_lines = []
    lineohex = ""
    for line in list_lines2:
        if line == "---*":
            lineohex = "---"
            hex_lines.append(lineohex)
        elif line == "- -*":
            lineohex = "- -"
            hex_lines.append(lineohex)
        else:
            lineohex = line
            hex_lines.append(lineohex)
        
    await ctx.reply('​'+list_lines1[5]+"\n"+'​'+list_lines1[4]+"\n"+'​'+list_lines1[3]+"\n"+'​'+list_lines1[2]+"\n"+'​'+list_lines1[1]+"\n"+'​'+list_lines1[0] + ', ' + hexagrams[tuple(hex_lines)])


@tzarbot.command()
async def rune(ctx, letter = commands.parameter(default="None", description="""An English letter or letter combination that can be turned into a rune by its sound.""")):
    '''Turns letters and some letter combinations into their Anglo-Saxon rune. Unicode can be found at https://en.wikipedia.org/wiki/Runic_(Unicode_block).'''
    
    rune_ucode = {'f':'\u16A0', 'u':'\u16A2', 'th':'\u16A6', 'o':'\u16A9', 'r':'\u16B1', 'c':'\u16B3', 'ge':'\u16B7',
                  'w':'\u16B9', 'h':'\u16BB', 'n':'\u16BE', 'i':'\u16C1', 'j':'\u16C4', 'eo':'\u16C7', 'p':'\u16C8',
                  'x':'\u16C9', 's':'\u16CB', 't':'\u16CF', 'b':'\u16D2', 'e':'\u16D6', 'm':'\u16D7', 'l':'\u16DA',
                  'ng':'\u16DD', 'oe':'\u16DF', 'd':'\u16DE', 'a':'\u16AA', 'ae':'\u16AB', 'y':'\u16A3', 'ie':'\u16E1',
                  'ea':'\u16E0', 'q':'\u16E2', 'k':'\u16E3', 'st':'\u16E5', 'ga':'\u16B8','v':'\u16C8\u16BB'}
    rune_list = ('f','u','th','o','r','c', 'ge', 'w', 'h', 'n', 'i', 'j', 'eo', 'p', 'x', 's', 't', 'b', 'e', 'm', 'l',
                 'ng', 'oe', 'd', 'a', 'ae', 'y', 'ie','ea','q','k','st','ga','v')
    if letter in rune_list:
        await ctx.reply(rune_ucode[str(letter)])


@tzarbot.command()
async def runify(ctx, *, text = commands.parameter(default="None", description= '''A block of English text to be translated into runes''')):
    '''Turns text into Anglo-Saxon runes for English words. Reasonable approximation for most words. The original is called Rune-Scribe by RollsW, at https://github.com/RollsW/Rune-Scribe, using a GPL V3.0 license.'''
    
    runic_dict = {
    "ing": "\u16DD", "ae": "\u16AB", "th": "\u16A6", "ea": "\u16E0", "ia": "\u16E1", "io": "\u16E1", "oe": "\u16DF", "st":"\u16E5",
    "ee": "\u16E0",  "gh": "\u16B8", "ch": "\u16E4", "sh":"\u16F2", "oo":"\u16F3", "a": "\u16AA", "b": "\u16D2", "c": "\u16B3", "d": "\u16DE",
    "e": "\u16D6", "f": "\u16A0", "g": "\u16B7", "h": "\u16BB", "i": "\u16C1", "j": "\u16C4", "k": "\u16F1", "l": "\u16DA",
    "m": "\u16D7", "n": "\u16BE", "o": "\u16A9", "p": "\u16C8", "q": "\u16E2", "r": "\u16B1", "s": "\u16CB", "t": "\u16CF",
    "u": "\u16A2", "v":"\u16C8\u16BB",
    #v":"\u16A2", "v": "\u16A1",   medieval version
    "w": "\u16B9", "x": "\u16C9", "y": "\u16A3", "z": "\u16CE", " ": "\u16EB", ",\u16EB": " \u16EC ", ";\u16EB": " \u16EC ",
    ":\u16EB": " \u16EC ", ".\u16EB": " \u16ED ", "?\u16EB": " \u16ED ", "!\u16EB": " \u16ED ", "'\u16EB": " \u16EB ", "'": " \u16EB ",
    ",": " \u16EC ", ";": " \u16EC ", ":": " \u16EC ", ".": " \u16ED ", "?": " \u16ED ", "!": " \u16ED ", '"': "",
    }

    text = text.lower()
    for k,v in runic_dict.items():
        text = text.replace(k, v)
    await ctx.reply(text)

@tzarbot.command()
async def unru(ctx, *, rune = commands.parameter(default="None", description= '''A block of runes to be translated into English''')):
    '''Turns Anglo-Saxon runes into their English equivalents.'''

    eng_dict = { '\u16C8\u16BB':'v','\u16DD':'ing','\u16AB':'ae','\u16A6':'th','\u16E0':'ea','\u16E1':'ia','\u16E1':'io','\u16DF':'oe',
                 '\u16E5':'st','\u16E0':'ee', '\u16D8':'gh','\u16E4':'ch','\u16F2':'sh','\u16F3':'oo','\u16AA':'a','\u16D2':'b',
                 '\u16B3':'c','\u16DE':'d','\u16D6':'e','\u16A0':'f','\u16B7':'g','\u16BB':'h','\u16C1':'i','\u16C4':'j','\u16F1':'k',
                 '\u16DA':'l','\u16D7':'m','\u16BE':'n','\u16A9':'o','\u16C8':'p','\u16E2':'q','\u16B1':'r','\u16CB':'s','\u16CF':'t',
                 '\u16A2':'u','\u16B9':'w','\u16C9':'x','\u16A3':'y','\u16CE':'z','\u16EB':' ','\u16EC':':','\u16ED':'?'}
    
    for k,v in eng_dict.items():
        rune = rune.replace(k,v)
    await ctx.reply(rune)

tzarbot.run(TOKEN)

