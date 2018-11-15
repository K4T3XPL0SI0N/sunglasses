import discord, asyncio
from discord.ext import commands

triggers = {
    "jake" : ":jake:505181297963040768",
    "ego" : ":ego:484169666806415378"
}

class AutoReactor():
    def __init__(self, client):
        self.client = client
        
    async def on_message(self, msg):
        for trigger in triggers:
            if trigger in msg.content.lower():
                try:
                    await msg.add_reaction(triggers[trigger])
                except discord.Forbidden:
                    pass       
    
    @commands.guild_only()
    @commands.command()
    async def autoreacts(self, ctx):
        returnValue = ""
        for i in trigger:
            returnValue += f"{i}, "
        return await ctx.send(f"Here's a list of the current autoreactions, these are __global__. ```py\n{returnValue}\n```")
                
def setup(client):
    client.add_cog(AutoReactor(client))
