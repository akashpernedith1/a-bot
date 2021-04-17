#Modules
import discord
import random
import math
import os
from discord.ext import commands
from keep_alive import keep_alive
import aiohttp

client=commands.Bot(command_prefix=".")
PI=3.14159
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,activity=discord.Game(".help"))
  print("Bot is ready.")

@client.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.CommandNotFound):
    await ctx.send("Invalid command used. Please key in `.help` to show a list of all available commands.")

#Functions
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

def distance(x1:float,x2:float,y1:float,y2:float):
  return ((x2-x1)**2+(y2-y1)**2)**0.5

def slope(x1:float,x2:float,y1:float,y2:float):
  return (y2-y1)/(x2-x1)

def midptx(x1:float,x2:float):
  return (x1+x2)/2

def midpty(y1:float,y2:float):
  return (y1+y2)/2

def py(a:float,b:float):
  return ((a**2)+(b**2))**0.5

def sin(a:float,b:float,c:float):
  return b/c

def cos(a:float,b:float,c:float):
  return a/c

def tan(a:float,b:float,c:float):
  return b/a

def triarea(b:float,h:float):
  return (b*h)*0.5

def quadarea(b:float,h:float):
  return b*h

def traparea(b1:float,b2:float):
  return 0.5*(b1+b2)

def circlearea(r:int):
  return PI*r**2

def cubevol(l:float,w:float,h:float):
  return l*w*h

def conevol(r:int,h:float):
  return PI*r**2*h/3

def spherevol(r:int):
  return 4/3*PI*r**3

def cylindervol(r:int,h:float):
  return PI*r**2*h

def circumference(r:int):
  return 2*PI*r

def diamarea(a:float):
  return a/PI

#Commands
@client.command(name="meme",help="Sends memes.")
async def meme(ctx):
  async with aiohttp.ClientSession() as cs:
    async with cs.get("https://www.reddit.com/r/memes.json") as r:
      memes=await r.json()
      embed=discord.Embed(color=discord.Color.purple())
      embed.set_image(url=memes["data"]["children"][random.randint(0,25)]["data"]["url"])
      embed.set_footer(text=f"Powered by r/memes! | Meme requested by {ctx.author}")
      await ctx.send(embed=embed)

@client.command(name="diamarea",help="Finds the diameter with area given of a circle.")
async def mathdiamarea(ctx,radius:int):
  try:
    result=diamarea(radius)
    await ctx.send(result)
  except:
    pass
@mathdiamarea.error
async def mathdiamarea_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="circumference",help="Finds the circumference of a circle.")
async def mathcircumference(ctx,radius:int):
  try:
    result=circumference(radius)
    await ctx.send(result)
  except:
    pass
@mathcircumference.error
async def mathcircumference_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="cylindervol",help="Finds the volume of a cylinder.")
async def mathcylindervol(ctx,radius:int,height:float):
  try:
    result=cylindervol(radius,height)
    await ctx.send(result)
  except:
    pass
@mathcylindervol.error
async def mathcylindervol_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="spherevol",help="Finds the volume of a sphere.")
async def mathspherevol(ctx,radius:int):
  try:
    result=spherevol(radius)
    await ctx.send(result)
  except:
    pass
@mathspherevol.error
async def mathspherevol_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="conevol",help="Finds the volume of a cone.")
async def mathconevol(ctx,radius:int,height:float):
  try:
    result=conevol(radius,height)
    await ctx.send(result)
  except:
    pass
@mathconevol.error
async def mathconevol_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="cubevol",help="Finds the volume of a cube.")
async def mathcubevol(ctx,length:float,width:float,height:float):
  try:
    result=cubevol(length,width,height)
    await ctx.send(result)
  except:
    pass
@mathcubevol.error
async def mathcubevol_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="circlearea",help="Finds the area of a circle.")
async def mathcirclearea(ctx,radius:int):
  try:
    result=circlearea(radius)
    await ctx.send(result)
  except:
    pass
