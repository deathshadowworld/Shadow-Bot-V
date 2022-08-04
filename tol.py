import discord




class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='[Talk] Merchant', description='Talk to the person behind the stall'),
            discord.SelectOption(label='[Talk] Old Man', description='Talk to the old man by the well'),
            discord.SelectOption(label='[Talk] Little Girl', description='Talk to the little girl selling flowers'),
            discord.SelectOption(label='[Proceed] Walk', description='Continue along the path out of the village')
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='What do you want to do?', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's 
        # selected options. We only want the first one.
        if self.values[0] == '[Talk] Merchant':
            await interaction.response.send_message("Hello there! Sorry I'm currently not open yet. Please come back later!")
        if self.values[0] == '[Talk] Old Man':
            await interaction.response.send_message("Hello there. I'm sure you're lovely but I would like some distance.. for now..")
        if self.values[0] == '[Talk] Little Girl':
            await interaction.response.send_message("Hello mister! Sorry I just ran out flowers. Come back later!")
        if self.values[0] == '[Proceed] Walk':
            await interaction.response.send_message("You walked down the path and met with an invisible wall. Seems like you're trapped in a virtual world.")


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())

async def startGame(ctx):
    view = DropdownView()
    await ctx.send("You arrived in an unfamiliar village. You don't have much recollection of your past. Just now, it felt like you just exist out of thin air. Looking around you, you can see various kind of people.", view=view)