from re import L
import pygame
import v2

WIN = pygame.display.set_mode((500,500))

button = v2.Button(WIN,
        {})


run = True

while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    button.draw()


    pygame.display.update()