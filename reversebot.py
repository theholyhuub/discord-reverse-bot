import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
 


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
has_clearpermisions = commands.has_permissions(manage_messages=True)

botstatus = cycle(["funny bot to troll your discord members!","easy to make yourself!","join https://discord.gg/sg4Qwgun if you need help","made by= theholyhuub"])

@tasks.loop(seconds=5)
async def changestatus():
    await client.change_presence(activity=discord.Game(next(botstatus)))

@client.event
async def on_ready():
    print("*biep* *biep* *biep*")
    print("ready to troll!:D")
    changestatus.start()

@client.event
async def on_message(message):
    if not message.author.bot:
        reversed_message = message.content[::-1]
        await message.channel.send(reversed_message)

if ("there is a secret command you know:]") in message.content:
        print("]: wonk uoy dnammoc terces a si ereht")
        
        await client.close()

client.run("put your own webhook here!")
