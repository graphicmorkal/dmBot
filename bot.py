import discord
import os

client = discord.client()

@client.event
async def on_ready():
    print("Sẵn sàng hoạt động!")

client.run(os.environ['DMBOT'])