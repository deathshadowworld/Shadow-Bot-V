import discord, os, postg, embd,tabulate
from discord.ext import commands
from discord.ext.commands import Context
from discord import Interaction,Button
from discord.utils import get
from dotenv import load_dotenv

intents = discord.Intents(messages=True, guilds=True, members=True, voice_states=True)
client = discord.Client(intents=intents)
load_dotenv()
owner = 259999538666930177


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def on_ready(self):
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="shadow dying"))
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
bot = Bot()


class thisButton(discord.ui.View):
    def __init__(self,ctx):
        super().__init__()
        self.uid = ctx.author.id
        self.channel = ctx.channel
        self.value = None

    @discord.ui.button(label='1')
    async def one(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            await interact.response.send_message('1')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

    @discord.ui.button(label='2')
    async def two(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            await interact.response.send_message('2')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

class charCreation(discord.ui.View):
    def __init__(self,ctx):
        super().__init__()
        self.uid = ctx.author.id
        self.channel = ctx.channel
        self.chosen = '0'
        self.name = ''
        self.value = None

    @discord.ui.button(label='Warrior')
    async def warrior(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.chosen = 'Warrior'
            #await interact.response.send_message('Warrior')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

    @discord.ui.button(label='Archer')
    async def archer(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.chosen = 'Archer'
            #await interact.response.send_message('Archer')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

    @discord.ui.button(label='Caster')
    async def caster(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.chosen = 'Caster'
            #await interact.response.send_message('Caster')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

    @discord.ui.button(label='Healer')
    async def healer(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.chosen = 'Healer'
            #await interact.response.send_message('Healer')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)
    


@bot.command()
async def testbutton(ctx:Context):
    view = thisButton(ctx)
    await ctx.send('Pick a number.', view=view)
    
@bot.command()
async def createChar(ctx:Context):
    view = charCreation(ctx)
    main = await ctx.send('Pick your class.', view=view)
    desc = await ctx.send('''```css
[1]   Warrior - Adept in hand-to-hand combat
[2]   Archer  - Adept in ranged attacks
[3]   Caster  - Adept in damaging spells
[4]   Healer  - Adept in healing and support spells```''')
    await view.wait()
    await desc.delete()
    await main.edit(content='What is your name?', view=None)
    def check(msg):
        return msg.author.id == view.uid and msg.channel == view.channel
    msg = await bot.wait_for('message', check=check)
    view.name = msg.content
    regChar = postg.registerChar(view)
    if regChar == None:
        await ctx.send('User already has a character.')
    elif regChar:
        await ctx.send('Your character of `'+view.name+'` has been created!')
    else: 
        await ctx.send('User is not registered. `sk register`')
    return view

async def deleteChar(ctx:Context):
    view = charDeletion(ctx)
    main = await ctx.send('Do you want to delete your character? (This will reset everything and irreversible.)', view=view)
    await view.wait()
    if view.chosen == 'yes':
        if postg.deleteChar(ctx.author):
            await main.edit(content='Character deleted.', view=None)
        else:
            await main.edit(content="You don't have any character.", view=None)
    if view.chosen == 'no':
         await main.edit(content='Command aborted.', view=None)
    return view

class charDeletion(discord.ui.View):
    def __init__(self,ctx):
        super().__init__()
        self.uid = ctx.author.id
        self.channel = ctx.channel
        self.chosen = '0'
        self.name = ''
        self.value = None

    @discord.ui.button(label='Yes')
    async def yes(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.chosen = 'yes'
            #await interact.response.send_message('Warrior')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

    @discord.ui.button(label='No')
    async def no(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.chosen = 'no'
            #await interact.response.send_message('Warrior')
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

@bot.command()
async def hello(ctx: Context):
    if ctx.author.id == owner:
        await ctx.send('Hello Shadow master!')

@bot.event
async def on_message(message):
    user = message.author
    

    if user == bot.user:
        return

    if user.id == owner:
        if message.content == 'hello':
            await message.channel.send('Hello Shadow!')
    

    
    if message.content.startswith('sk '):
        content = message.content.replace('sk ','')
        if user.id == owner:
            if content == "fix":
                postg.fix()
                await message.channel.send("Command executed.")
            if content == "reset":
                postg.resetAll()
                await message.channel.send("Database reset.")
            if content == "view all":
                player = embd.viewPlayers(user)
                chars = embd.viewChars(user)
                if not (player and chars):
                    await message.channel.send("One or all database empty.")
                else:
                    await message.channel.send("```css\n"+player+"```")
                    await message.channel.send("```css\n"+chars+"```")
        if content == "register":
            if postg.registerUser(user):
                await message.channel.send('User successfully registered!')
            else:
                await message.channel.send('User already registered!')
        if content == "view profile":
            embed = embd.viewProfile(user)
            if embed:
                #await message.channel.send('You are <@'+profile['id']+'>, name of '+profile['name']+' with status of '+profile['status'])
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('Profile not found. Please register using `sk register`.')

        if content == 'create':
            ctx = await bot.get_context(message)
            info = await createChar(ctx)
        if content == 'delete':
            ctx = await bot.get_context(message)
            await deleteChar(ctx)
        if content == 'help':
            await message.channel.send(embed=embd.viewHelp())
        if content.startswith('portrait '):
            content = content.replace('portrait ','')
            if content.startswith('update '):
                content = content.replace('update ','')
                img = postg.updateImg(content,user)
                if img == None:
                    await message.channel.send('Database not found.')
                if img:
                    await message.channel.send('Portrait updated!')
                else:
                    await message.channel.send('Something went wrong.')





    await bot.process_commands(message)


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


bot.run(str(os.environ.get('IV')))