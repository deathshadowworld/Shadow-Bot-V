from discord.ui import View,Button
from discord import Interaction
from discord.ext.commands import Context
import discord


class multipleChoice(discord.ui.View):
    def __init__(self,ctx,module):
        super().__init__()
        self.uid = ctx.author.id
        self.channel = ctx.channel
        self.question = module['question']
        self.answer = module['answer']
        self.value = None
    
    @discord.ui.button(label='A')
    async def one(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.value = 'A'
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)
    
    @discord.ui.button(label='B')
    async def two(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.value = 'B'
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

    @discord.ui.button(label='C')
    async def three(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.value = 'C'
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)

    @discord.ui.button(label='D')
    async def four(self, interact: Interaction,button: Button):
        if self.uid == interact.user.id:
            self.value = 'D'
            self.stop()
        else:
            await interact.response.send_message("You're not the expected user.", ephemeral=True)