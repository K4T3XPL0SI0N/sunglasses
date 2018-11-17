import discord, asyncio
from discord.ext import commands

def getRole(id : int, guild : discord.Guild):
    for role in guild.roles:
        if role.id == id:
            return role

confessionsRole = 513432922154467332
confessionsChannel = 513431665603903489
        
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
    
    @commands.command()
    async def confess(self, ctx, *, confession : str):
        authorRoles = ctx.author.roles
        if getRole(confessionsRole, self.client.get_guild(468119888058122241)) in authorRoles:
            channel = self.client.get_channel(confessionsChannel)
            await channel.send("```css\n[ NEW CONFESSION ]\n```\n{}".format(confession))
            await ctx.send(":thumbsup:")
            await ctx.message.delete()
        else:
            return await ctx.send("You aren't a {0.name}".format(getRole(confessionsRole, self.client.get_guild(468119888058122241)).name))
                
def setup(client):
    client.add_cog(AutoReactor(client))
