import cv2
import numpy as np

def preprocess_eye_region(eye_region):
    return cv2.GaussianBlur(eye_region, (5, 5), 0)
