#IMPORTS
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?', help_command=None, activity=discord.Game("?help"))

#EVENTS
@bot.event
async def on_ready():
    print('online')

@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)
        if bot.user.mentioned_in(message):
            await message.reply("Use **?help** to know more.")

#HANDLING COGS
#Loading all cogs at the start
for i in os.listdir('./cogs'):
    if i.endswith('.py'):
        bot.load_extension(f"cogs.{i[:-3]}")

#Loading a specific cog
@bot.command()
async def load(ctx, ext):
    bot.load_extension(f"cogs.{ext}")

#Unloading a specific cog
@bot.command()
async def unload(ctx, ext):
    bot.unload_extension(f"cogs.{ext}")

#Reloading a specific cog
@bot.command()
async def reload(ctx, ext):
    bot.unload_extension(f"cogs.{ext}")
    bot.load_extension(f"cogs.{ext}")

#RUN
TOKEN = os.getenv('DISCORD_MYBOT_TOKEN')
bot.run(TOKEN)
