import cv2 as cv
import pickle
import face_recognition
import numpy as np
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

cred = credentials.Certificate("AccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://attendancerealtime-d1465-default-rtdb.firebaseio.com/',
    'storageBucket': 'attendancerealtime-d1465.appspot.com'
})




cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#background = cv.imread('../Robotics/Internship project_Face recognition attendace/Resources/forFace.jpg')
#Add background images

#loading encoded file
print('Loading Encoded file...')
file = open('Encoded.p', 'rb')

encodeWithID = pickle.load(file)
file.close()
print('Encoded file loaded!')
encodeListKnown, matricule = encodeWithID
#print(matricule)

counter = 0

while True:
    success, img = cap.read()
    
    # imgS = cv.resize(img, (0,0), None, 0.25, 0.25)
    # imgS = cv.cvtColor(imgS, cv.COLOR_BGR2RGB)

    currentFrame = face_recognition.face_locations(img)
    encodeCurrentFrame = face_recognition.face_encodings(img, currentFrame)
    #cv.putText(img, 'Active', org= (0,70),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=3.0 ,color= (0, 255, 0), thickness=2)
    
    if currentFrame: #This is to make it active after no face is detected
    
    
        for encodeFace, faceloc in zip(encodeCurrentFrame, currentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print('Matches: ', matches)
            # print('Matches: ', faceDis)
            
            matchIndex = np.argmin(faceDis)
            #print('Match Index: ', matchIndex)
            
            if matches[matchIndex]:
            # cv.putText(img, 'Present', org= (0,60),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=3.0 ,color= (0, 255, 0), thickness=2)
                for (top, right, bottom, left) in currentFrame:
                    cv.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                    
                id = matricule[matchIndex]
                #print(id)
                
                if counter == 0:
                    counter = 1
        
        if counter != 0:
            
            if counter == 1:
                studentInfo = db.reference(f'Student Data/{id}').get()
                print(studentInfo)
                #update student attendance

                datetimeObject = datetime.strptime(studentInfo['last_attendance'], '%Y-%m-%d %H:%M:%S')
                
                
                timeElapse = (datetime.now()-datetimeObject).total_seconds()
                print(timeElapse)
                
                if timeElapse > 30: #incharge of time befor next attendance of that 
                
                    now = datetime.now()
                    newTime = now.strftime('%Y-%m-%d %H:%M:%S')
                    
                    ref = db.reference(f'Student Data/{id}')
                    studentInfo['total_attendance'] += 1
                    ref.child('total_attendance').set(studentInfo['total_attendance'])
                    ref.child('last_attendance').set(newTime)
                else:
                    cv.putText(img, 'Already Marked', org= (0,60),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=3.0 ,color= (0, 0, 255), thickness=2)
                    counter = 0
                    
                
            if 10 < counter < 20:
                cv.putText(img, 'Present', org= (0,60),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=3.0 ,color= (0, 255, 0), thickness=2)
            
            
            #infact at this level place the user data here, like names, total attendance and stuff like that
                
                
        counter += 1
        
        if counter >= 20:
            counter = 0
            cv.putText(img, 'Active', org= (0,60),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=3.0 ,color= (0, 255, 0), thickness=2)
            
            
            studentInfo = []
            
            
            
    else:
        cv.putText(img, 'Active', org= (0,60),fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=3.0 ,color= (0, 255, 0), thickness=2)
        counter = 0
        
    #background[3.36:107.1 + 107.1, 0.69:107.9 + 107.9] = img
    cv.imshow('Face recognition', img)
    cv.waitKey(1)