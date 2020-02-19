import discord
from discord.ext import commands

class comandos(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.bot_has_permissions(embed_links=True)
    @commands.command(description='Mostra o meu ping', usage='c.ping')
    async def ping(self, ctx):
        embed = discord.Embed(title="🏓 Pong!",
                              description=f' No Momento estou com: **{round(self.bot.latency * 1000)}ms**.',
                              color=0x36393f)
        embed.set_footer(text=self.bot.user.name + " © 2020", icon_url=self.bot.user.avatar_url_as())
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=90)
def setup(bot):
    bot.add_cog(comandos(bot))
