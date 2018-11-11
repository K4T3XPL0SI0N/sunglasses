import discord, asyncio
from discord.ext import commands

INFORMATION = {
    "GUILD ID": 488210121063923742,
    "ROLE ID" : 511223354296893441,
    "SHIFT DELAY" : 1.5
}

INFORMATION['SHIFT DELAY'] = INFORMATION['SHIFT DELAY'] * 500 # Changes seconds to milliseconds

class ColorShid():
    def __init__(self, client):
        self.client = client
        self.client.loop.create_task(self.colorLoop())

    def colorLoop(self):
        await client.wait_unitl_ready()
        guild = self.client.get_guild(INFORMATION['GUILD ID'])
        role = guild.get_role(INFORMATION['ROLE ID'])       

        while True:
            role.edit(colour=discord.Color(r=random.randint(0,255), g=random.randint(0,255), b=random.randint(0,255)), reason="Automatic Color Switch")
            asyncio.sleep(INFORMATION['SHIFT DELAY'])

def setup(client):
    client.add_cog(ColorShid(client))



