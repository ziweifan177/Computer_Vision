import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter

import variable_config

class image_operation:
    global FIGURE_SIZE 
    FIGURE_SIZE = variable_config.figure_size

    def edge_detection_canny(img, title):
        new_image_edges = cv.Canny(img,100,200)
        print(new_image_edges)

        plt.subplot(121)
        plt.imshow(img,  cmap='gray')
        plt.title(title), plt.xticks([]), plt.yticks([])

        plt.subplot(122)
        plt.imshow(new_image_edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()
        return new_image_edges


    def mean_filter(image_ori):
        image_cvt = cv.cvtColor(image_ori, cv.COLOR_HSV2BGR) # convert to HSV: it is first necessary to convert from RGB to HSV since the dimensions of RGB are dependent on one another where as the three dimensions in HSV are independent of one another (this allows us to apply filters to each of the three dimensions separately.)
        image_gray = cv.cvtColor(image_cvt, cv.COLOR_BGR2GRAY)

        figure_size = FIGURE_SIZE # the dimension of the x and y axis of the kernal.
        new_image_mean_filtered = cv.blur(image_gray,(figure_size, figure_size))

        plt.figure(figsize=(11,6))

        plt.subplot(131)
        plt.imshow(image_ori, cmap='gray')
        plt.title('Original')
        plt.xticks([]), plt.yticks([])

        plt.subplot(132)
        plt.imshow(image_gray, cmap='gray')
        plt.title('Step1: Converted to HSV and Gray color:')
        plt.xticks([]), plt.yticks([])
        
        plt.subplot(133)
        # plt.imshow(cv.cvtColor(new_image_mean_filtered, cv.COLOR_HSV2RGB))
        plt.imshow(new_image_mean_filtered, cmap='gray')
        plt.title('Step2: After Mean filter')
        plt.xticks([]), plt.yticks([])
        plt.show()

        return new_image_mean_filtered


    def Gaussian_filter(image_ori):
        image_cvt = cv.cvtColor(image_ori, cv.COLOR_BGR2HSV) # convert to HSV: it is first necessary to convert from RGB to HSV since the dimensions of RGB are dependent on one another where as the three dimensions in HSV are independent of one another (this allows us to apply filters to each of the three dimensions separately.)
        image_gray = cv.cvtColor(image_cvt, cv.COLOR_BGR2GRAY) # convert to Gray: Without 'gray', artifacts that are now present in the image that were not there previously; after apply gray color, some of the noise and does not create artifacts for a grayscale image

        figure_size = FIGURE_SIZE

        new_image = cv.GaussianBlur(image_gray, (figure_size, figure_size),0)
        plt.figure(figsize=(11,6))
        
        plt.subplot(131)
        plt.imshow(image_ori, cmap='gray')
        plt.title('Original Grayscale')
        plt.xticks([]), plt.yticks([])

        plt.subplot(132)
        plt.imshow(image_gray, cmap='gray')
        plt.title('Step1: Converted to HSV and gray color')
        plt.xticks([]), plt.yticks([])

        plt.subplot(133)
        # plt.imshow(cv.cvtColor(new_image, cv.COLOR_HSV2RGB))
        plt.imshow(new_image, cmap='gray')
        plt.title('Step2: After Gaussian Filter')
        plt.xticks([]), plt.yticks([])
        plt.show()

        return new_image

    '''median_filter: a 9 x 9 median filter can remove some of the salt and pepper noise while retaining the edges of the image.'''
    def median_filter(image_ori):
        image_cvt = cv.cvtColor(image_ori, cv.COLOR_BGR2HSV) # convert to HSV: it is first necessary to convert from RGB to HSV since the dimensions of RGB are dependent on one another where as the three dimensions in HSV are independent of one another (this allows us to apply filters to each of the three dimensions separately.)
        image_gray = cv.cvtColor(image_cvt, cv.COLOR_BGR2GRAY) # convert to Gray: Without 'gray', artifacts that are now present in the image that were not there previously; after apply gray color, some of the noise and does not create artifacts for a grayscale image

        figure_size = FIGURE_SIZE
        new_image = cv.medianBlur(image_gray, figure_size)

        plt.figure(figsize=(11,6))

        plt.subplot(131)
        plt.imshow(image_ori, cmap='gray')
        plt.title('Original Grayscale')
        plt.xticks([]), plt.yticks([])

        plt.subplot(132)
        plt.imshow(image_gray, cmap='gray' )
        plt.title('Step1: Converted to HSV and gray color')
        plt.xticks([]), plt.yticks([])

        plt.subplot(133)
        plt.imshow(new_image, cmap='gray')
        plt.title('Step2: After Median Filter')
        plt.xticks([]), plt.yticks([])
        plt.show()

        return new_image
    
    def laplacian_filter(image_ori):
        image_cvt = cv.cvtColor(image_ori, cv.COLOR_BGR2HSV) # convert to HSV: it is first necessary to convert from RGB to HSV since the dimensions of RGB are dependent on one another where as the three dimensions in HSV are independent of one another (this allows us to apply filters to each of the three dimensions separately.)
        image_gray = cv.cvtColor(image_cvt, cv.COLOR_BGR2GRAY) # convert to Gray: Without 'gray', artifacts that are now present in the image that were not there previously; after apply gray color, some of the noise and does not create artifacts for a grayscale image

        new_image = cv.Laplacian(image_gray, cv.CV_64F)

        plt.figure(figsize=(11,6))

        plt.subplot(221)
        plt.imshow(image_ori, cmap='gray')
        plt.title('Original')
        plt.xticks([]), plt.yticks([])

        plt.subplot(222)
        plt.imshow(image_gray, cmap='gray')
        plt.title('Step1: Converted to HSV and gray color')
        plt.xticks([]), plt.yticks([])

        plt.subplot(223)
        plt.imshow(new_image, cmap='gray')
        plt.title('Step2: After Laplacian Filter')
        plt.xticks([]), plt.yticks([])

        plt.subplot(224)
        res_image = image_gray + new_image
        plt.imshow(res_image, cmap='gray')
        plt.title('Resulting image')
        plt.xticks([]), plt.yticks([])
        plt.show()

        return res_image
