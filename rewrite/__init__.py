
import pygame

class Element():

    def addArg(self,name:str,default):
        
        if name in self.args:
            setattr(self, name, self.args[name])
        else:
            setattr(self, name, default)

    def compile(self):

        self.rect = pygame.Rect(self.pos,self.size)
        
        if self.outline:
            self.outline_rect = pygame.Rect(
                self.pos[0] - self.outline_size,
                self.pos[1] - self.outline_size,
                self.size[0] + self.outline_size,
                self.size[1] + self.outline_size)

    def setPos(self,pos):
        self.pos = pos
        self.compile()

    def setRelativePos(self,object,pos):
        self.pos = (object.pos[0]+pos[0],object.pos[1]+pos[1])
        self.compile()
    
    def setColor(self,color):
        self.color = color
        self.compile()
    
    def draw(self):
        
        if self.outline:
            pygame.draw.rect(self.outline_rect,self.outline_color)
        
        pygame.draw.rect(self.rect,self.color)

        for child in self.children:
            child.draw()

    def __init__(self,window,args):

        self.args = args
        self.window = window
        self.children = []

        self.addArg("pos",(0,0))
        self.addArg("color",(125,125,125))
        self.addArg("color_hover",(125,125,125))
        self.addArg("size",(125,125))
        self.addArg("outline",False)
        self.addArg("outline_size",1)
        self.addArg("outline_color",(0,0,0))
        self.addArg("color_hover",self.color)
        self.addArg("parent",None)

        if self.parent != None:
            self.parent.children.append(self)

        self.compile()









class Button(Element):

    def __init__(self,window,args):

        super().__init__(window,args)
        
        self.addArg("function_down",lambda:print("down"))
        self.addArg("function_up",lambda:print("up"))
        self.addArg("function_hold",lambda:print("hold"))
        self.addArg("function_dragoff",lambda:print("down"))

    def compile(self):
        
        super().compile()

        #

            
































