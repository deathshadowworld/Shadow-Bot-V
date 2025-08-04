import discord, os
from discord.ext import commands
from discord.ext.commands import Context
from controller.UserController import User
from controller.MessageController import Message
from db.db import getToken, migrate
from discord.utils import get

owner = 259999538666930177

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="sk ", intents=intents)

adminList = [
    259999538666930177,
    400781611588911116
]

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="shadow dying"))
    print(f'We have logged in as {bot.user}')
    await bot.tree.sync()
    print("Slash commands synced.")

# @bot.command(name='ping')
# async def gameRole(ctx:Context, *, args):
#     GUILD_ID = 784859857937236059
#     guild = bot.get_guild(GUILD_ID)
#     ROLES = {
#         'among us':994957809051516969,
#         'fall guys':994957622874738850,
#         'apex legends':994957847974649916,
#         'minecraft':994957974726529024,
#     }
#     print(args)
#     if args in ROLES:
#         role = get(guild.roles,id=ROLES[args])

#         if role in ctx.author.roles:
#             await ctx.author.remove_roles(role)
#             await ctx.send('Role removed.')
#         else:
#             await ctx.author.add_roles(role)
#             await ctx.send('Role added.')
#     else:
#         await ctx.send('Role not found.')

@bot.hybrid_command(name="register")
async def registerUser(ctx):
    if not User.checkExist(ctx.author.id):
        await ctx.send("What would you like to be called?")
        def check(msg):
            return msg.author.id == ctx.author.id and msg.channel == ctx.channel
        msg = await bot.wait_for('message', check=check)
        user = User(user_id=msg.author.id, nickname=msg.content)
        User.create(user)
        print('User '+ user.nickname +' | '+ str(user.user_id) +' is created successfully.')
        await ctx.send("User %s is registered~" % user.nickname)
    else:
        await ctx.send("User is already registered.")


@bot.command()
async def hello(ctx: Context):
    if ctx.author.id == owner:
        await ctx.send('Hello Shadow master!', ephemeral=True)

@bot.event
async def on_message(message):
    user = message.author
    
    if user == bot.user:
        return

    if user.id == owner:
        if message.content == 'hello':
            await message.channel.send('Hello Shadow!')
    await bot.process_commands(message)

@bot.event
async def on_voice_state_update(member, before, after):
    VCROLE = 992826737362739282
    GUILD_ID = 784859857937236059

    guild = bot.get_guild(GUILD_ID)
    vc_role = get(guild.roles, id=VCROLE)

    if  after.channel == None:
        await member.remove_roles(vc_role)

    if before.channel == None:
        await member.add_roles(vc_role)


@bot.hybrid_command(name="queue")
async def messageQueue (ctx, question):
    if ctx.author.id in adminList:
        msg = Message.queue(question)
        if msg:
            await ctx.send("Message is queued.\n"+msg)
        else:
            await ctx.send("Message failed to queue.")
    else:
        await ctx.send("No privilege.", ephemeral=True)
        
@bot.hybrid_command(name="view")
async def messageView (ctx):
    if ctx.author.id in adminList:
        result = Message.view()
        for x in result:
            await ctx.send(x)
    else:
        await ctx.send("No privilege.", ephemeral=True)
        
@bot.hybrid_command(name="pop")
async def messagePop (ctx):
    if ctx.author.id in adminList:
        await ctx.send("Question of the Day!\n\n"+ Message.pop())
    else:
        await ctx.send("No privilege.", ephemeral=True)
        
@bot.hybrid_command(name="resetall")
async def messageResetAll (ctx):
    if ctx.author.id in adminList:
        if Message.resetAll():
            await ctx.send("Message stack is reset.")
        else:
            await ctx.send("Message stack failed to reset.")
    else:
        await ctx.send("No privilege.", ephemeral=True)
        
@bot.hybrid_command(name="reset")
async def messageResetAll (ctx,id):
    if ctx.author.id in adminList:
        if Message.reset(id):
            await ctx.send("Message `" + str(id) + "` is reset")
        else:
            await ctx.send("Message `" + str(id) + "` failed to reset.")
    else:
        await ctx.send("No privilege.", ephemeral=True)

@bot.hybrid_command(name="admin")
async def adminCommands(ctx, command):
    if ctx.author.id in adminList:
        if command == "migrate":
            await ctx.send("Resetting database...")
            await ctx.send("Migrating...")
            migrate()
            await ctx.send("Migration finished")
    else:
        await ctx.send("No privilege.", ephemeral=True)

bot.run(getToken())