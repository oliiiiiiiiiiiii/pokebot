import discord
from discord.ext import commands

__all__ = "Pokebot"


class PokeBot(commands.Bot):
    """Subclassed bot class to be used for the bot"""

    def __init__(
        self,
        command_prefix=commands.when_mentioned_or("p!!"),
        help_command=None,
        **options
    ):
        super().__init__(command_prefix, help_command, **options)
        self.debug_guilds = {886951457948061778}
        self.bot_owners = {761932885565374474}

    async def on_ready(self):
        print("Ready")
