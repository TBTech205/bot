import discord
from discord.ext import commands

class helpc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em= discord.Embed(title="Help", color=0xffff00)

        em.add_field(name="__Main Commands__", value="`b!help commands`")
        em.add_field(name="__Mod Commands__", value="`b!help moderator`")
        em.set_footer(text="© BobCat Commands")
        
        await ctx.send(embed=em)

    @help.command(aliases=["commands", "cmds"])
    async def _commands(self, ctx):
        em= discord.Embed(title="Help: Commands", color=0x808000)

        em.add_field(name="`b!help` - List of BobCats Commands", value="** **", inline=False)
        em.add_field(name="`b!afk` - Sets your AFK", value="** **", inline=False) #afk.py 
        em.add_field(name="`b!ping` - Shows BobCats latency", value="** **", inline=False)
        em.add_field(name="`b!diceroll` - Rolls a dice of 1-6", value="** **", inline=False)
        em.add_field(name="`b!coinflip` - Lets Flip a Coin Heads/Tails", value="** **", inline=False)
        em.add_field(name="`b!avatar` - Shows your avatar", value="** **", inline=False)
        em.add_field(name="`b!dead` - Shows a dead chat message", value="** **", inline=False)
        em.add_field(name="`b!rank` - Shows Shows your rank", value="** **", inline=False)


        em.add_field(name="** **", value="** **", inline=False)
        em.add_field(name="**Help: Server**", value="** **", inline=False)
        em.add_field(name="`b!membercount` - Shows the membercount for the server", value="** **", inline=False)
        em.add_field(name="`b!servericon` - Shows the server icon", value="** **", inline=False)
        em.add_field(name="`b!serverbanner` - Shows the server banner", value="** **", inline=False)
        em.add_field(name="`b!serverinfo` - Shows info about the server", value="** **", inline=False)
        em.add_field(name="`b!roleinfo` - Shows info about a server role", value="** **", inline=False)
        
        em.set_footer(text="© BobCat Commands")
        await ctx.send(embed=em)

    @help.command(aliases=["mod"])
    async def moderator(self, ctx):
        mod=discord.Embed(title="Help: Moderation", color=0x808000)

        mod.add_field(name="`b!clear` `[number]` - Deletes a number of messages in a channel", value="** **", inline=False) 
        mod.add_field(name="`b!kick` `@user` `[reason]` - Kicks the member you mentioned", value="** **", inline=False)
        mod.add_field(name="`b!ban` `@user` `[reason]` - Bans a member from the server ", value="** **", inline=False)
        mod.add_field(name="`b!unban` `@user` - Unbans a member from the server", value="** **", inline=False)

        mod.add_field(name="`b!mute` `@user` `[reason]` - Mutes the member you mentioned", value="** **", inline=False)
        mod.add_field(name="`b!unmute` `@user` - Unmutes the member you mentioned ", value="** **", inline=False)
        mod.add_field(name="`b!slowmode` `[seconds]`- Sets the channels slowmode", value="** **", inline=False)
        mod.add_field(name="`b!giveaway` `[time]` `[tilte]` - Creates a giveaway in a channel", value="** **", inline=False)

        mod.add_field(name="** **", value="** **", inline=False)
        mod.add_field(name="**Help: Leveling**", value="Required Permission `administrator`", inline=False)
        mod.add_field(name="`b!levelconfig` `<on/off>` - Sets up the level system", value="** **", inline=False)
        mod.add_field(name="`b!setlevelchannel` `[channel]` - Sets the message channel", value="** **", inline=False)


        mod.set_footer(text="© BobCat Commands")
        await ctx.send(embed=mod)

    @help.command(aliases=["eco", "economy", "Economy"])
    async def money(self, ctx):
        em= discord.Embed(title="Help: Money", color=0x808000)

        em.add_field(name="`b!leaderboard` - Shows you the leaderboard", value="** **", inline=False)
        em.add_field(name="`b!balance` - Shows somes balance", value="** **", inline=False) #afk.py 
        em.add_field(name="`b!shop` - Shows whats in the shop", value="** **", inline=False)
        em.add_field(name="`b!work` - Gives you money", value="** **", inline=False)
        em.add_field(name="`b!withdraw` - Withdraws money from your bank", value="** **", inline=False)
        em.add_field(name="`b!deposit` - Deposit money into your bank account", value="** **", inline=False)
        em.add_field(name="`b!send` - Sends money to people", value="** **", inline=False)
        em.add_field(name="`b!rob` - Takes money from people", value="** **", inline=False)
        em.add_field(name="`b!buy` - Buy things from the shop", value="** **", inline=False)
        em.add_field(name="`b!sell` - Sell your items", value="** **", inline=False)

        em.set_footer(text="© BobCat Commands")
        await ctx.send(embed=em)


        
def setup(client):
    client.add_cog(helpc(client))