import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Sẵn sàng hoạt động!")

client.run(os.environ['DITMEMAY'])