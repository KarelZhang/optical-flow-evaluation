#! /usr/bin/python
# Author: Jiaao Zhang [DUT Media]
# Date: 13th Dec 2018


from lib import flowlib as fl
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import cv2

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


gt_file_path= 'gt_kitti_2015_flow.txt'
pred_file_path = 'pred_kitti_flow_EPIC.txt'

num_sample = count_text_lines(gt_file_path)
gt_paths = read_path(gt_file_path)
pred_path = read_path(pred_file_path)

print(num_sample)

sum_AEE = []
count = 0

for i in range(200):

    gt_flow1 = fl.read_flow(gt_paths[i])

    pre_flow1 = fl.read_flow(pred_path[i])

    res = fl.evaluate_flow(gt_flow1, pre_flow1)

    if res < 50:
        sum_AEE.append(res)
        count +=1

    #sum_AEE.append(res)

    print('running {}/{} file, aee is {}'.format(i+1, num_sample, res))


AEE = np.mean(sum_AEE)

print('the averge error is {}'.format(AEE))
print(count)

