import json
import cv2
import numpy as np
import pyautogui



with open('test.txt', 'r') as filehandle:
    basicList = json.load(filehandle)
    print(basicList)

file = open('test.txt', "r+")
file.truncate(0)
file.close()

with open('test.txt', 'w') as filehandle:
    json.dump(basicList+1, filehandle)
    dp = basicList+1
    nam = ("screen_record {}.avi".format(dp))
    print(nam)
    print('2')


screen_size=(1920,1080)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
print('3')
out=cv2.VideoWriter(nam,fourcc,20.0,(screen_size))


while True:

    img=pyautogui.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    #cv2.imshow("show",frame)
    if cv2.waitKey(1)  & 0xFF ==ord("q"):
        break


