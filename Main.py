import asyncio
import discord
from discord.ext.commands import Bot
import random
import math
import importlib
import Reminder as rem
from datetime import *

BOT_PREFIX = "!"
file = (open("token.txt").read()).split('\n')
TOKEN = file[0]

client = Bot(command_prefix=BOT_PREFIX)
reminder = rem.Main()

async def my_background_task():
    counter = 0
    await client.wait_until_ready()
    while not client.is_closed:
        for i in reminder.check_reminders():
            member = None
            for server in client.servers:
                for mem in server.members:
                    if member == None:
                        if int(i[0]) == int(mem.id):
                            member=mem
                    else:
                        break
                if not member == None:
                    break
            await client.send_message(member,i[1]+"\n"+i[2])
        await asyncio.sleep(60)

@client.command(
    aliases=["create_rem","cm"],
    pass_context=True
)
async def create_reminder(context,time,title,text=""):
    date= None
    if len(time) == 4:
        date = datetime(datetime.now().year,int(time[0:2]),int(time[2:4]))
    elif len(time) == 8:
        date = datetime(datetime.now().year,int(time[0:2]),int(time[2:4]),int(time[4:6]),int(time[6:8]))
    print(date)
    print(title)
    print(text)
    await client.say(str(time)+" "+str(title)+" "+text)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Not real WPCM member")
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    print(member.roles())
    client.add_roles(member)
    await client.send_message(discord.Object(id='342709832803155968'), fmt.format(member, server)), client.add_roles(
        member, role)


@client.command(
    description="Throws the dice for ya",
    brief="Throws the dice",
    pass_context=True
)
async def dice(context):
    response = random.randint(1, 6)
    await client.say(str(response) + ", " + context.message.author.mention)


@client.command(
    pass_context=True
)
async def ping(context):
    await client.say(context.message.author.mention)


@client.command()
async def square(N):
    number = int(N) * int(N)
    await client.say(str(number))


@client.event
async def on_ready():
    for server in client.servers:
        print(server.id)
    print("Logged in: " + client.user.name)


@client.command(
    name="q",
    description="(-b+-root(b*b-4*a*c))/(2*a)",
    brief="Calculate quadratic"
)
async def quadratic(A, B, C):
    D = int(B) * int(B) - 4 * int(A) * int(C)
    if D < 0:
        await client.say("Valós számokon nincs megoldás")
    elif D == 0:
        await client.say("Gyöke: " + str(-int(B) / (2 * int(A))))
    else:
        await client.say("Első gyöke: " + str((-int(B) + math.sqrt(D)) / (2 * int(A))) + "\n" +
                         "Második gyöke: " + str((-int(B) - math.sqrt(D)) / (2 * int(A))))

@client.command()
async def play():
    await client.say("UnderConstruction")


client.loop.create_task(my_background_task())
client.run(TOKEN)
