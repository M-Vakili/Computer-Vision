# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:00:56 2020

@author: Mr.Vakili
"""

import cv2
import numpy as np

pic=cv2.imread('3.jpg',cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 220;
params.maxThreshold = 255;

# Filter by Inertia
params.filterByInertia = 1
params.minInertiaRatio = 0.01

# Filter by Convexity
params.filterByConvexity = 1
params.minConvexity = 0.7

det=cv2.SimpleBlobDetector_create(params)
points=det.detect(pic)
draw_points=cv2.drawKeypoints(pic,points,np.array([]),(0,0,255))
cv2.imshow("POINTS",draw_points)
cv2.waitKey(0)
cv2.destroyAllWindows()

##################################################################################

pic=cv2.imread('3.jpg',cv2.IMREAD_GRAYSCALE)
_,threshold=cv2.threshold(pic,220,255,cv2.THRESH_BINARY)
contours,_ =cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(pic,[cnt],0,(60),3)
cv2.imshow("POINTS",pic)
cv2.waitKey(0)
cv2.destroyAllWindows()