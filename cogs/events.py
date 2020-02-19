import discord
import asyncio
from datetime import datetime
import pytz
import re
from discord.ext import commands
aviso1 = []
aviso2 = []
aviso3 = []

class events(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_ban(self , guild, member):
      if member.guild.id == 679015306437460008:
        await asyncio.sleep(3)
        #moderator = 'Não encontrado.'
        #reason = "Não informada."
        async for entry in guild.audit_logs(action=discord.AuditLogAction.ban ,limit=1):
            moderator = entry.user
            if moderator is None:
                moderator = "NADA"
            reason = entry.reason
            if reason is None:
                reason = "Não informada."
        embed = discord.Embed(color=0xe91e63,timestamp=datetime.now(pytz.timezone('America/Sao_Paulo')))
        embed.set_author(name=f"MEMBRO BANIDO", icon_url=guild.icon_url)
        embed.add_field(name=f"Usuário:", value=f"`{member.name}`")
        embed.add_field(name=f"Autor:",value=f"`{moderator}`")
        embed.add_field(name="Motivo:",value=f"``{reason}``")
        embed.set_footer(text=self.bot.user.name+" © 2020", icon_url=self.bot.user.avatar_url_as())
        embed.set_thumbnail(url=member.avatar_url_as(format='png'))
        logs_bans = guild.get_channel(679738999312744454)
        await logs_bans.send(embed=embed, content="@everyone")

    @commands.Cog.listener()
    async def on_member_unban(self , guild, member):
      if member.guild.id == 679015306437460008:
        await asyncio.sleep(3)
        moderator = 'Não encontrado.'
        async for entry in guild.audit_logs(action=discord.AuditLogAction.unban ,limit=1):
            moderator = entry.user
        embed = discord.Embed(color=0xe91e63,timestamp=datetime.now(pytz.timezone('America/Sao_Paulo')))
        embed.set_author(name=f"MEMBRO DESBANIDO", icon_url=guild.icon_url)
        embed.add_field(name=f"Usuário:", value=f"`{member.name}`")
        embed.add_field(name=f"Autor:",value=f"`{moderator}`")
        embed.set_footer(text=self.bot.user.name+" © 2020", icon_url=self.bot.user.avatar_url_as())
        embed.set_thumbnail(url=member.avatar_url_as(format='png'))
        logs_bans = guild.get_channel(679738999312744454)
        await logs_bans.send(embed=embed, content="@everyone")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
          comma = error.args[0].split('"')[1]
          quantidade = len(comma)
          if quantidade > 13:
            return await ctx.send('não tente me bugar poha')
          embed = discord.Embed(title=f" | Comando não encontrado", color=0x7289DA, description=f"O comando `{comma}` não existe.")
          await ctx.send(embed=embed)
        elif isinstance(error, commands.errors.CheckFailure):
          print("erro ao checar")
          pass
        elif isinstance(error, commands.CommandOnCooldown):
          m, s = divmod(error.retry_after, 60)
          return await ctx.send(f"**{ctx.author.name}**, aguarde **`{int(s)}`** segundo(s) para poder usar o comando **`{ctx.invoked_with}`** novamente.", delete_after=45)
        elif isinstance(error, commands.DisabledCommand):
          await ctx.send(f"<:incorreto:571040727643979782> | **{ctx.author.name}**, o comando **`{ctx.invoked_with}`** está temporariamente desativado.")
        elif isinstance(error, commands.MissingRequiredArgument):
          await ctx.send('faltando argumentos')

    @commands.Cog.listener()
    async def on_message(self, message):
      if re.search(r'discord(?:app\\?[\s\S]com\\?\/invite|\\?[\s\S]gg|\\?[\s\S]me)\/', message.content) or re.search(r'invite\\?[\s\S]gg\\?\/[\s\S]', message.content) or "privatepage" in message.content.lower() or "naked" in message.content.lower():
        if str("</Link>") in [r.name for r in message.author.roles if r.name != "@everyone"]:
            print("OK")
        else:
          if not message.author.id in aviso1:
            aviso1.append(message.author.id)
            await message.delete()
            embed=discord.Embed(description=f"<:incorreto:594222819064283161> **|** Olá {message.author.mention}, não é permitido **CONVITES** de outros servidores sem a permissão dos **Adminstradores** segundo as regras.\nTendo isso em mente irei avisa-lo esse é seu **1° Strike**.\nNo **3° Strike** você será banido.", color=0x7289DA)
            msg = await message.channel.send(embed=embed)
            await asyncio.sleep(10)
            await msg.delete()
          elif not message.author.id in aviso2:
            aviso2.append(message.author.id)
            await message.delete()
            embed=discord.Embed(description=f"<:incorreto:594222819064283161> **|** Olá {message.author.mention}, não é permitido **CONVITES** de outros servidores sem a permissão dos **Adminstradores** segundo as regras.\nTendo isso em mente irei avisa-lo esse é seu **2° Strike**.\nNo **3° Strike** você será banido.", color=0x7289DA)
            msg = await message.channel.send(embed=embed)
            await asyncio.sleep(10)
            await msg.delete()
          else:
            await message.delete()
            aviso1.remove(message.author.id)     
            aviso2.remove(message.author.id)       
            print('ban')
            await message.author.ban(reason="Divulgando.")

def setup(bot):
    bot.add_cog(events(bot))
