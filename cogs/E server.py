import discord
from discord.ext import commands
from modules import bot as v

class server(commands.Cog):
    def __init__(self, client):
        self.client = client

    #membercount, servericon, serverbanner, serverinfo, roleinfo

    @commands.command()
    async def membercount(self, ctx):
        embed = discord.Embed(title=f"There are {str(ctx.guild.member_count)} members!", colour=v.yellow, timestamp=ctx.message.created_at)
        embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon.url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["sicon", "guildicon"])
    async def servericon(self, ctx):
        if not ctx.guild.icon_url:
            await ctx.send("There is no Icon to show")
            return

        sicon_Embed = discord.Embed(title="", color=v.yellow)
        sicon_Embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=sicon_Embed)

    @commands.command(aliases=["serverinfo", "server-info", "serverinformation", "guildinfo", "si", "gi"])
    async def sinfo(self, ctx):
        embed = discord.Embed(title="Server information", color=v.yellow)

        embed.set_thumbnail(url=ctx.guild.icon.url)

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        embed.add_field(name="Server name", value=ctx.guild.name, inline=False)
        embed.add_field(name="ID", value=ctx.guild.id, inline=False)
        embed.add_field(name="Owner", value=ctx.guild.owner.mention, inline=False)
        embed.add_field(name="Region", value=ctx.guild.region, inline=False)
        embed.add_field(name="Created at", value=ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)
        embed.add_field(name="Members", value=len(list(filter(lambda m: not m.bot, ctx.guild.members))), inline=False)
        embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, ctx.guild.members))), inline=False)
        embed.add_field(name="Banned members", value=len(await ctx.guild.bans()), inline=False)
        embed.add_field(name="Text channels", value=len(ctx.guild.text_channels), inline=False)
        embed.add_field(name="Voice channels", value=len(ctx.guild.voice_channels), inline=False)
        embed.add_field(name="Categories", value=len(ctx.guild.categories), inline=False)
        embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=False)
        embed.add_field(name="Invites", value=len(await ctx.guild.invites()), inline=False)

        embed.add_field(name="Member statuses", value=f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", inline=False)
        embed.add_field(name="Server icon", value= f"{ctx.guild.icon.url}", inline=False)
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(server(client))