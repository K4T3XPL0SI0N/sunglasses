import discord, nekos, asyncio, random
from discord.ext import commands

class Roleplay:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kiss(self, ctx, whom : discord.Member):
        """Kiss someone special~ <3"""
        img = nekos.img('kiss')
        kissEmbed = discord.Embed(colour=0xDEADBF).set_footer(text="Powered by nekos.life")        
        kissEmbed.set_author(name="{0} kissed {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
        kissEmbed.set_image(url=img)
        await ctx.send(embed=kissEmbed)

    @commands.command()
    async def pat(self, ctx, whom : discord.Member):
        """Pat somebody~ <3"""
        img = nekos.img('pat')
        kissEmbed = discord.Embed(colour=0xDEADBF).set_footer(text="Powered by nekos.life")        
        kissEmbed.set_author(name="{0} patted {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
        kissEmbed.set_image(url=img)
        await ctx.send(embed=kissEmbed)

#    @commands.command()
#    async def spank(self, ctx, whom : discord.Member):
#        img = nekos.img('spank')
#        kissEmbed = discord.Embed(colour=0xDEADBF)        
#        kissEmbed.set_author(name="{0} spanked {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
#        kissEmbed.set_image(url=img)
#        await ctx.send(embed=kissEmbed)

    @commands.command()
    async def cuddle(self, ctx, whom : discord.Member):
        """Cuddle somebody you care about~ <3"""
        img = nekos.img('cuddle')
        kissEmbed = discord.Embed(colour=0xDEADBF).set_footer(text="Powered by nekos.life")        
        kissEmbed.set_author(name="{0} cuddled {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
        kissEmbed.set_image(url=img)
        await ctx.send(embed=kissEmbed)

    @commands.command()
    async def hug(self, ctx, whom : discord.Member):
        """Hug someone close to you~ <3"""
        img = nekos.img('hug')
        kissEmbed = discord.Embed(colour=0xDEADBF).set_footer(text="Powered by nekos.life")        
        kissEmbed.set_author(name="{0} hugged {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
        kissEmbed.set_image(url=img)
        await ctx.send(embed=kissEmbed)

    @commands.command()
    async def slap(self, ctx, whom : discord.Member):
        """Slap someone"""
        img = nekos.img('slap')
        kissEmbed = discord.Embed(colour=0xDEADBF).set_footer(text="Powered by nekos.life")        
        kissEmbed.set_author(name="{0} slapped {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
        kissEmbed.set_image(url=img)
        await ctx.send(embed=kissEmbed)

    @commands.command()
    async def tickle(self, ctx, whom : discord.Member):
        """Tickle somebody and make them laugh :)"""
        img = nekos.img('tickle')
        kissEmbed = discord.Embed(colour=0xDEADBF).set_footer(text="Powered by nekos.life")        
        kissEmbed.set_author(name="{0} tickled {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
        kissEmbed.set_image(url=img)
        await ctx.send(embed=kissEmbed)

    @commands.command()
    async def feed(self, ctx, whom : discord.Member):
        """Feed somebody to make their tummy full~ <3"""
        img = nekos.img('feed')
        kissEmbed = discord.Embed(colour=0xDEADBF).set_footer(text="Powered by nekos.life")
        kissEmbed.set_author(name="{0} fed {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
        kissEmbed.set_image(url=img)
        await ctx.send(embed=kissEmbed)

    @commands.command()
    async def poke(self, ctx, whom : discord.Member):
        """Poke somebody >:)"""
        img = nekos.img('poke')
        kissEmbed = discord.Embed(colour=0xDEADBF).set_footer(text="Powered by nekos.life")        
        kissEmbed.set_author(name="{0} poked {1}".format(ctx.author, whom), icon_url=ctx.author.avatar_url)
        kissEmbed.set_image(url=img)
        await ctx.send(embed=kissEmbed)

def setup(client):
    client.add_cog(Roleplay(client))
