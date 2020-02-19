import discord
import os
from config import secrets
from discord.ext import commands





class main(discord.ext.commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(secrets.PREFIXO),
                         case_insensitive=True,
                         pm_help=None,
                         description="um bot feito nas horas livres de Neo_")
        #self.staff = secrets.STAFF
        self.dono = secrets.DONO
        self.cor = 0x7289DA
        #self.database = secrets.DATAB
        self.token = 'blz,talvez outro dia.'
        self.carregados = 1
        self.falhas = 0
        for file in [c for c in os.listdir("cogs") if c.endswith(".py")]:
                name = file[:-3]
                try:
                    self.load_extension(f"cogs.{name}")
                    self.carregados += 1
                    print(f'MÓDULO [{file}] CARREGADO')
                except Exception as e:
                    print(f"FALHA AO CARREGAR  [{file}] MODULO ERROR [{e}]")
                    self.falhas += 1


    async def on_ready(self):
        print(f"[OK] - {self.user.name} ({self.user.id}) - (Status - Online)")
        print(f"[OK] - {len(bot.commands)} Comandos Ativos.")
        print(f"[OK] - {len(bot.cogs)} Cogs Ativas.")
        

    
    def iniciar(self):
       try:
           super().run(secrets.TOKEN,reconnect=True)
       except Exception as e:
           print(f"Erro ao logar o bot: {e}")
    


if __name__ == '__main__':
    bot = main()
    bot.iniciar()

