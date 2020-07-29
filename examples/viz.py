"""Functions to visualize human poses"""
import numpy as np
import os
import cv2
import sys
sys.path.insert(1, '../pyKinectAzure/')
# from pyKinectAzure import pyKinectAzure, _k4a, _k4abt
from _k4abttypes import *

link_list = [	
    [K4ABT_JOINT_NOSE, K4ABT_JOINT_EYE_LEFT], [K4ABT_JOINT_EYE_LEFT, K4ABT_JOINT_EAR_LEFT], # left face
    [K4ABT_JOINT_SPINE_CHEST, K4ABT_JOINT_CLAVICLE_LEFT], [K4ABT_JOINT_CLAVICLE_LEFT, K4ABT_JOINT_SHOULDER_LEFT], [K4ABT_JOINT_SHOULDER_LEFT, K4ABT_JOINT_ELBOW_LEFT], [K4ABT_JOINT_ELBOW_LEFT, K4ABT_JOINT_WRIST_LEFT], [K4ABT_JOINT_WRIST_LEFT, K4ABT_JOINT_HAND_LEFT], [K4ABT_JOINT_WRIST_LEFT, K4ABT_JOINT_THUMB_LEFT], [K4ABT_JOINT_HAND_LEFT, K4ABT_JOINT_HANDTIP_LEFT],# left arm
    [K4ABT_JOINT_PELVIS, K4ABT_JOINT_HIP_LEFT], [K4ABT_JOINT_HIP_LEFT, K4ABT_JOINT_KNEE_LEFT], [K4ABT_JOINT_KNEE_LEFT, K4ABT_JOINT_ANKLE_LEFT], [K4ABT_JOINT_ANKLE_LEFT, K4ABT_JOINT_FOOT_LEFT],# left leg
    [K4ABT_JOINT_NOSE, K4ABT_JOINT_EYE_RIGHT], [K4ABT_JOINT_EYE_RIGHT, K4ABT_JOINT_EAR_RIGHT], # RIGHT face
    [K4ABT_JOINT_SPINE_CHEST, K4ABT_JOINT_CLAVICLE_RIGHT], [K4ABT_JOINT_CLAVICLE_RIGHT, K4ABT_JOINT_SHOULDER_RIGHT], [K4ABT_JOINT_SHOULDER_RIGHT, K4ABT_JOINT_ELBOW_RIGHT], [K4ABT_JOINT_ELBOW_RIGHT, K4ABT_JOINT_WRIST_RIGHT], [K4ABT_JOINT_WRIST_RIGHT, K4ABT_JOINT_HAND_RIGHT], [K4ABT_JOINT_WRIST_RIGHT, K4ABT_JOINT_THUMB_RIGHT], [K4ABT_JOINT_HAND_RIGHT, K4ABT_JOINT_HANDTIP_RIGHT],# RIGHT arm
    [K4ABT_JOINT_PELVIS, K4ABT_JOINT_HIP_RIGHT], [K4ABT_JOINT_HIP_RIGHT, K4ABT_JOINT_KNEE_RIGHT], [K4ABT_JOINT_KNEE_RIGHT, K4ABT_JOINT_ANKLE_RIGHT], [K4ABT_JOINT_ANKLE_RIGHT, K4ABT_JOINT_FOOT_RIGHT], # RIGHT leg
    [K4ABT_JOINT_PELVIS, K4ABT_JOINT_SPINE_NAVEL], [K4ABT_JOINT_SPINE_NAVEL, K4ABT_JOINT_SPINE_CHEST], [K4ABT_JOINT_SPINE_CHEST, K4ABT_JOINT_NECK], [K4ABT_JOINT_NECK, K4ABT_JOINT_HEAD], [K4ABT_JOINT_HEAD, K4ABT_JOINT_NOSE], # torso
]

def draw_pose_2d(color_im, joint_list, confidence_level=None, link_list=link_list, radius=5, color=(0, 255, 0), thickness=5):
    for i, joint in enumerate(joint_list):
        if confidence_level is not None and \
            confidence_level[i] <= K4ABT_JOINT_CONFIDENCE_LOW:
            continue
        center_coordinates = (int(joint.xy.x), int(joint.xy.y))
        color_im = cv2.circle(color_im, center_coordinates, radius, color, thickness)
    
    for link in link_list:
        if confidence_level is not None:
            if confidence_level[link[0]] <= K4ABT_JOINT_CONFIDENCE_LOW and \
                confidence_level[link[1]] <= K4ABT_JOINT_CONFIDENCE_LOW:
                continue
        start_point = (int(joint_list[link[0]].xy.x), int(joint_list[link[0]].xy.y))
        end_point = (int(joint_list[link[1]].xy.x), int(joint_list[link[1]].xy.y))
        color_im = cv2.line(color_im, start_point, end_point, color, thickness)
        
    return color_im
