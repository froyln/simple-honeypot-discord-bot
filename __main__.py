import discord
import json
import os


class Bot(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")


try:
    with open("settings.json", "r") as f:
        settings = json.load(f)
except Exception:
    print("Error, no se encontro el archivo settings.json")
    os._exit(0)


honeypot_channel_id = settings["honeypot_channel_id"]
bot_token = settings["bot_token"]


intents = discord.Intents.default()
bot = Bot(command_prefix="!", intents=intents)


@bot.event
async def on_message(message):
    if message.channel.id == honeypot_channel_id:
        try:
            await message.guild.ban(message.author)
        except Exception:
            return None


bot.run(bot_token)

