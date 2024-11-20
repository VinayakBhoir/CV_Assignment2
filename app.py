import cv2
import numpy as np
import streamlit as st
from PIL import Image

def translate_image(image, tx, ty):
    """Translate the image by tx and ty."""
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    translated = cv2.warpAffine(image, M, (cols, rows))
    return translated

def rotate_image(image, angle):
    """Rotate the image by a specified angle."""
    rows, cols = image.shape[:2]
    center = (cols // 2, rows // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    rotated = cv2.warpAffine(image, M, (cols, rows))
    return rotated

def scale_image(image, fx, fy):
    """Scale the image by fx and fy."""
    scaled = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled

def shear_image(image, shear_factor, axis="x"):
    """Shear the image along the specified axis."""
    rows, cols = image.shape[:2]
    if axis == "x":
        M = np.float32([[1, shear_factor, 0], [0, 1, 0]])
    elif axis == "y":
        M = np.float32([[1, 0, 0], [shear_factor, 1, 0]])
    else:
        raise ValueError("Axis must be 'x' or 'y'.")
    sheared = cv2.warpAffine(image, M, (cols, rows))
    return sheared

# Streamlit UI
st.title("Affine Transformations")
st.write("Upload an image to see predefined transformations applied.")

# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = np.array(Image.open(uploaded_file))
    st.image(image, caption="Original Image", use_column_width=True)

    # Apply predefined transformations
    translated_image = translate_image(image, tx=50, ty=30)  # Translate 50px right, 30px down
    rotated_image = rotate_image(image, angle=45)            # Rotate 45 degrees
    scaled_image = scale_image(image, fx=1.5, fy=1.5)        # Scale 1.5x in both directions
    sheared_image = shear_image(image, shear_factor=0.3, axis="x")  # Shear along X-axis with factor 0.3

    # Display transformed images
    st.image(translated_image, caption="Translated Image (50px right, 30px down)", use_column_width=True)
    st.image(rotated_image, caption="Rotated Image (45°)", use_column_width=True)
    st.image(scaled_image, caption="Scaled Image (1.5x)", use_column_width=True)
    st.image(sheared_image, caption="Sheared Image (X-axis, factor=0.3)", use_column_width=True)
