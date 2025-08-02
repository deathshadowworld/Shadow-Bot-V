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

def getVocabEasy():
    module = []  
    module.append({
        'question':'Which word is similar to `hot`? \nA. Heat \nB. Cold \nC. Bot \nD. Fire',
        'answer':'A',
    })
    module.append({
        'question':'Which word is similar to `big`? \nA. Small \nB. Huge \nC. Tiny \nD. Amazing',
        'answer':'B',
    })
    module.append({
        'question':'Which word is similar to `cold`? \nA. Sunny \nB. WindY \nC. Freezing \nD. Raining',
        'answer':'C',
    })
    
    
    
    module.append({
        'question':'Her stature is \_\_\_\_\_\_\_\_. \nA. Slim \nB. Lanky \nC. Obese \nD. Fast',
        'answer':'B',
    })
    module.append({
        'question':'His car is \_\_\_\_\_\_\_\_. \nA. Wings \nB. Lanky \nC. Under \nD. Fast',
        'answer':'D',
    })

    return module

    module.append({
        'question':'Which word is similar to ``? \nA.  \nB.  \nC.  \nD. ',
        'answer':'',
    })
    module.append({
        'question':'\_\_\_\_\_. \nA.  \nB.  \nC.  \nD. ',
        'answer':'',
    })
    module.append({
        'question':' \nA.  \nB.  \nC.  \nD. ',
        'answer':'',
    })

def getVocabMed():
    module = []
    module.append({
        'question':'Which word is similar to `huge`? \nA. Minuscule \nB. Enormous \nC. Empowered \nD. Voluptuous',
        'answer':'B',
    })