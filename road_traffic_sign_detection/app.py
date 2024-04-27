from flask import Flask, request, render_template, send_file, Response
from ultralytics import YOLO
import torch
#import cv2
#import numpy as np
import os
import time
app = Flask(__name__)

def perform_object_detection(video_path):
    model = YOLO('road_traffic_sign_detection/model/road_traffic_sign_detection_model.pt')
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    current_time = time.strftime("%Y%m%d_%H%M%S")  # Get current timestamp
    name_dir = "traffic_sign_detection"+ current_time
    model.predict(video_path,  conf=0.25, name=name_dir, save=True)
    return name_dir

# Route to upload video and display the processed video
@app.route('/TrafficSignDetection', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'file' not in request.files:
            return render_template('index.html', message='No file part')
        file = request.files['file']
        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            return render_template('index.html', message='No selected file')
        if file:
            # Save the uploaded video
            video_path = "road_traffic_sign_detection/static/uploaded_video.mp4"
            file.save(video_path)
            # Perform object detection
            dir_name = perform_object_detection(video_path)
        
            current_time = time.strftime("%Y%m%d_%H%M%S")
            video_name = "uploaded_video.avi"
            video_path = os.path.join("runs", "detect", dir_name, video_name)
            print(video_path)
            return render_template('index.html', message='Video processed successfully', video_path=video_path)
    return render_template('index.html')

# Route to download the processed video
@app.route('/download_video')
def download_video():
    video_path = request.args.get('video_path')
    return send_file(video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True,host = "0.0.0.0", port = os.getenv("PORT"))
