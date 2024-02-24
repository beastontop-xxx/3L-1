import discord
import itertools
import os

# Function to generate all possible three-letter combinations
def generate_combinations():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return [''.join(combo) for combo in itertools.product(letters, repeat=3)]

# Function to check if a username is available on Discord
async def is_available(username):
    try:
        await client.fetch_user(username)
        return False
    except discord.NotFound:
        return True

# Main function to find available usernames
async def find_available_usernames():
    available_usernames = []
    combinations = generate_combinations()
    for username in combinations:
        if await is_available(username):
            available_usernames.append(username)
    return available_usernames

# Discord bot setup
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Example usage
@client.event
async def on_message(message):
    if message.content.startswith('!find_usernames'):
        available_usernames = await find_available_usernames()
        await message.channel.send(f'Available 3-letter usernames: {", ".join(available_usernames)}')

# Run the bot with the token from environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN)
