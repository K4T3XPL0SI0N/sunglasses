import discord, asyncio
from discord.ext import commands

triggers = {
    "jake" : ":jake:505181297963040768"
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
                
    @commands.command()
    async def invites(self, ctx):
        invites = await ctx.guild.invites()
        inviters = {}
        for i in invites:
            if i.inviter not in inviters:
                inviters[i.inviter] = 0
            inviters[i.inviter] += i.uses
        lb = sorted(inviters, reverse=True)
        
        if str(ctx.author) in inviters:
            embed = discord.Embed(title="Invite Leaderboard", description="Your invite(s) have been used `{}` times!".format(inviters[str(ctx.author)]))
        else:
            embed = discord.Embed(title="Invite Leaderboard", description="You have no invite links in this server, or they've all expired.")
        
        for i in range(10):
            embed.add_field(name=str(tuple(inviters[i])), value=str(inviters[str(tuple(inviters[i]))])) # this is confusing uwu
        return await ctx.send(embed=embed)
            
                
def setup(client):
    client.add_cog(AutoReactor(client))
