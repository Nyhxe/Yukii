#General commands module for Yukii

import discord
from discord.ext import commands
import random

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #-----Online Test-----#
    @commands.command(description = 'A basic check to see if the bot is online and responsive', 
                    brief = 'Online test')
    async def hello(self, ctx):
        await ctx.send("I'm awake!")

    #-----Copypasta-----#
    @commands.command(description = 'Sends the "Rawr x3" copypasta, why would you expect anything more from this command?',
                brief = 'Sends the Rawr x3 copypasta')
    async def rawr(self, ctx):
        await ctx.send("Rawr x3 nuzzles how are you pounces on you you're so warm o3o notices you have a bulge o: someone's happy ;) nuzzles your necky wecky~ murr~ hehehe rubbies your bulgy wolgy you're so big :oooo rubbies more on your bulgy wolgy it doesn't stop growing ·///· kisses you and lickies your necky daddy likies (; nuzzles wuzzles I hope daddy really likes $: wiggles butt and squirms I want to see your big daddy meat~ wiggles butt I have a little itch o3o wags tail can you please get my itch~ puts paws on your chest nyea~ its a seven inch itch rubs your chest can you help me pwease squirms pwetty pwease sad face I need to be punished runs paws down your chest and bites lip like I need to be punished really good~ paws on your bulge as I lick my lips I'm getting thirsty. I can go for some milk unbuttons your pants as my eyes glow you smell so musky :v licks shaft mmmm~ so musky drools all over your cock your daddy meat I like fondles Mr. Fuzzy Balls hehe puts snout on balls and inhales deeply oh god im so hard~ licks balls punish me daddy~ nyea~ squirms more and wiggles butt I love your musky goodness bites lip please punish me licks lips nyea~ suckles on your tip so good licks pre of your cock salty goodness~ eyes role back and goes balls deep mmmm~ moans and suckles o3o")
        print('Action completed: Rawr x3 sent')


    #-----Repeats user Simon-Says style-----#
    @commands.command(description = 'Repeats the user Simon-Says style, sending a message saying whatever you want her to and deletes the command message \n A great command to use to trick your more oblivious friends into thinking the bot is sentient ;)', 
                    brief = 'Says what you tell her to')
    async def say(self, ctx, *args):
        await ctx.message.delete()
        await ctx.send(' '.join(args))
        print('Action completed: "Repeat after me..."')


    #-----Ha, Benis-----#
    @commands.command(description = 'Haha, Benis :DDD',
                    brief = 'Benis')
    async def benis(self, ctx):
        embed=discord.Embed(title="BENIS", url="https://cdn.discordapp.com/attachments/556122403307126795/556166983113113620/1500003941502.png", description="Haha, Benis :DDD", color=0x975a3e)
        embed.set_author(name="Benis#1235")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/556122403307126795/556166983113113620/1500003941502.png")
        embed.set_image(url= "https://cdn.discordapp.com/attachments/499959279101673483/563180844928204801/1132020622_preview_12333.jpg")
        embed.set_footer(text="Benis")
        await ctx.send(embed=embed)

    #-----Embeds Member's Avi-----#
    @commands.command(description = 'Embed the avatar of the user or users mentioned in the command message. If no user is mentioned it sends your own \n'\
                    ' Usage: n!avi <@mention user>',
                    brief = 'Sends users avatar')
    async def avi(self, ctx, member='you'):
        if member == 'you':
            user = ctx.author
            embed=discord.Embed(title='', url='', description='')
            embed.set_image(url = user.avatar_url)

            await ctx.send(embed = embed)
        else:
            for user in ctx.message.mentions:
                embed=discord.Embed(title='', url='', description='')
                embed.set_image(url = user.avatar_url)

                await ctx.send(embed = embed)

    #-----Basic 8-Ball-----#
    @commands.command(name = 'oracle',
                        description = 'Gives "Magic 8-Ball" type answer to a question',
                        brief = 'Psychic Visions Incoming',
                        aliases = ['8ball', 'ora'])
    async def eight_ball(self, ctx):
        possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'You expect me to know that how?'
    ]
        await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)

    #-----Message of the Day-----#
    @commands.command(name = 'motd',
                        description = 'Sends a random "Message of the Day" chosen from a list that gets added to whenever Nyhxe feels like it',
                        brief = 'Message of the Day',
                        aliases = ['MOTD', 'think'])
    async def message_of_the_day(self, ctx):
        possible_motd = [
            'I need something to make my SPOON FOOD with',
            "I'm here for a good time, not a long time",
            "I am a very submissive pup. I love big boys! OwO",
            "Imagine being Stephen Hawking's wife and getting his quantiphysical rod up in your black hole as he's just spurtin' out rocket science",
            "I just feel like it's a slippery slope into incest from calling your boyfriend Daddy \nAnd I do not like that at all",
            "Pussy? Yes.",
            "I can't fit boobs in a panty",
            "Nothin' turns me on more than a camel in a porn video... with a horse",
            "I love the smell of trash it gets me horny",
            "Live soft, die hard",
            "You know you're having a good time if you feel resistance in the lower part of your body",
            "If dipping your balls in a freshly opened jar of Nutella is wrong, I don't want to be right!",
            "I once thought I was wrong, but I was mistaken",
            "Nothing is impossible unless you can't do it",
            "Why doesn't glue stick to the inside of a bottle?",
            "Hey, are you bonemeal? Cuz you turn my sapling into a tree",
            "Anal sex is the gateway to homosexuality",
            "That's not an asshole, that's a boy pussy!",
            "I'm no rocket surgeon",
            "Nothin' like a good ass lickin'!",
            "I ain't gay, I just have a dick fetish",
            "The ee in pee is silent",
            "When she nut but you keep sucking \nWait no",
            "TOO SOON",
            "If your pussy don't smell like wet monkey scalp I don't want it",
            "Rawr X3",
            "I'm not a furry shut up",
            "I wish my mom was a virgin",
            "It's not about the size of the bulge, but the motion in the ocean",
            "Don't sweat the petty things, and don't pet the sweaty things",
            "You're aren't",
            "Yo whattup ||niggas|| ma name's L'4che",
            "BALLS",
            "I'mma be real witchu, chief \nYou're a real hoe sometimes",
            "Yo who wants to OwO and do da furri",
            "I like to eat Vaseline on toast",
            "If you microwave a bagel you deserve to die",
            "Y'know, I'd say Hitler had the right idea",
            "Hey y'all I just wanna let you know I haVe a bOyFrIenD nAmEd bRanDoN aNd uH hE thInkS i'M cHeATinG oN hIm wItH aNiMe 'gIrLs'..",
            "Stick your dick in the beans bitch",
            "Does Mike Wazowski wink or blink?",
            "The F. in John F. Kennedy stood for Fortnite",
            "Live fast, eat ass",
            "Instructions unclear, dick in shampoo bottle",
            "Hey baby, are you a stone cutter? Cuz you're really fucking useless",
            "Ayy, baby, are you a fire alarm? 'Cause you're really fucking loud and annoying",
            "Incest is a wincest",
            "I've got about a 10% chance of working correctly 20% of the time \nThe other 80% of the time? Go fuck yourself",
            "I swear to God, if you ask me to do something **one more time**!; I will fill you with milk!!",
            "I'm harder than a nonce in a nursery",
            "I'm harder than a paedophile in a preschool",
            "I'm harder than a kiddie fiddler with a little piddler ;)",
            "Giving birth can really bring out the child in you",
            '1 inch long and 10 inches wide; bitches call me "The Plate"',
            "Vsauce is short for vagina sauce",
            "Corn rock",
            "Is it racist to say 'Let's role' to a person in a wheelchair?",
            "You think dogs will ever fuck 'human style'?"
    ]
        await ctx.send(random.choice(possible_motd))    

    #-----Custom help command-----#
    @commands.command(
       name='help',
       description='The help command!',
       brief='Sends this message',
       aliases=['commands', 'command'],
       usage='cog'
        )
    async def help_command(self, ctx, *, cog='all'):
   
        # The third parameter comes into play when
        # only one word argument has to be passed by the user

        colors = {
            'DEFAULT': 0x000000,
            'WHITE': 0xFFFFFF,
            'AQUA': 0x1ABC9C,
            'GREEN': 0x2ECC71,
            'BLUE': 0x3498DB,
            'PURPLE': 0x9B59B6,
            'LUMINOUS_VIVID_PINK': 0xE91E63,
            'GOLD': 0xF1C40F,
            'ORANGE': 0xE67E22,
            'RED': 0xE74C3C,
            'GREY': 0x95A5A6,
            'NAVY': 0x34495E,
            'DARK_AQUA': 0x11806A,
            'DARK_GREEN': 0x1F8B4C,
            'DARK_BLUE': 0x206694,
            'DARK_PURPLE': 0x71368A,
            'DARK_VIVID_PINK': 0xAD1457,
            'DARK_GOLD': 0xC27C0E,
            'DARK_ORANGE': 0xA84300,
            'DARK_RED': 0x992D22,
            'DARK_GREY': 0x979C9F,
            'DARKER_GREY': 0x7F8C8D,
            'LIGHT_GREY': 0xBCC0C0,
            'DARK_NAVY': 0x2C3E50,
            'BLURPLE': 0x7289DA,
            'GREYPLE': 0x99AAB5,
            'DARK_BUT_NOT_BLACK': 0x2C2F33,
            'NOT_QUITE_BLACK': 0x23272A
        }

        color_list = [c for c in colors.values()]
        help_embed = discord.Embed(
            title='Help',
            description='Use ``y-help <command group>`` for more info',
            color=random.choice(color_list)
        )
        help_embed.set_thumbnail(url=self.bot.user.avatar_url)
        help_embed.set_footer(
            text=f'Requested by {ctx.message.author.display_name}',
            icon_url=self.bot.user.avatar_url
        )

        # Get a list of all cogs
        cogs = [c for c in self.bot.cogs.keys()]

        # If cog is not specified by the user, we list all cogs and commands

        if cog == 'all':
            for cog in cogs:
                # Get a list of all commands under each cog

                cog_commands = self.bot.get_cog(cog).get_commands()
                commands_list = ''
                for comm in cog_commands:
                    commands_list += f'**{comm.name}** - *{comm.brief}*\n'

                # Add the cog's details to the embed.

                help_embed.add_field(
                    name=cog,
                    value=commands_list,
                    inline=False
                ).add_field(
                    name='\u200b', value='\u200b', inline=False
                )

                # Also added a blank field '\u200b' is a whitespace character.
            pass
        else:

            # If the cog was specified

            lower_cogs = [c.lower() for c in cogs]

            # If the cog actually exists.
            if cog.lower() in lower_cogs:

                # Get a list of all commands in the specified cog
                commands_list = self.bot.get_cog(cogs[ lower_cogs.index(cog.lower()) ]).get_commands()
                help_text=''

                # Add details of each command to the help text
                # Command Name
                # Description
                # [Aliases]
                #
                # Format
                for command in commands_list:
                    help_text += f'```{command.name}```\n' \
                        f'**{command.description}**\n\n'

                    # Also add aliases, if there are any
                    if len(command.aliases) > 0:
                        help_text += f'**Aliases :** `{"`, `".join(command.aliases)}`\n\n\n'
                    else:
                        # Add a newline character to keep it pretty
                        help_text += '\n'

                    # Finally the format
                    help_text += f'Format: `Yukii ' \
                        f' {command.name} {command.usage if command.usage is not None else ""}` OR `y-' \
                        f'{command.name} {command.usage if command.usage is not None else ""}`\n\n\n\n'

                help_embed.description = help_text
            else:
                # Notify the user of invalid cog and finish the command
                await ctx.send("Hmmm... I didn't recognize that command group.\nUse the `help` command to list all cogs.")
                return

        await ctx.send(embed=help_embed)
   
        return
        
def setup(bot):
    bot.add_cog(General(bot))
