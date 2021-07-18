#IMPORTS
import discord
import random
import asyncio
from discord.ext import commands
from pyrandmeme import *

#CONSTANTS AND FIXED VARIABLES
chances = {
    0:"No. Never.",
    10:"I don't think so",
    20:"Don't bet on it.",
    30:"Mostly not.",
    40:"Small chance.",
    50:"Maybe, maybe not.",
    60:"It might be so.",
    70:"Possible.",
    80:"High chance.",
    90:"Mostly yeah.",
    100:"Yes. Sure."
}
truth=[
    "When was the last time you lied?",
    "When was the last time you cried?",
    "What's your biggest fear?",
    "What's your biggest fantasy?",
    "What's something you're glad your parents doesn't know about you?",
    "Have you ever cheated on someone?",
    "What's the worst thing you've ever done?",
    "What's a secret you've never told anyone?",
    "Do you have a hidden talent?",
    "Who was your first celebrity crush?",
    "What are your thoughts on polyamory?",
    "What's the worst intimate experience you've ever had?",
    "Have you ever cheated in an exam?",
    "Have you ever broken the law?",
    "What's the most embarrassing thing you've ever done?",
    "What's the biggest mistake you've ever made?",
    "What's the most disgusting thing you've ever done?",
    "Who would you like to kiss in this room?",
    "What's the worst thing anyone's ever done to you?",
    "Have you ever had a run in with the law?",
    "What's your worst habit?",
    "What's the worst thing you've ever said to anyone?",
    "What's the strangest dream you've had?",
    "Have you ever been caught doing something you shouldn't have?",
    "What's the worst date you've been on?",
    "What's your biggest regret?",
    "What's the biggest misconception about you?",
    "Why did your last relationship break down?",
    "Have you ever lied to get out of a bad date?",
    "Say two honest things about everyone else in the group.",
]

dare=[
    "Jump from the 1st floor of any building.",
    "Do 100 squats.",
    "Show the most embarrassing photo on your phone.",
    "Give a foot massage to the person on your right.",
    "Say something dirty to the person on your left.",
    "Let the rest of the group DM someone from your Instagram account.",
    "Eat a banana without using your hands.",
    "Twerk for a minute.",
    "Keep your eyes closed until it’s your go again.",
    "Like the first 15 posts on your Facebook newsfeed.",
    "Send a text to the last person in your phonebook.",
    "Eat a raw onion.",
    "Keep three ice cubes in your mouth until they melt.",
    "Give a lap dance to someone of your choice.",
    "Yell out the first word that comes to your mind.",
    "Show off your orgasm face.",
    "Empty out your wallet/purse and show everyone what’s inside.",
    "Show the last five people you texted and what the messages said.",
    "Try to put your whole fist in your mouth.",
    "Remove four items of clothing.",
    "Eat a spoonful of mustard.",
    "Put 10 different available liquids into a cup and drink it.",
    "Do your best impression of a baby being born.",
    "Try to lick your elbow.",
    "Pretend to be the person to your right for 10 minutes.",
    "Be someone’s pet for the next 5 minutes.",
    "Try to drink a glass of water while standing on your hands.",
    "Do your best sexy crawl.",
    "Put as many snacks into your mouth at once as you can.",
    "Try and make the group laugh as quickly as possible."
]

#MAIN COG
class Minigames(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Meme
    @commands.command(name='meme')
    async def meme(self, ctx):
        await ctx.send(embed = await pyrandmeme())

    #8ball
    @commands.command(name='8ball', aliases=['chance','8b'])
    async def eightball(self, ctx, arg: str=None):
        if arg is None:
            await ctx.send(f"{ctx.author.mention}\nAsk me something valid pls.")
        else:
            chance=random.choice(list(chances.keys()))
            truth_embed = discord.Embed()
            truth_embed.add_field(name=f"{ctx.author.name}'s 8ball results", value=chances[chance])
            await ctx.send(f"{ctx.author.mention}", embed=truth_embed)

    #TruthOrDare
    @commands.command(name='truthordare',aliases=['tord'])
    async def truthordare(self, ctx, arg: str=None):
        if arg is None:
            await ctx.send(f"{ctx.author.mention} Truth? or Dare?")
        elif arg.lower() in ['truth','t']:
            await ctx.send(f"{ctx.author.mention} {random.choice(truth)}")
        elif arg.lower() in ['dare','d']:
            await ctx.send(f"{ctx.author.mention} {random.choice(dare)}")
        else:
            await ctx.send("Not an option.")

    #GuessTheNumber
    @commands.command(name='guessthenum',aliases=['guess','gtn'])
    async def guessnumber(self, ctx):
        num = random.randint(1,10)
        await ctx.send('The number is between 1 to 10. Go ahead, guess!')

        def check(msg):
            return (msg.author == ctx.author) and (msg.channel == ctx.channel)

        try:
            msg = await self.client.wait_for("message", check=check, timeout=30)
            try:
                guess = int(msg.content)
                if num==guess:
                    await ctx.send(f"{ctx.author.mention} You win!")
                else:
                    await ctx.send(f"Oops! The number was {num}.")
            except:
                await ctx.send(f"{ctx.author.mention} Give a number input.")

        except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author.mention} Sorry, you didn't reply in time!")

    #HighLow
    @commands.command(name='highlow',aliases=['hl'])
    async def highlow(self, ctx):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)

        value=f"I have chosen a number between 1 and 100. Your key number is: **{num2}**"

        hl_input_embed = discord.Embed()
        hl_input_embed.add_field(name=f"{ctx.author.name}'s HighLow game", value=value)

        await ctx.send(f"{ctx.author.mention}",embed=hl_input_embed)

        def check(msg):
            return (msg.author == ctx.author) and (msg.channel == ctx.channel)

        try:
            hl_output_embed = discord.Embed()
            msg = await self.client.wait_for("message", check=check, timeout=30)
            if num2 < num1:
                if msg.content.lower() in ['high','h']:
                    hl_output_embed.add_field(name=f"{ctx.author.name}'s HighLow game results.",
                                            value=f"That's right! The number is **{num1}** and the key is **{num2}**!")
                else:
                    hl_output_embed.add_field(name=f"{ctx.author.name}'s HighLow game results.",
                                            value=f"Oops! The number is **{num1}** and the key is **{num2}**!")
                await ctx.send(f"{ctx.author.mention}",embed=hl_output_embed)

            elif num2 > num1:
                if msg.content.lower() in ['low','l']:
                    hl_output_embed.add_field(name=f"{ctx.author.name}'s HighLow game results.",
                                            value=f"That's right! The number is **{num1}** and the key is **{num2}**!")
                else:
                    hl_output_embed.add_field(name=f"{ctx.author.name}'s HighLow game results.",
                                            value=f"Oops! The number is **{num1}** and the key is **{num2}**!")
                await ctx.send(f"{ctx.author.mention}",embed=hl_output_embed)

            elif num2 == num1:
                if msg.content.lower() in ['same','s']:
                    hl_output_embed.add_field(name=f"{ctx.author.name}'s HighLow game results.",
                                            value=f"That's right! The number is **{num1}** and the key is **{num2}**!")
                else:
                    hl_output_embed.add_field(name=f"{ctx.author.name}'s HighLow game results.",
                                            value=f"Oops! The number is **{num1}** and the key is **{num2}**!")
                await ctx.send(f"{ctx.author.mention}",embed=hl_output_embed)

        except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author.mention}Sorry, you didn't reply in time!")

def setup(client):
    client.add_cog(Minigames(client))
