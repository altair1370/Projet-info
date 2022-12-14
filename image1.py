# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:50:11 2022

@author: laure
"""

from PIL import Image
import numpy as np


mon_image = Image.open("Airfrance.jpg")
size = mon_image.size
#mon_image.show()

image2 = Image.new(mon_image.mode,size)
for i in range(size[0]):
    for j in range( size[1]):
        color=mon_image.getpixel((i,j))
        index=i+j*size[1]
        if (index % 3==0):
            image2.putpixel((size[0]-i-1,j),color)
            image2.putpixel((i,size[1]-j-1),color)

        else:
            image2.putpixel((i,j),color)
    
image2.show()
mon_image.close()