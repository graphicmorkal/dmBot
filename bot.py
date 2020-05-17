# idk nhưng sao bác lại đọc được dòng này vậy hic :<
import discord
import os
import random
import time
from utils import check_quyen
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
        if message.content.startswith('t!aolang,'):
            ctx = message.content.split()
            if (len(ctx) < 2):
                await message.channel.send('?')
            else:
                for status in ctx[1:]:
                    if status == 'info':
                        await message.channel.send('**Giải Ao Làng Đông Lào lần thứ 3 / SEA**\n*Thời gian tổ chức:* từ **8/5** đến **10/5**  \n__Giải được chia làm 2 bảng đấu:__\n - Bảng vinh quang: Dành cho những người rank Kin cương trở xuống\n - Bảng siêu sao: Dành cho những người Rank master và người vào chung kết trong bảng vinh quang.\n*Tổng cơ cấu giải thưởng:* 10 ổ bánh mì thịt chả trứng 20k chia đều cho 2 vô địch bảng.')
                    if status == "thamgia":
                        await message.channel.send('Tiếc quá , giải đấu đã kết thúc, hẹn lần sau nhé!')
                    if status == "bangdau":
                        if (len(ctx) < 3):
                            await message.channel.send('Bạn nhập thêm vinhquang hoặc sieusao để nhận thông tin cho bảng tương ứng nhé!')
                        else:
                            for status in ctx[1:]:
                                if status == "vinhquang":
                                    await message.channel.send('Giải đã kết thúc!')
                                if status == "sieusao":
                                    await message.channel.send('Giải đã kết thúc!')
                                if status == "vqrule":
                                    await message.channel.send('__**LUẬT GIẢI AO LÀNG ĐÔNG LÀO LẦN THỨ 3 / MÁY CHỦ SEA**__\nVới Bảng Vinh Quang (DSV1):\n\n- Vòng 16 sẽ đánh thể thức Bo1. Chung kết Bo5, còn lại các vòng khác Bo3.\n- Các tuyển thủ có mặt trước 4h30 để điểm danh. 5 giờ sẽ bắt đầu đánh chính thức, 16 tuyển thủ sẽ đánh cùng một lúc, 2 người còn lại sẽ ở bảng sau luôn (? :) ). Dự kiến thời gian từng cặp đấu sẽ là 45 phút. Nếu điểm danh trễ 15 phút sẽ được xử thua. Tính theo giờ GTM +7 (chấp nhận chênh 2 phút) các đấu thủ điểm danh trễ sẽ được xử thua.\n- Khi chiến thắng, các bạn tham gia cần thông báo ngay cho ban tổ chức để ghi danh đấu trận tiếp theo\n- Deck tự do, nhưng nếu đã thắng bằng deck X rồi thì sẽ không dùng deck đó để đấu **TRONG CẶP ĐÓ** nữa.\n- Người tham gia có thể livestream để ban tổ chức cập nhật sớm nhất + cho các bạn khác cùng theo dõi.\n- Nếu như có các hành vi xem trộm livestream để ăn gian ban tổ chức sẽ xử thua ngay lập tức và không cho tham gia giải #4\n- Các tuyển thủ phải tôn trọng đối thủ, không có các hành vi lăng mạ hay toxic, . . . phải tuân thủ theo luật, - Nếu không hiểu luật hoặc không rõ thể thức hãy liên hệ với ban tổ chức để hỏi. Nếu vi phạm, tùy theo mức độ mà xử lí.\n**- Quyết định của ban tổ chức là quyết định cuối cùng.**\n\nTL;DR: vinh quang v16 Bo1, ck Bo5, còn lại Bo3; 4h30 điểm danh, muộn là ăn đầu `____`; deck tự do, deck X win rồi k dùng lại trong cặp đó nữa; đá stream, vô văn hóa = ăn đầu `____`')
        if message.content.startswith('t!help'):
            ctx = message.content.split()
            if (len(ctx) < 2):
                await message.channel.send('Các lệnh hiện có:\n**LOR ĐÔNG LÀO:**\nt!aolang (info/thamgia/bangdau) : Các lệnh về Ao làng Đông lào\n\n**TỔNG THỂ:**\nt!clear <X> : xóa X tin nhắn\n\n||Có thế thôi à :<||')    

