# Imports Starts

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Imports Ends
# 
# 
# OpenCV_Simple Functions Definition Starts

# OpenCV Image Read
def read_cv(image_location  , image_mode_str='' , image_mode = -1):
    if image_mode_str:
        if image_mode == "cv2.IMREAD_COLOR":
            image_mode = -1
        elif image_mode == "cv2.IMREAD_GRAYSCALE":
            image_mode = 0
        elif image_mode == "cv2.IMREAD_UNCHANGED":
            image_mode = 1

    return cv2.imread(image_location , image_mode)

# OpenCV Image Write
def write_cv(image_location:str , image):
    return cv2.imwrite(image_location , image)

# OpenCV Image Display with matplotlib  (Compare with Jupyter Notebook)
def print_cv(image , title="Image"):
    # Display the image using Matplotlib
    plt.figure(title)
    # plt.title(title)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')  # Turn off axis labels
    plt.show() 

# OpenCV Image Display with OpenCV
def show_cv(image , title="Image" , end_time=0 ):
    # Display the image using matplotlib
    cv2.imshow(title, image)
    cv2.waitKey(end_time)
    cv2.destroyAllWindows()

# OpenCV Image Resize
def resize_cv(image , width , height):
    return cv2.resize(image , (width , height))

# OpenCV Image Rotate
def rotate_cv(image , rotation:int = 0):
    rotation = rotation % 4 - 1
    if rotation == -1:
        return image
    return cv2.rotate(image , rotation)


