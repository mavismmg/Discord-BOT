from discord.ext import commands

class TITULO(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ajuda(self, usuario):
        await usuario.send('comandos')

def setup(client):
    client.add_cog(TITULO(client))