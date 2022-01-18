import discord
from discord.ext import commands
from modules import bot as v

class user(commands.Cog):
    def __init__(self, client):
        self.client = client

    #avatar, #userinfo
    
    @commands.command()
    async def avatar(self, ctx, *,  member : discord.Member=None):
        if member is None:
            member = ctx.author

        embed = discord.Embed(title=f"{member.display_name}'s Avatar!", colour=v.yellow, timestamp=ctx.message.created_at)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["user-info", "u-info","uinfo"])
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        perm_list = [perm[0] for perm in member.guild_permissions if perm[1]]
        created = member.created_at.strftime("%a, %#d %B %Y")
        joined = member.joined_at.strftime("%a, %#d %B %Y")

        roles = [role for role in member.roles]
        roles = [role.mention for role in roles]

        userinfo_embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
        userinfo_embed.set_author(name=f"user info - {member}")
        userinfo_embed.set_thumbnail(url=member.avatar_url)

        userinfo_embed.add_field(name="Name + #Tag", value=f"`{member}`", inline=False)
        userinfo_embed.add_field(name="Member ID ", value=f"`{member.id}`", inline=False)
        userinfo_embed.add_field(name="Member Top role", value=f"{member.top_role.mention}", inline=False)
        userinfo_embed.add_field(name="Member Permissions: ", value=f"`{perm_list}`", inline=False)
        userinfo_embed.add_field(name=f"Roles ({len(roles)})", value=f"{roles}", inline=False)        
        userinfo_embed.add_field(name="Server Booster: ", value=f"`{(str(bool(member.premium_since)))}`", inline=False)
        userinfo_embed.add_field(name="Joined at: ", value=f"`{joined}`", inline=False)
        userinfo_embed.add_field(name="Created at: ", value=f"`{created}`", inline=False)

        userinfo_embed.set_footer(text=f" |   {ctx.author.name}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=userinfo_embed)


def setup(client):
    client.add_cog(user(client))