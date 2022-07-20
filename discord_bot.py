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
    
    if client.user.mentioned_in(message):
        await message.channel.send("Use $repack help for more information")

    elif message.content.startswith("$repack help"):
        embed = discord.Embed(title="Help", description="List of commands for the bot", color=0x00FF00)
        embed.add_field(name="$repack [name_of_game]", value="To show all games avaiable on fitgirl's site with the name", inline=False)
        embed.add_field(name="$repack upcoming", value="Show upcoming repacks", inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("$repack upcoming"):
        await message.channel.send("Finding ...")
        upcoming_results = main.upcoming_repacks()
        embed = discord.Embed(title="Upcoming Repacks", description="get a list of upcoming repacks")
        for i, j in enumerate(upcoming_results):
            embed.add_field(name=i, value=j, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("$repack"):
        await message.channel.send("Finding ...")
        message_content = message.content[8:]
        first_result = main.main(message_content)
        if len(first_result) == 0:
            await message.channel.send("Not Available :(")
        else:
            embed = discord.Embed(title="Results", description="List of games available on fitgirl repacks ")
            for i in first_result:
                embed.add_field(name=i[0], value=i[1], inline=False)
            await message.channel.send(embed=embed)


client.run(TOKEN)

