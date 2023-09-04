import PySimpleGUI as sg
import cv2

layout = [
    [sg.Image(key = "-i-")],
    [sg.Text("People Under = ",key = "-t-",expand_x = True,justification = "c")]
    ]

window = sg.Window("Face GUI",layout)
video = cv2.VideoCapture(2)
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    event,values = window.read(timeout = 0)
    if event == sg.WIN_CLOSED:
        break
    ret,frame = video.read()
    #print(ret)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame,1)
    faces = face_cascade.detectMultiScale(
        frame,
        scaleFactor = 1.3, 
        minNeighbors = 7,
        minSize =(30,30))
    #print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    imgbytes = cv2.imencode('.png',frame)[1].tobytes()
    window["-i-"].update(data = imgbytes)
    window["-t-"].update(f"People Under = {len(faces)}")
window.close()
