import os
from discord.ext import commands

client = commands.Bot(command_prefix='/')

@client.command()
async def carregar(cog_load):
    client.load_extension(f'cogs.{cog_load}')

@client.command()
async def descarregar(cog_load):
    client.unload_extension(f'cogs.{cog_load}')

@client.command()
async def re_carregar(cog_load):
    client.unload_extension(f'cogs.{cog_load}')
    client.load_extension(f'cogs.{cog_load}')

for arquivo in os.listdir('./cogs'):
    if arquivo.endswith('.py'):
        client.load_extension(f'cogs.{arquivo[:-3]}')

client.run('SEU TOKEN/NO SITE DISCORD DESENVOLVIMENTO')

