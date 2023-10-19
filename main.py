import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random as rnd

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class SimpleView(discord.ui.View):


    @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
    async def add_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("hello")

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Cancelling")

class Blackjackbutton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.did_hit = False
        self.did_reset = False
        self.did_stay = False

    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True

    async def on_timeout(self) -> None:
        await self.message.channel.send("Timeout")
        await self.disable_all_items()
        await self.message.edit(view=self)

    @discord.ui.button(label="Hit", style=discord.ButtonStyle.red)
    async def hit(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.did_hit = True
        self.stop()

    @discord.ui.button(label="Stay", style=discord.ButtonStyle.green)
    async def stay(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.did_stay = True
        self.stop()

    @discord.ui.button(label="Reset", style=discord.ButtonStyle.grey)
    async def reset(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.did_reset = True
        self.stop()

class TimeoutView(discord.ui.View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clicked = False
        self.foo = None
    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True

        await self.message.edit(view=self)

    # async def on_timeout(self) -> None:
    #     await self.message.channel.send("Timeout")
    #     await self.disable_all_items()

    @discord.ui.button(label="Play", style=discord.ButtonStyle.success)
    async def add_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.clicked = True
        print(self.clicked)

    
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









#BLACKJACK STARTS HERE

@bot.command()
async def blackjack(ctx):
    await ctx.send("Welcome to Blackjack!")

    view = TimeoutView(timeout=1)

    message = await ctx.send(view=view)
    view.message = message
    await view.wait()
    await view.disable_all_items()
    if view.clicked == True:
        class Card:
            def __init__(self, x, y, suit, number, picture):
                self.number = number
                self.x = x
                self.y = y
                self.picture = picture
                self.suit = suit
            # def draw(self, x, y):
            #     screen.blit(pygame.image.load(self.picture), (self.x + x, self.y + y))
        #hit counter
        hits = 0
        f = 0
        draw_state = "ready"
        enemy_draw = "ready"
        x = 0
        y = 0



        new_game = True
        #creates lists for each hand and deck
        names = ["Clubs", "Spades", "Diamonds", "Hearts"]
        draw_list = []
        player_hand = []
        enemy_hand = []
        deck = []
        # nested for loops to create all 52 cards
        # first loop runs through all 4 suits
        for name in names:
        #second loop runs thrpugh 1-13 for each of the suits
            for i in range (1, 13):
                index = i
                if i > 10:
                    index = 10
                if name == "Clubs":
        #creates the cards with position, suit, number, and image
        #the names of the clubs pngs were different so I used 2 appends
                    deck.append(Card(x, y, name, index, f"Cards/{name}/card{i}.png"))
                else:
                    deck.append(Card( x, y, name, index, f"Cards/{name}/{i}.png"))
        #shuffles deck
        rnd.shuffle(deck)  
        await ctx.send(f"you have a {deck[1].number} and a {deck[0].number}, your opponent has a {deck[2].number} and a {deck[3].number}") 
        blackjackview = Blackjackbutton() 
        message = await ctx.send(view=blackjackview)
        blackjackview.message = message
        await blackjackview.wait()
        await blackjackview.disable_all_items()
        on_hit = False
        on_stay = False
        on_reset = False
        if blackjackview.did_hit == True:
            await ctx.send("hit")
            on_hit = True

        if blackjackview.did_stay == True:
            await ctx.send("stay")
            on_stay = True

        if blackjackview.did_reset == True:
            await ctx.send("reset")
            on_reset = True
        running = True
        #game loop
        while running:

            if new_game:
                timer = 0
            #starting Hands and initial placement
                player_hand.append(deck[0])
                player_hand.append(deck[1])
                enemy_hand.append(deck[2])
                new_game = False

        

            if on_hit:
                hits += 1
                on_hit = False
                player_hand.append(deck[hits + 3])
                await ctx.send(f"you drew a {player_hand[2].number}")
                blackjackview = Blackjackbutton() 
                message = await ctx.send(view=blackjackview)
                blackjackview.message = message
                await blackjackview.wait()
                await blackjackview.disable_all_items()
                if blackjackview.did_hit == True:
                    await ctx.send("hit")
                    on_hit = True

                if blackjackview.did_stay == True:
                    await ctx.send("stay")
                    on_stay = True

                if blackjackview.did_reset == True:
                    await ctx.send("reset")
                    on_reset = True

            if on_reset:
            #resets game when button clicked
                rnd.shuffle(deck)
                player_hand = []
                enemy_hand = []
                player_hand.append(deck[0])
                player_hand.append(deck[1])
                enemy_hand.append(deck[2])

            #sets aces to either 1 or 11
            player_total = 0
            for i in range(len(player_hand)):
                if player_hand[i].number == 1:
                    player_hand[i].number = 11
                player_total += player_hand[i].number
                if player_total > 21:
                    for i in range(len(player_hand)):
                        if player_hand[i].number == 11:
                            player_total -= 10
                            player_hand[i].number = 1
            #calculates total points
            enemy_total = 0


        

            #after games ends
            if player_total > 21:
                await ctx.send("YOU BUSTOED YOU LOSE LOOOOOOOSER")
                draw_state = "wait"
                # end screen
            if on_stay:
                #enemy drawing
                for i in range(len(enemy_hand)):
                    if enemy_hand[i].number == 1:
                        enemy_hand[i].number = 11 
                    enemy_total += enemy_hand[i].number
                    if enemy_total > 21:
                        for i in range(len(enemy_hand)):
                            if enemy_hand[i].number == 11:
                                enemy_total -= 10
                                enemy_hand[i].number = 1
                if enemy_total <= 16:
                    hits += 1
                    enemy_hand.append(deck[hits + 1])
                    for i in range(len(enemy_hand)):
                        if enemy_hand[i].number == 1:
                            enemy_hand[i].number = 11 
                        enemy_total += enemy_hand[i].number
                        if enemy_total > 21:
                            for i in range(len(enemy_hand)):
                                if enemy_hand[i].number == 11:
                                    enemy_total -= 10
                                    enemy_hand[i].number = 1

                    if enemy_total <= 16:
                        hits += 1
                        enemy_hand.append(deck[hits + 1])
                        if enemy_total <= 16:
                            hits += 1
                            enemy_hand.append(deck[hits + 1])
                if enemy_total > 21:
                    await ctx.send("the bot busted, you win")
                
                    break
                    #take to end screen
                elif enemy_total > player_total:
                    await ctx.send("you lose")
                    break
                elif player_total > enemy_total:
                    await ctx.send("you win bot")
                    break
                else:
                    await ctx.send("tie")
                    break
            timer += 1







bot.run(TOKEN)
