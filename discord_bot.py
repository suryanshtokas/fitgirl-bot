import os

import discord
from dotenv import load_dotenv

import main

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERV_ID = os.getenv('SERV_ID')

client = discord.Client()

@client.event
async def on_ready():
    print("Connected to right serv")

@client.event
async def on_message(message):
    if message.author ==  client.user:
        return

    if message.content.startswith("$repack"):
        await message.channel.send("Finding ...")
        message_content = message.content[8:]
        first_result = main.main(message_content)
        if len(first_result) == 0:
            await message.channel.send("Not Available :(")
        else:
            await message.channel.send(first_result)


client.run(TOKEN)

