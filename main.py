import os
from discord.ext import commands
import logging
from simple import enablePrint as allow, blockPrint as disable
import json

#----------Starter----------#
logging.getLogger("asyncio").setLevel(logging.ERROR) #Used to block log from asyncio
logging.getLogger("discord").setLevel(logging.ERROR) #Used to block log from discord
#---------------------------#

#--------Define Bot--------#
bot = commands.Bot(
	command_prefix="LP.",  # Change to desired prefix
	case_insensitive=True, # Commands aren't case-sensitive
	help_command = None # Disable default help command  
)
bot.author_id = 650331064304271370  # Change to your discord id!!!
#--------------------------#

#-------When Bot Ready-------#
@bot.event 
async def on_ready():  # When the bot is ready
    allow();os.system('CLS');print('Welcome Back Guardian')
    print(bot.user)  # Prints the bot's username and identifier

#----------------------------#

#---Loads cogs extension---#
extensions = [
	'cogs.raidupdate','cogs.help'  # Same name as it would be if you were importing it
]
#--------------------------#

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loads every extension.

token = os.environ.get('TOKEN') 
bot.run(token)  # Starts the bot
