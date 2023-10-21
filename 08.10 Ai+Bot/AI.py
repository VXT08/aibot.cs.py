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
        await attachment.save(f"./imagess/{file_name}")
        mapp = get_class(f"./imagess/{file_name}")
        if mapp == '"стэирс", карта - "Мираж"':
            await ctx.send(mapp, "За Т сторону советую отбросить смоук на стэирс в начале раунда, в мастерской есть карты для тренировки смоков. За КТ сторону советую чекать палас или яму отсюда.")
        if mapp == '"тетрис", карта - "Мираж"':
            await ctx.send(mapp, "Можно спрятаться или пропушить.")
        if mapp == '"рампа А" или  же "яма", карта - "Мираж"':
            await ctx.send(mapp, "Советую закинуть молотов за КТ, чтобы замедлить Т сторону.")
        if mapp == '"палас", карта - "Мираж"':
            await ctx.send(mapp, "Будьте аккуратны, если собираетесь выходить с ПАЛАСА в начале раунда за Т сторону, ведь эта позиция просматривается со стэирса.")
        if mapp == '"сити" или же "КТ спавн", карта - "Мираж"':
            await ctx.send(mapp, 'За Т сторону советую кинуть смоук во время захода на А, за КТ сторону тут хорошо просматривается плэнт')
        if mapp == '"джангл", карта - "Мираж"':
            await ctx.send(mapp, 'За КТ сторону отлично просматривается стэирс и палас, за Т - накиньте смоук')
        if mapp == '"мид", карта - "Мираж"':
            await ctx.send(mapp, 'Не советую выходить в одиночку за Т, ведь эта позиция очень легко просматривается с АВП')
        if mapp == '"стул", карта - "Мираж"':
            await ctx.send(mapp, 'Хорошая нычка для Т, если вы играете за КТ, то будьте осторожны при выходе с шорта')
        if mapp == '"кон" или же "коннектор", карта - "Мираж"':
            await ctx.send(mapp, 'хорошая позиция для КТ, чтобы просматривать миди или шорт, а также неплохая для выхода на А для Т')
        if mapp == '"андер", карта - "Мираж"':
            await ctx.send(mapp, 'За Т можно тихо прокрасться, чтобы безопасно просматривать шорт, но КТ могут вас просматривать с коннектора')
        if mapp == '"шорт", карта - "Мираж"':
            await ctx.send(mapp, 'При выходе через аппарты за Т - вас может поджидать КТ, но если вы заняли Т, то можно поставить бомбу под шорт для преимущества в позиции')
        if mapp == '"окно", карта - "Мираж"':
            await ctx.send(mapp, 'Лучше закинуть смоук за Т, чтобы пройти на А или Б сайт. Через окно отлично просматривать за КТ, особенно со снайперками')
        if mapp == '"китчен" или же "кухня", карта - "Мираж"':
            await ctx.send(mapp, 'За КТ просматриваеться Б плэнт и Кар')
        if mapp == '"бенч" или же "форест", карта - Мираж':
            await ctx.send(mapp, 'можно спрятаться за КТ в начале раунда или за Т после установки бомбы')
        if mapp == '"машина" или же "кар", карта - "Мираж"':
            await ctx.send(mapp, 'За КТ просматривается апарты, советую прокинуть молотов за Т в начале раунда')
        if mapp == '"апарты", карта - "Мираж"':
            await ctx.send(mapp, 'при выходе на Б, за Т, советую прокинуть смоук на китчен и молотов на Кар, для лучшего входа')
        if mapp == '"Т спавн", карта - "Мираж"':
            await ctx.send(mapp, 'Просто спавн, практически никак не используется во время матчей')


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5): 
    await ctx.channel.purge(limit=amount)

bot.run("token")
