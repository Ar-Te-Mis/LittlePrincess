from simple import ResOCRToJson as res
import discord
from discord.ext import commands
from paddleocr import PaddleOCR, draw_ocr


def OCRImage(imageLink):
        ocr = PaddleOCR(use_angle_cls=True, lang="en") #define ocr
        text = ocr.ocr(imageLink,cls=True) #buat download attachment ke tmp.jpg
        result = ocr.ocr("tmp.jpg", cls=True) #OCR tmp.jpg
        res()

        return "Done"


class OCRcommands(commands.Cog, name ="OCRs Commands"):
    def __init__(self,bot):
        self.bot = bot

    

    @commands.command(name="ocr", aliases=['oc']) 
    async def ocr(self, message):
        print("working on it")
        link = message.message.attachments[0].url #ubah attachment ke link
        content = OCRImage(link) #nyalain function OCR
        #if content is not empty send embed
        if content:
            
            #Embed formatting
            embed=discord.Embed()
            embed.colour = 0x725E7A
            embed.set_author(name="Discord OCR")
            embed.add_field(name="Content:", value=content, inline=True)
            embed.set_footer(text="Made By: Ar-Te-Mis")
            await message.channel.send(embed=embed)

def setup(bot):
	bot.add_cog(OCRcommands(bot))