import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class SimpleView(discord.ui.View):

    @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
    async def add_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("hello world")

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cancelling")

class TimeoutView(discord.ui.View):

    foo = None
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True

        await self.message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timeout")
        await self.disable_all_items()

    @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
    async def add_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("hello world")
        self.foo = True
        self.stop

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cancelling")
        self.foo = True
        self.stop
        await self.disable_all_items()  # Disable all items in the view

class ButtonCalculator(discord.ui.View):
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True

        await self.message.edit(view=self)

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timeout")
        await self.disable_all_items()
    #-1 is nothin 0 is add 1 is subtracts 2 is multipkle 3 is divide
    operation = -1

    @discord.ui.button(label="Add", style=discord.ButtonStyle.success)
    async def add(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Currently Adding.....")
        self.operation = 0
        self.stop

    @discord.ui.button(label="Subtract", style=discord.ButtonStyle.success)
    async def sub(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Currently Subtracting.... ")
        self.operation = 2
        self.stop
    
    @discord.ui.button(label="Multiply", style=discord.ButtonStyle.success)
    async def mul(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Currently Multiplying..... ")
        self.operation = 3
        self.stop
    
    @discord.ui.button(label="Divide", style=discord.ButtonStyle.success)
    async def div(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Currently Dividing... ")
        self.operation = 4
        self.stop



#calculations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

@bot.command()
async def calculate(ctx, num1, operation, num2):
    a = int(num1)
    b = int(num2)

    if operation == "+":    
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "/":
        result = divide(a, b)
    elif operation == "*":
        result = multiply(a, b)
    else:
        result = "Invalid sign"

    await ctx.send(result)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    

@bot.command()
async def button(ctx):
    # a = int(num1)
    # b = int(num2)

    view = TimeoutView(timeout=5)

    message = await ctx.send(view=view)
    view.message = message
    await view.wait()
    await view.disable_all_items()

    if view.foo is None:
        print("Timeout")
    elif view.foo == True:
        print("ok")
    else:
        print("cancel")

@bot.command()
async def spam(ctx, num1):
    a = int(num1)
    for i in range(a):
        await ctx.send("@ ")

@bot.command()
async def buttonMath(ctx, arg1, arg2):
    b = int(arg1)
    a = int(arg2)

    # Send the initial message with buttons
    view = ButtonCalculator(timeout=20)
    message = await ctx.send(view=view)
    view.message = message

    # Start the view and wait for the timeout
    await view.wait()

    # Disable all items in the view after the timeout
    await view.disable_all_items()

    # Calculate the result based on the user's button click
    result = None
    if view.operation == 0:
        result = add(a, b)
    elif view.operation == 1:
        result = subtract(a, b)
    elif view.operation == 2:
        result = multiply(a, b)
    elif view.operation == 3:
        result = divide(a, b)

    # Send the result message if available
    if result is not None:
        await ctx.send(f"The result is {result}")




bot.run(TOKEN)