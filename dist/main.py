import pygame
import sys
import Anim

pygame.init()
pygame.mixer.init()
while True:
  try:
    window = pygame.display.set_mode((900,700), pygame.RESIZABLE)
    pygame.mixer.music.load('Music.wav')
    pygame.mixer.music.play()
    Anim.animback(window)
    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)
  except:
    sys.exit(1)

