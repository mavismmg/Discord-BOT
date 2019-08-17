import discord
import random
from discord.ext import commands

class COMANDOS(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def boot_bot(self):
        await self.client.change_presence(status=discord.Status.idle,
                                          activity=discord.Game('STATUS DESEJADO'))
        print('Carregado!')

    @commands.Cog.listener()
    async def member_join(self, membro):
        print(f'{membro} se juntou ao TEXTO!')

    @commands.Cog.listener()
    async def member_left(self, membro):
        print(f'{membro} deixou o TEXTO!')

    @commands.command()
    async def otaku(self, usuario, *, pergunta):
        respostas = ['example rep1',
                     'example rep12']
        await usuario.send(f'{random.choice(respostas)}')

    @commands.command()
    async def fixadas(self, usuario):
        respostas = ['example text1',
                     'example text2']
        await usuario.send(f'{random.choice(respostas)}')

    @commands.command()
    async def latencia(self, usuario):
        await usuario.send(f'Latencia: {round(self.client.latency * 1000)}ms')
    @commands.command()
    async def expulsar(self, membro: discord.Member, *, causa='Anime was a mistake'):
        await membro.kick(reason=causa)

    @commands.command()
    async def criador(self):
        print('mavis#8202')

def setup(client):
    client.add_cog(COMANDOS(client))