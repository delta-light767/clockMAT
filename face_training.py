import cv2
import numpy as np
import os

# Initialize face recognizer and Haar Cascade
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Path to the dataset folder
dataset_path = 'dataset'

# Function to get images and labels from image files
def get_images_and_labels_from_images(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.png')]
    face_samples = []
    ids = []
    
    for image_path in image_paths:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue  # Skip if the image can't be read
        id = int(os.path.split(image_path)[-1].split(".")[1])  # Extract ID from file name
        faces = face_cascade.detectMultiScale(img)
        
        for (x, y, w, h) in faces:
            face_samples.append(img[y:y+h, x:x+w])
            ids.append(id)
    
    return face_samples, ids

# Function to get images and labels from video files
def get_images_and_labels_from_videos(path):
    video_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.avi') or f.endswith('.mp4')]
    face_samples = []
    ids = []
    
    for video_path in video_paths:
        # Extract user ID from the filename assuming it's named in a consistent format
        id = int(os.path.split(video_path)[-1].split("_")[1])  # Extract ID assuming format 'User_{id}_video'
        
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Warning: Could not open video {video_path}")
            continue

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            
            for (x, y, w, h) in faces:
                face_samples.append(gray[y:y+h, x:x+w])
                ids.append(id)
            
            frame_count += 1
            if frame_count % 10 == 0:  # Process every 10th frame to reduce redundancy
                continue

        cap.release()
    
    return face_samples, ids

# Combine face samples and IDs from both image files and video files
face_samples_images, ids_images = get_images_and_labels_from_images(dataset_path)
face_samples_videos, ids_videos = get_images_and_labels_from_videos(dataset_path)

# Aggregate all face samples and IDs
faces = face_samples_images + face_samples_videos
ids = ids_images + ids_videos

# Train the recognizer
if faces and ids:  # Check that we have data to train on
    recognizer.train(faces, np.array(ids))
    recognizer.save('trainer.yml')
    print("Training complete and model saved as 'trainer.yml'.")
else:
    print("No face data found for training.")
