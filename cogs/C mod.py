import discord, datetime, random, asyncio, aiohttp
from io import BytesIO
from discord.ext import commands
from modules import bot as v

class mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    #clear, kick, ban, unban, mute, unmute, slowmode, createemoji, lockdown, unlock

# clear [amount]
    @commands.command(aliases=["purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        if amount == 0:
            clear = discord.Embed(title="❌ The amount cant be 0!", color=v.error)
            await ctx.send(embed=clear)
            return

        if amount > 150:
            clear = discord.Embed(title="❌ You cannot delete more then 150 messages!", color=v.error)
            await ctx.send(embed=clear)
            return

        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Cleared {amount} messages", delete_after=5.0)
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `Manage Messages` permission", color=v.error)
            await ctx.send(embed=error)
            return

# kick [member] [reason]
    @commands.command(aliases=["k"])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, *, reason=None):
        if member == ctx.guild.owner:
            kick = discord.Embed(title="❌ You can't kick the owner of this server", color=v.error)
            await ctx.send(embed=kick)
            return

        if member == ctx.message.author:
            kick = discord.Embed(title="❌ You can't kick yourself", color=v.error)
            await ctx.send(embed=kick)
            return

        if member == None:
            kick = discord.Embed(title="❌ Mention a member that you want to kick", color=v.error)
            await ctx.send(embed=kick)
            return

        else:
            await member.send(f"You got kicked from **{ctx.guild}** ```Reason: {reason}```")

            await member.kick(reason=reason)
            await ctx.send(f"{member} kicked for ```Reason: {reason}```")
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `kick Members` permission", color=v.error)
            await ctx.send(embed=error)
            return

# ban [member] [reason]
    @commands.command(aliases=["b"])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, *, reason=None):
        if member == ctx.guild.owner:
            ban = discord.Embed(title="❌ You can't ban the owner of this server", color=v.error)
            await ctx.send(embed=ban)
            return

        if member == ctx.message.author:
            ban = discord.Embed(title="❌ You can't ban yourself", color=v.error)
            await ctx.send(embed=ban)
            return

        if member == None:
            ban = discord.Embed(title="❌ Mention a member that you want to ban", color=v.error)
            await ctx.send(embed=ban)
            return
        
        else:
            await member.send(f"You got banned from **{ctx.guild}** ```Reason: {reason}```")

            await member.ban(reason=reason)
            await ctx.send(f"{member} Banned for ```Reason: {reason}```")
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `Ban Members` permission", color=v.error)
            await ctx.send(embed=error)
            return

# unban [member]
    @commands.command(aliases=["ub"])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.User):
        if member == None:
            unban = discord.Embed(title="❌ Mention a member that you want to unban", color=v.error)
            await ctx.send(embed=unban)
            return

        await member.send(f"You got unbanned from **{ctx.guild}**")

        await ctx.guild.unban(user=member)
        await ctx.send(f"{member} has been unbanned")
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `Ban Members` permission", color=v.error)
            await ctx.send(embed=error)
            return
        
# mute
    @commands.command(aliases=["m"])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member=None, *, reason=None):
        if member == ctx.guild.owner:
            mute = discord.Embed(title="❌ You can't mute the owner of this server", color=v.error)
            await ctx.send(embed=mute)
            return

        if member == ctx.message.author:
            mute = discord.Embed(title="❌ You can't mute yourself", color=v.error)
            await ctx.send(embed=mute)
            return

        if member == None:
            mute = discord.Embed(title="❌ Mention a member you want to mute", color=v.error)
            await ctx.send(embed=mute)
            return

        else:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

            for channel in ctx.guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False)
            
            await member.add_roles(mutedRole, reason=reason)
            
            await member.send(f"You got muted from **{ctx.guild}** for ```Reason: {reason}```")
            await ctx.send(f"{member} muted ```{reason}```")
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `kick Members` permission", color=v.error)
            await ctx.send(embed=error)
            return

# unmute
    @commands.command(aliases=["um"])
    @commands.has_permissions(kick_members=True)   
    async def unmute(self, ctx, member: discord.Member=None):
        if member == None:
            unmute = discord.Embed(title="❌ Mention a member you want to unmute", color=v.error)
            await ctx.send(embed=unmute)
            return

        else:
            mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
            await member.remove_roles(mutedRole)
            
            await member.send(f"You got unmuted from **{ctx.guild}**")
            await ctx.send(f"{member} unmuted")
    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `kick Members` permission", color=v.error)
            await ctx.send(embed=error)
            return


    @commands.command(aliases=["sm"])
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        if seconds == None:
            mute = discord.Embed(title="❌ You forgot to put an amount of seconds!", color=v.error)
            await ctx.send(embed=mute)
            return 

        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds :)")
    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `kick Members` permission", color=v.error)
            await ctx.send(embed=error)
            return


# stealemoji [url] [name]
    @commands.command(aliases=["addemoji", "ae", "ce", "steal"])
    @commands.has_permissions(manage_emojis=True)
    async def createemoji(self, ctx, url: str, *, name):
        guild = ctx.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    img_or_gif = BytesIO(await r.read())
                    b_value = img_or_gif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=b_value, name=name)
                        await ctx.message.delete()
                        await ctx.send(f"Successfully created emoji: <:{name}:{emoji.id}>")
                        await ses.close()
                        
                    else:
                        await ctx.send(f'❌ Error when making request | {r.status} response.')
                        await ses.close()
                        
                except discord.HTTPException:
                    await ctx.send('❌ File size is too big!')
    @createemoji.error
    async def createemoji_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `Manage Emojis` permission", color=v.error)
            await ctx.send(embed=error)
            return

# lockdown
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send(ctx.channel.mention + " Is now in lockdown!")
    @lockdown.error
    async def lockdown_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `Manage Channels` permission", color=v.error)
            await ctx.send(embed=error)
            return

# unlock
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send(ctx.channel.mention + " Has been unlocked!")
    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            error=discord.Embed(title="❌ Missing `Manage Channels` permission", color=v.error)
            await ctx.send(embed=error)
            return


def setup(client):
    client.add_cog(mod(client))