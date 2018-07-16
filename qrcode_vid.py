import numpy as np
from pyzbar.pyzbar import decode
import cv2
import xml.etree.ElementTree as ET
import datetime
q=""
cap=cv2.VideoCapture(1)
frame_width = int(cap.get(3))

frame_height = int(cap.get(4))

while cap.isOpened():
  ret,frame3=cap.read()


  if(ret==True):
    ret,frame=cap.read()
  #print frame ,ret
    a=decode(frame)

    for bcode in a:

        (x,y,w,h)=bcode.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #odeData = barcode.data.decode("utf-8")
        q= bcode.data.decode("utf-8")


  cv2.imshow("img",frame)



            #time.sleep(.5)
  if cv2.waitKey(1) & 0xFF == 27  :
    break

print q
cap.release()
cv2.destroyAllWindows()

n=datetime.datetime.now()

root = ET.fromstring(q)
p=root.tag
#for att in len(root.attrib):
#    o=att
#    print o
o=root.attrib
if n.year-int(o["yob"])>18:
    print o["name"],o["uid"],o["loc"],o["gname"],o["yob"],o["gender"],o["state"]
else:
    print "under 18"
