import discord
import random

TOKEN = "a token"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

consejos = [
    " Apaga las luces cuando no las estés usando para ahorrar energia.",
    " Cierra el chorro (grifo)mientras te cepillas los dientes para ahorrar agua.",
    " Separa los residuos reciclables de la basura común.",
    " Planta árboles y cuida las áreas verdes de tu comunidad.",
    " Siempre que puedas, camina o utiliza bicicleta en lugar de usar carros o coches por el petroleo.",
    " Utiliza bolsas reutilizables para reducir el consumo de plástico.",
    " Desconecta los aparatos electrónicos cuando no los estés utilizando.",
    " Evita los productos de plástico de un solo uso.",
    " Trata de no desperdiciar comida; aprovecha las sobras cuando sea posible.",
    " Recuerda que pequeñas acciones diarias pueden ayudar a cuidar nuestro planeta.",
    " Intenta no talar arboles cerca de tu zona o comunidad.",
    " Trata de no comprar cosas de un solo uso de plastico e intenta comprar de vidrio",
    " Recuerda que es importante proteger nuestro planeta",
    " Cuando puedas, intenta reciclar los contenedores de plastico o vidrio.",
    " Intenta no gastar mucha energia electrica",

    
]

@client.event
async def on_ready():
    print(f" Bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "$consejo":
        consejo = random.choice(consejos)
        await message.channel.send(consejo)

client.run(TOKEN)
