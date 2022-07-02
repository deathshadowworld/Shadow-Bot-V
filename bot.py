import discord
from discord.ext import commands
from discord.utils import get


intents = discord.Intents(messages=True, guilds=True, members=True, voice_states=True)
client = discord.Client(intents=intents)
me = '259999538666930177'
bona = '400781611588911116'
vcrole_id = 992826737362739282
workch_id = 861326204132392960
workch = client.get_channel(workch_id)
vc_role = ""




@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Shadow Bot V"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    user = str(message.author.id)
    #print(message.author,': ', message.content, ' -- in --', message.channel)
    if message.author == client.user:
        return

    if user == me or user == bona:
        if message.content.startswith('hello'):
            await message.channel.send('Hello '+message.author.name+'!')


@client.event
async def on_voice_state_update(member, before, after):
    for guild in client.guilds:
        if guild.id == 784859857937236059:
            global vc_role
            vc_role = get(guild.roles, id=vcrole_id)
        for x in guild.channels:
            if x.name == 'work-space':
                global workch
                workch = x

    #print (workch)
    if  after.channel == None:
        #print(member.name + ' disconnected.')
        #await workch.send(member.name + ' disconnected from '+ before.channel.name+'.')
        await member.remove_roles(vc_role)

    if before.channel == None:
        #print(member.name + ' connected.')
        #await workch.send(member.name + ' connected to '+ after.channel.name+'.')
        await member.add_roles(vc_role)
    









client.run('OTkyNzc1OTQxMzA4ODI5Njk2.GqIRpV.OdNYMoMTMdKCPH6kI74hVOsItDkSutcL1q0kQ0')