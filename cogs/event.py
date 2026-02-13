import discord
from discord.ext import commands
from discord.ext.commands import Cog

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        activ = discord.Activity(type=discord.ActivityType.streaming, name='', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        await self.bot.change_presence(activity=activ, status=discord.Status.online)
        print('Бот запущен')

    @Cog.listener()
    async def on_connect(self):
        print('Бот подключён к серверу')

    @Cog.listener()
    async def on_disconnect(self):
        print('Бот отключён от сервера')

    @Cog.listener()
    async def on_guild_remove(self, guild):
        print('Бота выгнали из {}.'.format(guild))

    @Cog.listener()
    async def on_guild_join(self, guild):
        print('Новый пользователь присоединился')    

    @Cog.listener()
    async def on_member_ban(self, guild, user):
        print(f'{user.display_name} забанен на сервере')

    @Cog.listener()
    async def on_member_unban(self, guild, user):
        print(f'{user.username} разбанен на сервере')

async def setup(bot):
    await bot.add_cog(Event(bot))
