#Make Simple :3

from paddleocr import PaddleOCR, draw_ocr
import os
import json
from PIL import Image


ocr = PaddleOCR(use_angle_cls=True, lang="en")

def ResOCRToJson():
    user_raid={}
    result = ocr.ocr("tmp.jpg", cls=True)

    
    txts = [line[1][0] for line in result]

    curdex = 0
    for a in txts:
        
        approval = True
        index = a.rfind("Lv.")
        if a == "1":
            approval=False
        if index > 0:

            #a[index:len(a)] = ""
            a = a[0:index:] + a[len(a) + 1::]
        index = a.rfind("LV.")
        if a == "1":
            approval=False
        if index > 0:

            

            #a[index:len(a)] = ""
            a = a[0:index:] + a[len(a) + 1::]
        
        index = a.rfind("lv.")
        if a == "1":
            approval=False
        if index > 0:

            

            #a[index:len(a)] = ""
            a = a[0:index:] + a[len(a) + 1::]

        index = a.rfind("/3")
        if index > 0:approval = False
        if(approval):
            curdex += 1
            if curdex%2 == 1:
                b=a
            else:
                a = a.replace(".","")
                print(b,a)
                
                user_raid[b]=int(a)
    sorteds = dict(sorted(user_raid.items(), key=lambda item: item[1], reverse=True))
    for i in sorteds:
        print(i)
    with open("DB/raid.json","w") as data_json:
        json.dump(sorteds,data_json)