@mathcirclearea.error
async def mathcirclearea_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="traparea",aliases=["paralleloarea","rhombusarea"],help="Finds the area of a trapezoid & other quads.")
async def mathtraparea(ctx,b1:float,b2:float):
  try:
    result=traparea(b1,b2)
    await ctx.send(result)
  except:
    pass
@mathtraparea.error
async def mathtraparea_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="triarea",help="Finds the area of a triangle.")
async def mathtriarea(ctx,base:float,height:float):
  try:
    result=triarea(base,height)
    await ctx.send(result)
  except:
    pass
@mathtriarea.error
async def mathtriarea_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="quadarea",aliases=["rectarea","squarearea"],help="Finds the area of a square/rectangle.")
async def mathquadarea(ctx,base:float,height:float):
  try:
    result=quadarea(base,height)
    await ctx.send(result)
  except:
    pass
@mathquadarea.error
async def mathquadarea_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="sin",help="Finds the sine value in decimal form.")
async def mathsin(ctx,a:float,b:float,c:float):
  try:
    result=sin(a,b,c)
    await ctx.send(result)
  except:
    pass
@mathsin.error
async def mathsin_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="cos",help="Finds the cosine value in decimal form.")
async def mathcos(ctx,a:float,b:float,c:float):
  try:
    result=cos(a,b,c)
    await ctx.send(result)
  except:
    pass
@mathcos.error
async def mathcos_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="tan",help="Finds the tangent value in decimal form.")
async def mathtan(ctx,a:float,b:float,c:float):
  try:
    result=tan(a,b,c)
    await ctx.send(result)
  except:
    pass
@mathtan.error
async def mathtan_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="pythagoras",help="Finds the C by using the pythagorean theorem.")
async def mathpy(ctx,a:float,b:float):
  try:
    result=py(a,b)
    await ctx.send(f"c: **{result}**")
  except:
    pass
@mathpy.error
async def mathpy_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="randomnum",help="Gives you a random number from 0 to 1000000.")
async def randomnum(ctx):
  await ctx.send(f"**{random.randint(0,1000000)}**")

@client.command(name="fortune",help="Tells your fortune.")
async def fortune(ctx):
  fortunes=["Plan for many pleasures ahead.","You can always find happiness at work on Friday.","You will live a long and happy life.","Little and often makes much.","Something you lost will soon turn up.","Love is like wildflowers, it is often found in the most unlikely places.","BAZINGA! -once again you fallen for one of my pranks!","Love is for the lucky and the brave","You will be invited to an exciting event","The secret of getting ahead is getting started.","Shame on you for thinking a cookie is psychic.","You need a mint, like bad.","Psst! They're being paid to love you!","**Error 404: Fortune not found.**","You just ate cat.","This cookie fell on the ground.","Someone in your life needs a letter from you.","Soon you will recieve a letter from a loved one.","A cheerful letter or message is on its way to you.","You will be called upon to celebrate some good news.","**Try Again.**","You will live a long time, long enough to open many, many fortune cookies.","You will recieve a fortune.","You are my sidekick.","You will be rich in the future.","You need to get help.","You need some milk!","You need to read the docs!","You need to key in `.help` to get help.","You need to get a life.","You have failed.","You passed the test!","You are a beast.","You are special.","You are loved."]
  await ctx.send(random.choice(fortunes))

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
  await ctx.send(f"Owner: `ash2176#0001`\n Bot Tags: **Moderation**, **Fun** \n API: discord.py")

@client.command(name="support",help="This is the support server for the bot.")
async def support(ctx):
  await ctx.send("https://discord.gg/99KgwBASDC")

@client.command(name="8ball",help="Gives a random answer to your questions.")
async def _8ball(ctx,*,question):
  responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'Try Again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
  await ctx.send(f"Question: {question}\n Answer: **{random.choice(responses)}**")
