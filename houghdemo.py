# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html

import cv2
import numpy as np

cimg = cv2.imread('TLF 2014-01-11 15.14.01.jpg',1)
#cv2.imshow('Read image',cimg)
#cv2.waitKey(0)
img = cv2.cvtColor(cimg, 7) # cv2.COLOR_RGB2GREY = 7L iflg Ipython, men den virker ikke her?
#cv2.imshow('Greyed',img)
#cv2.waitKey(0)
img = cv2.medianBlur(img,5)
#cv2.imshow('Blurred',img)
#cv2.waitKey(0)


circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,
                            param1=30,param2=25,minRadius=20,maxRadius=40)

#demo: circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                            param1=50,param2=30,minRadius=0,maxRadius=0)
                            
                            
circles = np.uint16(np.around(circles))
#print circles
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
cv2.namedWindow('detected circles', cv2.WINDOW_NORMAL)
cv2.imshow('detected circles',cimg)
cv2.imwrite('out.jpg', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
