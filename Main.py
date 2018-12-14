import asyncio
import discord
from discord.ext.commands import Bot
import random
import math

BOT_PREFIX = "!"
file = (open("token.txt").read()).split('\n')
TOKEN = file[0]

client = Bot(command_prefix=BOT_PREFIX)


async def my_background_task():
    counter = 0
    await client.wait_until_ready()
    while not client.is_closed:
        print(counter)
        counter += 1
        await asyncio.sleep(300)



@client.event
async def on_member_join(member):
    role = discord.utils.get(client.get_server('310350971962130432').roles, name="Not real WPCM member")
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    print(member.roles())
    client.add_roles(member)
    await client.send_message(discord.Object(id='342709832803155968'), fmt.format(member, server)), client.add_roles(member, role)


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
async def reminder():
    await client.say("UnderConstruction")


@client.command()
async def play():
    await client.say("UnderConstruction")


client.loop.create_task(my_background_task())
client.run(TOKEN)
