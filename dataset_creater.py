import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0)
def insertorupdate(id,Name,age):
  conn=sqlite3.connect("sqlite.db")
  cond="SELECT * FROM STUDENTS WHERE ID="+str(id)

  cursor=conn.execute(cond);
  isRecordExist=0
  for row in cursor:
    isRecordExist=1
  if(isRecordExist):
    conn.execute("UPDATE STUDENTS SET Name=? WHERE id=?",(Name,id))
    conn.execute("UPDATE STUDENTS SET age=? WHERE id=?",(age,id))
  else:
    conn.execute("INSERT INTO STUDENTS (id,Name,age) values(?,?,?)",(id,Name,age))
  conn.commit()
  conn.close()
id=input("Enter user id")
Name=input("Enter user name")
age=input("Enter user age")
insertorupdate(id,Name,age)
sampleNum=0
while(True):
  ret,img=cam.read()
  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces=faceDetect.detectMultiScale(gray,1.3,5)
  for (x,y,w,h) in faces:
    sampleNum=sampleNum+1
    cv2.imwrite("dataset/user."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+x+w])
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.waitKey(100)
  cv2.imshow("Face",img)
  cv2.waitKey(3)
  if(sampleNum>20):
    break
cam.release()
cv2.destroyAllWindows()
