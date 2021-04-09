import discord
import random
import math
import os
from discord.ext import commands
from keep_alive import keep_alive
client=commands.Bot(command_prefix=".")
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity=discord.Game(".help"))
  print("Bot is ready.")
@client.command(name="prefix",help="The prefix I respond to.")
async def prefix(ctx):
  await ctx.send(".")
@client.command(name="invite",help="Link to invite me to your server(s).")
async def invite(ctx):
  await ctx.send("https://discord.com/api/oauth2/authorize?client_id=823664697076875335&permissions=76800&scope=bot")
@client.command(name="ping",help="Returns Pong! with latency.")
async def ping(ctx):
  await ctx.send(f"**Pong!** {round(client.latency*1000)}ms")
@client.command(name="info",help="Tells info about owner/bot")
async def info(ctx):
  await ctx.send("Owner: `ash2176#0001`\n Bot Tags: **Moderation**, **Fun**")
@client.command(name="support",help="This is the support server for the bot.")
async def support(ctx):
  await ctx.send("https://discord.gg/99KgwBASDC")
@client.command(name="8ball",help="Gives a random answer to your questions.")
async def _8ball(ctx,*,question):
  responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'Try Again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
  await ctx.send(f"Question: {question}\n Answer: **{random.choice(responses)}**")
@client.command(name="rps",help="Play rock paper scissors")
async def rps(ctx,*,choice):
  choices=["Rock","Paper","Scissors"]
  await ctx.send(random.choice(choices))
  if choice==choices:
    await ctx.send("It's a tie!")
  if choice=="Rock" or "ROCK" or "rock" and choices=="Paper":
    await ctx.send("You win!")
  elif choice=="Rock" or "ROCK" or "rock" and choices=="Scissors":
    await ctx.send("You win!")
  elif choice=="Scissors" or "SCISSORS" or "scissors" and choices=="Paper":
    await ctx.send("I win!")
  elif choice=="Scissors" or "SCISSORS" or "scissors" and choices=="Rock":
    await ctx.send("I win!")
  elif choice=="Paper" or "PAPER" or "paper" and choices=="Rock":
    await ctx.send("You win!")
  elif choice=="Paper" or "PAPER" or "paper" and choices=="Scissors":
    await ctx.send("I win!")
@client.command(name="echo",help="Repeats your message.")
async def echo(ctx,*,message):
  await ctx.send(f"{message}")
@client.command(name="roll",help="Gives a random number like a dice from 1-6.")
async def roll(ctx):
  nums=[1,2,3,4,5,6]
  await ctx.send(f"I rolled a {random.choice(nums)}")
@client.command(name="coinflip",help="Flips an imaginary coin and says either heads or tails.")
async def coinflip(ctx):
  possibilities=["Heads","Tails"]
  await ctx.send(f"Result: **{random.choice(possibilities)}**")
@client.command(name="delete",help="Deletes any amount of messages.")
async def delete(ctx,amount=1):
  await ctx.channel.purge(limit=amount)
@client.command(name="kick",help="Kicks a member from the guild.")
async def kick(ctx,user:discord.User):
  guild=ctx.guild
  mbed=discord.Embed(title="Success!",description=f"{user} has successfully been kicked.")
  if ctx.author.guild_permissions.kick_members:
    await ctx.send(embed=mbed)
    await guild.kick(user=user)
@client.command(name="ban",help="Permanently bans a member from the guild.")
async def ban(ctx,user:discord.User):
  guild=ctx.guild
  mbed=discord.Embed(title="Success!",description=f"{user} has successfully been banned.")
  if ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=mbed)
    await guild.ban(user=user)
@client.command(name="unban",help="Unbans a member with the user id.")
async def unban(ctx,user:discord.User):
  guild=ctx.guild
  mbed=discord.Embed(title="Success!",description=f"{user} has successfully unbanned.")
  if ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=mbed)
    await guild.unban(user=user)
def add(n: float, n2: float):
	return n + n2
def sub(n: float, n2: float):
	return n - n2
def div(n: float, n2: float):
	return n / n2
def sqrt(n: float):
	return math.sqrt(n)
def mult(n: float, n2: float):
	return n * n2
def exp(n:float,n2:float):
  return n**n2

@client.command(name="add",help="Adds numbers (Calculator)")
async def mathadd(ctx, x: float, y: float):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass
    
@client.command(name="exponent",help="Exponentially increases numbers (Calculator)")
async def mathexp(ctx, x: float, y: float):
	try:
		result = exp(x, y)
		await ctx.send(result)

	except:
		pass

@client.command(name="subtract",help="Subtracts numbers (Calculator)")
async def mathsub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass

@client.command(name="divide",help="Divides numbers (Calculator)")
async def mathdiv(ctx, x: float, y: float):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass

@client.command(name="multiply",help="Multiplies numbers (calculator)")
async def mathmult(ctx, x: float, y: float):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass

@client.command(name="squareroot",help="Takes the square root from a number.")
async def mathsqrt(ctx, x: float):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass
keep_alive()
client.run(os.getenv("TOKEN"))
