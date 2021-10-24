import pygame
import pygame.freetype
from time import sleep 

i=0    

def animback(window):
  pygame.freetype.init()
  font=pygame.freetype.Font("JMH Cthulhumbus Arcade UG.ttf" , 36)
  global i
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit();
    if i >= 18:
      i = 0
    file = open("frame_" + str(i) + "_delay-0.1s.gif")
    sleep(.05)
    image = pygame.image.load(file)
    window.blit(image, (0, -300))
    text_surface, rect = font.render("Welcome to the Game..........", (100, 0, 0))
    window.blit(text_surface, (250, 350))
    pygame.display.update()
    i += 1



