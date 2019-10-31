import discord
from discord.ext import commands
import cogs.gearFunctions as gf

class Black_Desert(commands.Cog, name= "Black Desert"):
    def __init__(self, bot):
            self.bot = bot


    #-----Add character to database-----#
    @commands.command(description = "Allows you to add your current gear to the guild's database",
                      brief = 'Adds user gear to guild DB',
                      aliases = ['adC'])
    @commands.has_any_role("Shadows", "Followers of the Duchess", "EU Members")
    async def addChar(self, ctx):
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

	#-----Edit Character Entry in Database-----#
    @commands.command(description = 'Allows you to edit your entire entry in the guild gear database',
                      brief = 'Edits user gear in guild DB',
                      aliases = ['edC'])
    async def editChar(self, ctx):
        def check(ms):
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

        #--Guild ID--#
        guild = ctx.message.guild
        userID = ctx.message.author.id
        
        AP = 0
        AAP = 0
        DP = 0
        
        #--Get Family Name--#
        await ctx.send(content = 'What is your new family name?')
        msg = await self.bot.wait_for('message', check=check, timeout= 30)
        FN = msg.content

        #--Get Class--#
        await ctx.send(content = 'What new class do you **mainly** play now?')
        msg = await self.bot.wait_for('message', check=check, timeout= 30)
        Class = msg.content

        #--Get AP--#
        isNum = False
        while isNum == False:
            await ctx.send(content = 'What is your current AP?')
            msg = await self.bot.wait_for('message', check=check, timeout= 30)
    
            try:
                AP = int(msg.content)
                isNum = True

            except:
                await ctx.send('Please enter a number.')

        #--Get AAP--#
        isNum = False
        while isNum == False:
            await ctx.send(content = 'What is your current AAP?')
            msg = await self.bot.wait_for('message', check=check, timeout= 30)
    
            try:
                AAP = int(msg.content)
                isNum = True

            except:
                await ctx.send('Please enter a number.')

        #--Get DP--#
        isNum = False
        while isNum == False:
            await ctx.send(content = 'What is your current DP?')
            msg = await self.bot.wait_for('message', check=check, timeout= 30)
    
            try:
                DP = int(msg.content)
                isNum = True

            except:
                await ctx.send('Please enter a number.')

		#--Tells User Their Total GS--#
        gf.calcGS(userid)
        await ctx.send('Your database entry has been successfully updated!\n' \
            f'{gf.get_val(userid, "FN")}, your new gearscore is {gf.get_val(userid, "GS")}')

        #--Stores in database--#
        gf.new_char(userID, FN, Class, AP, AAP, DP)

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
                    character = gf.get_char(str(user.id))
                
                    embed=discord.Embed(color=0xfc1299)
                    embed.set_author(name = f"{user.display_name}'s character.")
                    embed.add_field(name = 'Family Name:', value = character[1], inline=False)
                    embed.add_field(name = 'Class:', value = character[2], inline=False)
                    embed.add_field(name = 'AP:', value = character[3], inline=False)
                    embed.add_field(name = 'AAP:', value = character[4], inline=False)
                    embed.add_field(name = 'DP', value = character[5], inline=False)
                    embed.add_field(name = 'GS', value = character[6], inline=False)
                    await ctx.send(embed = embed)

        else:
            character = gf.get_list()
                
            embed=discord.Embed(color=0xfc1299)
            embed.set_author(name = f"{ctx.message.author.display_name}'s character.")
            embed.add_field(name = 'Family Name:', value = character[1], inline=False)
            embed.add_field(name = 'Class:', value = character[2], inline=False)
            embed.add_field(name = 'AP:', value = character[3], inline=False)
            embed.add_field(name = 'AAP:', value = character[4], inline=False)
            embed.add_field(name = 'DP', value = character[5], inline=False)
            embed.add_field(name = 'GS', value = character[6], inline=False)
            await ctx.send(embed = embed)
          
            
    @commands.command(hidden = True)
    async def test(self, ctx):
        for user in list(ctx.message.mentions):
            await ctx.send(f'{ctx.message.author.id} -- Author ID \n {user.id} -- Mention ID')


def setup(bot):
    bot.add_cog(Black_Desert(bot))
