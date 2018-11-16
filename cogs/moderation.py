import discord, asyncio, os, json
from discord.ext import commands

class Moderation:
    def __init__(self, client):
        self.client = client

    async def on_message(self, msg):
        guild = self.client.get_guild(468119888058122241)
        
        if msg.channel == guild.get_channel(487768754155945995):
            if len(msg.attachments) == 0 and ctx.guild.get_role(468120454180372480) not in msg.author.roles: # there are no pictures attached to this image, so it's not a selfie
                try:
                    await msg.delete()
                    await msg.author.send("**{}** : Hey! You're not allowed to post anything but selfies in <#487768754155945995>".format(guild.name))
                except:
                    pass
            else:
                pass # because it is a selfie uwu
        
    @commands.command(aliases=['b', 'banish'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason : str = None):
        """Bans a member, then dm's them a reason (if provided)"""
        if reason == None:
            reason = "No reason provided." 
        try:
            await member.send(":hammer:**You were banned from **`{}`** for the reason: **`{}`**!**".format(ctx.guild.name, reason))
        except:
            pass
        try:
            await member.ban(reason=reason)
        except Exception as err:
            await ctx.send(":warning: **Couldn't ban `{}`!**\n*reason: `{}`".format(member, err))
        await ctx.send(embed=discord.Embed(title=':hammer: User banned!', description="{} has been banned for `{}`!".format(member, reason), color=0xFF0000))

    @commands.command(aliases=['k', 'boot'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        """Kicks a member, then dm's them a reason (if provided)"""
        try:
            await member.send(":boot:**You were kicked from **`{}`** for the reason: **`{}`**!**".format(ctx.guild.name, reason))
        except:
            pass
        try:
            await member.kick()
        except Exception as err:
            await ctx.send(":warning: **Couldn't kick `{}`!**\n*reason: `{}`".format(member, err))
        await ctx.send(embed=discord.Embed(title=':boot: User kicked!', description="{} has been kicked for `{}`!".format(member, reason), color=0xFF0000))

    @commands.command(aliases=['p','massdelete'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, count : int):
        """Purges a given amount of messages"""
        if count > 100:
            await ctx.send(":warning: **The global purge limit is set to `100` to reduce lag and to prevent the bot from crashing!**")
            return
        else:
            try:
                deleted = await ctx.channel.purge(limit=count + 1)
                asyncio.sleep(0.5)
                msgdel = await ctx.send(":thumbsup: {} Messages deleted".format(len(deleted)))
            except Exception as err:
                msgdel = await ctx.send(":x: **Some or all messages couldn't be deleted.**\n*Error: *`{}`".format(err))
            await asyncio.sleep(5)
            await msgdel.delete() # removes message after purge

    @commands.command(aliases=['rb'])
    @commands.has_permissions(administrator=True)
    async def roleban(self, ctx, role : discord.Role, *, reason = None):
        """Bans all users with the role provided and alerts them"""
        failed_bans = []
        finished_bans = []
        for member in role.members:
            try:
                member.send("**You were banned from {} for the reason: `{}`**".format(ctx.guild.name, reason))
            except:
                pass

            try:
                await member.ban()
            except:
                failed_bans.append(member.id)
            else:
                finished_bans.append(member.id)
        await ctx.send("Users banned: `{}`\nFailed bans: `{}`".format(len(finished_bans), len(failed_bans)))

    @commands.command(aliases=['lock'])
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx):
        role = ctx.guild.default_role
        await ctx.channel.set_permissions(role, send_messages=False)
        await ctx.send("{0.mention} has locked down {1.mention}".format(ctx.author, ctx.channel))    
    
    @commands.command(aliases=['release'])
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        role = ctx.guild.default_role
        await ctx.channel.set_permissions(role, send_messages=True)
        await ctx.send("{0.mention} has unlocked {1.mention}".format(ctx.author, ctx.channel))   

def setup(client):
    client.add_cog(Moderation(client))
