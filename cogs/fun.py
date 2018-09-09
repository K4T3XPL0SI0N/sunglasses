import discord, asyncio, random
from discord.ext import commands

current_dicks = {}

class Fun:
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def penis(self, ctx, member : discord.Member):
      if member.id not in current_dicks:
        current_dicks[member.id] = "8" + "="*random.randint(1,20) +"D"
        await ctx.send("{0.mention}'s dick: **{1}**".format(member, current_dicks[member.id]))
      else:
        await ctx.send(await ctx.send("{0.mention}'s dick: **{1}**".format(member, current_dicks[member.id])))
                 
def setup(client):
    client.add_cog(Fun(client))
