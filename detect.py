# import cv2
# import mediapipe as mp
# import numpy as np
# import time

# # ========== Constants ==========
# GAZE_LEFT_THRESHOLD = 60
# GAZE_RIGHT_THRESHOLD = -60

# # ========== Result Storage ==========
# results_data = {
#     "blinks": 0,
#     "gaze": [],
#     "stress": [],
#     "timestamps": []
# }

# # ========== Gaze Detection Logic ==========
# def detect_gaze(nose_x, eye_center_x):
#     offset = nose_x - eye_center_x
#     if offset > GAZE_LEFT_THRESHOLD:
#         return 'left'
#     elif offset < GAZE_RIGHT_THRESHOLD:
#         return 'right'
#     else:
#         return 'center'

# # ========== Start Detection ==========
# def start_detection(duration=30):  # Detection runs for 30 seconds
#     global results_data
#     results_data = {"blinks": 0, "gaze": [], "stress": [], "timestamps": []}

#     mp_face_mesh = mp.solutions.face_mesh
#     face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)
#     LEFT_EYE = [33, 160, 158, 133, 153, 144]
#     RIGHT_EYE = [362, 385, 387, 263, 373, 380]

#     def ear(eye):
#         A = np.linalg.norm(eye[1] - eye[5])
#         B = np.linalg.norm(eye[2] - eye[4])
#         C = np.linalg.norm(eye[0] - eye[3])
#         return (A + B) / (2.0 * C)

#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print(" Cannot open webcam")
#         return

#     blink_count = 0
#     blink_state = False
#     start_time = time.time()

#     while time.time() - start_time < duration:
#         success, frame = cap.read()
#         if not success:
#             break

#         h, w, _ = frame.shape
#         rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = face_mesh.process(rgb)
#         current_time = round(time.time() - start_time, 2)

#         if results.multi_face_landmarks:
#             face = results.multi_face_landmarks[0]
#             lm = face.landmark

#             left_eye = np.array([(int(lm[i].x * w), int(lm[i].y * h)) for i in LEFT_EYE])
#             right_eye = np.array([(int(lm[i].x * w), int(lm[i].y * h)) for i in RIGHT_EYE])
#             avg_ear = (ear(left_eye) + ear(right_eye)) / 2.0

#             if avg_ear < 0.22:
#                 if not blink_state:
#                     blink_count += 1
#                     blink_state = True
#             else:
#                 blink_state = False

#             nose_x = int(lm[1].x * w)
#             eye_x = int(np.mean(left_eye[:, 0]))
#             gaze_dir = detect_gaze(nose_x, eye_x)
#             stress = round(min(blink_count * 0.015, 1.0), 2)

#             #  Debug info for calibration
#             print(f"Nose X: {nose_x}, Eye Center X: {eye_x}, Offset: {nose_x - eye_x}, Gaze: {gaze_dir}")

#             # Display info on webcam frame
#             cv2.putText(frame, f'Blinks: {blink_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#             cv2.putText(frame, f'Gaze: {gaze_dir}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
#             cv2.putText(frame, f'Stress: {stress:.2f}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

#             # Store results
#             results_data["blinks"] = blink_count
#             results_data["gaze"].append(gaze_dir)
#             results_data["stress"].append(stress)
#             results_data["timestamps"].append(current_time)

#         # Show webcam preview
#         cv2.imshow("Webcam Detection (Press 'q' to stop early)", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# # ========== Return Result for Web ==========
# def get_detection_results():
#     return results_data
import cv2
import mediapipe as mp
import numpy as np
import time

# ========== Constants ========== (lowered for better sensitivity)
GAZE_LEFT_THRESHOLD = 20
GAZE_RIGHT_THRESHOLD = -20

# ========== Result Storage ==========
results_data = {
    "blinks": 0,
    "gaze": [],
    "stress": [],
    "timestamps": []
}

# ========== Gaze Detection ==========
def detect_gaze(nose_x, eye_center_x):
    offset = nose_x - eye_center_x
    print(f"[Gaze Offset] Nose: {nose_x}, Eye Center: {eye_center_x}, Offset: {offset}")
    if offset > GAZE_LEFT_THRESHOLD:
        return 'left'
    elif offset < GAZE_RIGHT_THRESHOLD:
        return 'right'
    else:
        return 'center'

# ========== Start Detection ==========
def start_detection(duration=30):
    global results_data
    results_data = {"blinks": 0, "gaze": [], "stress": [], "timestamps": []}

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)
    LEFT_EYE = [33, 160, 158, 133, 153, 144]
    RIGHT_EYE = [362, 385, 387, 263, 373, 380]

    def ear(eye):
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        C = np.linalg.norm(eye[0] - eye[3])
        return (A + B) / (2.0 * C)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    blink_count = 0
    blink_state = False
    start_time = time.time()

    while time.time() - start_time < duration:
        success, frame = cap.read()
        if not success:
            break

        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)
        current_time = round(time.time() - start_time, 2)

        if results.multi_face_landmarks:
            face = results.multi_face_landmarks[0]
            lm = face.landmark

            left_eye = np.array([(int(lm[i].x * w), int(lm[i].y * h)) for i in LEFT_EYE])
            right_eye = np.array([(int(lm[i].x * w), int(lm[i].y * h)) for i in RIGHT_EYE])
            avg_ear = (ear(left_eye) + ear(right_eye)) / 2.0

            if avg_ear < 0.22:
                if not blink_state:
                    blink_count += 1
                    blink_state = True
            else:
                blink_state = False

            nose_x = int(lm[1].x * w)
            eye_x = int(np.mean(left_eye[:, 0]))
            gaze_dir = detect_gaze(nose_x, eye_x)
            stress = round(min(blink_count * 0.015, 1.0), 2)

            # Debug print for gaze
            print(f"Gaze: {gaze_dir}, Blink Count: {blink_count}, Stress: {stress}")

            # Display info on webcam preview
            cv2.putText(frame, f'Blinks: {blink_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f'Gaze: {gaze_dir}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(frame, f'Stress: {stress:.2f}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            # Save results
            results_data["blinks"] = blink_count
            results_data["gaze"].append(gaze_dir)
            results_data["stress"].append(stress)
            results_data["timestamps"].append(current_time)

        # Webcam feed
        cv2.imshow("Webcam Detection (Press 'q' to quit)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ========== Serve Results ==========
def get_detection_results():
    return results_data
