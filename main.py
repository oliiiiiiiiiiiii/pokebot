from fileinput import filename
import os
from dotenv import load_dotenv
from bot import PokeBot

load_dotenv()

token = os.getenv("token")

bot = PokeBot()

if __name__ == "__main__":
    bot.run(token)
