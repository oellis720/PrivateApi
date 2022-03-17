import os
import random
import datetime as dt


import discord
from discord.ext import commands
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('CHANNEL_ID')
CLIENT = os.getenv('CLIENT_ID')

bot = commands.Bot(command_prefix='!')


#activates jeoff in the console
#and handles annoucements
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )
    activity = discord.Game(name="Taking Leon to get Taco Bell.")
    await bot.change_presence(activity=activity)

    time = dt.datetime.today()
    print (f'The time is {time}')
    if time.weekday == 4:
        if time.hour == 15:
            if time.minute == 00:
                print('i\'m working on it')
                message_channel = bot.get_channel(id=719674909550182443)
                await message_channel.send("This is just a test don't worry about it.")



#welcome message
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name=CHANNEL)
    await channel.send(f'{member.name} has joined. Welcome to the crew!')


#commands
@bot.command(name='hbd', help='Jeoffrey sends a birthday message!')
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    response = 'Have a good birthday, Boss.'
    await ctx.send(response)
    
    
#role assignment
@bot.command(name='roles', help='Jeoffrey auto-adds a role to the user specified')
async def add_role(ctx, member: discord.Member, role: discord.Role):
    confirm = [
        'On it, Boss.',
        'Got it, Boss.',
        'Done.',
        "It's ready."
    ]
    response = random.choice(confirm)
    await member.add_roles(role)
    await ctx.send(response)
    
#text responses
@bot.listen('on_message')
async def phrase(message):
    txt = message.content.lower()

    welcome = [
        'No problem.',
        'Happy to help.',
        'That\'s what I\'m here for.',
    ]

    okay = [
        "\U0001F44D",
        "\U0001F197",
        "\U0001F192",
    ]

    hello = [
        'Sup.',
        'Howdy.',
        "\U0001F44B",

    ]

    if 'hey jeoff' in txt:
        response = random.choice(hello)
        await message.channel.send(response)

    if ('thanks jeoff') in txt:
        response = random.choice(welcome)
        await message.channel.send(response)
    if 'i love you jeoff' in txt:
        response = random.choice(okay)
        await message.channel.send(response)

    if '69' in txt:
        await message.channel.send("Heh, nice.")


#command error handling
@add_role.error
async def role_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Didn't quite get that, Boss...")




bot.run(TOKEN)




#vvvvvvvvv old stuff I may implement in the future

#@tasks.loop(seconds=10)
#async def weekly_msg():
 #   message_channel = bot.get_channel(id=719674909550182443)
  #  print(f'Working in {message_channel}')
   # await message_channel.send("This is just a test don't worry about it.")

#@weekly_msg.before_loop
#async def before():
 #   await bot.wait_until_ready()
  #  print("Done waiting.")