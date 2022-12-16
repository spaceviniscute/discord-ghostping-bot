import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name='ghostping', description='Salje poruku oznacenom retardu.')
async def ghostping(ctx, user: discord.Member):
    await ctx.send(f'Ubij se {user.mention}')

bot.run('VAS AUTISTICNI TOKEN OD BOTA')
