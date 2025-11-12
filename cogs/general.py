import discord
from discord.ext import commands
import aiohttp

class General(commands.Cog):
  def __init__(self, bot):
        self.bot = bot

  @commands.command()
  async def cmds(self, ctx):
    help = discord.Embed(
      title = "COMMANDS",
      description = """
      $cmds⠀⠀⠀⠀⠀⠀⠀| Shows this help message\n
      $kanyequote⠀⠀⠀| Generates a Random Kanye Quote\n
      $hello⠀⠀⠀⠀⠀⠀⠀| The bot says hello\n
      """,
      color = discord.Color.blue(), 
    )
    await ctx.send(embed = help)

async def setup(bot):
    await bot.add_cog(General(bot))