# Imports
import deepface
import cv2
import os
from flask import Flask, request, render_template

# Setup
app = Flask(__name__)
face_detector = cv2.CascadeClassifier(PATH)
deepface.stream(enable_gpu=True, backend='facenet') 

# Face recognition
def identify_face(face):
    result = deepface.verify(img1_path=face, model_name='Facenet')
    if result["verified"]:
        username = # Get from result
        userid = 
        return username + '_' + str(userid)
    else:
        return "Unknown"

# Web routes
@app.route('/')
def home():
   # Display homepage

@app.route('/start')
def start():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        
        faces = extract_faces(frame)
        for face in faces:
            name = identify_face(face)  
            # Add attendance record   

@app.route('/add')  
def add():
    # Add new user
    train_deepface_model() 
     
if __name__ == '__main__':
    app.run(debug=True)
