import discord
import os
import random
import time
from discord.ext import commands

inAdmin = os.environ['ADMIN']

def authorIsAdmin(msg):
    identified = False
    for role in msg.author.roles:
        if (role.name == inAdmin):
            identified = True
            return True
    if identified == False:
        return False

client = discord.Client()

@client.event
async def on_ready():
    print("Sao phải print trong khi thằng làm bot chả bao giờ lên log!")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        if "uwu" in message.content.lower():
            await message.channel.send("UwU")
        if "owo" in message.content.lower():
            await message.channel.send("OwO")
        if "update" in message.content.lower():
            if "?" in message.content.lower():
                await message.channel.send("không biết bác có hỏi không, cơ mà có thì game sẽ update 2 tuần một lần, patch notes sẽ ra vào khoảng 0h sáng thứ 4 (giờ VN) - cũng là lúc cập nhật lên sóng.\n\nDù sao thì nếu chuẩn bị có update thì sẽ có thông báo ở #thông-báo nhé.")
                time.sleep(1)
                await message.channel.send("spam thì liệu đấy!")
        if "sai chính tả" in message.content.lower():
            if "bắt" in message.content.lower():
                if "." in message.content.lower():
                    await message.channel.send("Cảnh sát chính tả đây!")
                    await message.channel.send("https://cdn.discordapp.com/attachments/665774320911515685/708879643922530405/CANH_SAT_CHINH_TA.png")
        if "làm sao để có quyền lực" in message.content.lower():
            await message.channel.send("Biết đâu được...?")
            time.sleep(1)
            if authorIsAdmin(message):
                await message.channel.send("Mà khoan, bác có **quyền lực** rồi mà?")
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

# -Xmx1G -XX:+UseConcMarkSweepGC -XX:+CMSIncrementalMode -XX:-UseAdaptiveSizePolicy -Xmn128M
# C:\Program Files\Java\jre1.8.0_251\bin\javaw.exe
# D:\Requim\Minecraft