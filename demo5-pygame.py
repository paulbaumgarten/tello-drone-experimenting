from djitellopy import Tello
import cv2
import pygame, time, random
from pygame.locals import *
import time
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

tello = Tello()
print("Connecting")
tello.connect()
time.sleep(1)
pygame.init()
window = pygame.display.set_mode((300, 100))
font = pygame.font.SysFont("Arial", 18)
white = (255,255,255)
clock = pygame.time.Clock()
quit = False
while not quit:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_t:
                window.fill((0,0,0))
                window.blit(font.render("Take off", 1, white), (20,20))
                tello.takeoff()
            if event.key == K_UP:
                window.fill((0,0,0))
                window.blit(font.render("Forward", 1, white), (20,20))
                tello.send_rc_control(0, 30, 0, 0) # left, forward, up, rotate
            if event.key == K_DOWN:
                window.fill((0,0,0))
                window.blit(font.render("Back", 1, white), (20,20))
                tello.send_rc_control(0, -30, 0, 0) # left, forward, up, rotate
            if event.key == K_LEFT:
                window.fill((0,0,0))
                window.blit(font.render("Left", 1, white), (20,20))
                tello.send_rc_control(-30, 0, 0, 0) # left, forward, up, rotate
            if event.key == K_RIGHT:
                window.fill((0,0,0))
                window.blit(font.render("Right", 1, white), (20,20))
                tello.send_rc_control(30, 0, 0, 0) # left, forward, up, rotate
            if event.key == K_w:
                window.fill((0,0,0))
                window.blit(font.render("Up", 1, white), (20,20))
                tello.send_rc_control(0, 0, 30, 0) # left, forward, up, rotate
            if event.key == K_s:
                window.fill((0,0,0))
                window.blit(font.render("Down", 1, white), (20,20))
                tello.send_rc_control(0, 0, -30, 0) # left, forward, up, rotate
            if event.key == K_SPACE:
                window.fill((0,0,0))
                window.blit(font.render("All stop", 1, white), (20,20))
                tello.send_rc_control(0, 0, 0, 0) # left, forward, up, rotate
            if event.key == K_RETURN:
                window.fill((0,0,0))
                window.blit(font.render("Land", 1, white), (20,20))
                tello.land()
            if event.key == K_ESCAPE:
                window.fill((0,0,0))
                window.blit(font.render("Land & quit", 1, white), (20,20))
                tello.land()
                tello.end()
                quit = True
        pygame.display.update()
        clock.tick(25)

pygame.quit()

