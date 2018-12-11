#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 07:34:20 2018

@author: esar
"""

import freenect
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array
 
#function to get depth image from kinect
def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array

data=[]
if __name__ == "__main__":
    while 1:
        #get a frame from RGB camera
        frame = get_video()
        #get a frame from depth sensor
        depth = get_depth()
        #z=depth[200:300,209:380]
        #display RGB image
        cv2.imshow('RGB image',frame)
        #display depth image
        z=(int(np.mean(depth[140:209,220:360])))
        cv2.putText(depth,str(round(z,2)),(0,90), font, 3,(0,0,0),1,cv2.LINE_AA)
        cv2.rectangle(depth,(220,140),(360,209),(0,255,0),3)
        cv2.imshow('Depth image',depth)
        # quit program when 'esc' key is pressed
        # 5 mean 5 miliseconds per data taken
        k = cv2.waitKey(100) & 0xFF
                
        if k == 115:
            if len(data)< 20:
                data.append(z)
            else :
                print("DONE")
        if k == 27:
            break
cv2.imwrite('depth.jpg',depth)
with open('data.txt','w') as f:
    for i in range(len(data)):
        f.write("{}\n".format(data[i]))
freenect.sync_stop()
cv2.destroyAllWindows()