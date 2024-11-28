Face Recognition Attendance System

This system uses face recognition to mark student attendance and logs the data into an Excel file. It also allows the user to download the attendance report as a PDF. The system captures faces via webcam, identifies them using pre-trained models, and logs attendance based on roll numbers. If the student's face is recognized, their attendance is recorded.

Features
- Real-time **face recognition** to identify students.
- Attendance is logged **row-wise** in Excel, where each student's **name** is aligned to their **roll number**.
- **Duplicate entries** are avoided by checking if the student is already marked present.
- Generates a **PDF report** of attendance, which can be downloaded by the user.
- The system can handle **invalid roll numbers** gracefully and skip those students if their roll number is not recognized.

---

### **Requirements**
The following Python libraries must be installed:

1. **OpenCV**: For face detection and recognition.
2. **Pandas**: For handling data and logging it to Excel.
3. **ReportLab**: For generating PDF reports.

To install the necessary libraries, you can run the following commands:

```bash
pip install opencv-python pandas reportlab
```

---

### **Setup Instructions**

1. **Clone or Download the Repository**:
   - Download or clone this repository to your local machine.

2. **Prepare User Data**:
   - Create a CSV file (`user_data.csv`) containing the students' information. The CSV should have the following columns:
     - `Roll No`: The roll number of the student.
     - `Class`: The class name the student belongs to.
     - `Name`: The name of the student.

   Example:
   ```csv
   Roll No,Class,Name
   1,ClassA,John Doe
   2,ClassA,Jane Smith
   16,ClassB,Alex Ray
   ```

3. **Train the Model**:
   - Make sure you have already trained your face recognition model (`trainer.yml`). If not, you will need to follow the training steps (e.g., using a script like `face_training.py`).

4. **Start the Attendance System**:
   - Run the Python script for face recognition (`face_recognition.py`):
     ```bash
     python face_recognition.py
     ```

   - The webcam will open, and the system will begin detecting faces in real-time.

---

### **How the System Works**

1. **Face Detection and Recognition**:
   - The system uses OpenCV’s Haar Cascade classifier to detect faces.
   - The faces are then recognized using the LBPH (Local Binary Patterns Histograms) face recognizer, which compares them against the trained model.

2. **Logging Attendance**:
   - Each student's attendance is logged based on their **roll number**.
   - The system ensures that the attendance is recorded row-wise in the Excel sheet.
   - If a student is recognized, the attendance is marked as **Present**.
   - If the student is already marked present, the system shows a message "Attendance Taken."

3. **Excel File Format**:
   - The attendance for each class is recorded in separate sheets within the same Excel file.
   - The system logs the following details:
     - **Roll No**
     - **Name**
     - **Date**
     - **Status (Present)**

4. **PDF Generation**:
   - After marking the attendance, the user is prompted if they want to download the attendance report as a **PDF**.
   - The generated PDF contains:
     - **Class Name**
     - **Roll No**, **Name**, **Date**, and **Status** for each student.

---

### **How to Generate the PDF Report**

1. After the system has logged attendance, it will prompt you with:
   ```bash
   Do you want to download the attendance report as a PDF? (y/n):
   ```

2. Type **'y'** to generate the PDF report.
   - The PDF will be saved as `Attendance_Report.pdf` in the same directory.
   
---

### **Important Notes**

- The **Excel file** (`attendance.xlsx`) will be updated every time attendance is marked.
- The **PDF generation** will extract data from the Excel file to generate the report.
- Ensure that the **user_data.csv** file is correctly formatted and contains the right student information, as the system uses the roll number from this CSV to log attendance.
- Make sure that you have a properly trained **face recognition model** (`trainer.yml`) for the system to work.

---

### **Troubleshooting**

1. **"ModuleNotFoundError: No module named 'reportlab'"**:
   - This error occurs if the `reportlab` module is not installed. Install it by running:
     ```bash
     pip install reportlab
     ```

2. **"ValueError: invalid literal for int() with base 10"**:
   - This error occurs if an invalid roll number is encountered. The system skips invalid entries gracefully. Ensure that `user_data.csv` contains valid roll numbers.

3. **Webcam not opening**:
   - Ensure that your webcam is correctly connected and accessible to OpenCV.
   - If you are using a virtual environment, ensure that OpenCV and other libraries are correctly installed within it.

---

### **Future Improvements**

- Implement a **GUI** for better usability.
- Include **multi-class attendance tracking** and allow the system to recognize students from different classes.
- Add **email notifications** for teachers or administrators after marking attendance.

---

### **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README file provides an overview of the face recognition attendance system, setup instructions, and usage details.
