from djitellopy import Tello
import cv2
# import pygame
import numpy as np
import time
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

#    tello.send_rc_control(
#        left_right_velocity=0,
#        forward_backward_velocity=0,
#        up_down_velocity=0,
#        yaw_velocity=0
#    )

def do(tello, forward=0, left=0, rotate=0):
    print(f"Tello: height {tello.get_height()} battery {tello.get_battery()} temperature {tello.get_temperature()}")
    tello.send_rc_control(left, forward, 0, rotate) # Left/right, forward/back, up/down, rotate


def demo():
    # tello.send_rc_control(left_right_velocity, for_back_velocity, up_down_velocity, yaw_velocity)
    tello = Tello()
    tello.connect()
    time.sleep(1)
    print("Take off...")
    tello.takeoff()
    input()
    do(tello, forward=50)
    input()
    do(tello, forward=-0)
    input()
    do(tello, forward=-50)
    input()
    do(tello, forward=-0)


    print("Landing...")
    tello.land()
    tello.end()
    print(f"Tello: battery {tello.get_battery()} temperature {tello.get_temperature()}")
    print("Power off! :-)")

if __name__ == '__main__':
    demo()
