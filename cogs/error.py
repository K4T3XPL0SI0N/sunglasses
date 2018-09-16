import discord, asyncio
from discord.ext import commands

class ErrorHandler:
    def __init__(self, client):
        self.client = client

    async def on_command_error(self, ctx, err):

        if hasattr(ctx.command, 'on_error'):
            
            return

        ignored_errors = (commands.CommandNotFound)

        err = getattr(err, 'original', err)

        if isinstance(err, ignored_errors):
            return

        elif isinstance(err, (commands.MissingRequiredArgument, commands.BadArgument)):
            await ctx.send(":warning: **COMMAND ERROR**\n`{}`".format(err))

def setup(client):
    client.add_cog(ErrorHandler(client))
