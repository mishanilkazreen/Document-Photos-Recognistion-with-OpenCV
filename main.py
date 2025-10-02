# Libraries
import sys
import os
import glob

import cv2

import math
import matplotlib
import matplotlib.pyplot as plt

import numpy as np
from numpy import ndarray


# Function: Converting image files into matrices to operate and calculate on.
def convert_img_to_data(file_name: str) -> ndarray:
    file_data = cv2.imread(file_name, 1) # Reading as BGR colour data

    return file_data

# Function: Loading images into memory with their file data.
def load_img_into_memory(directory: str) -> list:
    img_data = []

    image_files = glob.glob(directory)
    image_files.sort()

    # Convert file data into matrix
    for file_name in image_files:
        data = convert_img_to_data(file_name)
        img_data.append(data)

    return img_data

# Function: Applies a Canny Filter to process an Image to provide the computer a reference for edge detection.
def apply_canny_on_img(file_data: ndarray) -> ndarray:
    canny_params = dict(
        threshold1=80,
        threshold2=120
    )

    img_grey = cv2.cvtColor(file_data, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_grey, (5, 5), 0) # Blurring reduces noise, providing better processing with Canny
    img_canny = cv2.Canny(img_blur, **canny_params)

    return img_canny

## canny -> detect the strongest edges -> apply homography -> threshold -> run through ocr model -> get text

if __name__ == '__main__':
    file_to_load = input(f"Enter the file directory to process into text.")

    some_variable_name = load_img_into_memory(file_to_load)

