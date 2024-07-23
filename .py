import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptik')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Merhaba benim adim {client.user}! ben bir botum!')
    if message.content.startswith("$merhaba bot"):
        await message.channel.send(f"Merhaba Admin!")
    if message.content.startswith("$sen kimsin?"):
        await message.channel.send(f"Merhaba ben {client.user}! Ben Zafer tarafindan yazilmiş bir discord botuyum")
    if message.content.startswith("$kirlilik fotosu"):
        with open("Kirlilik.jpeg","rb") as f:
            kirlilik = discord.File(f)
            await message.channel.send(file = kirlilik)
    if message.content.startswith("$Hangi element doğada ne kadar hizli çözünür?"):
        with open('kirlilik.txt', 'r', encoding="utf-8") as f:
            for line in f.readlines():
                await message.channel.send(line)
        
            

client.run("Your special token")
