import cv2 
import numpy as np
from controller import ledLight
from serial import Serial, SerialException
import serial.tools.list_ports as list_ports

video=cv2.VideoCapture("test1.gif")

data={'c_green': 0, 'c_red': 0, 'c_blue': 0} #'c_orange':0, 'c_yellow':0}

while True:
#     if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):
#         video.set(cv2.CAP_PROP_POS_FRAMES, 0)
#     ret,img = video.read()
#     img = cv2.resize(img,(640,480))
#     cv2.imshow("Frame", img)
#     k = cv2.waitKey(1)
#     if k == ord('q'):
#         break
# video.release()
# cv2.destroyAllWindows()
    if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT): #For counting the video frame, so that it does not stoppes automatically
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret,img = video.read()
    img = cv2.resize(img, (640,480)) # Resize the video frame
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Converting the RGB to hsv color to detect the color
    # Lower and Upper hsv value
    lower_green = np.array([40,70,80])
    upper_green = np.array([70,255,255])

    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])

    lower_blue = np.array([90,60,0])
    upper_blue = np.array([121,255,255])

    # lower_orange = np.array([10, 100, 20])
    # upper_orange = np.array([25, 255, 255])
    #
    # lower_yellow = np.array([20, 100, 100])
    # upper_yellow = np.array([30, 255, 255])

    # To detect the frame size and it gives the binary value only black and white
    mask1 = cv2.inRange(hsv, lower_green,upper_green)
    mask2 = cv2.inRange(hsv, lower_red,upper_red)
    mask3 = cv2.inRange(hsv, lower_blue,upper_blue)
    # mask4 = cv2.inRange(hsv, lower_orange, upper_orange)
    # mask5 = cv2.inRange(hsv, lower_yellow, upper_yellow)

#     cv2.imshow("Frame", img)
#     cv2.imshow("Frame1", mask1)
#     cv2.imshow("Frame2", mask2)
#     cv2.imshow("Frame3", mask3)
#     k = cv2.waitKey(1)
#     if k == ord('q'):
#         break
# video.release()
# cv2.destroyAllWindows()

    # TO get the contours(actual boarder size/box area)
    cnts1,hei=cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts2,hei=cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts3,hei=cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cnts4,hei=cv2.findContours(mask4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # cnts5,hei=cv2.findContours(mask5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    c_green=0
    c_red=0
    c_blue=0
    # c_orange = 0
    # c_yellow = 0

    print(data)
    ledLight(data)
#
    for c in cnts1:
        area = cv2.contourArea(c)
        if area>300:
            c_green = +1
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    data['c_green'] = c_green
######################################
 # puttext format #

# font                   = cv2.FONT_HERSHEY_SIMPLEX
# bottomLeftCornerOfText = (10,500)
# fontScale              = 1
# fontColor              = (255,255,255)
# thickness              = 1
# lineType               = 2
# cv2.putText(img,'Hello World!',
#     bottomLeftCornerOfText,
#     font,
#     fontScale,
#     fontColor,
#     thickness,
#     lineType)
#######################################
    cv2.putText(img,'G='+str(c_green),(30,25), cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
    for c in cnts2:
        area=cv2.contourArea(c)
        if area>300:
            c_red=+1
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    data['c_red'] = c_red
    cv2.putText(img,'R='+str(c_red),(30,65), cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0),1,cv2.LINE_AA)
    for c in cnts3:
        area=cv2.contourArea(c)
        if area>300:
            c_blue=+1
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)
    data['c_blue'] = c_blue
    cv2.putText(img,'B='+str(c_blue),(30,105), cv2.FONT_HERSHEY_COMPLEX, 1,(255,0,0),1,cv2.LINE_AA)

    # for c in cnts4:
    #     area = cv2.contourArea(c)
    #     if area > 300:
    #         c_orange = +1
    #         x, y, w, h = cv2.boundingRect(c)
    #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # data['c_orange'] = c_orange
    # cv2.putText(img, 'O=' + str(c_orange), (140, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    #
    # for c in cnts5:
    #     area = cv2.contourArea(c)
    #     if area > 300:
    #         c_yellow = +1
    #         x, y, w, h = cv2.boundingRect(c)
    #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # data['c_yellow'] = c_yellow
    # cv2.putText(img, 'Y=' + str(c_yellow), (140, 65), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
    # print("GREEN", c_green)
    # print("RED", c_red)
    # print("BLUE", c_green)

    cv2.imshow("Frame",img)
    k=cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
