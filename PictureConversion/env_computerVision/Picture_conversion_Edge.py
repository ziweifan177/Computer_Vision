# Create virtual env: python -m venv env_computerVision
# Check all envs: conda info --envs
# Activate env: activate env_computerVision
# Install some packages: pip install opencv-python numpy pillow

# Edge detection Comparation: OpenCV Canny

import image_operation as io
import cv2 as cv

path_img= './data/doggy.jpg'
img = cv.imread(path_img)
print(img)

# 1.1: Edge detection without filter:
new_image_edges = io.image_operation.edge_detection_canny(img, 'Original')

# 2.1: Edge detection after Mean filter:
new_image_mean_filtered = io.image_operation.mean_filter(img) 
new_image_mean_filtered_edged = io.image_operation.edge_detection_canny(new_image_mean_filtered, 'After Mean Filter')

# 2.2: Edge detection after Gaussian filter:
new_image_gaussian_filtered = io.image_operation.Gaussian_filter(img)
new_image_gaussian_filtered_edged = io.image_operation.edge_detection_canny(new_image_gaussian_filtered, 'After Gaussian Filter')

# 2.3: Edge detection after Median Filter:
new_image_median_filtered = io.image_operation.median_filter(img) 
new_image_median_filtered_edged = io.image_operation.edge_detection_canny(new_image_median_filtered, 'After Median Filter')

# 3: Apply laplacian_filter
new_image_laplacian_filter = io.image_operation.laplacian_filter(img) 








