import os

data_root = '/media/zhangjiaao/data/flow/kitti2015/training/flow_occ/'

list = os.listdir(data_root)

print(len(list))

for i in range(len(list)):
    sub_line = 'flow-' + str(i).zfill(6)+'_10.flo'
    right_line = str(i).zfill(6)+'_11.png'
    print('/media/zhangjiaao/data/flow/kitti2015/training/result_flow2.0/{}'.format(sub_line))
