import discord
import random
from discord.ext import commands
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

def get_duck_image_url():    
    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mostrar(ctx):
    """Lista los nombres de los archivos en la carpeta 'imagenes'."""
    images = os.listdir('images')
    if images:
        await ctx.send("Las imágenes disponibles son:\n" + "\n".join(images))
    else:
        await ctx.send("No hay imágenes disponibles en la carpeta 'imagenes'.")

@bot.command()
async def enviar(ctx, nombre_imagen: str):
    """Envía la imagen especificada por el usuario."""
    images = os.listdir('images')
    if nombre_imagen in images:
        with open(f'images/{nombre_imagen}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    else:
        await ctx.send(f"No se encontró la imagen '{nombre_imagen}'. Asegúrate de que el nombre sea correcto.")

@bot.command()
async def clear(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def curiosidad(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)
    #comentarios
 
    await ctx.send("¿Te gustaria saber quien fue aristoteles?")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content == "si":
            await ctx.send(""" 
            Aristóteles ​​​​ fue un filósofo, polímata y científico griego nacido en la ciudad de Estagira, al norte de la Antigua Grecia. Es considerado junto a Platón, el padre de la filosofía occidental.
            """)
 
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber sobre otro tema, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
 
    await ctx.send("Quieres mas informacion? 'si' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("""
            Fue discípulo de Platón y de otros pensadores, como Eudoxo de Cnido, durante los veinte años que estuvo en la Academia de Atenas.​ Poco después de la muerte de Platón, Aristóteles abandonó Atenas para ser el maestro de Alejandro Magno en el Reino de Macedonia durante casi cinco años.​ En la última etapa de su vida, fundó el Liceo en Atenas, donde enseñó hasta un año antes de su muerte.
            """) 
        else:
            await ctx.send("Está bien, si alguna vez necesitas hablar sobre otro tema, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Te gustaria que te envie una foto de aristoteles?")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response1.content == "si":
            image_path = 'images/Aristóteles.jpg'
 
        # Verificar si el archivo existe antes de enviarlo
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                picture = discord.File(f)
                await ctx.send("Aquí tienes una representacion artistica de aristoteles:", file=picture)
        else:
            await ctx.send("Lo siento, no pude encontrar la imagen. Verifica que la ruta sea correcta.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")

@bot.command()
async def sg(ctx):
    with open('images/meme4', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def rm(ctx):
    images = os.listdir('images')
    with open(f'images/{random.choice(images)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("algo")
