import discord, asyncio, random
from discord.ext import commands

INFORMATION = {
    "GUILD ID": 488210121063923742,
    "ROLE ID" : 497201609147940884,
    "SHIFT DELAY" : 1.5
}

INFORMATION['SHIFT DELAY'] = INFORMATION['SHIFT DELAY'] * 500 # Changes seconds to milliseconds

def get_role_id(roles, id):
    for role in roles:
        if role.id == id:
            return role
        else:
            pass
    return None

class ColorShid():
    def __init__(self, client):
        self.client = client
        self.client.loop.create_task(self.colorLoop())

    def colorLoop(self):
        #await self.client.wait_until_ready()
        guild = self.client.get_guild(INFORMATION['GUILD ID'])
        role = get_role_id(guild.roles, INFORMATION['ROLE ID'])       

        while True:
            color = discord.Color.from_rgb(1,2,3)
            await role.edit(colour=color, reason="Automatic Color Switch")
            await asyncio.sleep(INFORMATION['SHIFT DELAY'])

def setup(client):
    client.add_cog(ColorShid(client))



