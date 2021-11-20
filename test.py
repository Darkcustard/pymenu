from pygame_menu import *

WIN = pygame.display.set_mode((600,300))
element = button(WIN,{

    "pos":(30,30),
    "size":(300,100),

})

Run = True

while Run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False


    element.draw()
    pygame.display.update()