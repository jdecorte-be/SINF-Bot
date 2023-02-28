#yayy


import settings

import discord
from discord.ext import commands

from utils import log
from cmds.src.birthday import Birthday as Bd

intents = discord.Intents.all()

bot = commands.Bot(
	command_prefix=[settings.BOT_PREFIX, f"<@!{settings.BOT_ID}> "],
	case_insensitive=True,
	help_command=None,
	intents=intents,
	strip_after_prefix=True
)
bot.tree.synced : bool = False



@bot.event
async def on_ready():
	log("INFO", f"Logged in as {bot.user} (ID: {bot.user.id})")
	for ext in settings.extensions:
		await bot.load_extension(ext)
		log("INFO", f"{ext} loaded ")

	Bd._birthdays.start(bot)

	print("SINF illégal family bot online\n")


@bot.command()
async def ping(ctx:commands.Context):
	await ctx.send(f"🏓 **PONG!** je t'ai renvoyé la balle en `{round(bot.latency*1000)}`_ms_ !")



bot.run(settings.DISCORD_API_TOKEN)
