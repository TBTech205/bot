#pip install -U git+https://github.com/Pycord-Development/pycord ------ Keep this here
#pip install --upgrade discord-components

import discord, asyncio, os

from discord.ext import commands
from keep_alive import keep_alive
from modules import bot as v

client = commands.Bot(command_prefix=v.prefix, intents = v.intents, case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
client.run(v.token)