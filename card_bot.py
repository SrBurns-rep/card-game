# Discord card bot
import os
import discord
from dotenv import load_dotenv

# Token cannot be published in repo, it's defined by a
# environment variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# Test event
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

# Rest of the code: TO-DO