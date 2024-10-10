import time
from time import localtime, strftime
import pygame
import music
from pygame import mixer

pygame.init()

def delete_last_line():
    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

userTime = input("Put your desired time in here: ")

run = True
while run == True:
    mTime = strftime("%H:%M", localtime())
    if mTime == userTime:   
        run = False

music.music()
stop = int(input("Type 1 and press enter to stop the alarm clock: "))
