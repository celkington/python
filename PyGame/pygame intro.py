import pygame
pygame.init()

#Variables
width = 800
height = 500
border = 50

#The scenario

screen = pygame.display.set_mode(size=(width,height))

pygame.draw.rect(screen, pygame.Color('Blue'), pygame.rect((0,0),(width),(border)))
pygame.display.flip()