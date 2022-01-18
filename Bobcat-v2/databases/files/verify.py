import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle
from mods import bot as v

class Verification(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    @commands.has_any_role(865166038354231296)
    async def verify(self, ctx, channel: discord.TextChannel=None):
        embed = discord.Embed(title="Verification",
                            description="Welcome and thanks for joining us!\n\n"
                                        f"**__Please make sure you do the following after verifying:__**\n<:arroww:880572575166627850> Read the [**Rules**](https://canary.discord.com/channels/652899105496104960/837719832563941476/882983280968863764)\n<:arroww:880572575166627850> Select your **Roles**\n<:arroww:880572575166627850> Check out our **Socials**\n<:arroww:880572575166627850> And explore our server for its entirety!",
                            colour=v.yellow)

        embed.set_image(url=v.banner)
        await ctx.send(embed=embed,
                        components=[Button(style=ButtonStyle.blue, label="Verify now!", emoji='✅')])
        await ctx.message.delete()
        

def setup(client):
    client.add_cog(Verification(client))