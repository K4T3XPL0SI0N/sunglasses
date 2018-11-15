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
                
def setup(client):
    client.add_cog(AutoReactor(client))
