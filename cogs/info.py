import discord, asyncio
from discord.ext import commands

class Information:
    def __init__(client):
        self.client = client
        
    @commands.command()
    async def botinfo(self, ctx):
        _appInfo = await self.client.application_info()
        await ctx.send(embed=discord.Embed(title="{0.name}".format(_appInfo),
                                           description = "{0.name} was created by *`{0.owner.name}`* with :heart:".format(_appInfo),
                                           colour=0x9E1A1A)

def setup(client):
    client.add_cog(Information(client))
