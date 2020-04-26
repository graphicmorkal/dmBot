# idk nhưng sao bác lại đọc được dòng này vậy hic :<
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Sẵn sàng hoạt động!")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        if "uwu" in message.content.lower():
            await message.channel.send("UwU")
        if "owo" in message.content.lower():
            await message.channel.send("OwO")
        if "chào" in message.content.lower():
            await message.channel.send("Chào bạn tui!")
        if "hello" in message.content.lower():
            await message.channel.send("World!")

Bot.run(os.environ['DITMEMAY'])