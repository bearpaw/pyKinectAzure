# https://microsoft.github.io/Azure-Kinect-Body-Tracking/release/1.x.x/
import ctypes
from _k4atypes import *

# K4A_DECLARE_HANDLE(k4abt_tracker_t);
class _handle_k4abt_tracker_t(ctypes.Structure):
	 _fields_= [
		("_rsvd", ctypes.c_size_t),
	]
k4abt_tracker_t = ctypes.POINTER(_handle_k4abt_tracker_t)

# K4A_DECLARE_HANDLE(k4abt_frame_t);
class _handle_k4abt_frame_t(ctypes.Structure):
	 _fields_= [
		("_rsvd", ctypes.c_size_t),
	]
k4abt_frame_t = ctypes.POINTER(_handle_k4abt_frame_t)

#class k4abt_joint_id_t(CtypeIntEnum):
k4abt_joint_id_t = ctypes.c_int
K4ABT_JOINT_PELVIS = 0
K4ABT_JOINT_SPINE_NAVEL = 1
K4ABT_JOINT_SPINE_CHEST = 2
K4ABT_JOINT_NECK = 3
K4ABT_JOINT_CLAVICLE_LEFT = 4
K4ABT_JOINT_SHOULDER_LEFT = 5
K4ABT_JOINT_ELBOW_LEFT = 6
K4ABT_JOINT_WRIST_LEFT = 7
K4ABT_JOINT_HAND_LEFT = 8
K4ABT_JOINT_HANDTIP_LEFT = 9
K4ABT_JOINT_THUMB_LEFT = 10
K4ABT_JOINT_CLAVICLE_RIGHT = 11
K4ABT_JOINT_SHOULDER_RIGHT = 12
K4ABT_JOINT_ELBOW_RIGHT = 13
K4ABT_JOINT_WRIST_RIGHT = 14
K4ABT_JOINT_HAND_RIGHT = 15
K4ABT_JOINT_HANDTIP_RIGHT = 16 
K4ABT_JOINT_THUMB_RIGHT = 17
K4ABT_JOINT_HIP_LEFT = 18
K4ABT_JOINT_KNEE_LEFT = 19
K4ABT_JOINT_ANKLE_LEFT = 20
K4ABT_JOINT_FOOT_LEFT = 21
K4ABT_JOINT_HIP_RIGHT = 22
K4ABT_JOINT_KNEE_RIGHT = 23
K4ABT_JOINT_ANKLE_RIGHT = 24
K4ABT_JOINT_FOOT_RIGHT = 25
K4ABT_JOINT_HEAD = 26
K4ABT_JOINT_NOSE = 27
K4ABT_JOINT_EYE_LEFT = 28
K4ABT_JOINT_EAR_LEFT = 29
K4ABT_JOINT_EYE_RIGHT = 30
K4ABT_JOINT_EAR_RIGHT = 31
K4ABT_JOINT_COUNT = 32

#class k4abt_sensor_orientation_t(CtypeIntEnum):
k4abt_sensor_orientation_t = ctypes.c_int
K4ABT_SENSOR_ORIENTATION_DEFAULT = 0       
K4ABT_SENSOR_ORIENTATION_CLOCKWISE90 = 1     
K4ABT_SENSOR_ORIENTATION_COUNTERCLOCKWISE90 = 2
K4ABT_SENSOR_ORIENTATION_FLIP180 = 3 

#class k4abt_tracker_processing_mode_t(CtypeIntEnum):
k4abt_tracker_processing_mode_t = ctypes.c_int
K4ABT_TRACKER_PROCESSING_MODE_GPU = 0
K4ABT_TRACKER_PROCESSING_MODE_CPU = 1


class _k4abt_tracker_configuration_t(ctypes.Structure):
	_fields_= [
		("sensor_orientation", k4abt_sensor_orientation_t),
		("processing_mode", k4abt_tracker_processing_mode_t),
		("gpu_device_id", ctypes.c_int)
	]

k4abt_tracker_configuration_t = _k4abt_tracker_configuration_t

class _wxyz(ctypes.Structure):
	_fields_ = [
		("w", ctypes.c_float),
		("x", ctypes.c_float),
		("y", ctypes.c_float),
		("z", ctypes.c_float),
	]

class k4a_quaternion_t(ctypes.Union):
	_fields_= [
		("wxyz", _wxyz),
		("v", ctypes.c_float * 4),
	]

#class k4abt_joint_confidence_level_t(CtypeIntEnum):
k4abt_joint_confidence_level_t = ctypes.c_int
K4ABT_JOINT_CONFIDENCE_NONE = 0
K4ABT_JOINT_CONFIDENCE_LOW = 1           
K4ABT_JOINT_CONFIDENCE_MEDIUM = 2
K4ABT_JOINT_CONFIDENCE_HIGH = 3         
K4ABT_JOINT_CONFIDENCE_LEVELS_COUNT = 4


class _k4abt_joint_t(ctypes.Structure):
	_fields_= [
		("position", k4a_float3_t),
		("orientation", k4a_quaternion_t),
		("confidence_level", k4abt_joint_confidence_level_t)
	]

k4abt_joint_t = _k4abt_joint_t


class _k4abt_skeleton_t(ctypes.Structure):
	_fields_= [
		("joints", k4abt_joint_t * K4ABT_JOINT_COUNT),
	]

k4abt_skeleton_t = _k4abt_skeleton_t


class _k4abt_body_t(ctypes.Structure):
	_fields_= [
		("id", ctypes.c_uint32),
		("skeleton", k4abt_skeleton_t)
	]

k4abt_body_t = _k4abt_body_t

#define K4ABT_BODY_INDEX_MAP_BACKGROUND 255
K4ABT_BODY_INDEX_MAP_BACKGROUND = 255

#define K4ABT_INVALID_BODY_ID 0xFFFFFFFF
K4ABT_INVALID_BODY_ID = ctypes.c_uint(0xFFFFFFFF)

#define K4ABT_DEFAULT_TRACKER_SMOOTHING_FACTOR 0.0f
K4ABT_DEFAULT_TRACKER_SMOOTHING_FACTOR = ctypes.c_float(0.0)


