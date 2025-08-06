import cv2
from deepface import DeepFace
import time

def analyze_emotion_from_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        return None, "Webcam not found"
    emotions = []
    start_time = time.time()
    while time.time() - start_time < 10:
        ret, frame = cap.read()
        if not ret:
            continue
        if (time.time() - start_time) % 1 < 0.1:
            try:
                analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                if analysis:
                    emotion = analysis[0]['dominant_emotion']
                    emotions.append(emotion)
            except:
                pass
    cap.release()
    cv2.destroyAllWindows()
    if emotions:
        predominant_emotion = max(set(emotions), key=emotions.count)
        return predominant_emotion, None
    else:
        return None, "No face detected"