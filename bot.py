import discord
from discord.ext import commands

__all__ = "Pokebot"


class PokeBot(commands.Bot):
    """Subclassed bot class to be used for the bot"""

    def __init__(self, command_prefix="p!!", help_command=None, **options):
        super().__init__(command_prefix, help_command, **options)
        self.debug_guilds = {...}
        self.bot_owners = {...}

    async def on_ready(self):
        print("Ready")
