import discord, asyncio, random
from discord.ext import commands

INFORMATION = {
    "GUILD ID": 468119888058122241,
    "ROLE ID" : 468120454180372480,
    "SHIFT DELAY" : 1.5
}

#INFORMATION['SHIFT DELAY'] = INFORMATION['SHIFT DELAY'] * 500 # Changes seconds to milliseconds

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

    async def colorLoop(self):
        await self.client.wait_until_ready()
        guild = self.client.get_guild(INFORMATION['GUILD ID'])
        role = get_role_id(guild.roles, INFORMATION['ROLE ID'])       

        while True:
            color = discord.Color.from_rgb(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            await role.edit(colour=color)
            await asyncio.sleep(INFORMATION['SHIFT DELAY'])

def setup(client):
    client.add_cog(ColorShid(client))



