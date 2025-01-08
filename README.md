# Face Recognition Attendance System

---

## **Overview**
This project implements a **Face Recognition Attendance System** using Python. It leverages the `face_recognition` library to identify faces and Firebase Realtime Database to manage and update attendance records. The system captures live video from a webcam, detects faces, and updates attendance records for recognized individuals in real-time.

---

## **Features**
1. **Face Detection and Recognition**:
   - Detects faces from a live video feed using `face_recognition`.
   - Matches detected faces with pre-encoded data.

2. **Real-time Attendance Management**:
   - Tracks attendance using Firebase Realtime Database.
   - Ensures a minimum time interval (30 seconds) between consecutive attendance updates for the same individual.

3. **Data Handling**:
   - Pre-encoded face data is loaded from a serialized file (`Encoded.p`).
   - Attendance data includes:
     - Total attendance count.
     - Timestamp of the last recorded attendance.

4. **User Feedback**:
   - Provides visual feedback on the video feed:
     - Draws rectangles around detected faces.
     - Displays attendance status (e.g., "Present," "Already Marked").

---

## **Requirements**

### **Libraries**
- **Python Packages**:
  - `opencv-python` (`cv2`): For video capture and image processing.
  - `face_recognition`: For face detection and encoding.
  - `numpy`: For numerical computations.
  - `firebase-admin`: For Firebase database interaction.
- **Other Dependencies**:
  - `pickle`: For loading pre-encoded face data.
  - `datetime`: For managing timestamps.

### **Hardware**
- A computer with a webcam (for live face detection).

---

## **Setup and Configuration**

1. **Clone the Repository**:
   Clone the project repository to your local machine.

2. **Install Dependencies**:
   Install the required Python libraries using `pip`:
   ```bash
   pip install opencv-python face_recognition numpy firebase-admin
   ```

3. **Configure Firebase**:
   - Set up a Firebase project and Realtime Database.
   - Download the Firebase Admin SDK credentials (`AccountKey.json`) and place it in the project directory.
   - Update the `databaseURL` and `storageBucket` in the script to match your Firebase configuration.

4. **Prepare Encoded Data**:
   - Use the `face_recognition` library to encode known faces and save the data as `Encoded.p`.
   - The encoded file should include:
     - `encodeListKnown`: A list of face encodings.
     - `matricule`: Corresponding unique IDs for the faces.

5. **Run the Script**:
   Execute the script to start the attendance system:
   ```bash
   python attendance_system.py
   ```

---

## **How It Works**
1. **Face Detection**:
   - The webcam captures live video frames.
   - The system detects faces in each frame and encodes them.

2. **Face Recognition**:
   - Detected faces are compared against the pre-encoded data using `face_recognition.compare_faces` and `face_recognition.face_distance`.

3. **Attendance Management**:
   - If a face is recognized:
     - The system retrieves the user's data from Firebase.
     - Updates attendance if sufficient time has elapsed since the last recorded attendance.
   - Attendance updates include:
     - Incrementing the total attendance count.
     - Updating the last attendance timestamp.

4. **User Feedback**:
   - Visual feedback is displayed on the video feed (e.g., bounding boxes, attendance status).

---

## **Code Highlights**
- **Firebase Integration**:
  - Uses Firebase Admin SDK to interact with the Realtime Database.
  - Retrieves and updates user attendance records.
  
- **Face Recognition**:
  - Efficient face matching using `face_recognition.face_distance` and `np.argmin`.

- **Attendance Logic**:
  - Ensures no duplicate attendance is recorded within a short time window.

---

## **Known Issues**
1. **Performance**:
   - The script may lag when processing multiple faces or running on low-end hardware.
2. **Face Encoding**:
   - Requires pre-encoded face data (`Encoded.p`). New faces cannot be dynamically added during runtime.
3. **Error Handling**:
   - Limited error handling for missing Firebase data or invalid configurations.

---

## **Future Improvements**
1. **Dynamic Face Registration**:
   - Add functionality to register new faces directly from the live feed.
2. **Enhanced Error Handling**:
   - Handle cases like missing data or invalid Firebase configurations gracefully.
3. **Improved UI**:
   - Overlay detailed user information on the video feed.
   - Add a GUI for easier interaction and monitoring.

---

## **Acknowledgments**
This project utilizes:
- **OpenCV** for image processing.
- **face_recognition** for efficient face detection and recognition.
- **Firebase Realtime Database** for storing and managing attendance data.
