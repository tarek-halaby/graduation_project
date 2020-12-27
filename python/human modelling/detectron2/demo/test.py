import cv2
import torch
import numpy as np
import gc
from flask import jsonify

from detectron2.detectron2.config import get_cfg
from detectron2.detectron2.data.detection_utils import read_image
from detectron2.detectron2.engine.defaults import DefaultPredictor


def detect_human(image_path):
    confidence_threshold = 0.7
    config_file = 'detectron2/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml'
    opts = ['MODEL.WEIGHTS',
            'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl',
            'MODEL.DEVICE', 'cpu']

    cfg = get_cfg()
    cfg.merge_from_file(config_file)
    cfg.merge_from_list(opts)
    cfg.MODEL.RETINANET.SCORE_THRESH_TEST = confidence_threshold
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = confidence_threshold
    cfg.MODEL.PANOPTIC_FPN.COMBINE.INSTANCES_CONFIDENCE_THRESH = confidence_threshold
    cfg.freeze()

    img = read_image(image_path, format="BGR")
    image = cv2.imread(image_path)

    predictor = DefaultPredictor(cfg)
    predictions = predictor(img)
    # print(predictions)
    detecting=True
    # t=0
    # while (detecting):
    #     jsonify({'i' + t : t})
    #     t += 1
    i = 0
    for box in predictions["instances"].pred_boxes:
        if predictions["instances"].pred_classes[i] == 0:

            pred_mask = predictions["instances"].pred_masks[i]
            mask = np.zeros(image.shape, dtype=np.uint8)

            for i in range(image.shape[0]):
                for j in range(image.shape[1]):
                    if pred_mask[i][j]:
                        mask[i][j] = 255

            result = cv2.bitwise_and(image, mask)
            result[mask == 0] = 255
            # (startX, startY, endX, endY) = box
            # startX = startX.type(torch.int64)
            # startY = startY.type(torch.int64)
            # endY = endY.type(torch.int64)
            # endX = endX.type(torch.int64)
            # crop_img = result[startY:endY, startX:endX + 5]
            # cv2.imshow('image' + str(startX), crop_img)

        i = +1
    cv2.imwrite("detectron2/demo/img.jpg", result)
    del confidence_threshold
    del config_file
    del opts
    del cfg
    del img
    del image
    del predictor
    del predictions
    del pred_mask
    del mask
    gc.collect()

def detect_parts(image, image_path, part_name):
    confidence_threshold = 0.7
    config_file = '../configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml'
    opts = ['MODEL.WEIGHTS',
            'detectron2://COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x/137849621/model_final_a6e10b.pkl',
            'MODEL.DEVICE', 'cpu']
    cfg = get_cfg()
    cfg.merge_from_file(config_file)
    cfg.merge_from_list(opts)
    cfg.MODEL.RETINANET.SCORE_THRESH_TEST = confidence_threshold
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = confidence_threshold
    cfg.MODEL.PANOPTIC_FPN.COMBINE.INSTANCES_CONFIDENCE_THRESH = confidence_threshold
    cfg.freeze()

    img = read_image(image_path, format="BGR")
    # image = cv2.imread(image_path)

    predictor = DefaultPredictor(cfg)
    predictions = predictor(img)
    if part_name == 'leg':
        top_left = 11
        top_right = 12
        bottom = 15
    if part_name == 'chest':
        top_left = 5
        top_right = 6
        bottom = 11

    keypoints = predictions["instances"].pred_keypoints[0]
    for idx, keypoint in enumerate(keypoints):
        # draw keypoint
        x, y, prob = keypoint
        if prob > 0.05:
            if idx == top_right:
                startX = x
                startY = y
            if idx == bottom:
                endY = y
            if idx == top_left:
                endX = x

    startX = startX.type(torch.int64)
    startY = startY.type(torch.int64)
    endY = endY.type(torch.int64)
    endX = endX.type(torch.int64)

    # print(startX-20)
    # print(endX+20)
    # print(startY)
    # print(endY)
    # print(image.shape)

    crop_img = image[startY-10:endY, startX-20:endX+20]
    # cv2.imshow('imagex', crop_img)
    # cv2.waitKey(0)

    return crop_img

#
# image_path = 'detectron2/demo/l.jpg'
#
# # human_img = detect_human(image_path)
# print('DONE..')