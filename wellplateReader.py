#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wellplateReader.py
#
#----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <mwormleonhard@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. 
# Martin Worm-leonhard
# ----------------------------------------------------------------------------

import cv2
import numpy as np

def updateTrackbars(dummyVal):
	cimg = cv2.imread('TLF 2014-01-11 15.07.37a.jpg',1)
	p1 = cv2.getTrackbarPos('param1', 'detected circles')
	p2 = cv2.getTrackbarPos('param2', 'detected circles')
	minR = cv2.getTrackbarPos('minRadius', 'detected circles')
	maxR = cv2.getTrackbarPos('maxRadius', 'detected circles') 
	circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=minR, maxRadius=maxR)
	circles = np.uint16(np.around(circles))
	#print circles
	for i in circles[0,:]:
		# draw the outer circle
		cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
		# draw the center of the circle
		cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
	cv2.imshow('detected circles',cimg)
                            

cimg = cv2.imread('TLF 2014-01-11 15.07.37a.jpg',1)

img = cv2.cvtColor(cimg, 7) # cv2.COLOR_RGB2GREY = 7L iflg Ipython, men den virker ikke her?
img = cv2.medianBlur(img,5)
cv2.namedWindow('detected circles', cv2.WINDOW_NORMAL)
cv2.createTrackbar('param1', 'detected circles', 30, 100, updateTrackbars) 
cv2.createTrackbar('param2', 'detected circles', 25, 100, updateTrackbars) 
cv2.createTrackbar('minRadius', 'detected circles', 20, 500, updateTrackbars) 
cv2.createTrackbar('maxRadius', 'detected circles', 40, 500, updateTrackbars) 
updateTrackbars(None)



#demo: circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                            param1=50,param2=30,minRadius=0,maxRadius=0)

while(True):
	cv2.waitKey(0)
	                            
                            

cv2.imwrite('out.jpg', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
