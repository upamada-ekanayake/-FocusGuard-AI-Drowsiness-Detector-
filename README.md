# 🚗💤 FocusGuard: AI Drowsiness Detector

**FocusGuard** is a real-time computer vision application designed to prevent driver fatigue accidents. It uses **MediaPipe's Face Mesh** technology to track 468 facial landmarks and mathematically calculates the **Eye Aspect Ratio (EAR)** to detect drowsiness with high precision.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OpenCV](https://img.shields.io/badge/Library-OpenCV-green)
![MediaPipe](https://img.shields.io/badge/AI-MediaPipe-orange)

## 🌟 Features
* **Real-Time Tracking:** Monitors eye blinks and closure duration in milliseconds.
* **Intelligent Logic:** Distinguishes between natural blinks and "micro-sleeps" using a calibrated EAR threshold (0.15).
* **Dual Alarm System:** Triggers a **Red Visual Border** and an **Audio Alert** when fatigue is detected.
* **Privacy First:** All processing happens locally on the device (Edge AI); no video is sent to the cloud.

## 🛠️ Tech Stack
* **Language:** Python
* **Computer Vision:** OpenCV (`cv2`)
* **AI Model:** Google MediaPipe (Face Landmarker Task)
* **Math:** NumPy / Python Math (Euclidean Geometry)

## ⚙️ How It Works
The system uses the **Eye Aspect Ratio (EAR)** formula to quantify eye openness:

$$
EAR = \frac{||p_2 - p_6|| + ||p_3 - p_5||}{2 \times ||p_1 - p_4||}
$$

* **EAR > 0.20:** Eyes are Open (Safe)
* **EAR < 0.15:** Eyes are Closed (Drowsy)
* If the EAR remains low for **1.5 seconds**, the Alarm triggers.

## 🚀 Quick Start

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/upamada-ekanayake/-FocusGuard-AI-Drowsiness-Detector-.git
    cd -FocusGuard-AI-Drowsiness-Detector-
    ```

2.  **Install Dependencies**
    ```bash
    pip install opencv-python mediapipe
    ```

3.  **Run the App**
    ```bash
    python main.py
    ```

## 📂 Project Structure
* `main.py`: The core application logic.
* `face_landmarker.task`: The pre-trained AI model file.
* `diagnostic.py`: Diagnostic script for audio drivers.

---
*Created by [Upamada Ekanayake](https://github.com/upamada-ekanayake)*