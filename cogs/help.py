from simple import ResOCRToJson as res
import discord
from discord.ext import commands
from paddleocr import PaddleOCR, draw_ocr



class General(commands.Cog, name ="General Commands"):
    def __init__(self,bot):
        self.bot = bot

    

    @commands.command(name="help") 
    async def ocr(self, message):
            
        #Embed formatting
        embed=discord.Embed()
        embed.colour = 0x725E7A
        embed.set_author(name="Little Princess")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/807044084119764995/918648000421703740/unknown.png')
        embed.add_field(name="Content:", value='a', inline=True)
        embed.set_footer(text="Made By: WATAME")
        await message.channel.send(embed=embed)

def setup(bot):
	bot.add_cog(General(bot))