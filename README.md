
# pymenu
Pygame based library for ui simplification
Elements can be individually handled or parented to another element to be handled automatically under the parents.draw() method
Each element has a lot of customization but default values permit you to use the library with very little code.



# Usage

1. Initialize a pygame window object:  WIN = pygame.display.set_mode((WIDTH,HEIGHT))
2. Make sure your pymenu elements are defined and parented if you want automatic handling of events and such
3. Call the objects.draw() method to draw and handle its events and all events of its child objects. (This should be done in a loop)
4. Finally call pygame.display.update() to refresh the window.

# Todo

* Get absolute position relative to window method (v1)
* Organise Arg handlers by type (v2)
* Implement Remaining functionality from v1 into v2
* Add Image capability to Element's compile method



