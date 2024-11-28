import cv2
import os
import csv

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Face Capture", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Face Capture", 640, 480)

# Get user details
user_class = input("Enter class: ")
user_roll = input("Enter roll number: ")
user_name = input("Enter name: ")
user_id = input("Enter user ID: ")

# Save user details to CSV
if not os.path.exists("user_data.csv"):
    with open("user_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Class", "Roll No", "Name"])
with open("user_data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([user_id, user_class, user_roll, user_name])

# Ensure dataset directory exists
if not os.path.exists('dataset'):
    os.makedirs('dataset')

print("Capturing images. Please look at the camera.")
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        count += 1
        face = frame[y:y+h, x:x+w]
        cv2.imwrite(f"dataset/User.{user_id}.{count}.jpg", face)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("Face Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
        break

cap.release()
cv2.destroyAllWindows()
