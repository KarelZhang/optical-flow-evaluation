#! /usr/bin/python
# Author: Ruoteng Li
# Date: 6th Aug 2016
"""
Demo.py
This file demonstrates how to use kittitool module to read
 and visualize flow file saved in kitti format .png
"""
from lib import flowlib as fl

import cv2
import numpy as np

# read kitti format optical flow file (.png)
print ("Visualizing KITTI flow example ...")
flow_file_KITTI = './data/example/KITTI/flow-000000_10.flo'
flow_KITTI = fl.read_flow(flow_file_KITTI)

flow = cv2.imread(flow_file_KITTI)

#print(flow[:,:,2])

#
# invalid_idx = (flow[:, :, 0] == 0)
#
# flow[:, :, 0:2] = (flow[:, :, 0:2] - 2 ** 15) / 64.0
# flow[invalid_idx, 2] = 0
# flow[invalid_idx, 1] = 0
#
# img = np.zeros((256, 512, 2))
#
# img[:,:,0]=flow[:,:,2]
# img[:,:,1]=flow[:,:,1]
#
# print(flow.shape)
#
# #fl.visualize_flow(img)
fl.visualize_flow(flow_KITTI)

# read Middlebury format optical flow file (.flo)
#print ("Visualizing Middlebury flow example ...")
# flow_file_Middlebury = 'data/example/Middlebury/flow_gt.flo'
# flow_Middlebury = fl.read_flow(flow_file_Middlebury)
# fl.visualize_flow(flow_Middlebury)
