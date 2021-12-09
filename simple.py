#Make Simple :3

from paddleocr import PaddleOCR, draw_ocr
import os
import json
from PIL import Image


ocr = PaddleOCR(use_angle_cls=True, lang="en")

def ResOCRToJson():
    user_raid={} #empty dictionary
    result = ocr.ocr("tmp.jpg", cls=True) #read tmp.jpg

    
    txts = [line[1][0] for line in result] #retrieving text in image

    curdex = 0
    for a in txts:
        
        approval = True
        
        if len(a) == 1: #ignore rank
            approval=False

        index = a.rfind("Lv.") * a.rfind("LV.") * a.rfind("lV.") * a.rfind("lv.") #ignore lvl
        if index < 0:
            a = a[0:abs(index):] + a[len(a) + 1::]
        
        index = a.rfind("/3") #ignore raid attemp
        if index > 0:approval = False
        if(approval): #if only damage and user
            curdex += 1
            if curdex%2 == 1:
                b=a
            else:
                a = a.replace(".","") #replace . to none cuz of 1.232.534 is illegal to tramform to int
                
                user_raid[b]=int(a) #updating dictionary
    sorteds = dict(sorted(user_raid.items(), key=lambda item: item[1], reverse=True)) #sort dictionary by dmg
    with open("DB/raid.json","w") as data_json: #update the json
        json.dump(sorteds,data_json)
