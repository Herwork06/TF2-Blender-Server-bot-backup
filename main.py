import discord
import os
import random
from keepalive import keep_alive

client = discord.Client()
bot = discord.Bot()
myid = [
  '<@1009171722601246750>'
]

#Interactions

#Word lists
d4_words = [
  "!roll a d4",
  "!roll d4",
] 

d6_words = [
  "!roll a d6",
  "!roll d6",
]

d8_words = [
  "!roll a d8",
  "!roll d8",
]

d10_words = [
  "!roll a d10",
  "!roll d10",
]

d12_words = [
  "!roll a d12",
  "!roll d12",
]

d20_words = [
  "!roll a d20",
  "!roll d20",
]

coin_words = [
  "!coinflip",
  "!coin flip",
  "!flip a coin",
]

collection_words = [
  "!props",
  "!hats",
  "!weapons",
]

spy_words = [
  "!spy",
  "!spyware",
  "!espion",
  "!espionrepacker",
]

#Responses
filmic = [
  "https://media.discordapp.net/attachments/626911954375540748/1008157957093077012/caption.gif",
  "https://media.discordapp.net/attachments/626911954375540748/999075033383186482/FILMIC_.gif",
  "https://cdn.discordapp.com/attachments/723010093033062540/1009189495033315369/caption-2.gif",
  "https://cdn.discordapp.com/attachments/761155438749810688/1010950045220225054/meme2.gif",
]

standard = [
  "https://cdn.discordapp.com/attachments/626911954375540748/1009191135765352632/caption.gif",
]

slander = [
  "https://media.discordapp.net/attachments/626911954375540748/1008113640571932732/meme.gif",
]

started = [
  "!letsgetitstarted",
  "!getmestarted",
  "!getstarted",
  "!started"
]

coin_flip = [
  "You flipped **tails**",
  "You flipped **heads**",
]

d4 = [
   "You rolled a *1*",
  "You rolled a **2**",
  "You rolled a **3**",
  "You rolled a ***4***",
]

d6 = [
  "You rolled a *1*",
  "You rolled a **2**",
  "You rolled a **3**",
  "You rolled a **4**",
  "You rolled a **5**",
  "You rolled a ***6***",
]

d8 = [
  "You rolled a *1*",
  "You rolled a **2**",
  "You rolled a **3**",
  "You rolled a **4**",
  "You rolled a **5**",
  "You rolled a **6**",
  "You rolled a **7**",
  "You rolled a ***8***",
]

d10 = [
  "You rolled a *1*",
  "You rolled a **2**",
  "You rolled a **3**",
  "You rolled a **4**",
  "You rolled a **5**",
  "You rolled a **6**",
  "You rolled a **7**",
  "You rolled a **8**",
  "You rolled a **9**",
  "You rolled a ***10***",
]

d12 = [
  "You rolled a *1*",
  "You rolled a **2**",
  "You rolled a **3**",
  "You rolled a **4**",
  "You rolled a **5**",
  "You rolled a **6**",
  "You rolled a **7**",
  "You rolled a **8**",
  "You rolled a **9**",
  "You rolled a **10**",
  "You rolled a **11**",
  "You rolled a ***12***",
]

d20 = [
  "You rolled a *1*",
  "You rolled a **2**",
  "You rolled a **3**",
  "You rolled a **4**",
  "You rolled a **5**",
  "You rolled a **6**",
  "You rolled a **7**",
  "You rolled a **8**",
  "You rolled a **9**",
  "You rolled a **10**",
  "You rolled a **11**",
  "You rolled a **12**",
  "You rolled a **13**",
  "You rolled a **14**",
  "You rolled a **15**",
  "You rolled a **16**",
  "You rolled a **17**",
  "You rolled a **18**",
  "You rolled a **19**",
  "You rolled a ***20***",
]

#When the bot starts
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Team Fortress 2'))
    print('We have logged in as {0.user}, bot is ready'.format(client))

