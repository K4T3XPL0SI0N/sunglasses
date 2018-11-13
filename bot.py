import discord, asyncio, os, sys
from discord.ext import commands
sys.path.insert(0, './cogs')

bot = commands.Bot(command_prefix=commands.when_mentioned_or("j"), pm_help=True)
all_cogs = ['utility', 'fun', 'info', 'moderation', 'error','rp', 'multicolor'] # list of cogs

@bot.event
async def on_ready():
    print("Bot is ready :ok_hand:")

@bot.event
async def on_command_completion(ctx):
    if str(ctx.command) == 'help':
        if isinstance(ctx.channel, discord.TextChannel) == True:
            msg = await ctx.channel.send("{} Check your direct messages!".format(ctx.author.mention))
            await asyncio.sleep(3)
            await msg.delete()
    else:
        pass

@bot.command()
@commands.is_owner()
async def load_cog(ctx, cog):
    """Loads a Cog"""
    try:
        bot.load_extension(cog)
        await ctx.send("```python\nCog: '{}' Loaded Properly!\n```".format(cog))
    except Exception as err:
        await ctx.send("```python\nTried to Load Cog: '{}', Exception Recieved: ['{}']\n```".format(cog, err))

@bot.command()
@commands.is_owner()
async def unload_cog(ctx, cog):
    """Unloads a Cog"""
    try:
        bot.unload_extension(cog)
        await ctx.send("```python\nCog: '{}' Unloaded Properly!\n```".format(cog))
    except Exception as err:
        await ctx.send("```python\nTried to Unload Cog: '{}', Exception Recieved: ['{}']\n```".format(cog, err))

@bot.command()
@commands.is_owner()
async def close(ctx):
    """Closes the bot's connection"""
    try:
        await bot.close()
    except Exception as err:
        await ctx.send("Couldn't close the connection: ['{}']".format(err))

@bot.command()
@commands.is_owner()
async def reload_cog(ctx, cog):
    """Reloads a Cog Quickly"""
    try:
        bot.unload_extension(cog)
        await asyncio.sleep(2)
        bot.load_extension(cog)
        await ctx.send("```python\nCog: '{}' Reloaded Properly!\n```".format(cog))
    except Exception as err:
        await ctx.send("```python\nCog '{}' Couldn't Reload: ['{}']```".format(cog, err))

@bot.command(aliases=['cogs', 'cl'])
@commands.is_owner()
async def cog_list(ctx):
    """Lists all the cogs enabled"""
    p = ''
    for cog in bot.cogs:
        p += cog +'\n'    
    await ctx.send(embed=discord.Embed(title="**Currently Enabled Cogs**",description=p, color=0xed1c24))

if __name__ == "__main__":
    for extension in all_cogs:
        try:
            bot.load_extension(extension)
            print('LOADED EXTENSION "{}" PROPERLY!'.format(extension))
        except Exception as err:
            print('ERROR LOADING "{}" FOR REASON [{}]'.format(extension, err))
            
    bot.run(os.getenv('TKN'))
