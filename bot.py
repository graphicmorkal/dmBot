# idk nhưng sao bác lại đọc được dòng này vậy hic :<
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
        if "sai chính tả" in message.content.lower():
            await message.channel.send("https://cdn.discordapp.com/attachments/665774320911515685/708879693545472080/GIU_GIN_SU_TRONG_SANG_CUA_TIENG_VIET.png")
            time.sleep(5)
            await message.channel.send("https://cdn.discordapp.com/attachments/665774320911515685/708879643922530405/CANH_SAT_CHINH_TA.png")
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
                        await message.channel.send('**Giải Ao Làng Đông Lào lần thứ 3 / SEA**\n*Thời gian tổ chức:* từ **8/5** đến **10/5**  \n__Giải được chia làm 2 bảng đấu:__\n - Bảng vinh quang: Dành cho những người rank Kin cương trở xuống\n - Bảng siêu sao: Dành cho những người Rank master và người vào chung kết trong bảng vinh quang.\n*Tổng cơ cấu giải thưởng:* 10 ổ bánh mì thịt chả trứng 20k chia đều cho 2 vô địch bảng.')
                    if status == "thamgia":
                        await message.channel.send('Tiếc quá , giải đấu đã đóng đăng ký rồi, hẹn lần sau nhé!')
                    if status == "bangdau":
                        if (len(ctx) < 3):
                            await message.channel.send('Bạn nhập thêm vinhquang hoặc sieusao để nhận thông tin cho bảng tương ứng nhé!')
                        else:
                            for status in ctx[1:]:
                                if status == "vinhquang":
                                    await message.channel.send('Đang chuẩn bị, hãy quay lại sau!')
                                if status == "sieusao":
                                    await message.channel.send('Đang chuẩn bị, hãy quay lại sau!')
                                if status == "vqrule":
                                    await message.channel.send('__**LUẬT GIẢI AO LÀNG ĐÔNG LÀO LẦN THỨ 3 / MÁY CHỦ SEA**__\nVới Bảng Vinh Quang (DSV1):\n\n- Vòng 16 sẽ đánh thể thức Bo1. Chung kết Bo5, còn lại các vòng khác Bo3.\n- Các tuyển thủ có mặt trước 4h30 để điểm danh. 5 giờ sẽ bắt đầu đánh chính thức, 16 tuyển thủ sẽ đánh cùng một lúc, 2 người còn lại sẽ ở bảng sau luôn (? :) ). Dự kiến thời gian từng cặp đấu sẽ là 45 phút. Nếu điểm danh trễ 15 phút sẽ được xử thua. Tính theo giờ GTM +7 (chấp nhận chênh 2 phút) các đấu thủ điểm danh trễ sẽ được xử thua.\n- Khi chiến thắng, các bạn tham gia cần thông báo ngay cho ban tổ chức để ghi danh đấu trận tiếp theo\n- Deck tự do, nhưng nếu đã thắng bằng deck X rồi thì sẽ không dùng deck đó để đấu **TRONG CẶP ĐÓ** nữa.\n- Người tham gia có thể livestream để ban tổ chức cập nhật sớm nhất + cho các bạn khác cùng theo dõi.\n- Nếu như có các hành vi xem trộm livestream để ăn gian ban tổ chức sẽ xử thua ngay lập tức và không cho tham gia giải #4\n- Các tuyển thủ phải tôn trọng đối thủ, không có các hành vi lăng mạ hay toxic, . . . phải tuân thủ theo luật, - Nếu không hiểu luật hoặc không rõ thể thức hãy liên hệ với ban tổ chức để hỏi. Nếu vi phạm, tùy theo mức độ mà xử lí.\n**- Quyết định của ban tổ chức là quyết định cuối cùng.**\n\nTL;DR: vinh quang v16 Bo1, ck Bo5, còn lại Bo3; 4h30 điểm danh, muộn là ăn đầu `____`; deck tự do, deck X win rồi k dùng lại trong cặp đó nữa; đá stream, vô văn hóa = ăn đầu `____`')
        if message.content.startswith('t!help'):
            ctx = message.content.split()
            if (len(ctx) < 2):
                await message.channel.send('Các lệnh hiện có:\n**LOR ĐÔNG LÀO:**\nt!aolang (info/thamgia/bangdau) : Các lệnh về Ao làng Đông lào\n\n**TỔNG THỂ:**\nt!clear <X> : xóa X tin nhắn\n\n||Có thế thôi à :<||')



          

bot = commands.Bot(command_prefix='t!')

client.run(os.environ['DITMEMAY'])



#------------------------
# chỗ này để học nghề, đừng động vào, làm ơn, và cảm ơn.
#------------------------


