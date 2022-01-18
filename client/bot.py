from twitchio.ext import commands
from tools import Config

class Bot(commands.Bot):

    def __init__(self):
        config = Config()
        self.config = config
        super().__init__(token=config.token, prefix='!', initial_channels=config.channels)


    async def event_ready(self):
        print(f'Logged in as {self.nick}')


    async def event_message(self, message):
        # Messages sent by the bot
        if message.echo:
            return

        # Handle and invoke commands
        await self.handle_commands(message)

    
    # Future commands will be listed in the commands.ini files instead of the client script
    # Command list
    @commands.command(aliases=['hi', 'hey'])
    async def hello(self, ctx: commands.Context):

        await ctx.send(f'Hello {ctx.author.name}!')


    @commands.command()
    async def dc(self, ctx: commands.command):

        await ctx.send('Bot is now offline!')
        self.close()
