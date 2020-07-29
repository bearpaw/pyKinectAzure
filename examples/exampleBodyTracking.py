# https://docs.microsoft.com/en-us/azure/kinect-dk/build-first-body-app
# https://docs.microsoft.com/en-us/azure/kinect-dk/get-body-tracking-results\
# https://docs.microsoft.com/en-us/azure/kinect-dk/access-data-body-frame
import sys
sys.path.insert(1, '../pyKinectAzure/')

import numpy as np
from pyKinectAzure import pyKinectAzure, _k4a, _k4abt
import cv2
import viz

# Path to the module
# TODO: Modify with the path containing the k4a.dll from the Azure Kinect SDK
k4a_path = '/home/weiy/Softwares/Azure-Kinect-Sensor-SDK/release/v1.4.1/lib/libk4a.so'
k4abt_path = '/usr/lib/libk4abt.so.1.0'

if __name__ == "__main__":
	# Initialize the library with the path containing the module
	pyK4A = pyKinectAzure(k4a_path, k4abt_path)

	# Open device
	pyK4A.device_open()

	# Modify camera configuration
	device_config = pyK4A.k4a_config
	device_config.color_resolution = _k4a.K4A_COLOR_RESOLUTION_720P
	device_config.depth_mode = _k4a.K4A_DEPTH_MODE_NFOV_2X2BINNED
	print(device_config)

	# Start cameras using modified configuration
	pyK4A.device_start_cameras(device_config)
	
	calibration = pyK4A.get_calibration()
    							 
	k4abt_config = pyK4A.k4abt_config
	pyK4A.tracker_create(calibration, k4abt_config)
	
	key = 0
	frame_cnt = 0
	while True:
		frame_cnt += 1
		print('frame #: ', frame_cnt)
		# Get capture
		pyK4A.device_get_capture()
		
		# Get body tracking
		pyK4A.tracker_enqueue_capture()
		pyK4A.tracker_pop_result()
		num_bodies = pyK4A.get_num_bodies()
		
		# print(pyK4A.get_body_id(0))
		index_map_handle = pyK4A.get_body_index_map()
		
		# Get the depth image from the capture
		depth_image_handle = pyK4A.capture_get_depth_image()
		
		# Get the color image from the capture
		color_image_handle = pyK4A.capture_get_color_image()
		
		if color_image_handle:
			color_image = pyK4A.image_convert_to_numpy(color_image_handle)
			pyK4A.image_release(color_image_handle)	
				
		# Check the image has been read correctly
		if depth_image_handle:

			# Read and convert the image data to numpy array:
			depth_image = pyK4A.image_convert_to_numpy(depth_image_handle)

			# Convert depth image (mm) to color, the range needs to be reduced down to the range (0,255)
			depth_color_image = cv2.applyColorMap(np.round(depth_image/30).astype(np.uint8), cv2.COLORMAP_JET)

			# Release the image
			pyK4A.image_release(depth_image_handle)
		
		if index_map_handle:
			pyK4A.image_release(index_map_handle)
		
		
		# Visualization of body tracking
		for i in range(num_bodies):
			body_skeleton = pyK4A.get_body_skeleton(i)
			body_id = pyK4A.get_body_id(i)
			joints2d_color, confidence_level = pyK4A.project_skeleton_to_color(body_skeleton)
			joints2d_depth, _ = pyK4A.project_skeleton_to_depth(body_skeleton)
			color_image = viz.draw_pose_2d(color_image, joints2d_color, confidence_level=confidence_level)
			depth_color_image = viz.draw_pose_2d(depth_color_image, joints2d_depth, confidence_level=confidence_level)
		
		# Visualization		
		cv2.imshow("Color", color_image)
		cv2.imshow("Depth", depth_color_image)
		key = cv2.waitKey(1)

		pyK4A.capture_release()

		if key == 27:    # Esc key to stop
			break
	
	print('Exit.')
	pyK4A.destroy()