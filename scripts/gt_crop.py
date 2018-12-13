import cv2

def read_gt_path(file_path):

    f = open(file_path, 'r')
    gt_path = f.readlines()
    print(len(gt_path))

    gt_paths = []
    for path in gt_path:
        gt_paths.append(path.replace('\n', ''))

    return gt_paths

def repalce_path(path):

    newpath = path.replace('flow_noc', 'flow_crop')

    return newpath


gt_txt= 'gt_kitti_2015_flow.txt'

# paths = read_gt_path(gt_txt)
#
# for i in range(len(paths)):
#
#     path = paths[i]
#
#     img = cv2.imread(path)
#
#     print('{} {}'.format(i+1, img.shape))

a = cv2.imread('/media/zhangjiaao/data/flow/kitti2015/training/image_2/000050_10.png')
print(a.shape)