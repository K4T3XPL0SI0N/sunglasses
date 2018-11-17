import discord, asyncio, string, random
from discord.ext import commands

def getRole(id : int, guild : discord.Guild):
    for role in guild.roles:
        if role.id == id:
            return role

n = string.ascii_uppercase + string.digits
n = tuple(n)

def createID(length : int):
    re = ""
    for i in range(length):
        re += random.choice(n)
    return re

        
confessionsRole = 513432922154467332
confessionsChannel = 513431665603903489
confessChannel = 513452033886519306
        
triggers = {
    "jake" : ":jake:505181297963040768",
    "ego" : ":ego:484169666806415378"
}

class AutoReactor():
    def __init__(self, client):
        self.client = client
        
    async def on_message(self, msg):
        if msg.channel != self.client.get_channel(confessionsChannel):
            for trigger in triggers:
                if trigger in msg.content.lower():
                    try:
                        await msg.add_reaction(triggers[trigger])
                    except discord.Forbidden:
                        pass
        else:
            authorRoles = msg.author.roles
            if getRole(confessionsRole, self.client.get_guild(468119888058122241)) in authorRoles:
                channel = self.client.get_channel(confessionsChannel)
                conID = createID(16)
                em = discord.Embed(colour=0xffff87, description = msg.content)
                em.set_author(name="Confession")
                await msg.channel.send(":thumbsup:")
                await msg.delete()
                await channel.send(embed=em)
            else:
                await msg.channel.send(":thumbsdown:")
                await msg.delete()
                    
    
    @commands.guild_only()
    @commands.command()
    async def autoreacts(self, ctx):
        returnValue = ""
        for i in trigger:
            returnValue += f"{i}, "
        return await ctx.send(f"Here's a list of the current autoreactions, these are __global__. ```py\n{returnValue}\n```")
              
def setup(client):
    client.add_cog(AutoReactor(client))
