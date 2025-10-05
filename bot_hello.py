import os, asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands
import pyhook
INTERVAL = 10

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("DISCORD_TOKEN missing")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

async def countdown_edit(channel, seconds):
    msg = await channel.send(f"Countdown: {seconds}s")
    for rem in range(seconds - 1, -1, -1):
        await asyncio.sleep(1)
        await msg.edit(content=f"Countdown: {rem}s")
    await msg.edit(content="Done!")
    asyncio.create_task(pull(channel))

async def pull(channel):
    await channel.send("PULLING THE KEYSTOKES")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.lower().strip() == "start":
        asyncio.create_task(countdown_edit(message.channel, INTERVAL))
    if message.content.lower().strip() == "end":
       await bot.close()    
    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(TOKEN)
