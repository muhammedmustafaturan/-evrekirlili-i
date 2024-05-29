import discord
from discord.ext import commands
import os
import random
import requests


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send(f'Merhaba {client.user}! ben bir botum!')
    elif  message.content.startswith('Çevre kirliliğini önlemek için ne yapmalıyım?'):
        await message.channel.send("Çöplerimizi kesinlikle doğaya atmamalı, kağıt,cam,plastik gibi atıkların geri dönüşümünü sağlamalıyız. Ev ve fabrika bacalarından çıkan gazlar hava kirliliğine yol açtığı için filtre kullanmalıyız. Yeşil alanları arttırarak orman tahribatını önlemeliyiz. Ozon tabakasına zararı olan herhangi bir üründen kaçınmalıyız.")
    elif message.content.startswith('Atık yönetiminin ilk adımı nedir?'):
        await message.channel.send(' İlk aşama atığın oluşmasının önlenmesi, eğer bu sağlanamıyorsa atığın minimizasyonu, diğer bir deyişle atığın en aza indirilmesi amaçlanır. Daha sonra atığın Yeniden kullanımı eğer bu da mümkün olmuyorsa önce geri dönüşüm ve sonra enerji geri kazanımı amaçlanır.')
    elif message.content.startswith("Çevre kirliliği nedir?"):
        await message.channel.send("Çevre kirliliği doğanın, doğal kaynakların ve yaşanılan çevrenin aşırı ölçüde ve yanlış kullanılması nedeniyle doğal dengenin bozulması durumudur.")

    
    #RESİM
    elif message.content.startswith('Çevre kirliliğini önlemezsek ne olur?'):
        dosya = os.listdir("çevre kirliliği resimleri")
        resim = random.choice(dosya)
        with open(f'çevre kirliliği resimleri/{resim}', "rb") as f:
            resim = discord.File(f)
            await message.channel.send(file = resim)

            
client.run("TOKEN")
