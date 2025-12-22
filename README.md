## 🧑‍🦱 Face Detection Web App using MTCNN & Streamlit

This project is a face detection web application built using MTCNN (Multi-Task Cascaded Convolutional Neural Network) and Streamlit.
The app detects multiple faces in an uploaded image and highlights:

- Face bounding boxes
- Facial landmarks (eyes, nose, mouth)

The application is deployed on Streamlit Cloud and works fully in a browser.

## 🚀 Live Demo  
👉 **Streamlit App:** [Click Here to Try It!](https://customerchurnpredictionapp-hmcfsvqludm74y9cuvydpj.streamlit.app/)

---
🚀 Features

- Upload an image from your system
- Detect multiple faces using MTCNN
- Draw bounding boxes around faces
- Detect facial keypoints:
    - Left eye
    - Right eye
    - Nose
    - Mouth (left & right)
 
---
## 🛠 Tech Stack

Python
- Streamlit – Web app framework
- MTCNN – Face detection model
- TensorFlow – Backend for MTCNN
- OpenCV (headless) – Image processing
- NumPy

---
▶️ How to Run Locally

## 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/face_detection_using_mtcnn.git
cd face_detection_using_mtcnn
```
2️⃣ Create a virtual environment

```bash
python -m venv .venv
```
Windows
```bash
.venv\Scripts\activate
```
## 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Run the Streamlit app
```bash
streamlit run face_detector.py
```

## 🎯 Future Improvements

- Add face confidence scores
- Face cropping & download option
- Webcam-based real-time face detection

## 👤 Author

Anand

Aspiring Data Scientist | Machine Learning Enthusiast

