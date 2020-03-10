# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 11:59:08 2020

@author: Mr.Vakili
"""

import cv2
import numpy as np

#############################################LPF in RGB image##
pic=cv2.imread('2.jpg')
pic=cv2.resize(pic,(400,300))

#kernel for mean filter
kernel = (1/9)*np.ones((3,3), np.uint8)

#define for zero padding
pic_pad = np.zeros((302,402,3), np.uint8)

#zero padded pic
pic_pad[1:301,1:401]=pic

for x in range(1,301):
    for y in range(1,401):
        #picks a 3*3 section
        section=pic_pad[x-1:x+2,y-1:y+2]
        
        #element-wise multiplication
        q=kernel*section
        
        #sum of elements
        pic_pad[x,y]=q[0,0]+q[0,1]+q[0,2]+q[1,0]+q[1,1]+q[1,2]+q[2,0]+q[2,1]+q[2,2]

pic_LPF=pic_pad[1:301,1:401]


############################################LPF in gray scale##
pic_gray=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
kernel = (1/9)*np.ones((3,3), np.uint8)
pic_pad = np.zeros((302,402), np.uint8)
pic_pad[1:301,1:401]=pic_gray
for x in range(1,301):
    for y in range(1,401):
        section=pic_pad[x-1:x+2,y-1:y+2]
        q=kernel*section
        pic_pad[x,y]=q[0,0]+q[0,1]+q[0,2]+q[1,0]+q[1,1]+q[1,2]+q[2,0]+q[2,1]+q[2,2]
pic_lpf=pic_pad[1:301,1:401]

#######################################detect edge in y direction#
pic_pad = np.zeros((302,402), np.uint8)
pic_pad[1:301,1:401]=pic_lpf
kernel = np.array([[0,-1,1]])
for x in range(1,301):
    for y in range(1,401):
        section=pic_pad[x,y-1:y+2]
        q=kernel*section
        s=q[0,0]+q[0,1]+q[0,2]
        pic_pad[x,y]=abs(s)
pic_y=pic_pad[1:301,1:401]
#######################################detect edge in x direction#
pic_pad = np.zeros((302,402), np.uint8)
pic_pad[1:301,1:401]=pic_lpf
kernel = np.array([[0,-1,1]])
for x in range(1,301):
    for y in range(1,401):
        section=pic_pad[x-1:x+2,y]
        q=kernel*section
        s=q[0,0]+q[0,1]+q[0,2]
        pic_pad[x,y]=abs(s)
pic_x=pic_pad[1:301,1:401]
##################################################edge detection#
edge = np.zeros((300,400), np.uint8)
for x in range(0,300):
    for y in range(0,400):
        a=int((pic_x[x,y]**2 + pic_y[x,y]**2)**0.5)
        if a>255:
            edge[x,y]=255
        else:
            edge[x,y]=a
            
_,edge=cv2.threshold(edge,10,255,cv2.THRESH_BINARY)
_,pic_y=cv2.threshold(pic_y,10,255,cv2.THRESH_BINARY)
_,pic_x=cv2.threshold(pic_x,10,255,cv2.THRESH_BINARY)

cv2.imshow('INITIAL IMAGE',pic)
cv2.imshow('EDGE',edge)
cv2.imshow('INITIAL GRAY IMAGE',pic_gray)
cv2.imshow('LPF GRAY',pic_lpf)
cv2.imshow('Y EDGE',pic_y)
cv2.imshow('X EDGE',pic_x)
cv2.imshow('LPF RGB',pic_LPF)
while True:
    key=cv2.waitKey(0)
    if key==ord('e'):
        cv2.destroyAllWindows()
        break
    elif key==ord('s'):
        cv2.imwrite('X.jpg',pic_x)
        cv2.imwrite('Y.jpg',pic_y)
        cv2.destroyAllWindows()
        break
    else:
        pass