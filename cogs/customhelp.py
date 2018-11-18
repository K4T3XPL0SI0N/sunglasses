import discord, asyncio
from discord.ext import commands

_commandPrefix = "j" # Replace with the bot's prefix

class HelpCommands():
    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')

    @commands.command(aliases=['h'])
    async def help(self, ctx, *, com = commands.command):

        appInfo = await self.client.application_info()

        if com == None:
            # send regular help message, list of all commands
            cogs = {} # this will store the cogs that exist, to help organize commands into special categories
            cogList = list(self.client.cogs)
            cogList.append(None)
            for cog in cogList:
                cogs[cog] = [] # this will store each command

            for command in self.client.commands:
                if command.cog_name in cogs:
                    if command.hidden != True:
                        cogs[command.cog_name].append(command.name) # add command to the containing cog's list
                    elif command.hidden == True and ctx.author.id == appInfo.owner.id:
                        cogs[command.cog_name].append(command.name) # if the command is hidden add it only if the help user is the bot owner
                else:
                    print("Uhh... Something went wrong with the help command uwu")

            helpEmbed = discord.Embed(colour=0xFFFFFF, title="Help Dialog", description="`{0}` is this bot's prefix\nUse `{0}help <command>` if you'd like help on a certain command".format(_commandPrefix))
            helpEmbed.set_thumbnail(url=appInfo.icon_url)
            for c in cogs:
                if len(cogs[c]) > 0:
                    helpEmbed.add_field(name=str(c) + " [`{}`]".format(len(cogs[c])), value=", ".join(cogs[c]), inline=False) # this field contains the name of the cog and all the commands in a list like, this, and, that
                else:
                    pass # It wouldn't add a cog that has zero commands because no help is needed for that command
            
            await ctx.send(embed=helpEmbed)
        else:
            # send help regarding the command "com" unless the command doesn't exist, then return "Command Not Found" error
            print(com.usage)

def setup(client):
    client.add_cog(HelpCommands(client))
