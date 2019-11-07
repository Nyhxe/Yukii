import discord
from discord.ext import commands
import cogs.gearFunctions as gf

class Black_Desert(commands.Cog, name= "Black Desert"):
    def __init__(self, bot):
            self.bot = bot


    #-----Add character to database-----#
    @commands.command(description = "Allows you to add or edit your current gear in the guild's database",
                      brief = 'Set user gear to guild DB',
                      name = ('log gear'),
                      aliases = ['lg', 'logG'])
    @commands.has_any_role("Shadows", "Followers of the Duchess", "EU Members")
    async def Set_Char(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

        #--Guild ID--#
        guild = ctx.message.guild
        userid = ctx.message.author.id


        AP = 0
        AAP = 0
        DP = 0

        #--Get Family Name--#
        await ctx.send(content = 'What is your family name?')
        msg = await self.bot.wait_for('message', check=check, timeout= 30)
        FN = msg.content

        #--Get Class--#
        await ctx.send(content = 'What class do you **mainly** play?')
        msg = await self.bot.wait_for('message', check=check, timeout= 30)
        CLASS = msg.content

        #--Get AP--#
        isNum = False
        while isNum == False:
            await ctx.send(content = 'What is your current AP?')
            msg = await self.bot.wait_for('message', check=check, timeout= 30)

            try:
                msgap = int(msg.content)
                AP = msgap
                isNum = True
            except:
                import traceback
                traceback.print_exc()
                await ctx.send('Please enter a number.')

        #--Get AAP--#
        isNum = False
        while isNum == False:
            await ctx.send(content = 'What is your current AAP?')
            msg = await self.bot.wait_for('message', check=check, timeout= 30)

            try:
                msgap = int(msg.content)
                AAP = msgap
                isNum = True
            except:
                import traceback
                traceback.print_exc()
                await ctx.send('Please enter a number.')

        #--Get DP--#
        isNum = False
        while isNum == False:
            await ctx.send(content = 'What is your current DP?')
            msg = await self.bot.wait_for('message', check=check, timeout= 30)

            try:
                msgap = int(msg.content)
                DP = msgap
                isNum = True
            except:
                import traceback
                traceback.print_exc()
                await ctx.send('Please enter a number.')

        #--Tells User Their Total GS--#
        GS = ((AP + AAP) / 2) + DP
        await ctx.send(f'''**{FN}**, your current gear score is **{int(GS)}** keep it up! \nYour information has been added to the database, remember to keep it updated please!''')
        gf.new_char(userid, FN, CLASS, AP, AAP, DP, int(GS))

    #-----Edit Element of Character Entry-----#
    @commands.command(description = 'Edit any singular part of your gear entry in the database',
                      brief = 'Edit your entry',
                      aliases = ['edP'])
    @commands.has_any_role("Shadows", "Followers of the Duchess", "EU Members")
    async def editPart(self, ctx, PART):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

        #--Local Vars--#
        guild = ctx.message.guild
        userid = ctx.message.author.id
        part = str(PART)

        #--Get Family Name--#
        if part.lower() == 'fn':
            await ctx.send(content = 'What is your new family name?')
            msg = await self.bot.wait_for('message', check=check, timeout= 30)
            FN = msg.content
            gf.set_value(userid, "FN", FN)

          
        #--Get Class--#
        elif part.lower() == 'class':
            await ctx.send(content = 'What new class do you **mainly** play?')
            msg = await self.bot.wait_for('message', check=check, timeout= 30)
            CLASS = msg.content
            gf.set_value(userid, "CLASS", CLASS)

        #--Get AP--#
        elif part.lower() == 'ap':
            isNum = False
            while isNum == False:
                await ctx.send(content = 'What is your current AP?')
                msg = await self.bot.wait_for('message', check=check, timeout= 30)

                try:
                    msgap = int(msg.content)
                    AP = msgap
                    isNum = True
                except:
                    import traceback
                    traceback.print_exc()
                    await ctx.send('Please enter a number.')
            gf.set_value(userid, "AP", AP)

        #--Get AAP--#
        elif part.lower() == 'aap':
            isNum = False
            while isNum == False:
                await ctx.send(content = 'What is your current AP?')
                msg = await self.bot.wait_for('message', check=check, timeout= 30)

                try:
                    msgaap = int(msg.content)
                    AAP = msgaap
                    isNum = True
                except:
                    import traceback
                    traceback.print_exc()
                    await ctx.send('Please enter a number.')
            gf.set_value(userid, "AAP", AAP)

        #--Get DP--#
        elif part.lower() == 'dp':
            isNum = False
            while isNum == False:
                await ctx.send(content = 'What is your current DP?')
                msg = await self.bot.wait_for('message', check=check, timeout= 30)

                try:
                    msgdp = int(msg.content)
                    DP = msgdp
                    isNum = True
                except:
                    import traceback
                    traceback.print_exc()
                    await ctx.send('Please enter a number.')
            gf.set_value(userid, "DP", DP)

        else:
            await ctx.send("That's not a valid part of the log, I can't edit that. Do n!help for info on how to use this command.")

        gf.calcGS(userid)
        await ctx.send('Your database entry has been successfully updated!\n' \
            f'{gf.get_val(userid, "FN")}, your new gearscore is {gf.get_val(userid, "GS")}')

	#-----Returns Characters-----#
    @commands.command(description = 'Returns a list of stored character of the person you mention in an embed.',
                      brief = 'Returns mentioned character.',
                      aliases = ['gs'])
    async def gearscore(self, ctx, *NAME):
        guild = ctx.message.guild
        
        if len(list(ctx.message.mentions)) != 0:
            for user in list(ctx.message.mentions):
                    userid = user.id
                
                    embed=discord.Embed(color=0xfc1299)
                    embed.set_author(name = f"{ctx.message.author.display_name}'s character.")
                    embed.add_field(name = 'Family Name:', value = gf.get_val(userid, "FN"), inline=False)
                    embed.add_field(name = 'Class:', value = gf.get_val(userid, "CLASS"), inline=False)
                    embed.add_field(name = 'AP:', value = gf.get_val(userid, "AP"), inline=False)
                    embed.add_field(name = 'AAP:', value = gf.get_val(userid, "AAP"), inline=False)
                    embed.add_field(name = 'DP', value = gf.get_val(userid, "DP"), inline=False)
                    embed.add_field(name = 'GS', value = gf.get_val(userid, "GS"), inline=False)
                    await ctx.send(embed = embed)

        else:
            userid = ctx.message.author.id
                
            embed=discord.Embed(color=0xfc1299)
            embed.set_author(name = f"{ctx.message.author.display_name}'s character.")
            embed.add_field(name = 'Family Name:', value = gf.get_val(userid, "FN"), inline=False)
            embed.add_field(name = 'Class:', value = gf.get_val(userid, "CLASS"), inline=False)
            embed.add_field(name = 'AP:', value = gf.get_val(userid, "AP"), inline=False)
            embed.add_field(name = 'AAP:', value = gf.get_val(userid, "AAP"), inline=False)
            embed.add_field(name = 'DP', value = gf.get_val(userid, "DP"), inline=False)
            embed.add_field(name = 'GS', value = gf.get_val(userid, "GS"), inline=False)
            await ctx.send(embed = embed)
          
    #-----Returns All Charcters-----#
    @commands.command(name = 'list gear',
                      description = "List all members in the database and their gearscore, ranked from highest to lowest",
                      brief = "Lists all gearscores",
                      aliases = ['grank', 'gear rank', 'listgear'])
    async def return_all_chars(self, ctx):
        user = ctx.message.author
        ranks = gf.get_rank()
        i = 1

        embed=discord.Embed(title = "Shadows of Nyhxe gear ranking", color=0xfc1299)
        for score, FN in ranks:
            embed.add_field(name = f'{i}.) {FN}', value = f'{score}', inline = False)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/622396893800169472/639515518608474133/lgog.jpg")
        #embed.set_author(name = "Yukii", icon_url = "https://cdn.discordapp.com/avatars/601196851663732740/c935550c9456463ed61a8a31aed6a487.webp?size=2048")
        embed.set_footer(text = f"Guild ranking requested by {user.display_name}", icon_url = user.avatar_url)

        await ctx.send(embed=embed)
            
    @commands.command(hidden = True)
    async def test(self, ctx):
        for user in list(ctx.message.mentions):
            await ctx.send(f'{ctx.message.author.id} -- Author ID \n {user.id} -- Mention ID')

    #-----Sets up PvP Matches-----#
    @commands.command(name = 'match',
                      description = '',
                      brief = '',
                      aliases = [])
    @commands.has_any_role("Shadows", "Followers of the Duchess", "EU Members")
    async def pvp_matching(self, ctx):
        ranks = gf.get_rank()
        user = ctx.message.author
        
        usergear = gf.get_val(user.id, "GS")
        emb = discord.Embed(title = f"Possible matchups for {user.display_name}")

        for score, fn in ranks:
            difference = abs(usergear - score)
            if difference > 50:
                pass
            elif difference <= 50:
                emb.add_field(name = fn, value = f"Gearscore: {score} \nGearscore difference: {difference}")

        await ctx.send(embed = emb)



def setup(bot):
    bot.add_cog(Black_Desert(bot))
