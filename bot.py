# idk nhưng sao bác lại đọc được dòng này vậy hic :<
import discord
import os
import random
import time
from discord.ext import commands

inAdmin = os.environ['ADMIN']

inDN = os.environ['BUNHIN']

def authorIsAdmin(msg):
    identified = False
    for role in msg.author.roles:
        if (role.name == inAdmin):
            identified = True
            return True
    if identified == False:
        return False

def authorIsBuNhin(msg):
    identified = False
    for role in msg.author.roles:
        if (role.name == inDN):
            identified = True
            return True
    if identified == False:
        return False

client = discord.Client()

@client.event
async def on_ready():
    print("Sẵn sàng hoạt động!")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        if "ê bot, spam đi" in message.content.lower():
            await message.channel.send("Đ")
            await message.channel.send("ã")
            await message.channel.send(".")
            await message.channel.send("R")
            await message.channel.send("õ")
            await message.channel.send(".")
            await message.channel.send("R")
            await message.channel.send("ồ")
            await message.channel.send("i")
            await message.channel.send(".")
            await message.channel.send("N")
            await message.channel.send("h")
            await message.channel.send("é")
            await message.channel.send(".")
            await message.channel.send("UwU")
            await message.channel.send("UwU")
            time.sleep(1)
            await message.channel.send("https://tenor.com/view/dr-stone-smiling-senku-oops-my-bad-sorry-gif-16445162")
        if "uwu" in message.content.lower():
            await message.channel.send("UwU")
        if "owo" in message.content.lower():
            await message.channel.send("OwO")
        if "sai chính tả" in message.content.lower():
            if "bắt" in message.content.lower():
                await message.channel.send("https://cdn.discordapp.com/attachments/665774320911515685/708879643922530405/CANH_SAT_CHINH_TA.png")
        if "làm sao để có quyền lực" in message.content.lower():
            await message.channel.send("Biết đâu được...?")
            time.sleep(1)
            if authorIsAdmin(message):
                await message.channel.send("Mà khoan, bác có **quyền lực** rồi mà?")
            if authorIsBuNhin(message):
                await message.channel.send("Bù nhìn à? Khó à nha....")
            else:
                await message.channel.send("Chịu thôi...")
        # Check nếu là admin (chạy code ở dưới)
        if message.content.startswith('t!clear'):
            con = message.content.split()
            await message.channel.send("?")
            if authorIsAdmin(message):
                con = message.content.split()
                msg = []
                lists = await message.channel.history(limit=int(con[1])+1).flatten()
                for x in lists:
                    msg.append(x)
                await message.channel.delete_messages(msg)
                await message.channel.send(f"{message.author.mention} đã xoá %s tin nhắn!" % con[1])

bot = commands.Bot(command_prefix='t!')

client.run(os.environ['DITMEMAY'])



#------------------------
# chỗ này để học nghề, đừng động vào, làm ơn, và cảm ơn.
#------------------------


