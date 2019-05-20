import os, sys, math, functools
from PIL import Image, ImageStat

no_spaces = False
thresh = 150
# defaults
cur_res = 20
darkchar = "*"
lightchar = "."


ret_str = " "

if len(sys.argv) < 2:
    quit()
else:
    global cur_path
    for i, argc in enumerate(sys.argv):
        if i == 1:
            cur_path = argc
        elif i == 2:
            cur_res = int(argc)
        elif i == 3:
            thresh = int(argc)
        elif i == 4:
            darkchar = argc.strip()
        elif i ==5:
            lightchar = argc.strip()
        elif i == 6:
            no_spaces = True
            
        

            
try:
    global im, cur_w, cur_h
    im = Image.open(cur_path)
    cur_w, cur_h = im.size
except:
    quit()

if no_spaces:
    ret_str = ""
    
cur_resh = math.floor((cur_h/cur_w)*cur_res)
cur_step = math.floor(cur_w/cur_res)


for j,y in  enumerate([h*cur_step for h in range(cur_resh)]):
    for i,x in enumerate([w*cur_step for w in range(cur_res)]):
        w0 = cur_step
        h0 = cur_step
        lastcol = i == (cur_res - 1)
        if lastcol:
            w0 = (cur_w - x)
        if j == (cur_resh - 1):
            h0 = (cur_h - y)
        cur_box = (x, y, x+w0, y + h0)
        cur_sq = im.crop(cur_box)
        cur_means = ImageStat.Stat(cur_sq).mean
        cur_mean = functools.reduce(lambda x,y: x+y, cur_means)/len(cur_means)
        #print(cur_means, cur_mean)
        if(cur_mean < thresh):
            ret_str += darkchar
        else:
            ret_str += lightchar
        if lastcol:
            ret_str += "\n"
        if no_spaces == False:
            ret_str += " "

print(ret_str)

        
    


    

