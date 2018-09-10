import discord, asyncio
from discord.ext import commands

class Information:
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def botinfo(self, ctx):
        """Get information about the bot"""
        _appInfo = await self.client.application_info()
        await ctx.send(embed=discord.Embed(title="{0.name}".format(_appInfo),
                                           description = "{0.name} is owned by *`{0.owner.name}`* with :heart:\n{0.name} was originally made by <@104660856658210816>".format(_appInfo),
                                           colour=0x9E1A1A))
                       
    @commands.command()
    async def github(self, ctx): # Please leave this be, it'd be nice to have a little bit of credit <3
        """Grab the github link for the source code"""
        await ctx.send(embed=discord.Embed(title="Github Repo", 
                                           description="[Click here to go to the repo!](https://github.com/boopdev/sunglasses)",
                                           colour = 0x9E1A1A))
                       

def setup(client):
    client.add_cog(Information(client))
