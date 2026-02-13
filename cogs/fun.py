from discord.ext import commands
import discord
import requests
import json
from random import choice
from bs4 import BeautifulSoup

class Fun(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.randomAnswerBall = ['Духи говорят "Да".', 'Духи говорят "Нет"', 'Повтори.', 'Не уверен', 'Да', 'Конечно']
        self.weather_info = 'https://www.google.com/search?sxsrf=ALeKk02RS2OLulk15WTgcF8EPx2Kd7V18w%3A1599998140219&ei=vAheX7XmDM2nrgTEwLugDw&q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1CxIFixIGDOImgAcAJ4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwi1tKfGiebrAhXNk4sKHUTgDvQQ4dUDCAw&uact=5'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        self.dollar_rub = 'https://www.google.com/search?sxsrf=ALeKk01faovKHhed2JGtVzwzuHGLeOlNcQ%3A1598179078575&source=hp&ei=BkdCX5vDIMqTlwStjruADA&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=rehc&gs_lcp=CgZwc3ktYWIQARgAMgcIIxCxAhAnMggIABAKEAEQQzIICAAQChABEEMyBAgAEAoyBAgAEEMyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAo6BAgjECc6BQgAELEDOggILhCxAxCDAToHCAAQsQMQQzoECC4QQzoKCAAQChABEEMQKjoGCAAQChABOggILhAKEAEQQ1CeBFjmCWC7FmgAcAB4AIABmQGIAbQEkgEDMC40mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab'

    def check_weather(self):
        full_page = requests.get(self.weather_info, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')

        time = soup.findAll('div', {'id': 'wob_dts'})
        weather = soup.findAll('span', {'id': 'wob_dc'})
        temperature = soup.findAll('span', {'id': 'wob_tm'})
        answer = [time[0].text, weather[0].text, temperature[0].text]

        return answer


    @commands.command()
    async def fox(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xffa722, title = 'Random fox') 
        embed.set_image(url=json_data['link']) 
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        response = requests.get('https://some-random-api.ml/img/cat')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xc1c0bd, title = 'Random cat') 
        embed.set_image(url=json_data['link']) 
        await ctx.send(embed=embed)

    @commands.command()
    async def rPanda(self, ctx):
        response = requests.get('https://some-random-api.ml/img/red_panda')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff4400, title = 'Random red panda') 
        embed.set_image(url=json_data['link']) 
        await ctx.send(embed=embed)

    @commands.command()
    async def mBall(self, ctx, question):
        answer = choice(self.randomAnswerBall)
        image_url = 'https://i.gifer.com/XDZT.gif'

        emb = discord.Embed(title='Магический шар говорит...', colour=0xA21EC3)
        if question == 'Да' or question == 'да' or answer == 'Да':
            image_url = 'https://www.meme-arsenal.com/memes/de042c267bd29e1dbea8525bf88d4449.jpg'
            answer = 'Да'
        emb.set_image(url=image_url)
        emb.add_field(name='Твой вопрос: ', value=question)
        emb.add_field(name='Ответ шара: ', value=answer)

        await ctx.send(embed=emb)

    @commands.command()
    async def weather(self, ctx):
        answer = self.check_weather()
        emb = discord.Embed(title='Погода в Москве', colour=0x218dde)
        emb.add_field(name='Время:', value=answer[0])
        emb.add_field(name='Погода:', value=answer[1])
        emb.add_field(name='Темпиратура:', value=answer[2])

        await ctx.send(embed=emb)
    
    @commands.command()
    async def usdRub(self, ctx):
        await ctx.send(self.check_currency_dollars())
    
    @commands.command()
    async def vote(self, ctx, *, theme):
        emb = discord.Embed(title=theme)
        message = await ctx.send(embed=emb) # Возвращаем сообщение после отправки
        await message.add_reaction('✅')
        await message.add_reaction('❌')

async def setup(bot):
    await bot.add_cog(Fun(bot))
