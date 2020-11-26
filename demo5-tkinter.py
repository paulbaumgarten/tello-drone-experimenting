from djitellopy import Tello
import cv2
# import pygame
import tkinter
import numpy as np
import time
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

tello = Tello()

def left(e):
    print("Left")
    tello.send_rc_control(-20, 0, 0, 0) # left, forward, up, rotate

def right(e):
    print("Right")
    tello.send_rc_control(20, 0, 0, 0) # left, forward, up, rotate

def forward(e):
    print("Forward")
    tello.send_rc_control(0, 20, 0, 0) # left, forward, up, rotate

def back(e):
    print("Back")
    tello.send_rc_control(0, -20, 0, 0) # left, forward, up, rotate

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
    print("Land")
    tello.land()
    tello.end()

def takeoff(e):
    print("Take off")
    tello.takeoff()

def takeoff(e):
    print("Take off")
    tello.takeoff()

print("Connecting")
tello.connect()
time.sleep(1)
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
