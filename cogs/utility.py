import discord
from discord.ext import commands
import aiohttp
import typing

class Utility(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #PING COMMAND
  @commands.command()
  async def ping(self, ctx):
    await ctx.send(f"Pong! Latency is {round(self.bot.latency * 1000)}ms")

  #WHOIS COMMAND
  @commands.command()
  async def whois(self, ctx, member: typing.Optional[discord.Member] = None):
    if member is None:
      member = ctx.author

    whoisinfo = discord.Embed(
      title = "INFO",
      color = member.color,
    )
    whoisinfo.set_thumbnail(url = member.display_avatar.url)
    whoisinfo.add_field(name = "USERNAME", value = str(member), inline=True)
    whoisinfo.add_field(name = "ID", value = member.id, inline=True)
    whoisinfo.add_field(name = "JOINED", value = discord.utils.format_dt(member.joined_at, style='R'), inline = True)
    
    await ctx.send(embed = whoisinfo)
  
async def setup(bot):
    await bot.add_cog(Utility(bot))