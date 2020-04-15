from djitellopy import Tello
import cv2
import cv2.aruco as aruco
import pygame
import numpy as np
import time, math

class AruCode:
    """
    Information about any AruCode found in an image
    """
    def __init__(self, id, corners):
        self.x1,self.y1 = int(corners[0][0][0]), int(corners[0][0][1])
        self.x2,self.y2 = int(corners[0][2][0]), int(corners[0][2][1])
        self.w = abs(self.x2-self.x1)
        self.h = abs(self.y2-self.y1)
        self.x = int(abs(self.x1)/2+abs(self.x2)/2)
        self.y = int(abs(self.y1)/2+abs(self.y2)/2)
        self.id = id
        self.size = int(abs(self.w)/2+abs(self.h)/2)
        diagonal = 0
        if self.x1 == self.x2:
            diagonal = abs(self.y2-self.y1)
        elif self.y1 == self.y2:
            diagonal = abs(self.x2-self.x1)
        else:
            diagonal = math.sqrt(abs(self.y2-self.y1)**2 + abs(self.x2-self.x1)**2)
        self.diagonal = diagonal
    
    def __repr__(self):
        return f"Arucode {self.id} found at {self.x},{self.y}"
    
    @staticmethod
    def parse_ids_and_corners(ids, corners):
        """ Will iterate through the ids and corners returned by aruco.detectMarkers to produce a dictionary of AruCode objects """
        data = {}
        if ids is not None:
            for i in range(len(ids)):
                id = ids[i][0]
                data[id] = AruCode(id, corners[i])
        return data

def demo():
    # Setup for arucodes
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    parameters = aruco.DetectorParameters_create()
    # Confirm take off
    confirm = input("To initiate take off type 'go' >> ")
    if not confirm == "go":
        print("Aborting!")
        return()
    # Initialise
    tello = Tello()
    tello.connect()
    # Wait for video stream
    ok = tello.streamon()
    frame_read = tello.get_frame_read()
    while not frame_read.grabbed:
        frame_read = tello.get_frame_read()
    img = frame_read.frame
    cv2.imshow("video", img)
    k = cv2.waitKey(10) & 0xff
    # Take off
    print(f"Take off. Height: {tello.get_height()}, Battery: {tello.get_battery()}, Temp: {tello.get_temperature()}")
    tello.takeoff()
    # Start the main loop
    keep_going = True
    while keep_going:
        frame_read = tello.get_frame_read()
        if frame_read.grabbed:
            # Get frame
            img = frame_read.frame
            height, width, channels = img.shape
            # Check for arucodes
            corners, ids, rejectedImgPoints = aruco.detectMarkers(img, aruco_dict, parameters=parameters)
            arucodes = AruCode.parse_ids_and_corners(ids, corners)
            delta = 10
            up_down = 0
            rotate = 0
            forward_back = 0
            if 0 in arucodes.keys():
                cv2.rectangle(img, (0,0), (width, height), (255,0,0), 100) # Color us BGR
                keep_going = False
            elif 1 in arucodes.keys():
                cv2.rectangle(img, (0,0), (width, height), (0,0,0), 100) # Color us BGR
                followme = arucodes[1]
                x_percentile = int(100* followme.x / width)
                y_percentile = int(100* followme.y / height)
                if y_percentile < 40:
                    cv2.rectangle(img, (0,0), (width, 0), (0,255,0), 100) # Color us BGR
                    print("move up", time.time())
                    up_down = 30
                elif y_percentile > 60:
                    cv2.rectangle(img, (0,height), (width, height), (0,255,0), 100) # Color us BGR
                    print("move down", time.time())
                    up_down = -30
                if x_percentile < 40:
                    cv2.rectangle(img, (0,0), (0, height), (0,255,0), 100) # Color us BGR
                    print("rotate ccw", time.time())
                    rotate = -40
                elif x_percentile > 60:
                    cv2.rectangle(img, (width,0), (width, height), (0,255,0), 100) # Color us BGR
                    print("rotate cw", time.time())
                    rotate = 40
                if followme.diagonal < 150:
                    cv2.circle(img, (int(width/2), int(height/2)), 50, (0,255,0), -1)
                    print("forward", followme.w, time.time())
                    forward_back = 40
                else:
                    print("stop", time.time())
                    forward_back = 0
            else: # No valid arucode found
                cv2.rectangle(img, (0,0), (width, height), (0,0,255), 100) # Color us BGR
            # Send to RC
            print(f"tello: forward: {forward_back}, up: {up_down}, yaw: {rotate}")
            tello.send_rc_control(
                left_right_velocity=0,
                forward_backward_velocity=forward_back,
                up_down_velocity=up_down,
                yaw_velocity=rotate
            )
            # Preview the image on screen
            cv2.imshow("video", img)
            # Wait 30 milliseconds for a keyboard press
            k = cv2.waitKey(10) & 0xff
            # If ESC key pressed, close out
            if k == 27:
                keep_going = False
    print(f"Landing. Height: {tello.get_height()}, Battery: {tello.get_battery()}, Temp: {tello.get_temperature()}")
    tello.land()
    tello.end()
    print(f"Power off. Battery: {tello.get_battery()}, Temp: {tello.get_temperature()}")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    demo()
