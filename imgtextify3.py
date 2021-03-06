import os, sys, math, functools
from PIL import Image, ImageStat

no_spaces = False
thresh = 150
thresh2 = 150
thresh3 = 150
# defaults
res = 20
darkchar = "*"
lightchar = "."
darkchar2 = "@"
lightchar2 = "-"
darkchar3 = "o"
lightchar3 = "_"

num_newlines = 1

def line_array(cur_img, cur_res, cur_thresh, cur_dark, cur_light, cur_nospaces, resize_dim):
    if(resize_dim[0] > 0 and resize_dim[1] > 0):
        cur_img = cur_img.resize(resize_dim)
    cur_w, cur_h = cur_img.size
    cur_resh = round((cur_h/cur_w)*cur_res)
    cur_step = round(cur_w/cur_res)
    ret_arr = []
    for j,y in  enumerate([h*cur_step for h in range(cur_resh)]):
        cur_str = ""
        if cur_nospaces == False:
            cur_str += " "
        for i,x in enumerate([w*cur_step for w in range(cur_res)]):
            w0 = cur_step
            h0 = cur_step
            lastcol = i == (cur_res - 1)
            if lastcol:
                w0 = (cur_w - x)
            if j == (cur_resh - 1):
                h0 = (cur_h - y)
            cur_box = (x, y, x+w0, y + h0)
            cur_sq = cur_img.crop(cur_box)
            cur_means = ImageStat.Stat(cur_sq).mean
            cur_mean = functools.reduce(lambda x,y: x+y, cur_means)/len(cur_means)
            #print(cur_means, cur_mean)
            if(cur_mean < cur_thresh):
                cur_str += cur_dark
            else:
                cur_str += cur_light
            if cur_nospaces == False:
                cur_str += " "
        ret_arr += [cur_str]
    return ret_arr

# line_arrs = array of line arrays
# line_nl = number of newlines in between joined lines in line_arrs
# group_nl = number of newlines in between groups of joined lines
def build_string(line_arrs, line_nl, group_nl):
    ret_str = ""
    line_join = "".join(["\n"]*max(line_nl,1))
    group_join = "".join(["\n"]*max(group_nl,1))
    if len(line_arrs) <= 1:
        ret_str = group_join.join(line_arrs[0])
    else:
        ret_str = group_join.join([line_join.join(i) for i in zip(*line_arrs)])
    return ret_str

if len(sys.argv) < 2:
    quit()
else:
    global cur_path, cur_path2
    for i, argc in enumerate(sys.argv):
        if i == 1:
            cur_path = argc
        elif i== 2:
            cur_path2 = argc
        elif i == 3:
            cur_path3 = argc
        elif i == 4:
            res = int(argc)
        elif i == 5:
            thresh = int(argc)
        elif i == 6:
            thresh2 = int(argc)
        elif i== 7:
            thresh3 = int(argc)
        elif i == 8:
            darkchar = argc.strip()
        elif i == 9:
            lightchar = argc.strip()
        elif i ==10:
            darkchar2 = argc.strip()
        elif i == 11:
            lightchar2 = argc.strip()
        elif i == 12:
            darkchar3 = argc.strip()
        elif i == 13:
            lightchar3 = argc.strip()
        elif i == 14:
            num_newlines = int(argc)
        elif i== 15:
            no_spaces = True
            
        

            
try:
    global im, cur_w, cur_h
    im = Image.open(cur_path)
    im2 = Image.open(cur_path2)
    im3 = Image.open(cur_path3)
    im_dims = im.size
    ret_arr = line_array(im, res, thresh, darkchar, lightchar, no_spaces, (0,0))
    ret_arr2 = line_array(im2, res, thresh2, darkchar2, lightchar2, no_spaces, im_dims)
    ret_arr3 = line_array(im3, res, thresh3, darkchar3, lightchar3, no_spaces, im_dims)
    ret_str = build_string([ret_arr, ret_arr2, ret_arr3], num_newlines,num_newlines)
    print(ret_str)
    
except:
    print("generation failed!")
    quit()


        
    


    

