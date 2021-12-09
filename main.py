import os
from discord.ext import commands

bot = commands.Bot(
	command_prefix="LP.",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 650331064304271370  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
	'cogs.commandmain','cogs.raidupdate'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

token = os.environ.get('TOKEN') 
bot.run(token)  # Starts the bot