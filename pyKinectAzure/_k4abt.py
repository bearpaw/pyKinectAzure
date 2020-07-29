import ctypes
import sys
from _k4atypes import *
from _k4abttypes import *
import traceback

class k4abt:
    def __init__(self, modulePath):
        try:
            dll = ctypes.CDLL(modulePath)
        except Exception as e:
            print("Failed to load library", e, ee)
            sys.exit(1)
        
        # k4abt_tracker_create
        self.k4abt_tracker_create = dll.k4abt_tracker_create
        self.k4abt_tracker_create.restype = ctypes.c_int
        self.k4abt_tracker_create.argtypes = (ctypes.POINTER(k4a_calibration_t),
    								   k4abt_tracker_configuration_t,
    								   ctypes.POINTER(k4abt_tracker_t)
                                       )
        
        # k4abt_tracker_enqueue_capture                 
        self.k4abt_tracker_enqueue_capture = dll.k4abt_tracker_enqueue_capture
        self.k4abt_tracker_enqueue_capture.restype = ctypes.c_int
        self.k4abt_tracker_enqueue_capture.argtypes = (
            k4abt_tracker_t,
            k4a_capture_t,
            ctypes.c_int)
        
        # k4abt_tracker_pop_result
        self.k4abt_tracker_pop_result = dll.k4abt_tracker_pop_result
        self.k4abt_tracker_pop_result.restype = ctypes.c_int
        self.k4abt_tracker_pop_result.argtypes = (
            k4abt_tracker_t,
            ctypes.POINTER(k4abt_frame_t),
            ctypes.c_int)
        
        # k4abt_tracker_shutdown
        self.k4abt_tracker_shutdown = dll.k4abt_tracker_shutdown
        self.k4abt_tracker_shutdown.restype = None
        self.k4abt_tracker_shutdown.argtypes = (k4abt_tracker_t,)
        
        # k4abt_tracker_destroy
        self.k4abt_tracker_destroy = dll.k4abt_tracker_destroy
        self.k4abt_tracker_destroy.restype = None
        self.k4abt_tracker_destroy.argtypes = (k4abt_tracker_t,)
        
        # k4abt_frame_get_num_bodies
        self.k4abt_frame_get_num_bodies = dll.k4abt_frame_get_num_bodies
        self.k4abt_frame_get_num_bodies.restype = ctypes.c_uint32
        self.k4abt_frame_get_num_bodies.argtypes = (k4abt_frame_t,)
        
        # k4abt_frame_get_body_id()
        self.k4abt_frame_get_body_id = dll.k4abt_frame_get_body_id
        self.k4abt_frame_get_body_id.restype = ctypes.c_uint32
        self.k4abt_frame_get_body_id.argtypes = (k4abt_frame_t, ctypes.c_uint32)
        
        # k4abt_frame_get_body_index_map()
        self.k4abt_frame_get_body_index_map = dll.k4abt_frame_get_body_index_map
        self.k4abt_frame_get_body_index_map.restype = k4a_image_t
        self.k4abt_frame_get_body_index_map.argtypes = (k4abt_frame_t,)
        
        # k4abt_frame_get_body_skeleton()
        self.k4abt_frame_get_body_skeleton = dll.k4abt_frame_get_body_skeleton
        self.k4abt_frame_get_body_skeleton.restype = k4a_result_t
        self.k4abt_frame_get_body_skeleton.argtypes = (
            k4abt_frame_t,
            ctypes.c_uint32,
            ctypes.POINTER(k4abt_skeleton_t))
        
        # k4abt_frame_get_capture()
        self.k4abt_frame_get_capture = dll.k4abt_frame_get_capture
        self.k4abt_frame_get_capture.restype = k4a_capture_t
        self.k4abt_frame_get_capture.argtypes = (k4abt_frame_t,)
        
        # k4abt_frame_get_device_timestamp_usec()
        self.k4abt_frame_get_device_timestamp_usec = dll.k4abt_frame_get_device_timestamp_usec
        self.k4abt_frame_get_device_timestamp_usec.restype = ctypes.c_uint64
        self.k4abt_frame_get_device_timestamp_usec.argtypes = (k4abt_frame_t,)
    
        # k4abt_frame_reference()
        self.k4abt_frame_reference = dll.k4abt_frame_reference
        self.k4abt_frame_reference.restype = None
        self.k4abt_frame_reference.argtypes = (k4abt_frame_t,)
        
        # k4abt_frame_release()
        self.k4abt_frame_release = dll.k4abt_frame_release
        self.k4abt_frame_release.restype = None
        self.k4abt_frame_release.argtypes = (k4abt_frame_t,)
        
        # k4abt_tracker_set_temporal_smoothing()
        self.k4abt_tracker_set_temporal_smoothing = dll.k4abt_tracker_set_temporal_smoothing
        self.k4abt_tracker_set_temporal_smoothing.restype = None
        self.k4abt_tracker_set_temporal_smoothing.argtypes = (
            k4abt_tracker_t,
            ctypes.c_float)
        
        
        
        