import datetime
import pygame
import music
from pygame import mixer

pygame.init()

def delete_last_line():
    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

time = datetime.datetime(timeHMS)
print(time)
