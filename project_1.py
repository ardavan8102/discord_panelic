import discord
from discord.ext import commands
from discord import Intents
import asyncio
import datetime
from colorama import Fore,init
init()

class CONFIG:
    TOKEN = '' # Bot Token
    PREFIX = '' #  Bot Command Prefix


client = commands.Bot(command_prefix=CONFIG.PREFIX, intents = Intents.all())
client.remove_command('help')


def onmsg():
    print(Fore.LIGHTRED_EX+'\n  BOT IS ONLINE')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name='Ardavan Git ...'))
    onmsg()


@client.command()
async def get(ctx, member:discord.Member=None):


    checkmark = '✅'
    crossmark = '❌'

    
    idembed = discord.Embed(
        title = 'ᴀʀᴅᴀᴠᴀɴ ɢɪᴛʜᴜʙ',
        url = 'https://github.com/ardavan8102',
        description = "ɪ ɢᴏᴛ ᴛʜᴇ ᴜꜱᴇʀ'ꜱ ɪᴅ\nɴᴏᴡ , ᴡᴀɴᴛ ᴛᴏ ꜱᴇᴇ ᴡʜᴀᴛ ᴄᴀɴ ʏᴏᴜ ᴅᴏ ᴡɪᴛʜ ɪᴛ?",
        colour = 0x00FF00
    )
    idembed.timestamp = datetime.datetime.utcnow()
    idembed.set_footer(text='By Ardavan81 | ', icon_url=f'{ctx.author.avatar_url}')
    idembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/907733995855421482/912401814169739304/1200px-Eo_circle_green_white_checkmark.svg.png')

    noneembed = discord.Embed(
        title = 'ᴀʀᴅᴀᴠᴀɴ ɢɪᴛʜᴜʙ',
        url = 'https://github.com/ardavan8102',
        description = "ʏᴏᴜ ᴅɪᴅɴ'ᴛ ᴛᴀɢ ᴀɴʏᴏɴᴇ !\nᴘʟᴇᴀꜱᴇ , ᴜꜱᴇ ᴄᴏᴍᴍᴀɴᴅ ᴀɢᴀɪɴ & ᴛᴀɢ ꜱᴏᴍᴇᴏɴᴇ !",
        colour = 0xFF0000
    )
    noneembed.timestamp = datetime.datetime.utcnow()
    noneembed.set_footer(text='By Ardavan81 | ', icon_url=f'{ctx.author.avatar_url}')
    noneembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/907733995855421482/912403820770914364/Red-Cross-PNG-Transparent.png')

    if member is not None:
        msg = await ctx.channel.send(embed=idembed)
        await msg.add_reaction(checkmark)
        await msg.add_reaction(crossmark)

        def check(reaction, user):
            return user == ctx.author and str(
                reaction.emoji) in [checkmark, crossmark]

        reaction, user = await client.wait_for("reaction_add", timeout=10.0, check=check)

        if str(reaction.emoji) == checkmark:
                await msg.delete()
                listembed = discord.Embed(
                    title = 'ᴀʀᴅᴀᴠᴀɴ ɢɪᴛʜᴜʙ',
                    url = 'https://github.com/ardavan8102',
                    description = "ꜰᴇᴀᴛᴜʀᴇꜱ ʟɪꜱᴛ ꜰᴏʀ ʏᴏᴜ : ",
                    colour = 0x00F253
                )
                listembed.add_field(name='ᴛᴏ ꜱᴇᴇ ʀᴏʟᴇꜱ : ', value='`` ᴛʏᴘᴇ "roles" ``', inline=True)
                listembed.add_field(name='ᴛᴏ ꜱᴇᴇ ɪᴅ : ', value='`` ᴛʏᴘᴇ "id" ``', inline=True)
                listembed.timestamp = datetime.datetime.utcnow()
                listembed.set_footer(text='By Ardavan81 | ', icon_url=f'{ctx.author.avatar_url}')
                listembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/907733995855421482/912401814169739304/1200px-Eo_circle_green_white_checkmark.svg.png')

                msg2 = await ctx.send(embed=listembed)

                def check_message(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["roles", "id"]

                answer = await client.wait_for("message", check=check_message)

                if answer.content.lower() == 'roles':
                    await msg2.delete()

                    list = (" , \n".join([str(r.name) for r in member.roles]))

                    rolesembed = discord.Embed(
                        title = 'ᴀʀᴅᴀᴠᴀɴ ɢɪᴛʜᴜʙ',
                        url = 'https://github.com/ardavan8102',
                        description = f"ʜᴇʀᴇ ᴀʀᴇ ᴜꜱᴇʀ'ꜱ ʀᴏʟᴇꜱ : \n\n {list}",
                        colour = 0x00F253
                    )
                    rolesembed.timestamp = datetime.datetime.utcnow()
                    rolesembed.set_footer(text='By Ardavan81 | ', icon_url=f'{ctx.author.avatar_url}')
                    rolesembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/907733995855421482/912401814169739304/1200px-Eo_circle_green_white_checkmark.svg.png')

                    await ctx.send(embed=rolesembed)
                    
                else:
                    await msg2.delete()

                    memid = discord.Embed(
                        title = 'ᴀʀᴅᴀᴠᴀɴ ɢɪᴛʜᴜʙ',
                        url = 'https://github.com/ardavan8102',
                        description = f"ʜᴇʀᴇ ɪꜱ ᴜꜱᴇʀ'ꜱ ɪᴅ : \n ||{member.id}||",
                        colour = 0x00F253
                    )
                    memid.timestamp = datetime.datetime.utcnow()
                    memid.set_footer(text='By Ardavan81 | ', icon_url=f'{ctx.author.avatar_url}')
                    memid.set_thumbnail(url='https://cdn.discordapp.com/attachments/907733995855421482/912401814169739304/1200px-Eo_circle_green_white_checkmark.svg.png')

                    await ctx.send(embed=memid)

        if str(reaction.emoji) == crossmark:
                await msg.delete()

                cancelembed = discord.Embed(
                    title = 'ᴀʀᴅᴀᴠᴀɴ ɢɪᴛʜᴜʙ',
                    url = 'https://github.com/ardavan8102',
                    description = "ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴅᴇᴄɪꜱɪᴏɴ ,\nᴛʜɪꜱ ᴘʀᴏᴄᴇꜱꜱ ʜᴀꜱ ʙᴇᴇɴ ᴄᴀɴᴄᴇʟᴇᴅ ! ",
                    colour = 0xFF0000
                )
                cancelembed.add_field(name='ᴄᴀɴᴄᴇʟᴇᴅ ʙʏ : ', value=f'||{user.mention}||', inline=True)
                cancelembed.timestamp = datetime.datetime.utcnow()
                cancelembed.set_footer(text='By Ardavan81 | ', icon_url=f'{ctx.author.avatar_url}')
                cancelembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/907733995855421482/912403820770914364/Red-Cross-PNG-Transparent.png')

                await ctx.send(embed=cancelembed)
            
        
    elif member is None:
        await ctx.channel.send(embed=noneembed)
        
    else:
        await ctx.channel.send(f'{ctx.author.mention}\n|| Unknown Problem ! ||')
    


client.run(CONFIG.TOKEN)