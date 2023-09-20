# Imports Starts

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
# Imports Ends
# 

#  Linux KDE Error
def qt_error():
    os.environ['QT_QPA_PLATFORM'] = 'xcb'

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
def show_cv(image , title="Image" , wait=0 ):
    # Display the image using matplotlib
    cv2.imshow(title, image)

    cv2.waitKey(wait)
    cv2.destroyAllWindows()

# OpenCV Image Resize
def resize_cv(image , height = 0 , width = 0 , scale_x = 1 , scale_y = 1, scale = -1 ):
    if scale != -1:
        scale_x = scale
        scale_y = scale
    return cv2.resize(image , (width , height) , fx = scale_x , fy = scale_y)

# OpenCV Image Rotate
def rotate_cv(image , rotation:int = 0):
    rotation = rotation % 4 - 1
    if rotation == -1:
        return image
    return cv2.rotate(image , rotation)

def size_cv(image):
    return image.shape

# def cvtcolor_cv(image , mode):
#     return cv2.cvtColor(image , exec(mode))


def video_cv(source , live = True , exit_key = 'q' , wait = 1):
    cap = cv2.VideoCapture(source)
    while True:
        ret, frame = cap.read()
        
        cv2.imshow("Video", frame)
        if cv2.waitKey(wait) == ord(exit_key):
            break
    cap.release()
    cv2.destroyAllWindows()