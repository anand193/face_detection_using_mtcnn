import streamlit as st
from mtcnn import MTCNN
import cv2
from PIL import Image

st.title("Face Detection using MTCNN")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Read image with PIL
    image = Image.open(uploaded_file)
    img_rgb = cv2.cvtColor(cv2.imread(uploaded_file.name), cv2.COLOR_BGR2RGB)

    detector = MTCNN()
    output = detector.detect_faces(img_rgb)

    # Draw keypoints and boxes
    for i in output:
        x, y, width, height = i['box']
        keypoints = i['keypoints']

        cv2.rectangle(img_rgb, (x, y), (x + width, y + height), (255, 0, 0), 2)
        for point in keypoints.values():
            cv2.circle(img_rgb, point, 2, (255, 0, 0), 2)

    # Show image in Streamlit
    st.image(img_rgb, caption="Detected Faces", width=700)
