#Main module of a custom made bot for the Shadows of Nyhxe BDO guild, Yukii

import discord
from discord.ext import commands
import sys, traceback
import keep_alive
import os

keep_alive.keep_alive()

startup_extensions = ["cogs.general", "cogs.moderation", "cogs.blackDesert"]

bot = commands.Bot(command_prefix = commands.when_mentioned_or('y-', 'Y-', 'Yukii '))
bot.remove_command('help')

GAME = discord.Game("Nyhxe | y-help")
STATUS = discord.Status.online

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(status=STATUS, activity=GAME)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print(f'Extension {extension} loaded successfully')
        except Exception as e:
            import traceback
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
            traceback.print_exc()

def isDND():
    m = None
    for s in bot.guilds:
        m = s.get_member(bot.user.id)
        break

    return m.status == discord.Status.dnd

@bot.check
async def mtncmde(ctx):
    dnd = isDND()

    if dnd == False or ctx.author.id == 170715982728265730:
        return True
    else:
        return False

bot.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
