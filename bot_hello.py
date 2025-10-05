import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True   # REQUIRED to read message text

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id: {bot.user.id})")

@bot.event
async def on_message(message):
    # ignore messages from bots (including itself)
    if message.author.bot:
        return

    # exact match, case-insensitive
    if message.content.lower().strip() == "hello":
        await message.channel.send("Hello world!")

    # allow commands to still work if you add them later
    await bot.process_commands(message)

if __name__ == "__main__":
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        raise SystemExit("Set DISCORD_TOKEN environment variable")
    bot.run(token)
