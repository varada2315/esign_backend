import base64
import cv2
import numpy as np

def decode_base64_image(data):
    try:
        image_data = base64.b64decode(data.split(",")[1])
        np_arr = np.frombuffer(image_data, np.uint8)
        return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except:
        return None

def save_image(image, path):
    cv2.imwrite(path, image)