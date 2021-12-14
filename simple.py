#Make Simple :3
from paddleocr import PaddleOCR, draw_ocr
import os
import json
from PIL import Image
import sys

#--Optional Functions!!--#
def blockPrint(): #Disable LOG from my module
    sys.stdout = open(os.devnull, 'w')
def enablePrint(): #Enable LOG from my module
    sys.stdout = sys.__stdout__
blockPrint() #Used to block print from paddleocr start
#------------------------#

ocr = PaddleOCR(use_angle_cls=True, lang="en", ocr_version = 'PP-OCR')

def ResOCRToJson(Server):
    with open("DB/raid.json","r") as f:
        Data = json.load(f)

    Server = str(Server)
    
    result = ocr.ocr("tmp.jpg", cls=True) #read tmp.jpg
    
    #If New
    if Server not in Data:
        Data[Server] = {}
    ####

    user_raid = Data[Server]
    txts = [line[1][0] for line in result] #retrieving text in image

    curdex = 0
    for a in txts:
        
        approval = True
        
        if len(a) == 1: #ignore rank
            approval=False

        index = a.rfind("Lv.") * a.rfind("LV.") * a.rfind("lV.") * a.rfind("lv.") #ignore lvl
        if index < 0:
            a = a[0:abs(index):] + a[len(a) + 1::]
        
        index = a.rfind("/3")
        if index > 0:
            approval = False
            c=a.replace('/3',"")
        if(approval): #if only damage and user
            curdex += 1
            if curdex%2 == 1:
                b=a.replace(' ','') ; b = b.upper()
            else:
                a = a.replace(".","") #replace . to none cuz of 1.232.534 is illegal to tramform to int
                user_raid.update({f'{b}':(int(a),int(c))}) #updating dictionary [0] = raid dmg, [1] = raid attempt
    user_raid = dict(sorted(user_raid.items(), key=lambda item: item[1][0], reverse=True))
    Data[Server] = user_raid
    with open("DB/raid.json","w") as data_json: #update the json
        json.dump(Data,data_json)


