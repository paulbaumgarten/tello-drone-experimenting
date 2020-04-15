from djitellopy import Tello
import cv2
import pygame
import numpy as np
import time


#    tello.send_rc_control(
#        left_right_velocity=0,
#        forward_backward_velocity=0,
#        up_down_velocity=0,
#        yaw_velocity=0
#    )

def demo():
    input("Press enter to go!")
    tello = Tello()
    tello.connect()
    tello.takeoff()
    time.sleep(1)
    print(f"Tello: height {tello.get_height()} battery {tello.get_battery()} temperature {tello.get_temperature()}")
    tello.flip_left()
    time.sleep(1)
    print(f"Tello: height {tello.get_height()} battery {tello.get_battery()} temperature {tello.get_temperature()}")
    tello.move_forward(100)
    tello.move_right(100)
    tello.rotate_clockwise(180)
    tello.move_forward(100)
    tello.move_right(100)
    tello.rotate_clockwise(180)
    time.sleep(1)
    tello.flip_right()
    time.sleep(1)
    print(f"Tello: height {tello.get_height()} battery {tello.get_battery()} temperature {tello.get_temperature()}")
    tello.land()
    print(f"Tello: height {tello.get_height()} battery {tello.get_battery()} temperature {tello.get_temperature()}")
    tello.end()
    print("Power off! :-)")

if __name__ == '__main__':
    demo()
