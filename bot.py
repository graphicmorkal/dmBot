# idk nhưng sao bác lại đọc được dòng này vậy hic :<
import discord
import os

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
            await message.channel.send("Hello World!")
        if "wibu" in message.content.lower():
            await message.channel.send("Nói gì wibu đấy?")
        if "mọe" in message.content.lower():
            await message.channel.send("Lỗi chính tả kìa...\nSửa nhanh kẻo bay màu giờ!!!")
        if "trính tả" in message.content.lower():
            await message.channel.send("Lỗi chính tả kìa...\nSửa nhanh kẻo bay màu giờ!!!")
        # Check nếu là admin (chạy code ở dưới)
        if authorIsAdmin(message):
            if message.content.startswith('t!clear'):
                con = message.content.split()
                msg = []
                lists = await message.channel.history(limit=int(con[1])+1).flatten()
                for x in lists:
                    msg.append(x)
                await message.channel.delete_messages(msg)
                await message.channel.send(f"{message.author.mention} đã xoá %s tin nhắn!" % con[1])
        if message.content.startswith('t!aolang'):
            ctx = message.content.split()
            if (len(ctx) < 2):
                await message.channel.send('**Giải Ao Làng Đông Lào lần thứ 3**\n*Thời gian tổ chức:* từ **5/5** đến **7/5**  \n__Giải được chia làm 2 bảng đấu:__\n - Bảng vinh quang: Dành cho những người rank Kin cương trở xuống\n - Bảng siêu sao: Dành cho những người Rank master và người vào chung kết trong bảng vinh quang.\n*Cơ cấu giải thưởng:* 10 chai sting dành cho vô địch bảng (10k/chai)')

bot = commands.Bot(command_prefix='t!')

client.run(os.environ['DITMEMAY'])



#------------------------
# chỗ này để học nghề, đừng động vào, làm ơn, và cảm ơn.
#------------------------


