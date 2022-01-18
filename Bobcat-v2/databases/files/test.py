import discord
from discord.ext import commands

from discord_components import (
    Button,
    ButtonStyle,
)

class ExampleCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def button(self, ctx):
        embed=discord.Embed()
        embed.add_field(name="Test", value="This a test")

        await ctx.send(
            embed=embed, 
            components=[
                Button(style=ButtonStyle.blue, label="Test Button", custom_id="button1")])

        res = await self.client.wait_for(
            "button_click", check=lambda inter: inter.custom_id == "button1"
        )

        await res.send(content="Button Clicked")


def setup(client):
    client.add_cog(ExampleCog(client))

