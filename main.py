import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import math

# --- CONFIGURATION ---
LEFT_EYE_INDICES = [362, 385, 387, 263, 373, 380]
RIGHT_EYE_INDICES = [33, 160, 158, 133, 153, 144]

# --- FAST TEST SETTINGS ---
DROWSY_THRESHOLD = 0.15   # EAR must be below this to count as closed
WAIT_FRAMES = 15          # 15 frames = approx 0.5 seconds

def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def get_eye_ratio(landmarks, indices, w, h):
    points = []
    for index in indices:
        p = landmarks[index]
        class Point: pass
        point = Point()
        point.x = p.x * w
        point.y = p.y * h
        points.append(point)

    v1 = calculate_distance(points[1], points[5])
    v2 = calculate_distance(points[2], points[4])
    hor = calculate_distance(points[0], points[3])
    return (v1 + v2) / (2.0 * hor)

# --- SETUP ---
model_path = 'face_landmarker.task'
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.FaceLandmarkerOptions(base_options=base_options, num_faces=1)
face_landmarker = vision.FaceLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
frame_counter = 0

print("✅ NEW CODE LOADED! System is ready.")
print("Look at the scrolling numbers below...")

while True:
    ret, frame = cap.read()
    if not ret: break
    
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    results = face_landmarker.detect(mp_image)

    status_text = "Safe"
    status_color = (0, 255, 0) # Green

    if results.face_landmarks:
        landmarks = results.face_landmarks[0]
        
        left_ear = get_eye_ratio(landmarks, LEFT_EYE_INDICES, w, h)
        right_ear = get_eye_ratio(landmarks, RIGHT_EYE_INDICES, w, h)
        avg_ear = (left_ear + right_ear) / 2.0

        # --- LOGIC ---
        if avg_ear < DROWSY_THRESHOLD:
            frame_counter += 1
            status_text = f"Closing {frame_counter}"
            status_color = (0, 165, 255) # Orange
        else:
            frame_counter = 0

        # --- ALARM ---
        if frame_counter >= WAIT_FRAMES:
            status_text = "ALARM!!"
            status_color = (0, 0, 255) # Red
            cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 10)
            print(f"!!! ALARM !!! EAR: {avg_ear:.3f}")
        else:
            # Print status every frame so we can debug
            print(f"Status: {status_text} | EAR: {avg_ear:.3f}")

        cv2.putText(frame, status_text, (50, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, status_color, 3)

    cv2.imshow('Fast Test Mode', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()