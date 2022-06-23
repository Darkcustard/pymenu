
import pygame

class Element():

    def addArg(self,name:str,default):
        
        if name in self.args:
            setattr(self, name, self.args[name])
        else:
            setattr(self, name, default)

    def compile(self):

        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        
        if self.outline:
            self.outline_rect = pygame.Rect(self.pos,self.size)




    def __init__(self,window,args):

        self.args = args
        self.window = window
        self.children = []

        self.addArg("pos",(0,0))
        self.addArg("color",(125,125,125))
        self.addArg("size",(125,125))
        self.addArg("outline",False)
        self.addArg("outline-size",1)
        self.addArg("outline-color",(0,0,0))
        self.addArg("color-hover",self.color)
        self.addArg("parent",None)

        if self.parent != None:
            self.parent.children.append(self)

        self.compile()

class Button(Element):

    def __init__(self,window,args):

        super().__init__(window,args)
        
        self.addArg("function-down",lambda:print("down"))
        self.addArg("function-up",lambda:print("up"))
        self.addArg("function-hold",lambda:print("hold"))
        self.addArg("function-dragoff",lambda:print("down"))



            
































