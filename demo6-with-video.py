from djitellopy import Tello
import cv2
# import pygame
import tkinter
import numpy as np
import time
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

tello = Tello()
landed = False
# Setup video capture
out = cv2.VideoWriter("flight.avi",cv2.VideoWriter_fourcc(*'MJPG'), 20.0, (800,600))

def left(e):
    print("Left")
    tello.send_rc_control(40, 0, 0, 0) # left, forward, up, rotate

def right(e):
    print("Right")
    tello.send_rc_control(-40, 0, 0, 0) # left, forward, up, rotate

def forward(e):
    print("Forward")
    tello.send_rc_control(0, 40, 0, 0) # left, forward, up, rotate

def back(e):
    print("Back")
    tello.send_rc_control(0, -40, 0, 0) # left, forward, up, rotate

def up(e):
    print("Up")
    tello.send_rc_control(0, 0, 30, 0) # left, forward, up, rotate

def down(e):
    print("Down")
    tello.send_rc_control(0, 0, -30, 0) # left, forward, up, rotate

def allstop(e):
    print("All stop")
    tello.send_rc_control(0, 0, 0, 0) # left, forward, up, rotate

def land(e):
    global landed
    landed = True
    print("Land")
    tello.land()
    tello.end()

def takeoff(e):
    print("Take off")
    tello.takeoff()

print("Connecting")
tello.connect()
time.sleep(0.5)
if not tello.streamoff():
    print("Could not stop video stream")
    exit()
time.sleep(0.5)
if not tello.streamon():
    print("Could not start video stream")
    exit()

time.sleep(0.5)
app = tkinter.Tk()
app.title("My drone!")
app.bind("<Left>", left)
app.bind("<Right>", right)
app.bind("<Up>", forward)
app.bind("<Down>", back)
app.bind("<Escape>", land)
app.bind("<Return>", land)
app.bind("<space>", allstop)
app.bind("<t>", takeoff)
app.bind("<w>", up)
app.bind("<s>", down)
app.mainloop()
while not landed:
    frame = tello.get_frame_read()
    out.write(frame)
    cv2.imshow("Drone", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # ESC key
        break
# Saving video
out.release()
