import cv2
import numpy as np
import face_recognition
import pickle
from datetime import datetime
import os


date = datetime.now().strftime('%Y-%m-%d')

def markAttendance(name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "Attendance.csv")
    splitter = name.split('_')
    with open(csv_path, "a") as f:
        row_data = [splitter[1],splitter[0],date]
        f.write(f"\n{row_data[0]},{row_data[1]},{row_data[2]}")

def recognize_faces(image_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    encodings_path = os.path.join(script_dir, "face_encodings.pkl")
    encodings_path2 = os.path.join(script_dir, "ClassNames.pkl")

    # Load known face encodings and IDs
    with open(encodings_path, "rb") as f:
        data = pickle.load(f)
    encodeListKnown = data
    with open(encodings_path2, "rb") as f:
        data2 = pickle.load(f)
    classNames = data2

    img = face_recognition.load_image_file(image_path)
    encodesCurFrame = face_recognition.face_encodings(img)
    result = []
    for i in range(len(encodesCurFrame)):
        faceDis = face_recognition.face_distance(encodeListKnown, encodesCurFrame[i])

        matchIndex = np.argmin(faceDis)
        if faceDis[matchIndex] < 0.7:
            name = classNames[matchIndex]
            result.append(name)
            markAttendance(name)


    return set(result)


    
