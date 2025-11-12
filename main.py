import discord
from discord.ext import commands
import os
import aiohttp 
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and not filename.startswith('__'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
  print(f'Stand Ready for {bot.user} Arrival Worm')

keep_alive()
bot.run(os.getenv('TOKEN'))