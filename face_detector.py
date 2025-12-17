import streamlit as st
import cv2
import numpy as np
from mtcnn import MTCNN
from PIL import Image

st.title("Face Detection App")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    img = np.array(image)
    
    # Convert RGB to BGR (for OpenCV)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    
    # Detect faces
    detector = MTCNN()
    faces = detector.detect_faces(img)
    
    # Draw rectangles/circles
    for face in faces:
        x, y, width, height = face['box']
        cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)
        for key, point in face['keypoints'].items():
            cv2.circle(img, point, 2, (0, 255, 0), 2)
    
    # Convert back to RGB for Streamlit
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Display image
    st.image(img_rgb, caption="Detected Faces", width=700)