@_8ball.error
async def _8ball_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="rps",help="Play rock paper scissors by saying rock, paper, or scissors only.")
async def rps(ctx,*,option):
  choices=["Rock","Paper","Scissors"]
  await ctx.send(random.choice(choices))

@rps.error
async def rps_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="echo",help="Repeats your message.")
async def echo(ctx,*,message):
  await ctx.send(f"{message}")
@echo.error
async def echo_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="ascii",help="Repeats your message in ascii format.")
async def ascii(ctx,*,message):
  await ctx.send(f"`{message}`")
@echo.error
async def ascii_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="bold",help="Repeats your message in bold.")
async def bold(ctx,*,message):
  await ctx.send(f"**{message}**")
@echo.error
async def bold_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="italic",help="Repeats your message in italics.")
async def italic(ctx,*,message):
  await ctx.send(f"*{message}*")
@echo.error
async def italic_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="strike",help="Repeats your message in a striked form.")
async def strike(ctx,*,message):
  await ctx.send(f"~~{message}~~")
@echo.error
async def strike_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

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
  mbed=discord.Embed(title="Success!",description=f"{user} has been kicked.")
  if ctx.author.guild_permissions.kick_members:
    await ctx.send(embed=mbed)
    await guild.kick(user=user)

@client.command(name="ban",help="Permanently bans a member from the guild.")
async def ban(ctx,user:discord.User):
  guild=ctx.guild
  mbed=discord.Embed(title="Success!",description=f"{user} has been banned.")
  if ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=mbed)
    await guild.ban(user=user)

@client.command(name="unban",help="Unbans a member with their user id.")
async def unban(ctx,user:discord.User):
  guild=ctx.guild
  mbed=discord.Embed(title="Success!",description=f"{user} is now unbanned!")
  if ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=mbed)
    await guild.unban(user=user)

@client.command(name="midpoint",help="Finds the mispoint of two points")
async def mathmidpt(ctx,x1:float,x2:float,y1:float,y2:float):
  try:
    resultx=midptx(x1,x2)
    resulty=midpty(y1,y2)
    await ctx.send(f"(**{resultx}**,**{resulty}**)")
  except:
    pass
@mathmidpt.error
async def mathmidpt_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="slope",help="Finds the slope of a line that passes through two points.")
async def mathslope(ctx,x1:float,x2:float,y1:float,y2:float):
  try:
    result=slope(x1,y1,x2,y2)
    await ctx.send(result)
  except:
    pass
@mathslope.error
async def mathslope_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="distance",help="Finds the distance between two points.")
async def mathdist(ctx,x1:float,x2:float,y1:float,y2:float):
  try:
    result=distance(x1,y1,x1,y2)
    await ctx.send(result)
  except:
    pass
@mathdist.error
async def mathdist_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="add",help="Adds numbers (Calculator)")
async def mathadd(ctx, x: float, y: float):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass
@mathadd.error
async def mathadd_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")
    
@client.command(name="exponent",help="Exponentially increases numbers (Calculator)")
async def mathexp(ctx, x: float, y: float):
	try:
		result = exp(x, y)
		await ctx.send(result)

	except:
		pass
@mathexp.error
async def mathexp_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="subtract",help="Subtracts numbers (Calculator)")
async def mathsub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass
@mathsub.error
async def mathsub_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="divide",help="Divides numbers (Calculator)")
async def mathdiv(ctx, x: float, y: float):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass
@mathdiv.error
async def mathdiv_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="multiply",help="Multiplies numbers (calculator)")
async def mathmult(ctx, x: float, y: float):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass
@mathmult.error
async def mathmult_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")

@client.command(name="squareroot",help="Takes the square root from a number.")
async def mathsqrt(ctx, x: float):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass
@mathsqrt.error
async def mathsqrt_error(ctx,error):
  if isinstance(error,commands.MissingRequiredArgument):
    await ctx.send("Please pass in all required arguments. If you are still confused, please key in `.help <name_of_command>` for more info on that command & how to use it.")
keep_alive()
client.run(os.getenv("TOKEN"))
