import discord, asyncio, os, inspect
from discord.ext import commands

class Utility:
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *, code):
        """Evaluates Code"""
        code = code.strip("` ")
        pyform = '```python\n{}\n```'


        embedD = discord.Embed(colour=0xDEADBF)

        try:
            result = eval(code)
            if inspect.isawaitable(result):
                result = await result
            print(result)
        except Exception as e:
            embedD.add_field(name="Input",value=pyform.format(code), inline=False)
            embedD.add_field(name="Output", value=pyform.format(type(e).__name__, e), inline=False)
            await ctx.send(embed=embedD)
        else:
            embedD.add_field(name="Input",value=pyform.format(code), inline=False)
            embedD.add_field(name="Output", value=pyform.format(result), inline=False)
            await ctx.send(embed=embedD)
        await ctx.message.delete()
        
def setup(client):
    client.add_cog(Utility(client))
