from discord import client
from simple import ResOCRToJson as res
import discord
from discord.ext import commands
import json
from paddleocr import PaddleOCR, draw_ocr
import random


is_access = [822629972975812639,650331064304271370,768725675850072084]

def verify(ctx):
    return ctx.message.author.id in is_access


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
    @commands.check(verify)
    async def preview(self, ctx):
        with open("DB/raid.json","r") as f:
            Data = json.load(f)
        with open("DB/avatar.json","r") as ava:
            Avatar = json.load(ava)
            
        if str(ctx.guild.id) not in Data:
            embeds=discord.Embed()
            embeds.colour = 0x725E7A
            embeds.set_author(name="Sorry, I couldn't find any server records from this server")
            embeds.add_field(name="Status : ", value='Error', inline=True)
            await ctx.channel.send(embed=embeds)
        else:
            Data,rank = Data[str(ctx.guild.id)],0
            for i in Data:
                names,avatar = random.choice(list(Avatar.items()))
                rank+=1
                embeds=discord.Embed()
                embeds.colour = 0xe69fd2
                embeds.set_author(name=f"{i}")
                embeds.set_thumbnail(url=avatar)
                embeds.add_field(name=f"Raid Damage : {'{:,}'.format(Data[i][0])}\nEntry : {Data[i][1]}/3",value='--------------------------', inline=True)
                embeds.set_footer(text=f"Rank : {rank}/{len(Data)}")
                await ctx.channel.send(embed=embeds)

    
    @commands.command(name="update", aliases=['upd']) 
    @commands.check(verify)
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