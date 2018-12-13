#! /usr/bin/python
# Author: Ruoteng Li
# Date: 6th Aug 2016
"""
Demo.py
This file demonstrates how to use kittitool module to read
 and visualize flow file saved in kitti format .png
"""
from lib import flowlib as fl
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import cv2
# read kitti format optical flow file (.png)
# print ("Visualizing KITTI flow example ...")
# flow_file_KITTI = 'data/example/KITTI/frame1.flo'
# flow_KITTI = fl.read_flow(flow_file_KITTI)
# fl.visualize_flow(flow_KITTI)

# read Middlebury format optical flow file (.flo)
#print ("Visualizing Middlebury flow example ...")
# flow_file_Middlebury = 'data/example/Middlebury/flow_gt.flo'
# flow_Middlebury = fl.read_flow(flow_file_Middlebury)
# fl.visualize_flow(flow_Middlebury)
def count_text_lines(file_path):
    f = open(file_path, 'r')
    lines = f.readlines()
    lines = lines[:-1]
    f.close()
    return len(lines)


def read_path(file_path):

    f = open(file_path, 'r')
    gt_path = f.readlines()
    print(len(gt_path))

    gt_paths = []
    for path in gt_path:
        gt_paths.append(path.replace('\n', ''))

    return gt_paths


print ("Evaluating KITTI flow example ...")
gt_file_path= 'gt_kitti_2015_flow.txt'
pred_file_path = 'pred_flow_flownet2.txt'

num_sample = count_text_lines(gt_file_path)
gt_paths = read_path(gt_file_path)
pred_path = read_path(pred_file_path)

print(num_sample)


sum_AEE = np.zeros(200)
count = 0

for i in range(num_sample):

    gt_flow1 = fl.read_flow(gt_paths[i])

    pre_flow1 = fl.read_flow(pred_path[i])

    res = fl.evaluate_flow(gt_flow1, pre_flow1)

    #if res < 30:

    sum_AEE[i] = res

    #else:

    #    count += 1



    print('running {}/{} file, aee is {}'.format(i+1, num_sample, res))


AEE = np.mean(sum_AEE)

print('the averge error is {}'.format(AEE))
print(count)

#sn.distplot(sum_AEE)

plt.plot(int(sum_AEE))