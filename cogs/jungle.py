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
confessionsLogging = 513538555050721285 # temporary channel, just for testing etc.
mutedRole = 468143090863964182
        
triggers = {
    "jake" : ":jake:505181297963040768",
    "ego" : ":ego:484169666806415378"
}

cons = {}

class AutoReactor():
    def __init__(self, client):
        self.client = client
        
    async def on_message(self, msg):
        if msg.channel != self.client.get_channel(confessChannel):
            for trigger in triggers:
                if trigger in msg.content.lower():
                    try:
                        await msg.add_reaction(triggers[trigger])
                    except discord.Forbidden:
                        pass
        elif msg.channel.id == confessChannel and msg.author.id != 488205899782160415:
            authorRoles = msg.author.roles
            try:
                channel = self.client.get_channel(confessionsChannel)
                confessionsTotal = await channel.history().flatten()
                confessionsNumber = int(len(confessionsTotal) + 1)
                conID = createID(16)
                cons[conID] = {'author' : msg.author, 'content' : msg.content}
                em = discord.Embed(colour=0xffff87, description = msg.content)
                em.set_author(name="Confession #{}".format(str(confessionsNumber)))
                em.set_footer(text=conID)
                if len(msg.attachments) > 0:
                    if str(msg.attachments[0].filename)[-4:] in ('.jpg', '.png', '.gif'):
                        em.set_image(url = msg.attachments[0].proxy_url)
                e = await msg.channel.send(":thumbsup:")
                await msg.delete()
                await channel.send(embed=em)
                await self.client.get_channel(confessionsLogging).send(":telescope: **Confession #{0}** `{1}` was sent by **{2}** `[{2.id}]`".format(confessionsNumber, conID, msg.author))
            except Exception as err: 
                e = await msg.channel.send(":thumbsdown: `{}`".format(err))
                await msg.delete()
            await asyncio.sleep(5)
            await e.delete()
                    
    
    @commands.guild_only()
    @commands.command()
    async def autoreacts(self, ctx):
        returnValue = ""
        for i in trigger:
            returnValue += f"{i}, "
        return await ctx.send(f"Here's a list of the current autoreactions, these are __global__. ```py\n{returnValue}\n```")
              
    @commands.is_owner()
    @commands.command(hidden=True)
    async def concheck(self, ctx, conID):
        return str(cons[conID].id)
    
    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def fban(self, ctx, user : discord.Member, *, reason = None):
        muted = getRole(mutedRole, self.client.get_guild(468119888058122241))
        if reason == None:
            reason = "None specified"
        await ctx.message.delete()
        msg = await ctx.send(":hammer: **{0}** has been banned by {1} for the reason : `{2}`".format(user, ctx.author, reason))
        await user.add_roles(muted)
        await asyncio.sleep(10)
        await user.remove_roles(muted)
        await msg.edit(content="just kiddin' they're still here ;)")
        await asyncio.sleep(5)
        await msg.delete()
        
def setup(client):
    client.add_cog(AutoReactor(client))
