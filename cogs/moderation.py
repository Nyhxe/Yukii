import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def isNyx(ctx):
        return ctx.author.id == 170715982728265730

    #-----Clears Messages-----#
    @commands.command(description = 'Bulk deletes a specified amount of messages \n Usage: n!clear <number> \n EX: n!clear 20 will clear the 20 most recent messages not counting the command message', 
                    brief = 'Bulk deletes messages')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, NUMBER):
        guild = ctx.message.guild
        num = int(NUMBER)

        await ctx.message.delete()
        await ctx.channel.purge(limit = num, bulk = True)

    #-----Kick Member(s)-----#
    @commands.command(description = 'Kicks the mentioned user or users from the server \n Usage: n!kick <@mention user>',
                        brief = 'Kicks member from server')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, *, REASON):
        guild = ctx.message.guild
        rsn = str(REASON)

        for user in ctx.message.mentions:
            await user.kick(reason = rsn)

    #-----Puts the bot into maintenance mode-----#
    @commands.command(description = "Puts the bot into maintenance mode, where she will only respond to Nyhxe",
                        brief = "Puts Yukii in maintenance mode")
    @commands.check(isNyx)
    async def maintenance(self, ctx):
        def isDND():
            m = None
            for s in self.bot.guilds:
                m = s.get_member(self.bot.user.id)
                break

            return m.status == discord.Status.dnd

        dnd = isDND()

        if dnd == True:
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Game("with Nyhxe | y-help"))

            await ctx.send("Maintenance mode off!")
        elif dnd == False:
            await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game("in maintenance mode..."))

            await ctx.send("Maintenance mode on!")

    #-----Assign Correct Roles-----#
    @commands.command(description = 'Assigns the user the correct roles to see channels based on what platform/region they play on.',
                      brief = 'Escorts into the castle')
    @commands.bot_has_permissions(manage_roles=True)
    #@commands.has_role("Wishful Thinkers")
    async def escort(self, ctx):
        try:
            def check(ms):
                return ms.channel == ctx.message.channel and ms.author == ctx.message.author

            guild = ctx.message.guild
            user = ctx.message.author
            pc = guild.get_role(516581204334608385)
            xb = guild.get_role(532628851763838983)
            eu = guild.get_role(616312514116059168)

            pc2 = guild.get_role(478669674985553923)
            xb2 = guild.get_role(616312344833818634)
            eu2 = guild.get_role(532627648682131458)

            if user not in guild.get_role(497492466576916491).members:
                await ctx.send("Don't leave us! \nTalk to an officer or leader if you need to switch platforms or regions")
                pass
            else:

                await ctx.send(content = 'What platform do you play on? (PC/Xbox)')
                msg = await self.bot.wait_for('message', check=check, timeout= 30)
                plat = msg.content            

                if plat == 'pc' or plat == 'PC' or plat == 'Pc':
                    await ctx.send(content = 'What region servers do you play on? (NA/EU)')
                    msg = await self.bot.wait_for('message', check=check, timeout= 30)
                    reg = msg.content

                    if reg == 'NA' or reg == 'na' or reg == 'Na':
                        await user.add_roles(pc, reason= "Escorting...")
                        await ctx.send(f"{user.display_name} has been safely escorted inside")
                    elif reg == 'EU' or reg == 'eu' or reg == 'Eu':
                        await user.add_roles(eu, reason= "Escorting...")
                        await ctx.send(f"{user.display_name} has been safely escorted inside")
                    else:
                        await ctx.send("Sorry, I don't recognize that region. Please try again")

                elif plat == 'xbox' or plat == 'Xbox':
                    await user.add_roles(xb, reason= "Escorting...")
                    await ctx.send(f"{user.display_name} has been safely escorted inside")

                else:
                    await ctx.send("Sorry, I don't recognize that platform. Please try again")

                await user.remove_roles(guild.get_role(497492466576916491))
        except Exception as e:
            await ctx.send(f"I've encountered an error...\n```{e}```")


def setup(bot):
    bot.add_cog(Moderation(bot))
