import discord, asyncio, inspect, colorama, json, os, io, textwrap, copy, traceback
from contextlib import redirect_stdout
from discord.ext import commands

class Utility:
    def __init__(self, client):
        self.client = client
        self._last_result = None

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    async def __local_check(self, ctx):
        return await self.client.is_owner(ctx.author)

    def get_syntax_error(self, e):
        if e.text is None:
            return '```py\n{0.__class__.__name__}: {0}\n```'.format(e)
        return '```py\n{0.text}{"^":>{0.offset}}\n{0.__class__.__name__}: {0}```'.format(e)

    @commands.command()
    async def ping(self, ctx):
        """Checks to see if the bot is online"""    
        print("Ponged!")
        await ctx.send("Ponged!\nWebsocket: `{}ms`".format(round(self.client.latency * 500, 2)))

    @commands.is_owner()
    @commands.command(pass_context=True, hidden=True, name='eval')
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""

        env = {
            'client': self.client,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = 'async def func():\n' + textwrap.indent(body, "  ")

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send('```py\n{0.__class__.__name__}: {0}\n```'.format(e))

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send('```py\n{0}'.format(value) + traceback.format_exc() + '\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send('```py\n' + value + '\n```')
            else:
                self._last_result = ret
                await ctx.send('```py\n'+ value + ret + '\n```')

def setup(client):
    client.add_cog(Utility(client))
