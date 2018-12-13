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


pred_flow_dir = '/media/zhangjiaao/data/flow/deepflow/middleburry/'
gt_flow_txt = 'gt_midburry_flow.txt'

gt_number = count_text_lines(gt_flow_txt)
gt_paths = read_path(gt_flow_txt)

flow_list = os.listdir(pred_flow_dir)

print(gt_number)

pred_flow_names = []
for var in flow_list:

    name = var.split('_')[1]

    name = name.split('.')[0]

    pred_flow_names.append(name)

sum_AEE = []
count = 0
for pred_name in pred_flow_names:

    for gt_path in gt_paths:

        if (pred_name in gt_path) and (pred_name != 'Venus'):

            count += 1
            print(pred_name)

            pred_flow = fl.read_flow(pred_flow_dir + '_' + pred_name + '.flo')
            gt_flow = fl.read_flow(gt_path)

            fl.visualize_flow(pred_flow)
            fl.visualize_flow(gt_flow)

            res = fl.evaluate_flow(gt_flow, pred_flow)
            sum_AEE.append(res)

            print('running file, aee is {}'.format(res))

AEE = np.mean(sum_AEE)

print('the averge error is {}'.format(AEE))
print(count)





