#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:56:49 2018

@author: esar
"""

#import the necessary modules
import freenect
import cv2
import numpy as np
import time


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
cnt=[]
data=[]

t1 = time.time()
waktu =0

if __name__ == "__main__":
    while 1:
        t2=time.time()-t1
        t1 = time.time()
        waktu=waktu+t2
        #get a frame from RGB camera
        frame = get_video()
        #get a frame from depth sensor
        depth = get_depth()
        #display RGB image
        cv2.imshow('RGB image',frame)
        #display depth image
        #ROI chest breath
        z=(int(np.mean(depth[185:259,220:360])))
        #ROI diaphragm breath
        #z=int(np.mean(depth[250:320,209:380]))
        data.append(z)
        
        
        cnt.append(waktu)
        cv2.putText(depth,str(round(z,2)),(0,90), font, 3,(0,0,0),1,cv2.LINE_AA)
        cv2.putText(depth,str(round(waktu,2)),(240,90), font, 3,(0,0,255),1,cv2.LINE_AA)
        #display ROI chest breath
        cv2.rectangle(depth,(220,185),(360,259),(0,255,0),3)
        #display ROI diaphragm breath
        #cv2.rectangle(depth,(209,250),(380,320),(0,255,0),3)
        cv2.imshow('Depth image',depth)
 
        # quit program when 'esc' key is pressed
        # 5 mean 5 miliseconds per data taken
        k = cv2.waitKey(100) & 0xFF
        if k == 27:
            break
        elif waktu==120:
            break
cv2.imwrite('depth.jpg',depth)
with open('depth_take.txt','w') as f:
    for i in range(len(data)):
        f.write("{} {}\n".format(data[i], cnt[i]))
#print(z)
freenect.sync_stop()
cv2.destroyAllWindows()