# Computer_Vision
 
## PictureConversion:
- This project will compare a number of the most well known image filters and how they will improve the edge detection.
### Why edge detection?
- Enhancing the edges of an image can help a model detect the features of an image.
- It reduces the amount of data in an image and preserves the structural properties of an image.
### Filters Introduction
#### Overview
- Image filters can be used to reduce the amount of noise(speckle noise, salt-and-pepper noise) in an image and to enhance the edges in an image. 
 1. Speck noise: occurs during image acquisition
 2. Salt-and-pepper noise: (which refers to sparsely occurring white and black pixels) is caused by #sudden disturbances# in an image signal.
- Pre-processing step can improve the accuracy of machine learning models.
#### How to 'filter'?
- Applying a digital filter involves taking the convolution of an image with a #kernel# (a small matrix).
- For Python, the Open-CV and PIL packages to apply.

#### Types of filters:
- #### Mean filter: ####
  - #### Why? ####  
  1. Used to blur an image in order to remove noise 
  2. Smooths the edges of the image
  - #### How? #### 
  1.  The pixel intensity of the center element is then replaced by the mean. 
  2.  Convert from RGB to HSV before filter: Since the dimensions of RGB are dependent on one another where as the three dimensions in HSV are independent of one another, so HSV can apply filters to each of the three dimensions separately.)
- #### Gaussian filter: ####
  - #### Why? ####
    It does a better job of preserving edges than a similarly sized mean filter.
  - #### How? ####
  - Similar to the mean filter, but it involves a *weighted average* of the surrounding pixels and has a parameter sigma. 
  - The kernel represents a discrete approximation of a *Gaussian distribution*.
  - Python: ‘GaussianBlur’ function from the Open-CV package can be used to implement a Gaussian filter, to specify *shape of the kernel* and sigma value is specified then it is considered the *sigma* value for both the x and y directions.
- #### Median filter: #### 
  - #### How? #### 
    - Calculates the median of the pixel intensities that surround the center pixel in a n x n kernel.