#Message events
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    #If staring word
    if msg.startswith('!help'):
        helpEmbed = discord.Embed(title="Commands", description="I can do all this stuff :D", color=0xC82C30)
        helpEmbed.add_field(name="!help", value="Shows this menu", inline=True)
        helpEmbed.add_field(name="!mercs", value="Links hisanimations's Ultimate TF2 Blender Port video", inline=True)
        helpEmbed.add_field(name="!weapons, !hats, !props", value="Links hisanimations's TF2 Collection for Blender video", inline=True)
        helpEmbed.add_field(name="!spy, !spyware, !espion, !espionrepacker", value="Links [spy]'s EspionRepacker'", inline=True)
        helpEmbed.add_field(name="!materials", value="Links hisanimations's TF2 materials port", inline=True)
        helpEmbed.add_field(name="!taunts", value="Links hisanimations's TF2 taunts port", inline=True)
        helpEmbed.add_field(name="!sheets", value="Links Woha and hisanimations's Source Engine to Blender All In One Guide", inline=True)
        helpEmbed.add_field(name="!docs", value="Links Woha, [spy], and hisanimations's Source2Blender Documentation page", inline=True)
        helpEmbed.add_field(name="!getmestarted", value="Links a whole bunch of useful stuff to get you started porting TF2 (and other Source content) to Blender")
        helpEmbed.add_field(name="!slander, !filmic, !standard", value="Fun lil commands that send fun lil gifs", inline=True)
        helpEmbed.add_field(name="!open", value="Opens a support ticket", inline=True)
        helpEmbed.add_field(name="!coinflip", value="Flips a coin, you can get either heads or tails", inline=True)
        helpEmbed.add_field(name="!roll a d#", value="Rolls the dice of the specified number, options are as follows: d4, d6, d8, d10, d12, d20", inline=True)
        helpEmbed.add_field(name="!repl", value="Brings you to the replit.com page where I'm being hosted", inline=True)
        helpEmbed.add_field(name="!git", value="Directs you to the source code of the bot, hosted on GitHub", inline=True)
        await message.channel.send(embed=helpEmbed)
    if any(word in msg for word in started):
        await message.channel.send("Waiting for replit to update Python before this message works, stay tuned!")
    if msg.startswith('!mercs'):
        await message.channel.send("Here ya go: https://www.youtube.com/watch?v=7rH6_eq-I0c")
    if any(word in msg for word in collection_words):
        await message.channel.send("Here ya go: https://www.youtube.com/watch?v=0DMz-n1LSII")
    if any(word in msg for word in spy_words):
        await message.channel.send("Here ya go: https://github.com/spy-ware/EspionRepacker/releases")
    if msg.startswith('!materials'):
        await message.channel.send("Here ya go: https://drive.google.com/file/d/1nZmlYQ8DjSK3ikDE35B__C6RURI1Jlx-/view?usp=sharing")
    if msg.startswith('!taunts'):
        await message.channel.send("Here ya go: https://drive.google.com/file/d/1raq59AfiU9uUXwoQmxGE5RcpxoZv5H61/view?usp=drivesdk")
    if msg.startswith('!sheets'):
        await message.channel.send("Here ya go: https://docs.google.com/spreadsheets/d/1F29uWEPtJdfKUX26WGMa5j9trjW9wEWlOHgXIJupoFU/edit#gid=0")
    if msg.startswith('!docs'):
        await message.channel.send("Here ya go: https://source2blender.readthedocs.io/en/latest/index.html")
    if msg.startswith('!repl'):
        await message.channel.send("Here ya go: https://replit.com/@tazzan/TF2-Blender-Server-bot")
    if msg.startswith('!git'):
        await message.channel.send("Here ya go: https://github.com/tazzanmc/TF2-Blender-Server-bot")
    if msg.startswith('!eevee'):
        await message.channel.send("https://media.discordapp.net/attachments/807047989683683328/1009211129651798158/unknown.png")
    if msg.startswith('!open'):
        await message.channel.send("https://media.discordapp.net/attachments/723010093033062540/1009476752466264105/ezgif-1-0b7aad519d.gif")
    if msg.startswith('!filmic'):
        await message.channel.send(random.choice(filmic))
    if msg.startswith('!standard'):
        await message.channel.send(random.choice(standard))
    if msg.startswith('!slander'):
        await message.channel.send(random.choice(slander))
    if any(word in msg for word in coin_words):
        await message.channel.send(random.choice(coin_flip))
    if any(word in msg for word in d20_words):
        await message.channel.send(random.choice(d20))
    if any(word in msg for word in d12_words):
        await message.channel.send(random.choice(d12))
    if any(word in msg for word in d10_words):
        await message.channel.send(random.choice(d10))
    if any(word in msg for word in d8_words):
        await message.channel.send(random.choice(d8))
    if any(word in msg for word in d6_words):
        await message.channel.send(random.choice(d6))
    if any(word in msg for word in d4_words):
        await message.channel.send(random.choice(d4))

#Finishing up
keep_alive()
client.run(os.getenv('TOKEN'))