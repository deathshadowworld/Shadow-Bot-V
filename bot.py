import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord import Interaction,Button
from discord.utils import get
import os, postg
from dotenv import load_dotenv

intents = discord.Intents(messages=True, guilds=True, members=True, voice_states=True)
client = discord.Client(intents=intents)
#load_dotenv()
owner = 259999538666930177


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def on_ready(self):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Shadow dying"))
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
bot = Bot()


class thisButton(discord.ui.View):
    def __init__(self,uid):
        super().__init__()
        self.uid = uid
        self.value = None

    @discord.ui.button(label='1')
    async def one(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            await interact.response.send_message('1')
            self.stop()
        else:
            await interact.response.send_message("You're not the poster of this.", ephemeral=True)

    @discord.ui.button(label='2')
    async def two(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            await interact.response.send_message('2')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

@bot.command()
async def start(ctx:Context):
    view = thisButton(ctx.author.id)
    await ctx.send('Pick a number.', view=view)

@bot.command()
async def hello(ctx: Context):
    if ctx.author.id == owner:
        await ctx.send('Hello Shadow master!')

@bot.event
async def on_message(message):
    if message.author.id == owner:
        if message.content == 'hello':
            await message.channel.send('Hello Shadow!')

    user = message.author
    user = User(user.name,user.id)
    #print(message.author,': ', message.content, ' -- in --', message.channel)
    if message.author == bot.user:
        return

    if user.id == owner:
        if message.content.startswith('hello'):
            await message.channel.send('Hello '+user.name+'!')
    
    if message.content.startswith('sk '):
        content = message.content.replace('sk ','')
        if user.id == owner:
            if content == "fix":
                postg.fix()
                await message.channel.send("fixed i think")
            if content == "reset":
                postg.resetAll()
                await message.channel.send("database reset")
                
        if content == "register":
            if postg.registerUser(user):
                await message.channel.send('SUCCESS!')
            else:
                await message.channel.send('FAILED!')
        if content == "view profile":
            profile = postg.viewUser(user)
            if profile:
                await message.channel.send('You are <@'+profile['id']+'>, name of '+profile['name']+' with status of '+profile['status'])
            else:
                await message.channel.send('not found please register')
        if content == "view all":
            userlist = postg.viewUsers()
            if userlist == []:
                await message.channel.send("database empty")
            else:
                n = ''
                for x in userlist:
                    m = "`|     NAME     |        ID        |   STATUS   |`\n"
                    n = n+"`|  "+x[1]+"  |  "+str(x[0])+"  |  "+x[2]+"  |`\n"
                m = m+n
                await message.channel.send(m)
    await bot.process_commands(message)



class User:
    def __init__(self,name='',id='',status='0'):
        self.name = name
        self.id = id
        self.status = status

@bot.event
async def on_voice_state_update(member, before, after):
    VCROLE = 992826737362739282
    GUILD_ID = 784859857937236059
    #vcr,guid = 993370884683333782,718068370070568990

    guild = bot.get_guild(GUILD_ID)
    vc_role = get(guild.roles, id=VCROLE)

    if  after.channel == None:
        await member.remove_roles(vc_role)

    if before.channel == None:
        await member.add_roles(vc_role)

token = str(os.environ.get('V'))
bot.run(token)