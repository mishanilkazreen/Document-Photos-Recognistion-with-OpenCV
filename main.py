# Libraries
from glob import glob

import cv2

import matplotlib
import matplotlib.pyplot as plt

import numpy as np
from numpy import ndarray

# Function: Converting image files into matrices to operate and calculate on.
def convert_img_to_data(file_name: str) -> ndarray:
    file_data = cv2.imread(file_name, cv2.IMREAD_COLOR) # Reading as BGR colour data

    return file_data

# Function: Loading images into memory with their file data.
def load_img_into_memory(directory: str) -> list:
    img_data_arr = []

    image_files = glob(directory)
    image_files.sort()

    # Convert file data into matrix
    for file_name in image_files:
        data = convert_img_to_data(file_name)
        img_data_arr.append(data)

    return img_data_arr

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

# Function: Conducts a matrix multiplication to find the intersection points between two lines
# Goal (x,y) from: p = x*sin(theta) + y*sin(theta)
def find_intersection(line_1: ndarray, line_2: ndarray) -> ndarray:
    rho_1, theta_1 = line_1
    rho_2, theta_2 = line_2

    # cos(theta) sin(theta)
    matrix_a = np.array([
        [np.cos(theta_1), np.sin(theta_1)],
        [np.cos(theta_2), np.sin(theta_2)]
    ])

    # p
    matrix_b = np.array([[rho_1], [rho_2]])

    # Solving simultaneous equations to obtain the intersection points
    try:
        x0, y0 = np.linalg.solve(matrix_a, matrix_b)

        return [int(np.round(x0).item()), int(np.round(y0).item())]

    except np.linalg.LinAlgError:
        return None

# Function: Processing an image and obtaining line intersections, and grabbing the corners of the object
def extract_document_corners(file_data: ndarray) -> ndarray:
    line_intersections = []
    hough_lines_params = dict(
        rho=1,
        theta=(np.pi / 180), # Radians
        threshold=180
    )

    canny_img = apply_canny_on_img(file_data) # Pre-processing for Hough Transform

    # https://learnopencv.com/hough-transform-with-opencv-c-python/
    lines = cv2.HoughLines(canny_img, **hough_lines_params)

    if lines is None:
        return None

    lines.reshape(-1, 2) # Convert to a 2D matrix

    for i in range(len(lines)):

        for v in range(i+1, len(lines)):
            cords = find_intersection(lines[i], lines[v])

            if cords is not None:
                x, y = cords

                # Check to make sure the coordinates are in the file resolution
                if 0 <= x < file_data.shape[1] and 0 <= y < file_data.shape[0]:
                    line_intersections.append(cords)

    line_intersections = np.array(line_intersections) # Convert array -> ndarray

    if len(line_intersections) < 4: # We need at least 4 intersections otherwise we won't be able to formulate a quadrilateral :(
        return None

    # Heuristical Approach. We will obtain the furthest point intersections based on region
    sums = line_intersections.sum(axis=1)
    differences = np.diff(line_intersections, axis=1).flatten()

    top_left = line_intersections[np.argmin(sums)]
    bottom_right = line_intersections[np.argmax(sums)]

    top_right = line_intersections[np.argmin(differences)]
    bottom_left = line_intersections[np.argmax(differences)]

    corners = np.array([top_left, top_right, bottom_right, bottom_left])

    return corners


## canny -> detect the strongest edges -> apply homography -> threshold -> run through ocr model -> get text

if __name__ == '__main__':
    file_to_load = "img/LinedPaperTemplate.png" # input(f"Enter the file(s) directory to process.")

    some_variable_name = load_img_into_memory(file_to_load)
    some_data_name = extract_document_corners(some_variable_name[0])

