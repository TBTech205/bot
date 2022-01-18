import discord, random
import giphy_client
from discord.ext import commands
from modules import bot as v

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    #b!help

    @commands.command(aliases=["pong"])
    async def ping(self, ctx):
        ping_Embed = discord.Embed(color=v.yellow)
        ping_Embed.add_field(name="Bot's ping", value=f"{round(self.client.latency*1000)}ms", inline=False)
        await ctx.send(embed=ping_Embed)
    
    @commands.command()
    async def dead(self, ctx):
        dead_Embed = discord.Embed(color=v.yellow)
        dead_Embed.add_field(name="Dead Chat", value=f"The chat was declared dead by {ctx.author.display_name}", inline=False)  
        dead_Embed.set_footer(icon_url=ctx.author.avatar_url, text=f" |   {ctx.author.name}")  
        await ctx.message.delete()
        await ctx.send(embed=dead_Embed)

    @commands.command()
    async def diceroll(self, ctx):
        responses = ["1","2","3","4","5","6"]
    
        embed = discord.Embed(title="Dice Roll", color=v.yellow)
        embed.add_field(name=f"you rolled the number: ", value=f"{random.choice(responses)}  <:dicer:879688529125470259>", inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f" |   {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["flip"])
    async def coinflip(self, ctx):
        coin = ["Heads", "Tales"]
    
        coin_embed = discord.Embed(title="Heads or Tales", color=v.yellow)
        coin_embed.add_field(name=f"Result is...", value=f"{random.choice(coin)}", inline=False)
        coin_embed.set_footer(icon_url=ctx.author.avatar_url, text=f" |   {ctx.author.name}")
        await ctx.send(embed=coin_embed)

    @commands.command(aliases=["suggestion"])
    async def suggest(self, ctx, trigger, *, suggestion: str):
        em = discord.Embed(title="Your suggestion has been recorded!", color=discord.Color.green())
        await ctx.reply(embed=em)

        sugg_em = discord.Embed(title=f"New Suggestion", color=0xffff00)
        sugg_em.set_thumbnail(url=ctx.author.avatar_url)
        sugg_em.add_field(name=f"shit", value=f"{trigger}", inline=False)
        sugg_em.add_field(name=f"fuxk", value=f"{suggestion}", inline=False)
        sugg_em.add_field(name=f"author", value=f"{ctx.author.display_name}", inline=False)
        mes= await self.client.get_channel(894911154550353951).send(embed=sugg_em)
        await mes.add_reaction('✅')
    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            error=discord.Embed(title="Missing Required Argument please do \n!suggest {trigger} {suggestion}", color=0xed5757)
            await ctx.send(embed=error)
            return

def setup(client):
    client.add_cog(misc(client))