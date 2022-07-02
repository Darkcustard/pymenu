
import pygame
pygame.font.init()


class Element():

    def addArg(self,name:str,default):
        
        if name in self.args:
            setattr(self, name, self.args[name])
        else:
            setattr(self, name, default)
    
    # build associated rects and objects based off of attribs.
    def compile(self):
        
        # basepanel
        self.rect = pygame.Rect(self.pos,self.size)
        
        # outline
        if self.outline:
            self.outline_rect = pygame.Rect(
                self.pos[0] - self.outline_size,
                self.pos[1] - self.outline_size,
                self.size[0] + self.outline_size*2,
                self.size[1] + self.outline_size*2)
        
        # text
        if self.text != None:
            
            self.font = pygame.font.Font(self.text_font,self.text_size)
            self.font.bold = self.text_bold
            self.font.italic = self.text_bold
            self.font.underline = self.text_underline
            self.text_object_pos = self.text_pos

            if self.text_relative_pos:
                self.text_object_pos = (self.text_pos[0]+self.pos[0],self.text_pos[1]+self.pos[1])
            
            self.text_object = self.font.render(
                    self.text,
                    self.text_antialias,
                    self.text_color,
                    self.text_color_background)
        

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
            pygame.draw.rect(self.window,self.outline_color,self.outline_rect)
        
        pygame.draw.rect(self.window,self.color,self.rect)

        if self.text != None:
            self.window.blit(self.text_object,self.text_object_pos)

        for child in self.children:
            child.draw()

    def __init__(self,window,args):

        self.args = args
        self.window = window
        self.children = []

        self.addArg("pos",(0,0))
        self.addArg("parent",None)
        self.addArg("size",(125,125))

        self.addArg("color",(125,125,125))
        self.addArg("color_default",self.color)

        self.addArg("outline",False)
        self.addArg("outline_size",1)
        self.addArg("outline_color",(0,0,0))

        self.addArg("image",None)
        self.addArg("image_size",None)
        self.addArg("image_pos",(0,0))

        self.addArg("text",None)
        self.addArg("text_color",(255,255,255))
        self.addArg("text_color_background",(0,0,0,0))
        self.addArg("text_pos",self.pos)
        self.addArg("text_font","Arial")
        self.addArg("text_bold",False)
        self.addArg("text_italic",False)
        self.addArg("text_size",15)
        self.addArg("text_underline",False)
        self.addArg("text_antialias",True)
        self.addArg("text_relative_pos",True)

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
        self.addArg("color_hover",(100,100,100))
        self.addArg("color_clicked",(75,75,75))


        self.lastclickstatus = False
        self.compile()

    def compile(self):
        
        super().compile()

        #button stuff
    
    def checkHover(self):

        self.mousepos = pygame.mouse.get_pos()

        #x 
        if self.mousepos[0] > self.pos[0] and self.mousepos[0] < self.pos[0] + self.size[0]:
            #y
            if (self.mousepos[1] > self.pos[1] and self.mousepos[1] < self.pos[1] + self.size[1]):

                return True

        return False


    def handleClicks(self):
        
        #get edge triggers
        currentclickstatus, _, _ = pygame.mouse.get_pressed()
        
        #check hovering
        if self.checkHover():
            #up
            if ( not currentclickstatus and self.lastclickstatus):
                self.function_up()

            #down
            if (currentclickstatus and not self.lastclickstatus):
                self.function_down()

        self.lastclickstatus = currentclickstatus

    def draw(self):

        self.handleClicks()

        super().draw() 





            
































