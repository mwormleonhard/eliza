#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wellplateReader.py
#demo: circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                            param1=50,param2=30,minRadius=0,maxRadius=0)
# If well edges aren't colored p1=30, p2=25 are better.
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
import math

def doNothing():
    pass

def measureRGBmean(x, y, r, img):
    result=[0,0,0]
    k=0.0 #k must be float to get float result from division
    for i in xrange(x-r, x+r):
        for j in xrange(y-r, y+r):
            if math.sqrt( (i - x)**2 + (j - y)**2 ) < r:
                result+=img[j,i] #Y-coordinate is the first dimension of the array. 
                k+=1
    return result/k #Values reported: [B,G,R]
                            
imagefile='BlankFar.jpg'

def readImage(filename):
    cimg = cv2.imread(imagefile,cv2.CV_LOAD_IMAGE_COLOR)
    img = cv2.cvtColor(cimg, cv2.COLOR_BGR2GRAY) 
    img = cv2.medianBlur(img,5)
    return cimg, img
    
def showWindow(cimg, img):
    cv2.namedWindow('detected circles', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('param1', 'detected circles', 50, 100, doNothing) 
    cv2.createTrackbar('param2', 'detected circles', 30, 100, doNothing) 
    cv2.createTrackbar('minRadius', 'detected circles', 20, 500, doNothing) 
    cv2.createTrackbar('maxRadius', 'detected circles', 40, 500, doNothing)
    cv2.imshow('detected circles',cimg)
   
def updateWindow():
    cimg, img = readImage(imagefile) #Reread image file to clear overlays
    p1 = cv2.getTrackbarPos('param1', 'detected circles')
    p2 = cv2.getTrackbarPos('param2', 'detected circles')
    minR = cv2.getTrackbarPos('minRadius', 'detected circles')
    maxR = cv2.getTrackbarPos('maxRadius', 'detected circles')
    
    circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=minR, maxRadius=maxR)
    circles = np.uint16(np.around(circles[0,:])) #Remove extra dimension of array, round to integers and cast to uint16
    #print circles
    wellcol = circles[:,0].argsort() // 8 # column
    wellrow = circles[:,1].argsort() // 12 #row
    # Make every circle the same size, so area is constant. Maybe subtract 10%?
    circles[:,2] = np.around(np.mean(circles[:,2])*0.9) 
    #print circles[:,2]
   

    for (x,y,r) in circles:
         # draw the outer circle
         cv2.circle(cimg,(x,y),r,(0,255,0),2)
         # draw the center of the circle
         cv2.circle(cimg,(x,y),2,(0,0,255),3)
        
    cv2.imshow('detected circles',cimg)

def saveOutput():
    cimg, img = readImage(imagefile) #Reread image file to clear overlays
    p1 = cv2.getTrackbarPos('param1', 'detected circles')
    p2 = cv2.getTrackbarPos('param2', 'detected circles')
    minR = cv2.getTrackbarPos('minRadius', 'detected circles')
    maxR = cv2.getTrackbarPos('maxRadius', 'detected circles')
    
    circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=p1, param2=p2, minRadius=minR, maxRadius=maxR)
    circles = np.uint16(np.around(circles[0,:])) #Remove extra dimension of array, round to integers and cast to uint16
    #print circles
    wellcol = circles[:,0].argsort() // 8 # column
    wellrow = circles[:,1].argsort() // 12 #row
    # Make every circle the same size, so area is constant. Maybe subtract 10%?
    circles[:,2] = np.around(np.mean(circles[:,2])*0.9) 
    #print circles[:,2]
   

    for (x,y,r) in circles:
        print measureRGBmean(x,y,r,cimg) #Do this before drawing on the image!    


#main
cimg, img = readImage(imagefile)
showWindow(cimg, img)

while(True):
    k = cv2.waitKey(10) & 0xFF
    if k == ord('u'):
        updateWindow()
    elif  k == ord('x'):
        cv2.destroyAllWindows()
        exit(0)
    elif  k == ord('s'):
        saveOutput()


cv2.imwrite('out.jpg', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()



