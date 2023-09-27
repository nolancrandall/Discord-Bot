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

    view = SimpleView()
    button = discord.ui.Button(label = "Click me")
    view.add_item(button)
    await ctx.send(view=view)

@bot.command()
async def spam(ctx, num1):
    a = int(num1)
    for i in range(a):
        await ctx.send("@everyone")

bot.run(TOKEN)