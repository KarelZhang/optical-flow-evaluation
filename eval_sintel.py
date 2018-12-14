#! /usr/bin/python
# Author: Jiaao Zhang [DUT Media]
# Date: 13th Dec 2018

from lib import flowlib as fl
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import cv2
import os

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


pred_flow_txt = 'pred_sintel_final_flow_LDOF.txt'
gt_flow_txt = 'gt_sintel_flow.txt'

gt_number = count_text_lines(gt_flow_txt)
gt_paths = read_path(gt_flow_txt)

pred_number = count_text_lines(pred_flow_txt)
pred_paths = read_path(pred_flow_txt)

print(gt_number)
print(pred_number)

sum_AEE = []
count = 0
for i in range(gt_number):


    pred_flow = fl.read_flow(pred_paths[i])

    gt_flow = fl.read_flow(gt_paths[i])

    res = fl.evaluate_flow(gt_flow, pred_flow)

    # sum_AEE.append(res)
    # count += 1

    if res < 50:
        sum_AEE.append(res)
        count += 1

    print('running file, aee is {}'.format(res))

AEE = np.mean(sum_AEE)

print('the averge error is {}'.format(AEE))
print(count)





