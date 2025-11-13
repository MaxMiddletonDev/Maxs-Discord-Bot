import discord
from discord.ext import commands
import aiohttp

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #HELP COMMAND
  @commands.command()
  async def cmds(self, ctx):
    help = discord.Embed(
      title = "COMMANDS",
      description = """
      GENERAL
      --------
      $cmds | Shows this help message\n
      $hello | The bot says hello\n\n
      FUN
      --------
      $kanyequote | Generates a Random Kanye Quote\n
      $flipacoin | (mention someone) (call)\n
      $teamgen | (amount of teams) (mention) (mention) etc..\n\n
      UTILITY
      --------
      """,
      color = discord.Color.blue(), 
    )
    await ctx.send(embed = help)

    #HELLO COMMAND
    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")

async def setup(bot):
    await bot.add_cog(General(bot))