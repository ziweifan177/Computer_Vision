# Computer_Vision
 
## PictureConversion:
- This project will compare a number of the most well known image filters and how they will improve the edge detection.
### Why edge detection?
- Enhancing the edges of an image can help a model detect the features of an image.
- It reduces the amount of data in an image and preserves the structural properties of an image.
### Filter?
#### Overview
- Image filters can be used to reduce the amount of noise(speckle noise, salt-and-pepper noise) in an image and to enhance the edges in an image. 
 - Speck noise: occurs during #image acquisition#
 - Salt-and-pepper noise: (which refers to sparsely occurring white and black pixels) is caused by #sudden disturbances# in an image signal.
- Pre-processing step can improve the accuracy of machine learning models.
#### How to 'filter'?
- Applying a digital filter involves taking the convolution of an image with a #kernel# (a small matrix).
- For Python, the Open-CV and PIL packages to apply.

#### Types of filters:
- #### Mean filter: ####
 - Why? 
  -- Used to blur an image in order to remove noise
  -- Smooths the edges of the image
 - How?
  --  The pixel intensity of the center element is then replaced by the mean.
  --  Convert from RGB to HSV before filter: Since the dimensions of RGB are dependent on one another where as the three dimensions in HSV are independent of one another, so HSV can apply filters to each of the three dimensions separately.)
