import cv2,os
import numpy as np
from PIL import Image 
import sqlite3

def getprofile(id):
	connection = sqlite3.connect("summarize.db")
	cmd = " SELECT * FROM Authentication WHERE Id ="+str(id)
	cursor = connection.execute(cmd)
	profile = None
	for row in cursor :
		profile = row
	connection.close()
	return profile
	
	
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('Rec_auth/traingdata.yml')
haarcascadepath="haarcascade_frontalface_default.xml"
extracted_info=cv2.CascadeClassifier(haarcascadepath);
path='sum_samples'
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
scale=1.2
color=(0,0,255)
yes=0
no=0
while True:
	ret,im=cam.read()
	gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	faces = extracted_info.detectMultiScale(gray,scaleFactor = 1.2, minNeighbors = 5, minSize=(100,100), flags = cv2.CASCADE_SCALE_IMAGE)
	for (x,y,w,h) in faces : 
		id,cof = rec.predict(gray[y:y+h, x:x+w])
		cv2.rectangle(im,(x,y),(x+w,y+h), (225,0,0),2)
		cv2.putText(im,"Authenticating user", (35,35),font,scale,color,lineType=cv2.LINE_AA)
		profile = getprofile(id)
		
		prediction = rec.predict(gray[y:y+h, x:x+w])
		
		if prediction[1]>50:

			cv2.putText(im,"UNKNOWN", (x,y+h+30), font,scale,color,lineType=cv2.LINE_AA)
			no+=1
			if no>60:
				cam.release()
				cv2.destroyAllWindows() 
				helmetCheck()
				
				exit()
		else:
			cv2.putText(im, str(profile[1]), (x,y+h+30), font,scale,color,lineType=cv2.LINE_AA)
			yes+=1
			if yes>35:
				cam.release()
				cv2.destroyAllWindows()
				helmetCheck()
				
				exit()
	cv2.imshow('im',im)
	if cv2.waitKey(1)== ord('q'):
			break;
cam.release()
cv2.destroyAllWindows() 