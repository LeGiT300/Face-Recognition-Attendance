import cv2 as cv
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("AccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://attendancerealtime-d1465-default-rtdb.firebaseio.com/',
    'storageBucket': 'attendancerealtime-d1465.appspot.com'
})


folderpath = 'Images'

pathlist = os.listdir(folderpath)
imglist = []
matricule = []
for path in pathlist:
    imglist.append(cv.imread(os.path.join(folderpath, path)))
    matricule.append(os.path.splitext(path)[0])
    #matricule = os.path.splitext(path)[0]
    
    fileName =  f'{folderpath}/{path}'   
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    
    

print(matricule)


def find_encodings(imagelist):
    
    encodelist = []
    
    for img in imagelist:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


print('Encoding Started...')
encodeListKnown = find_encodings(imagelist=imglist)
encodeWithID = [encodeListKnown, matricule]
print(encodeWithID)
print('Encodings complete!')

with open('Encoded.p', 'wb') as file:
    pickle.dump(encodeWithID, file)
    
file.close
print('File saved!')