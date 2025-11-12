import discord
from discord.ext import commands
import aiohttp
import random

async def get_kanye_quote():
  async with aiohttp.ClientSession() as session:
    async with session.get("https://api.kanye.rest") as response:
      json_data = await response.json()
      quote = json_data['quote'] + " - Kanye West"
      return (quote)

class Fun(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kanyequote(self, ctx):
        quote = await get_kanye_quote()
        await ctx.send(quote)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")

    @commands.command()
    async def flipacoin(self, ctx, member: discord.Member, user_call: str):
      call = user_call.lower()
      
      if call not in ['heads', 'tails']:
          await ctx.send(f"Sorry, {ctx.author.mention}, you must call 'heads' or 'tails'")
          return

      options = ['heads', 'tails']
      result = random.choice(options)

      message = f"Coin flip for {member.mention} and {ctx.author.mention}!\n\n"
      message += f"The coin landed on: **{result.upper()}**!\n\n"

      if call == result:
          message += f"{ctx.author.name} wins and {member.name} loses!"
      else:
          message += f"{ctx.author.name} lost and {member.name} wins!"
        
      await ctx.send(message)
      
async def setup(bot):
  await bot.add_cog(Fun(bot))