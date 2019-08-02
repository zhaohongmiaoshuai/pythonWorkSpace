#_*_ coding:UTF-8 _*_
import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800,700),0,32)
pygame.display.set_caption("Hello,World!")
background1 = pygame.image.load('..\\1.jpg').convert()
background2 = pygame.image.load('..\\1.png').convert()
plane = pygame.image.load('plane.png').convert_alpha()
background = background1
i = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            i = (i+1)%2
            if i == 1:
                background = background1
            else:
                background = background2
    screen.blit(background,(0,0))
    x,y = pygame.mouse.get_pos()
#    x-=plane.get_width()/2
#    y-=plane.get_height()/2
    screen.blit(plane,(x,y))
    pygame.display.update()

#end