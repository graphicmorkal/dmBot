# idk nhưng sao bác lại đọc được dòng này vậy hic :<
import discord
import os
import random

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
        if "yo" in message.content.lower():
            await message.channel.send("Yo!")
        if "làm sao để có quyền lực" in message.content.lower():
            await message.channel.send("Biết đâu được...?")
            if authorIsAdmin(message):
                await message.channel.send("Mà khoan, bác có **quyền lực** rồi mà?")
        # Check nếu là admin (chạy code ở dưới)
        if message.content.startswith('t!clear'):
            con = message.content.split()
            await message.channel.send("Ai cho bác cái quyền để xóa tin nhắn vậy?")
            if authorIsAdmin(message):
                con = message.content.split()
                msg = []
                lists = await message.channel.history(limit=int(con[1])+1).flatten()
                for x in lists:
                    msg.append(x)
                await message.channel.delete_messages(msg)
                await message.channel.send(f"> Ai cho bác cái quyền để xóa tin nhắn vậy?\nÀ nhầm, xin lỗi {message.author.mention} nhé! Xoá %s tin nhắn rồi đấy!" % con[1])
        if message.content.startswith('t!aolang'):
            ctx = message.content.split()
            if (len(ctx) < 2):
                await message.channel.send('nah')
            else:
                for status in ctx[1:]:
                    if status == 'info':
                        await message.channel.send('**Giải Ao Làng Đông Lào lần thứ 3 / SEA**\n*Thời gian tổ chức:* từ **8/5** đến **10/5**  \n__Giải được chia làm 2 bảng đấu:__\n - Bảng vinh quang: Dành cho những người rank Kin cương trở xuống\n - Bảng siêu sao: Dành cho những người Rank master và người vào chung kết trong bảng vinh quang.\n*Cơ cấu giải thưởng:* 10 chai sting dành cho vô địch bảng (10k/chai)')
                    if status == "thamgia":
                        await message.channel.send('Tiếc quá {message.author.mention}, giải đấu đã đóng đăng ký rồi, hẹn lần sau nhé!')
                    if status == "bangdau":
                        ctx = message.content.split()
                        if (len(ctx) < 2):
                            await message.channel.send('Bạn nhập thêm vinhquang hoặc sieusao để nhận thông tin cho bảng tương ứng nhé!')
                        else:
                            for status in ctx[1:]:
                                if status == "vinhquang":
                                    await message.channel.send('Chưa có thông tin!')
                                if status == "sieusao":
                                    await message.channel.send('Chưa có thông tin!')
        if message.content.startswith('t!help'):
            ctx = message.content.split()
            if (len(ctx) < 2):
                await message.channel.send('Các lệnh hiện có:\n\nt!aolang (info/thamgia/bangdau) : Các lệnh về Ao làng Đông lào\n\n||Có thế thôi à :<||')



          

bot = commands.Bot(command_prefix='t!')

client.run(os.environ['DITMEMAY'])



#------------------------
# chỗ này để học nghề, đừng động vào, làm ơn, và cảm ơn.
#------------------------


