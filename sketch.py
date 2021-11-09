import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "RX-78-2.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989, 0.5870, 0.1140])
    # it is 2 dimensional array formula to convert image to grayscale

def dodge(front, back):
    final_sketch = front*255/(255-back)
    #if image is greater than 255 
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    # to convert any suitable existing column to categorical type we will use aspect function
    # uint8 is for 8-bit signed integer
    return final_sketch.astype('uint8')

ss = imageio.imread(img) # to read the given image
gray = rgb2gray(ss) # first we will image to B & W that means grayscale

i = 255-gray # 0,0,0 is for the darkest color and 255, 255, 255 is the brightest color

# to convert it into the blur image (sigma is the intensity of bluriness of the image)
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)

r =  dodge(blur,gray) # this function will convert our image to sketch by taking 2 parameters as blur and gray

cv2.imwrite('RX-78-2.png', r)