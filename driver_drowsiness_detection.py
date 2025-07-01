import cv2
import mediapipe as mp
import numpy as np
import winsound
from scipy.spatial import distance as dist
buzzer_on = False
# EAR calculation function
def calculate_ear(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Eye and face landmarks
LEFT_EYE_IDX = [33, 160, 158, 133, 153, 144]
RIGHT_EYE_IDX = [362, 385, 387, 263, 373, 380]
FACE_BOX_POINTS = list(range(10, 338))  # Jawline to forehead for bounding box

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        continue  # Try again if frame failed

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            # Get face box
            x_list = [int(face.landmark[i].x * w) for i in FACE_BOX_POINTS]
            y_list = [int(face.landmark[i].y * h) for i in FACE_BOX_POINTS]
            x_min, x_max = min(x_list), max(x_list)
            y_min, y_max = min(y_list), max(y_list)

            # Get eye landmarks
            left_eye = [(int(face.landmark[i].x * w), int(face.landmark[i].y * h)) for i in LEFT_EYE_IDX]
            right_eye = [(int(face.landmark[i].x * w), int(face.landmark[i].y * h)) for i in RIGHT_EYE_IDX]

            # Calculate EAR
            left_ear = calculate_ear(left_eye)
            right_ear = calculate_ear(right_eye)
            avg_ear = (left_ear + right_ear) / 2.0
            # Set box color and play/stop buzzer accordingly
            if avg_ear <= 0.25:
                box_color = (0, 0, 255)  # Red box
                if not buzzer_on:
                    winsound.PlaySound("sound.WAV", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
                    buzzer_on = True
            else:
                box_color = (0, 255, 0)  # Green box
                if buzzer_on:
                    winsound.PlaySound(None, winsound.SND_PURGE)
                    buzzer_on = False


            # Set box color: red if drowsy, else green
            box_color = (0, 255, 0) if avg_ear > 0.25 else (0,0,255)
            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), box_color, 2)

            # Draw eye landmarks
            for pt in left_eye + right_eye:
                cv2.circle(frame, pt, 2, (144, 238, 144), -1)

            # Show EAR value
            cv2.putText(frame, f'EAR: {avg_ear:.2f}', (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
