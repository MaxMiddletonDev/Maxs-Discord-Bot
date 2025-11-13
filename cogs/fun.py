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
    
    #KANYE QUOTE COMMAND
    @commands.command()
    async def kanyequote(self, ctx):
        quote = await get_kanye_quote()
        await ctx.send(quote)
      
    #FLIP A COIN COMMAND
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

    #TEAM GENERATOR COMMAND
    @commands.command()
    async def teamgen(self, ctx, team_amount: int, *members: discord.Member):
      if not members:
        await ctx.send("No One Mentioned...")
        return

      if team_amount <= 0:
        return
        
      if len(members) < team_amount:
        await ctx.send("Not Enough People")
        return

      member_list = list(members)
      random.shuffle(member_list)

      teams = [[] for i in range(team_amount)]

      for index, member in enumerate(member_list):
          team_index = index % team_amount
          teams[team_index].append(member)

      embed = discord.Embed(
        title = "Team Generator Results",
        color = discord.Color.blue()
    )

      for i, team in enumerate(teams):
          
          team_members_str = "\n".join([m.mention for m in team])
          
          if not team_members_str:
              team_members_str = "Empty"
              
          embed.add_field(
              name = f"Team {i + 1}",
              value = team_members_str,
              inline = False 
          )

      await ctx.send(embed=embed)

async def setup(bot):
  await bot.add_cog(Fun(bot))