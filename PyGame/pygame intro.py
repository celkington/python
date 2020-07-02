import pygame
pygame.init()

#Variables
width = 800
height = 500
border = 25

#The scenario

screen = pygame.display.set_mode(size=(width,height))

pygame.draw.rect(screen, pygame.Color('blue'), pygame.Rect((0,0),((width),(border))))
pygame.draw.rect(screen, pygame.Color('blue'), pygame.Rect((0,475),((width),(border))))
pygame.draw.rect(screen, pygame.Color('blue'), pygame.Rect((0,0), ((border), (height))))
pygame.display.flip()
