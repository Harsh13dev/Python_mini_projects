# Driver Drowsiness Detection

import cv2
import dlib
import pygame
from imutils import face_utils
from scipy.spatial import distance


def play_alarm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alert_sound.mp3")
    pygame.mixer.music.play(-1)  # Play the alarm sound indefinitely


def stop_alarm_sound():
    pygame.mixer.music.stop()


def calculate_eye_aspect_ratio(eye_points):
    A = distance.euclidean(eye_points[1], eye_points[5])
    B = distance.euclidean(eye_points[2], eye_points[4])
    C = distance.euclidean(eye_points[0], eye_points[3])
    ear = (A + B) / (2.0 * C)
    return ear


# Constants for eye aspect ratio (EAR) and threshold for drowsiness detection
EAR_THRESHOLD = 0.20        # 0.25
CONSECUTIVE_FRAMES = 35     # 48

# Initialize variables
frame_counter = 0
alarm_playing = False
drowsy = False

# Load the dlib face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:/Users/HARSH/AppData/Local/Programs/Python/Python311/Lib/site-packages/face_recognition_models/models/shape_predictor_68_face_landmarks.dat")

# Start the video stream
video_stream = cv2.VideoCapture(0)

while True:
    ret, frame = video_stream.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        left_eye = shape[36:42]
        right_eye = shape[42:48]

        left_ear = calculate_eye_aspect_ratio(left_eye)
        right_ear = calculate_eye_aspect_ratio(right_eye)

        ear = (left_ear + right_ear) / 2.0

        left_eye_hull = cv2.convexHull(left_eye)
        right_eye_hull = cv2.convexHull(right_eye)
        cv2.drawContours(frame, [left_eye_hull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [right_eye_hull], -1, (0, 255, 0), 1)

        if ear < EAR_THRESHOLD:
            frame_counter += 1
            if frame_counter >= CONSECUTIVE_FRAMES and not alarm_playing:
                alarm_playing = True
                play_alarm_sound()
                cv2.putText(frame, "Drowsy!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            frame_counter = 0
            if alarm_playing:
                alarm_playing = False
                stop_alarm_sound()

    cv2.imshow("Driver Drowsiness Detector", frame)

    if cv2.waitKey(1) == ord("q"):
        break

# Cleanup
video_stream.release()
cv2.destroyAllWindows()
