import discord
from discord.ext import commands


class PokeBot(commands.Bot):
    def __init__(self, command_prefix="p!!", help_command=None, **options):
        super().__init__(command_prefix, help_command, **options)

    async def on_ready(self):
        print("Ready")