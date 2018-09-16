import thighs, discord, asyncio, furry, json, nekos
from discord.ext import commands

thigh_key = '2M4oFqhjv3RejNhBP1ZaSA5H7S1JXrwb12J47JZAzBX2V1i3W6KB8xT7.Q8jozfw2udVL4flu..cvzroEqiagAZrkYkl6iC832uEsX.y.Dmq1O93ivAo..NPlg.9XmeN6twLcOaXZv3O2vBFA3E6N5mYa1U.96QwzAUCZDgq.8luykGH9X3b.1jDDiFs7ZJrjvHEqM9.yuqVn.aHooJ1xihKuHkPe1KsyH.XFw0u1afB1DUjrZ49wSUmjR'

class NSFW:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def thighs(self, ctx):
        """Sends some thigh pictures, only usable in NSFW channels"""
        if ctx.channel.is_nsfw() == True:
            api = thighs.ThighAPI(api_key=thigh_key)

            image = api.get('thighs', 'random')

            if image.status_code != '200':
                await ctx.send("**Sorry, The API call returned nothing!**")
            else:
                thigh_embed = discord.Embed(colour=0xDEADBF)
                thigh_embed.set_image(url=image.url)
                thigh_embed.set_footer(text="Provided by the ThighAPI")
                await ctx.send(embed=thigh_embed)
        else:
            await ctx.send(":x: {}, You can't use NSFW commands outside of an NSFW channel!".format(ctx.author.mention))

    @commands.command(aliases=['furr', 'yiff'])
    async def furry(self, ctx, endpoint = None):
        """Sends a furry photo, if you provide a NSFW argument it will display a nsfw image but that argument can only be used in a NSFW channel"""
        api = furry.FurryAPI()
        furryEmbed = discord.Embed(color=0xDEADBF).set_footer(text="Provided by sheri.fun")
        if endpoint == 'nsfw':
            if ctx.channel.is_nsfw() == True:
                img_get = api.get('yiff')
                img = json.loads(img_get)['url']
                if img == None:
                    await ctx.send(":x: API returned nothing.")
                else:
                    furryEmbed.set_image(url=img)
                    await ctx.send(embed=furryEmbed)
            else:
                await ctx.send(":x: {}, You can't use NSFW commands outside of an NSFW channel!".format(ctx.author.mention))
        elif endpoint == 'sfw' or endpoint == None:
            img_get = api.get('mur')
            img = json.loads(img_get)['url']
            if img == None:
                await ctx.send(":x: API returned nothing")
            else:
                furryEmbed.set_image(url=img)
                await ctx.send(embed=furryEmbed)
        else:
            await ctx.send(":warning: {}, That isn't a proper filter".format(ctx.author.mention))

    @commands.command(aliases=['nekos'])
    async def neko(self, ctx, tag = None):
        """Uses the neko.life library, this provides SFW and NSFW tags, so we've just blacklisted all from non-NSFW channels"""
        if ctx.channel.is_nsfw() == True:
            possible = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
            'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk',
            'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron',
            'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar',
            'gasm', 'poke', 'anal', 'hentai', 'avatar', 'erofeet', 'holo',
            'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'pussy_jpg',
            'pwankg', 'classic', 'kuni', 'waifu', 'femdom',
            'erok', 'fox_girl', 'boobs', 'Random_hentai_gif',
            'smallboobs', 'ero']

            if tag not in possible:
                await ctx.send(":warning: You didn't use a valid tag... Here's all valid tags:\n```{}```".format(possible))
                return
            else:
                img = nekos.img(tag)

            if img == None:
                await ctx.send(":x: API returned nothing.")
            else:
                nekoEmbed = discord.Embed(color=0xDEADBF).set_footer(text="Provided by nekos.life")
                nekoEmbed.set_image(url=img)
                await ctx.send(embed=nekoEmbed)
        else:
            await ctx.send(":x: {}, You can't use NSFW commands outside of an NSFW channel!".format(ctx.author.mention))

def setup(client):
    client.add_cog(NSFW(client))