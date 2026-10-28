
from PIL import Image
import cv2
import numpy as np


def analyze_image(uploaded_file):
    """
    Perform basic image processing.
    This function does not diagnose skin conditions.
    """
    image = Image.open(uploaded_file).convert("RGB")

    # Keep image size manageable for processing.
    image.thumbnail((1024, 1024))

    image_array = np.array(image)

    # Convert RGB to OpenCV's BGR format.
    cv_image = cv2.cvtColor(
        image_array,
        cv2.COLOR_RGB2BGR
    )

    height, width = cv_image.shape[:2]

    # Calculate average color of the entire image.
    average_color = np.mean(image_array, axis=(0, 1))

    # Convert image to grayscale for basic quality information.
    gray_image = cv2.cvtColor(
        cv_image,
        cv2.COLOR_BGR2GRAY
    )

    brightness = float(np.mean(gray_image))
    sharpness = float(cv2.Laplacian(
        gray_image, cv2.CV_64F
    ).var())

    return {
        "image": image,
        "width": width,
        "height": height,
        "average_color": average_color.tolist(),
        "brightness": round(brightness, 2),
        "sharpness": round(sharpness, 2),
    }
