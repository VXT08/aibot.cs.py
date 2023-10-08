import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def help_cs(ctx):
     #потом добвалю сюда список команд

@bot.command()
async def savex(ctx):
    attechments = ctx.message.attachments
    for attachment in attechments:
         file_name = attachment.filename
         file_url = attachment.url
         await attachment.save(f"./images/{file_name}")
         await ctx.send("Картинка сохранена :)")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5): 
    await ctx.channel.purge(limit=amount)

bot.run("token")
