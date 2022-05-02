# pymenu
Pygame based library for ui simplification
Elements can be individually handled or parented to another element to be handled automatically under the parents.draw() method
Each element has a lot of customization but default values permit you to use the library with very little code.


---------------------------------------------------------------------------------------------------------------------------------
A small amount of boilerplate is necessary for the library to work properly:
---------------------------------------------------------------------------------------------------------------------------------
1: Initialize a pygame window object:  WIN = pygame.display.set_mode((WIDTH,HEIGHT))
2: Make sure your pymenu elements are defined and parented if you want automatic handling of events and such
3: Call the objects.draw() method to draw and handle its events and all events of its child objects. (This should be done in a loop)
5: Finally call pygame.display.update() to refresh the window.
---------------------------------------------------------------------------------------------------------------------------------
