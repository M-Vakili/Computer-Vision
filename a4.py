# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:16:31 2020

@author: Mr.Vakili
"""

import cv2
import numpy as np


##########################################  LoG ##############################
#pic=cv2.imread('2.jpg')
#pic_gray=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
#pic_blur=cv2.GaussianBlur(pic_gray,(5,5),0)
#edge_LoG_64F = cv2.Laplacian(pic_blur,cv2.CV_64F)
#edge_LoG_8U = cv2.Laplacian(pic_blur,cv2.CV_8U)
#_,edge_LoG_8U=cv2.threshold(edge_LoG_8U,5,255,cv2.THRESH_BINARY)
#
######################################## Sobel ################################
#edge_x=cv2.Sobel(pic_blur,cv2.CV_64F,1,0,ksize=5)
#edge_y=cv2.Sobel(pic_blur,cv2.CV_64F,0,1,ksize=5)
#edge_sobel_8U=cv2.Sobel(pic_blur,cv2.CV_8U,1,1,ksize=5)
##_,edge_sobel_8U=cv2.threshold(edge_sobel_8U,40,255,cv2.THRESH_BINARY)
#edge_sobel_64F=cv2.Sobel(pic_blur,cv2.CV_64F,1,1,ksize=5)
###################################### Canny ##################################
#edge_canny = cv2.Canny(pic_gray,100,200)
#
#
#
#cv2.imshow('LoG_64F',edge_LoG_64F)
#cv2.imshow('LoG_8U',edge_LoG_8U)
#cv2.imshow('SobelX',edge_x)
#cv2.imshow('SobelY',edge_y)
#cv2.imshow('Sobel_64F',edge_sobel_64F)
#cv2.imshow('Sobel_8U',edge_sobel_8U)
#cv2.imshow('Canny',edge_canny)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#######################################################################################################
#######################################################################################################
#######################################################################################################

##########################################  LoG ##############################
pic=cv2.imread('1.jpg')
pic=cv2.resize(pic,(300,600))
pic_gray=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
pic_blur=cv2.GaussianBlur(pic_gray,(3,3),0)
edge_LoG_64F = cv2.Laplacian(pic_blur,cv2.CV_64F)
edge_LoG_8U = cv2.Laplacian(pic_blur,cv2.CV_8U)
_,edge_LoG_8U=cv2.threshold(edge_LoG_8U,5,255,cv2.THRESH_BINARY)

####################################### Sobel ################################
edge_x=cv2.Sobel(pic_blur,cv2.CV_64F,1,0,ksize=5)
edge_y=cv2.Sobel(pic_blur,cv2.CV_64F,0,1,ksize=5)
edge_sobel_8U=cv2.Sobel(pic_blur,cv2.CV_8U,1,1,ksize=5)
#_,edge_sobel_8U=cv2.threshold(edge_sobel_8U,40,255,cv2.THRESH_BINARY)
edge_sobel_64F=cv2.Sobel(pic_blur,cv2.CV_64F,1,1,ksize=5)
##################################### Canny ##################################
edge_canny = cv2.Canny(pic_gray,100,200)




cv2.imshow('LoG_64F',edge_LoG_64F)
cv2.imshow('LoG_8U',edge_LoG_8U)
cv2.imshow('SobelX',edge_x)
cv2.imshow('SobelY',edge_y)
cv2.imshow('Sobel_64F',edge_sobel_64F)
cv2.imshow('Sobel_8U',edge_sobel_8U)
cv2.imshow('Canny',edge_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()