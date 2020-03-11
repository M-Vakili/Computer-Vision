# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:26:49 2020

@author: Mr.Vakili
"""

import numpy as np
import cv2

file=cv2.VideoCapture('hw.avi')

while True:
     #start getting frames
    _,frame = file.read()          
    
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_blur=cv2.GaussianBlur(frame_gray,(5,5),0)
    
    #canny
    edge_canny = cv2.Canny(frame_gray,50,200)
    
    #sobel
    #blurred
    edge_x_blur=cv2.Sobel(frame_blur,cv2.CV_64F,1,0,ksize=5)
    edge_y_blur=cv2.Sobel(frame_blur,cv2.CV_64F,0,1,ksize=5)
    edge_sobel_blur=cv2.Sobel(frame_blur,cv2.CV_8U,1,1,ksize=5)
    
    #sobel
    #org
    edge_x=cv2.Sobel(frame_gray,cv2.CV_64F,1,0,ksize=5)
    edge_y=cv2.Sobel(frame_gray,cv2.CV_64F,0,1,ksize=5)
    edge_sobel=cv2.Sobel(frame_gray,cv2.CV_8U,1,1,ksize=5)
    
    
    #prewitt
    #blur
    xkernel=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    ykernel=np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    xedge_prewitt_blur=cv2.filter2D(frame_blur,-1,xkernel)
    yedge_prewitt_blur=cv2.filter2D(frame_blur,-1,ykernel)
    
    #prewitt
    #org
    xedge_prewitt=cv2.filter2D(frame_gray,-1,xkernel)
    yedge_prewitt=cv2.filter2D(frame_blur,-1,ykernel)
    
    

    #show frames to produce video
    cv2.imshow("CANNY",edge_canny)
    cv2.imshow('Sobel_ORG',edge_sobel)
    cv2.imshow('Sobel_BLUR',edge_sobel_blur)
    cv2.imshow('PrewittX_BLUR',xedge_prewitt_blur)
    cv2.imshow('PrewittY_BLUR',yedge_prewitt_blur)
    cv2.imshow('PrewittX_ORG',xedge_prewitt)
    cv2.imshow('PrewittY_ORG',yedge_prewitt)
    key=cv2.waitKey(20)
    if key == ord('e'):
        break
    else:
        pass
    
cam.release()
cv2.destroyAllWindows()
