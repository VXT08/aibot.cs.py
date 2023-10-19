import discord
from model import get_class
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#@bot.command()
#async def help_cs(ctx):
     #потом добвалю сюда список команд

@bot.command()
async def savex(ctx):
    attechments = ctx.message.attachments
    for attachment in attechments:
         file_name = attachment.filename
         file_url = attachment.url
         await attachment.save(f"./images/{file_name}")
         mapp = get_class(f"./images/{file_name}")
         if mapp == '"стэирс", карта - "Мираж"':
            await ctx.send("За Т сторону советую отбросить смоук на стэирс в начале раунда, в мастерской есть карты для тренировки смоков. За КТ сторону советую чекать палас или яму отсюда.")
            if mapp == '"тетрис", карта - "Мираж"':
                await ctx.send("Можно спрятаться или пропушить.")
            if mapp == '"рампа А" или  же "яма", карта - "Мираж"':
                await ctx.send("Советую закинуть молотов за КТ, чтобы замедлить Т сторону.")
            if mapp == '"палас", карта - "Мираж"':
                await ctx.send(mapp)
                await ctx.send("Будьте аккуратны, если собираетесь выходить с ПАЛАСА в начале раунда за Т сторону, ведь эта позиция просматривается со стэирса.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5): 
    await ctx.channel.purge(limit=amount)

bot.run("token")
