import pygame
pygame.init()

# Variables
width = 1275
height = 700
border = 25
VELOCITY = -1
bgcolor = pygame.Color('Black')
fgcolor = pygame.Color('Blue')

# Classes

class Ball:
    RADIUS = height// 35
    
    def __init__(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        
    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)
        
    def update(self):
        global bgcolor, fgcolor
        self.show(bgcolor)
        self.x = self.x + self.x_velocity
        self.y = self.y + self.y_velocity
        self.show(fgcolor)
        
        if self.x == border + Ball.RADIUS:
            self.x_velocity = -self.x_velocity
        elif self.y == height - border - Ball.RADIUS or self.y == border + Ball.RADIUS:
            self.y_velocity = -self.y_velocity
        elif self.x == width - border - Ball.RADIUS and abs(self.y + self.y_velocity - paddle.y) < Paddle.pad_height:
            self.x_velocity = -self.x_velocity

class Paddle:
    pad_height = height// 7
    def __init__(self,x,y, y_velocity):
        self.x = x
        self.y = y
        self.y_velocity = y_velocity
    
    def show(self, color):
        global screen
        pygame.draw.rect(screen, color, pygame.Rect((self.x, self.y), ((border), (self.pad_height))))
    
    def update(self):
        global bgcolor, fgcolor
        self.show(bgcolor)
        self.y = pygame.mouse.get_pos()[1]
        self.show(fgcolor)
        
        if self.y < border:
            self.y_velocity = 0
        elif self.y > height - border - Paddle.pad_height:
            self.y_velocity = 0
    
# Objects

paddle = Paddle((width - border), Paddle.pad_height, 1)
ball_1 = Ball((width//2) - Ball.RADIUS, (height//2) - Ball.RADIUS, VELOCITY, VELOCITY)

# Scenario

screen = pygame.display.set_mode(size=(width,height))

pygame.draw.rect(screen, fgcolor, pygame.Rect((0, 0), ((width), (border))))
pygame.draw.rect(screen, fgcolor, pygame.Rect((0, height - border), ((width), (border))))
pygame.draw.rect(screen, fgcolor, pygame.Rect((0, 0), ((border), (height))))
ball_1.show(fgcolor)
paddle.show(fgcolor)
while 1:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        quit()
        break
    pygame.display.flip()
    ball_1.update()  
    paddle.update()
