# -*- coding:utf-8 -*-
# Image模块开篇例子
from PIL import Image,ImageDraw,ImageFont
import random

def color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

text = input("shu ru:")
im = Image.open(r'C:\\Users\\Administrator\\Downloads\343823636.jpg') # 读取图片
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 30)#设置字体和字符显示大小
width,height = im.size
draw = ImageDraw.Draw(im)
start = width - 30*len(text)-10*(len(text)-1)
print(width,height,start)
for i in range(len(text)):
    draw.text((30*i+start//2,50),text[i],font=font,fill=(255,255,255))#中文不能输出跟选择的字体有关，比如Arial.ttf无法显示中文
    offsetx, offsety = font.getoffset(text[i]) # 获得文字的offset位置
    text_width, text_height = font.getsize(text[i])
    print(text[i],offsetx,offsety,text_width,text_height)
im.save('code.jpg', 'jpeg')

#合成图片
def paste_image(image_list):
    total_heigth = 0
    total_width = 0
    if (len(image_list) < 1):
        return "no pic or only one pic"
    else:
        for image in image_list:
            w,h = image.size
            total_heigth += h
            total_width = w
        newimage = Image.new("RGB", (total_width,total_heigth), (255, 255, 255))
        left = 0
        right = h
        for image in image_list:
            temp = image.resize((w, h), Image.ANTIALIAS)#resize也是图片的自带属性，可赋值给变量，type是image
            #image.thumbnail((w, h), Image.ANTIALIAS)#thumbnail是图片自带的属性，不可以赋值给对应，返回的type是nonetype，此时的图片已经被按比例缩放过，直接show（）即可显示
            newimage.paste(temp,(0,left,w,right))#竖着拼接图片的方式，如果横着拼接图片需变换为（left，0，right，h），left += w，right += w
            left += h
            right += h
        newimage.save('merge.jpg', 'jpeg')

im1 = Image.open(r'C:\\Users\\Administrator\\Downloads\1215632720.jpg')
im1_width,im1_height = im1.size
print(len(list(im1.getdata())))
image_list = []
image_list.append(im1)
image_list.append(im)
paste_image(image_list)
