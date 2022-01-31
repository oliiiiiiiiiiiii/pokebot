from os import getenv
from dotenv import load_dotenv
from bot import PokeBot

load_dotenv()

token = getenv("token")

bot = PokeBot()

if __name__ == "__main__":
    bot.run(token)
