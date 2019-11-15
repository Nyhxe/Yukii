#Main module of a custom made bot for the Shadows of Nyhxe BDO guild, Yukii

import discord
from discord.ext import commands
import sys, traceback
#import keep_alive
import os
from dotenv_config import load_dotenv

load_dotenv('vars.env')
TOKEN = os.getenv('TOKEN')
#keep_alive.keep_alive()

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

class Log():
    @bot.event
    async def on_message_delete(msg):
        logmsg = f"__**Message Deleted**__\n\n{msg.content}"

        #Checks if there are any attachments and adds them to the log message.
        attList = []
        attURL = ''
        if len(msg.attachments) > 0:
            for attachment in msg.attachments:
                attList.append(attachment.url)
                attURL = f'{attachment.url}'
            logmsg = f"__**Message Deleted**__\n\n{msg.content}\n||{'|| ||'.join(attList)}||"

        #Checks if there are any embeds and sends those with the message.
        embList = []
        if len(msg.embeds) > 0:
            for embed in msg.embeds:
                embList.append(embed)

        #Creates the log embed.
        emb = discord.Embed(
                color = discord.Color.from_rgb(255, 0, 0), 
                description = logmsg)

        emb.set_author(name = f"{bot.get_user(msg.author.id)}\nUser ID: {msg.author.id}", icon_url = msg.author.avatar_url)
        if attURL != None:
            emb.set_image(url = attURL)
        else:
            pass
        emb.set_footer(text = f"Deleted in #{msg.channel}/{msg.channel.mention}", icon_url = msg.channel.guild.icon_url)

        #Send the message to the servers log channel.
        chnl = bot.get_channel(639521589662056468)

        await chnl.send(embed = emb)
        for embd in embList:
            await chnl.send(embed = embd)

    @bot.event
    async def on_bulk_message_delete(msgs):
        embList = []
        logmsgs = []
        for msg in msgs:

            #Checks if there are any embeds and sends those with the message.
            attList = []
            if len(msg.attachments) > 0:
                for attachment in msg.attachments:
                    attList.append(attachment.url)
                logmsgs.append(("__**Message(s)/Attachment(s) Deleted**__", f"{msg.content}\n||{'|| ||'.join(attList)}||"))

            #Checks if there are any embeds and sends those with the message.
            if len(msg.embeds) > 0:
                for embed in msg.embeds:
                    embList.append(embed)
                logmsgs.append(("__**Embed Deleted**__", f"Embed Deleted"))

            if not (len(msg.embeds) > 0) and not (len(msg.attachments) > 0):
                logmsgs.append(("__**Message Deleted**__", f"{msg.content}"))

        emb = discord.Embed(
                color = discord.Color.from_rgb(255, 0, 0))

        emb.set_author(name = "Message Bulk Delete", icon_url = bot.user.avatar_url)

        emb.set_footer(text = f"Deleted in #{msgs[0].channel}/{msgs[0].channel.mention}", icon_url = msgs[0].channel.guild.icon_url)

        for log in logmsgs:
            emb.add_field(name = f"{log[0]}", value = f"{log[1]}", inline = False)

        #Send the message to the servers log channel.
        chnl = bot.get_channel(639521589662056468)

        await chnl.send(embed = emb)
        for embd in embList:
            await chnl.send(embed = embd)

    @bot.event
    async def on_message_edit(bfr, aft):
        if not bfr.author.bot:
            before = ""
            after = ""

            if len(bfr.content) > 0 or len(aft.content) > 0:
                before = bfr.content
                after = aft.content
                
            if len(bfr.attachments) > 0:
                attList = []
                for attachment in bfr.attachments:
                    attList.append(attachment.url)
                before = f"{before}\n||{'|| ||'.join(attList)}||"

            if len(aft.attachments) > 0:
                attList = []
                for attachment in aft.attachments:
                    attList.append(attachment.url)
                after = f"{after}\n||{'|| ||'.join(attList)}||"

            emb = discord.Embed(
                    color = discord.Color.from_rgb(255, 255, 0))

            emb.set_author(name = f"{bot.get_user(bfr.author.id)}\nMessage Edit", icon_url = bfr.author.avatar_url)

            emb.set_footer(text = f"Edited in #{bfr.channel}/{bfr.channel.mention}", icon_url = bfr.channel.guild.icon_url)

            emb.add_field(name = "__**Before**__", value = f"{before}\n\n**Pin Status**\n{bfr.pinned}", inline = False)

            emb.add_field(name = "__**After**__", value = f"{after}\n\n**Pin Status**\n{aft.pinned}", inline = False)

            #Send the message to the servers log channel.
            chnl = bot.get_channel(639521589662056468)

            await chnl.send(embed = emb)

bot.run(TOKEN, bot=True, reconnect=True)