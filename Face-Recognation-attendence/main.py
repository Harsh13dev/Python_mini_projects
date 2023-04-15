import face_recognition_models
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# load known faces
harsh_image= face_recognition_models.load(open("faces/harsh.jpg"))
harsh_encoding = face_recognition_models.face_encodings(harsh_image)[0]

known_face_encodings = [harsh_encoding]
known_face_names = ["Harsh"]

# list of expected students
students = known_face_names.copy()

face_location = []
face_encodings = []

# get the current date and time

now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_location = face_recognition_models.face_recognition_model_location(rgb_small_frame)
    face_encodings = face_recognition_models.face_recognition_model_location(rgb_small_frame, face_location)

    for face_encoding in face_encodings:
        mathes = face_recognition_models.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition_models.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

    cv2.imshow("Attendace", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break