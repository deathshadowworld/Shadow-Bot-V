from collections import UserList
from discord import Embed
import postg
import datetime
from tabulate import tabulate

def  viewProfile(ctx):
    embed = Embed(title="Profile", colour=0x339ca8)
    user = postg.findUser(ctx)
    char = postg.findChar(ctx)
    if user['status'] == '0':
        user['status'] = 'Active'
    embed.add_field(name='Name',value=user['name'],inline=True)
    embed.add_field(name='ID',value=user['id'],inline=True)
    embed.add_field(name='Status',value=user['status'],inline=False)
    embed.set_footer(text='sk view profile | '+ str(datetime.datetime.now()))
    embed.set_thumbnail(url=ctx.avatar.url)
    if char:
        embed.add_field(name='Name',value=char['name'],inline=True)
        embed.add_field(name='Class',value=char['class'],inline=True)
        embed.add_field(name='Level',value=char['level'],inline=True)
        embed.add_field(name='Experience',value=char['exp'],inline=True)
        embed.set_image(url=char['image'])
    return embed

def viewPlayers(ctx):
    users = postg.viewPlayerTable()
    if not len(users):
        return False
    else:
        table =  tabulate(users, ["ID", "Name","Status"]) 
        embed = Embed(title='Database', description='Lists certain table that is requested.', colour=0x339ca8)
        embed.add_field(name='Players', value="```"+table+"```", inline=False)
        embed.set_footer(text='sk view all | '+ str(datetime.datetime.now()))
        embed.set_thumbnail(url=ctx.avatar.url)
    return tabulate(users,['ID','Name', 'Status'],tablefmt='psql')

def viewChars(ctx):
    chars = postg.viewCharTable()
    if not len(chars):
        return False
    else:
        table =  tabulate(chars) 
        embed = Embed(title='Database', description='Lists certain table that is requested.', colour=0x339ca8)
        embed.add_field(name='Characters', value="```"+table+"```", inline=False)
        embed.set_footer(text='sk view all | '+ str(datetime.datetime.now()))
        embed.set_thumbnail(url=ctx.avatar.url)
    

    return tabulate(chars,['ID','Name','Class','Lvl','EXP','VIT','STR','DEX','INT','WIS','CHA','Owner','IMG','$','blb'],tablefmt='psql')

def viewHelp():
    string = '''
    `sk register` - register the user/player to database
    `sk view profile` - view your profile
    `sk create` - create a character
    `sk portrait update [image url]` - updates your character avatar
    `sk delete` - deletes your character
    `sk help` - this message
    '''
    embed = Embed(title='Help!', description=string, colour=0x339ca8)
    embed.set_footer(text='sk help | '+ str(datetime.datetime.now()))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/616833107965771776/967787217676288060/92583070_p0.jpg')
    return embed
