#Make Simple :3

from paddleocr import PaddleOCR, draw_ocr
import os
import json
from PIL import Image

f=open("DB/raid.json") ; Data = json.load(f)

ocr = PaddleOCR(use_angle_cls=True, lang="en")

def ResOCRToJson(Server):
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
                b=a
            else:
                a = a.replace(".","") #replace . to none cuz of 1.232.534 is illegal to tramform to int
                print(b,a)
                
                user_raid[b]=(int(a),int(c)) #updating dictionary [0] = raid dmg, [1] = raid attempt
    Data[Server] = user_raid
    with open("DB/raid.json","w") as data_json: #update the json
        json.dump(Data,data_json)