#gửi tin nhắn chào mừng

class Gateway(commands.Cog):
    """Gateway Cog."""

    def __init__(self, bot):
        """Init method."""
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Actually handles printing the welcome message."""
        welcome_channels = await \
            self.bot.pg_utils.get_welcome_channels(
                member.guild.id, self.bot.logger)
        welcome_message = await \
            self.bot.pg_utils.get_welcome_message(
                member.guild.id, self.bot.logger)
        for ch_id in welcome_channels:
            channel = self.bot.get_channel(ch_id)
            await channel.send(welcome_message.replace(
                f'%user%', member.mention).replace(
                f'%server%', member.guild.name))

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """Actually handles printing the role greeting message."""
        if before.roles == after.roles:
            return
        role_diff = set(after.roles) - (set(before.roles))
        for role in role_diff:
            role_greetings = await \
                self.bot.pg_utils.get_role_greetings(
                    role.id, self.bot.logger)
            for role_greet in role_greetings:
                channel = self.bot.get_channel(role_greet["channel_id"])
                if not channel:
                    self.bot.logger.error("Kênh đã bị xóa.")
                    continue
                await channel.send(role_greet['greeting'].replace(
                    f'%user%', after.mention).replace(
                    f'%server%', after.guild.name))

    @commands.group()
    @commands.guild_only()
    @check_quyen.is_admin()
    async def welcome(self, ctx):
        """Welcome message command."""
        """If no subcommand is
        invoked, it will return the current welcome message."""
        welcome_msg = await self.bot.pg_utils.get_welcome_message(
            ctx.guild.id,
            self.bot.logger
        )
        if ctx.invoked_subcommand is None:
            local_embed = discord.Embed(
                title=f'Tin nhắn chào mừng hiện tại: ',
                description=welcome_msg
            )
            await ctx.send(embed=local_embed)

    @welcome.command(name='set')
    async def setwelcome(self, ctx, *, welcome_string: str=None):
        """Attempt to set welcome message to string passed in."""
        if not welcome_string:
            local_embed = discord.Embed(
                title=f'Nhập gì đi chứ, để trống vậy thì ai chơi :<',
                description=' ',
                color=0x651111
            )
            await ctx.send(embed=local_embed)
            return
        success = await self.bot.pg_utils.set_welcome_message(
            ctx.guild.id,
            welcome_string,
            self.bot.logger
        )
        if success:
            desc = welcome_string.replace(
                f'%user%', ctx.message.author.mention).replace(
                f'%server%', ctx.guild.name)
            local_embed = discord.Embed(
                title=f'Set tin nhắn chào mừng:',
                description=f'**Xem trước**\n{desc} ',
                color=0x419400
            )
        else:
            local_embed = discord.Embed(
                title=f'Internal error occured, please contact @dashwav#7785',
                description=' ',
                color=0x651111
            )
        await ctx.send(embed=local_embed)
        return

    @welcome.command(aliases=['on'])
    async def enable(self, ctx):
        """Enable the welcome message in this channel."""
        success = await self.bot.pg_utils.add_welcome_channel(
            ctx.guild.id, ctx.message.channel.id, self.bot.logger
        )
        if success:
            local_embed = discord.Embed(
                title=f'Đã thêm kênh:',
                description=f'{ctx.message.channel.name} '
                'was added to welcome list.',
                color=0x419400
            )
        else:
            local_embed = discord.Embed(
                title=f'Internal error, please contact @dashwav#7785',
                description=' ',
                color=0x651111
            )
        await ctx.send(embed=local_embed)

    @welcome.command(aliases=['off'])
    async def disable(self, ctx):
        """Enable the welcome message in this channel."""
        try:
            success = await self.bot.pg_utils.rem_welcome_channel(
                ctx.guild.id, ctx.message.channel.id, self.bot.logger
            )
        except ValueError:
            local_embed = discord.Embed(
                title=f'Kênh này vẫn chưa ở trong danh'
                'sách kênh chào mừng',
                description=' ',
                color=0x651111
            )
            await ctx.send(embed=local_embed)
            return
        if success:
            local_embed = discord.Embed(
                title=f'Kênh đã bị xóa:',
                description=f'{ctx.message.channel.name} '
                'đã được gỡ khỏi danh sách chào mừng.',
                color=0x419400
            )
        else:
            local_embed = discord.Embed(
                title=f'Internal error, please contact @dashwav#7785',
                description=' ',
                color=0x651111
            )
        await ctx.send(embed=local_embed)


    @commands.group(aliases=["greetings"])
    @commands.guild_only()
    @check_quyen.is_admin()
    async def greeting(self, ctx):
        """Role greeting command."""
        """If no subcommand is
        invoked, it will return the current role greetings."""
        if ctx.invoked_subcommand is None:
            role_greetings = await \
                self.bot.pg_utils.get_all_role_greetings(
                    ctx.guild.id, self.bot.logger)
            string = ""
            for role_greet in role_greetings:
                role = ctx.guild.get_role(role_greet['role_id'])
                channel = self.bot.get_channel(role_greet["channel_id"])
                if not channel or not role:
                    self.bot.logger.error("Channel/role removed")
                    continue
                string += f"Role: {role.mention} "
                string += f"- Channel: {channel.mention}\n"
            local_embed = discord.Embed(
                title=f'Current role_greetings: ',
                description=string
            )
            await ctx.send(embed=local_embed)


    @greeting.command(name='set')
    async def setgreeting(self, ctx, role: discord.Role , *, welcome_string: str=None):
        """Attempt to set role greeting message to string passed in."""
        if not welcome_string:
            local_embed = discord.Embed(
                title=f'Nhập gì đó đi chứ, để trống vậy thì ai chơi :<',
                description=' ',
                color=0x651111
            )
            await ctx.send(embed=local_embed)
            return
        success = await self.bot.pg_utils.set_role_greeting(
            ctx.guild.id,
            ctx.channel.id,
            role.id,
            welcome_string,
            self.bot.logger
        )
        if success:
            desc = welcome_string.replace(
                f'%user%', ctx.message.author.mention).replace(
                f'%server%', ctx.guild.name)
            local_embed = discord.Embed(
                title=f'Role greeting message set:',
                description=f'**Preview:**\n{desc} ',
                color=0x419400
            )
        else:
            local_embed = discord.Embed(
                title=f'Internal error occured, please contact @dashwav#7785',
                description=' ',
                color=0x651111
            )
        await ctx.send(embed=local_embed)
        return

    @greeting.command(name='remove', aliases=['rem'])
    async def remgreeting(self, ctx, role: discord.Role):
        """Attempt to set role greeting message to string passed in."""
        success = await self.bot.pg_utils.del_role_greeting(
            role.id,
            ctx.channel.id,
            self.bot.logger
        )
        if success:
            local_embed = discord.Embed(
                title=f'Role greeting message deleted from this channel',
                color=0x419400
            )
        else:
            local_embed = discord.Embed(
                title=f'Internal error occured, please contact @dashwav#7785',
                description=' ',
                color=0x651111
            )
        await ctx.send(embed=local_embed)
        return

    @greeting.command(name='get')
    async def getgreeting(self, ctx, role: discord.Role):
        """Attempt to set role greeting message to string passed in."""
        role_greeting = await self.bot.pg_utils.get_channel_role_greeting(
            role.id,
            ctx.channel.id,
            self.bot.logger
        )
        if not role_greeting:
            local_embed = discord.Embed(
                title=f'No role greetings in this channel',
                color=0x419400
            )
            await ctx.send(embed=local_embed)
            return
        local_embed = discord.Embed(
            title=f'Current role greeting: ',
            description=role_greeting["greeting"]
        )
        await ctx.send(embed=local_embed)


bot = commands.Bot(command_prefix='t!')

client.run(os.environ['DITMEMAY'])



#------------------------
# chỗ này để học nghề, đừng động vào, làm ơn, và cảm ơn.
#------------------------


