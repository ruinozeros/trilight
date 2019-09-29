#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import numpy as np
from PIL import Image, ImageDraw
from scipy import signal


def main():
    laplacian_edge_detection("path")



def density(r,g,b):
    return 0.2126 * r + 0.7152 * g + 0.0722 * b




def laplacian_edge_detection(path):
    
    img = Image.open('/home/ru1/Desktop/DSC_0062_3.jpg')
    
    rgp_values = img.load()
    
    width = img.size[0]
    height = img.size[1]
    
    rgb_dens = np.zeros((height, width, 3), dtype=np.uint8)
    dens = np.zeros((height, width), dtype=np.uint8)
    
    print(img.size)
    
    for x in range(width):
        for y in range(height):
            r = rgp_values[x,y][0]
            g = rgp_values[x,y][1]
            b = rgp_values[x,y][2]
            d = density(r,g,b)
            rgb_dens[y,x] = [d, d, d]
            dens[y,x] = density(r,g,b)
            
    
    
    img_out = Image.fromarray(rgb_dens, 'RGB')
    
    draw = ImageDraw.Draw(img_out)
    
    #img_out.show()
    
    
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])
        
        
#    kernel = np.array([[-1, -1, -1, -1, -1],
#                       [-1,  1, -1, -1, -1],
#                       [-1, -1, 24, -1, -1],
#                       [-1, -1, -1, -1, -1],
#                       [-1, -1, -1, -1, -1]])
#        
        
    res = signal.convolve2d(dens, kernel)
    
    res_img = np.zeros((height, width, 3), dtype=np.uint8)
    
    for x in range(width):
        for y in range(height):
            m = res[y,x]
            res_img[y,x] =[m,m,m]
    
    
    res_out = Image.fromarray(res_img, 'RGB')
    res_out.show()
    #img_out.save("/home/ru1/Desktop/rui-grey.png")
    
    
if __name__ == "__main__":
    main()