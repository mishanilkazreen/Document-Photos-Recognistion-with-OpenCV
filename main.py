# Libraries
from glob import glob

import cv2

import matplotlib
import matplotlib.pyplot as plt

import numpy as np
from numpy import ndarray

# Setting up OCR
import config.settings as settings
from paddleocr import PaddleOCR

ocr = PaddleOCR(
    # We have our own inbuilt perspective warp
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,

    lang=settings.LANG,
)

# Function: Resizing image data with an aspect ratio given width
def resize_to_width(img_data: ndarray, target_width: int) -> tuple[float, ndarray]:
    height, width = img_data.shape[:2]

    aspect_ratio = target_width / width
    target_height = int(height * aspect_ratio)

    img_data = cv2.resize(img_data, (target_width, target_height), interpolation=cv2.INTER_AREA)

    return aspect_ratio, img_data

# Function: Scales coordinates based on scale factor
def scale_coordinates(coordinates_data: ndarray, scale_factor: float) -> ndarray:
    scaled_coordinates = (coordinates_data / scale_factor).astype(int)

    return scaled_coordinates

# Function: Converting image files into matrices to operate and calculate on.
def convert_img_to_data(file_name: str) -> ndarray:
    img_data = cv2.imread(file_name, cv2.IMREAD_COLOR) # Reading as BGR colour data

    return img_data

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
def apply_canny_on_img(img_data: ndarray) -> ndarray:
    canny_params = dict(
        threshold1=80,
        threshold2=120
    )
    gaussian_blur_params = dict(
        ksize=(5,5),
        sigmaX=0
    )

    img_grey = cv2.cvtColor(img_data, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_grey, **gaussian_blur_params) # Blurring reduces noise, providing better processing with Canny
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
def extract_document_corners(img_data: ndarray) -> ndarray:
    line_intersections = []
    hough_lines_params = dict(
        rho=1,
        theta=(np.pi / 180), # Radians
        threshold=180
    )

    canny_img = apply_canny_on_img(img_data) # Pre-processing for Hough Transform

    # https://learnopencv.com/hough-transform-with-opencv-c-python/
    lines = cv2.HoughLines(canny_img, **hough_lines_params)

    if lines is None:
        return None

    lines = lines.reshape(-1, 2) # Convert to a 2D matrix

    for i in range(len(lines)):

        for v in range(i+1, len(lines)):
            cords = find_intersection(lines[i], lines[v])

            if cords is not None:
                x, y = cords

                # Check to make sure the coordinates are in the file resolution
                if 0 <= x < img_data.shape[1] and 0 <= y < img_data.shape[0]:
                    line_intersections.append(cords)

    line_intersections = np.array(line_intersections) # Convert array -> ndarray

    if len(line_intersections) < 4: # We need at least 4 intersections otherwise we won't be able to formulate a quadrilateral
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

# Function: Applies homography and a perspective warp to achieve a flat document view
def apply_perspective_warp(img_data: ndarray, corners: ndarray) -> ndarray:
    a4_width = 1000
    a4_height = int(a4_width * np.sqrt(2))
    # Creating a resolution of A4 Ratio as a reference for the warp, and to set the new resolution to
    destination_points = np.array([
        [0,0],
        [a4_width-1, 0],
        [a4_width-1, a4_height-1],
        [0, a4_height-1]
    ], dtype=np.float32)

    homography_matrix, retval = cv2.findHomography(corners, destination_points)

    if retval is None:
        return None

    warped_img = cv2.warpPerspective(img_data, homography_matrix, (a4_width, a4_height))

    return warped_img

if __name__ == '__main__':
    file_to_load = "img/LineWritten.jpeg" # input(f"Enter the file directory to process.")

    img_files = load_img_into_memory(file_to_load)

    for img_file in img_files:
        aspect_ratio, img_file_downsized = resize_to_width(img_file, 800) # Improves performance with pre-processing when scaling down

        corner_data_downsized = extract_document_corners(img_file_downsized)
        corner_data_normal = scale_coordinates(corner_data_downsized, aspect_ratio) # Return coordinates for the original image

        warped_img = apply_perspective_warp(img_file, corner_data_normal)

        result = ocr.predict(warped_img)

        for page in result:
            record_texts = page.get('rec_texts', [])
            record_scores = page.get('rec_scores', [])

            for text, score in zip(record_texts, record_scores):
                print(f'Text: {text}, Confidence Level: {score:.2f}')
