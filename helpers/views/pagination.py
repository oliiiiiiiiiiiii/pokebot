import discord

class Pagination(discord.ui.View):
    def __init__(self, pages :list[discord.Embed]):
        super().__init__(timeout=60)
        self.current = 0
        self.pages = pages
        self.msg = None

    @discord.ui.button(emoji="⬅️", style=discord.ButtonStyle.blurple)
    async def back(self, button: discord.ui.Button, interaction: discord.Interaction):
        if not self.current == 0:
            self.current -= 1
        else:
            self.current = len(self.pages)-1
        await self.msg.edit(embed=self.pages[self.current])

    @discord.ui.button(emoji="➡️", style=discord.ButtonStyle.blurple)
    async def next(self, button: discord.ui.Button, interaction: discord.Interaction):
        if not self.current == len(self.pages)-1:
            self.current += 1
        else:
            self.current = 0
        await self.msg.edit(embed=self.pages[self.current])