from discord import Game
from discord.ext.commands import Bot
import random
import math

BOT_PREFIX = "!"
TOKEN = "NTIxMzkxNzA2OTEwNzUyNzc4.Du77YQ.F3_WjZeDXh-ZcV7fYRNqLF4hvUA"

client = Bot(command_prefix=BOT_PREFIX)


@client.command(
    description="Throws the dice for ya",
    brief="Throws the dice",
    pass_context=True
)
async def dice(context):
    response = random.randint(1, 6)
    await client.say(str(response) + ", " + context.message.author.mention)


@client.command()
async def square(N):
    number = int(N) * int(N)
    await client.say(str(number))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Learning"))
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

client.run(TOKEN)