from discord import client
from simple import ResOCRToJson as res
import discord
from discord.ext import commands
import json
from paddleocr import PaddleOCR, draw_ocr

def OCRImage(imageLink,ServerID):
        ocr = PaddleOCR(use_angle_cls=True, lang="en", ocr_version = 'PP-OCR') #define ocr
        text = ocr.ocr(imageLink,cls=True) #buat download attachment ke tmp.jpg
        #result = ocr.ocr("tmp.jpg", cls=True) #OCR tmp.jpg
        res(ServerID)

        return "Done"

def previewEmbed():
    return None


class OCRcommands(commands.Cog, name ="OCRs Commands"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="preview", aliases =['hi'])
    async def preview(self, ctx):
        with open("DB/raid.json","r") as f:
            Data = json.load(f)
        if str(ctx.guild.id) not in Data:
            embeds=discord.Embed()
            embeds.colour = 0x725E7A
            embeds.set_author(name="Sorry, I couldn't find any server records from this server")
            embeds.add_field(name="Status : ", value='Error', inline=True)
            await ctx.channel.send(embed=embeds)
        else:
            Data = Data[str(ctx.guild.id)]
            for i in Data:

                embeds=discord.Embed()
                embeds.colour = 0x725E7A
                embeds.set_author(name=f"{i}")
                embeds.add_field(name="Raid Damage : ", value=Data[i][0], inline=True)
                await ctx.channel.send(embed=embeds)
                await ctx.author.send(embed=embeds)

    
    @commands.command(name="update", aliases=['upd']) 
    async def ocr(self, message):
        if len(message.message.attachments)>0:
            embeds=discord.Embed()
            embeds.colour = 0x725E7A
            embeds.set_author(name="Member's Raid Damage Update")
            embeds.add_field(name="Status : ", value='Working on it...', inline=True)
            await message.channel.send(embed=embeds)
            link = message.message.attachments[0].url #ubah attachment ke link
            content = OCRImage(link,message.guild.id) #nyalain function OCR
            #if content is not empty send embed
            if content:
                
                #Embed formatting
                embed=discord.Embed()
                embed.colour = 0x725E7A
                embed.set_author(name="Member's Raid Damage Update")
                embed.add_field(name="Status : ", value='Done', inline=True)
                embed.add_field(name="Preview : ", value='LP.Preview', inline=True)
                embed.set_footer(text="Updated By : Your Beloved Little Princess")
                await message.channel.send(embed=embed)
        else:
            embeds=discord.Embed()
            embeds.colour = 0x725E7A
            embeds.set_author(name="Member's Raid Damage Update")
            embeds.add_field(name="Status : ", value='Error!!', inline=True)
            embeds.set_footer(text="Tips : Please give Little Princess a valid Picture")
            await message.channel.send(embed=embeds)


def setup(bot):
	bot.add_cog(OCRcommands(bot))