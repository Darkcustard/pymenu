

import pygame
pygame.font.init()


class Panel():

    def addArg(self,name:str,default):
        
        if name in self.args:
            setattr(self, name, self.args[name])
        else:
            setattr(self, name, default)
    
    # build associated rects and objects based off of attribs.
    def compile(self):
        
        #image
        if self.image != None:
            self.image_object = pygame.image.load(self.image).convert_alpha()

            if self.image_size != None:
                self.image_object = pygame.transform.scale(self.image_object,self.image_size)



        
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
                    self.text_color_background).convert_alpha()
        

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
        if self.image != None:
            self.window.blit(self.image_object,self.image_pos)

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
        self.addArg("text_color",(10,10,10))
        self.addArg("text_color_background",None)
        self.addArg("text_pos",self.pos)
        self.addArg("text_font",None)
        self.addArg("text_bold",False)
        self.addArg("text_italic",False)
        self.addArg("text_size",15)
        self.addArg("text_underline",False)
        self.addArg("text_antialias",True)
        self.addArg("text_relative_pos",True)

        if self.parent != None:
            self.parent.children.append(self)

        if self.__class__ == Panel:
            self.compile()
            

class Input(Panel):

    def __init__(self,window,args):

        super().__init__(window,args) #compiles

        self.addArg("input_size",(100,15))
        self.addArg("input_color",(80,80,80))
        self.addArg("input_pos",(0,0))
        self.addArg("input_relative_pos", True)

        self.addArg("input_outline",False)
        self.addArg("input_outline_size",1)
        self.addArg("input_outline_color",(0,0,0))
        
        self.addArg("input_text","Default Text")
        self.addArg("input_text_color",(255,255,255))
        self.addArg("input_text_color_background",None)
        self.addArg("input_text_pos",self.input_pos)
        self.addArg("input_text_font",None)
        self.addArg("input_text_bold",False)
        self.addArg("input_text_italic",False)
        self.addArg("input_text_size",15)
        self.addArg("input_text_underline",False)
        self.addArg("input_text_antialias",True)
        self.addArg("input_text_relative_pos",True)

        # input box

        if self.input_relative_pos:
            self.input_pos = (self.input_pos[0] + self.pos[0], self.input_pos[1] + self.pos[1])


        self.active = False
        self.previousMouseState = False
        self.compile()

    def checkHover(self):
        

        self.mousepos = pygame.mouse.get_pos()
        #x 
        if (self.mousepos[0] > self.input_pos[0] and self.mousepos[0] < self.input_pos[0] + self.input_size[0]):
            #y
            if (self.mousepos[1] > self.input_pos[1] and self.mousepos[1] < self.input_pos[1] + self.input_size[1]):
                return True


        return False


    def handleSelection(self):
        
        mouseState, _, _ = pygame.mouse.get_pressed()
        hovering = self.checkHover()

        #down
        if mouseState and not self.previousMouseState:
            if hovering:
                self.active = True
            else:
                self.active = False

        self.previousMouseState = mouseState

        

    def handleTyping(self):
        
        keydownList = []
        self.keyboardState = pygame.key.get_pressed()
        
        for x in range(len(self.keyboardState)):
            


            key = self.keyboardState[x]
            keyPrevState = self.previousKeyboardState[x]
            
            if key and not keyPrevState:
                
                keydownList.append(True)

            else:

                keydownList.append(False)

        for x in range(len(keydownList)):
            if keydownList[x]:
                
                if x == 8:
                    self.input_text = self.input_text[:-1]

                else:
                    self.input_text += chr(x)


        self.compile()



        self.previousKeyboardState = self.keyboardState

    def compile(self):

        self.input_rect = pygame.Rect(self.input_pos[0],self.input_pos[1],self.input_size[0],self.input_size[1])
        self.previousKeyboardState = pygame.key.get_pressed()



        #outline
        if self.input_outline:
            self.input_outline_rect = pygame.Rect(self.input_pos[0],self.input_pos[1],self.input_size[0],self.input_size[1])


        # text
        if self.input_text != None:
            
            self.input_font = pygame.font.Font(self.input_text_font,self.input_text_size)
            self.input_font.bold = self.input_text_bold
            self.input_font.italic = self.input_text_bold
            self.input_font.underline = self.input_text_underline
            self.input_text_object_pos = self.input_text_pos

            if self.input_text_relative_pos:
                self.input_text_object_pos = (self.input_text_pos[0]+self.pos[0],self.input_text_pos[1]+self.pos[1])
            
            self.input_text_object = self.input_font.render(
                    self.input_text,
                    self.input_text_antialias,
                    self.input_text_color,
                    self.input_text_color_background).convert_alpha()

            super().compile()
        
    def draw(self):
        
        
        self.handleSelection()

        if self.active:
            self.handleTyping()

        super().draw()

        if self.input_outline:
            pygame.draw.rect(self.window,self.input_outline_color,self.input_outline_rect)

        pygame.draw.rect(self.window,self.input_color,self.input_rect)

        if self.input_text != None:
            self.window.blit(self.input_text_object,self.input_text_object_pos)

class Button(Panel):

    def __init__(self,window,args):

        super().__init__(window,args) #compiles
        
        self.addArg("function_down",None)
        self.addArg("function_up",lambda:print("up"))
        self.addArg("function_hold",None)
        self.addArg("function_dragoff",None)
        self.addArg("color_hover",(100,100,100))
        self.addArg("color_clicked",(75,75,75))


        self.lastclickstatus = False
        self.lasthoverstatus = False

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

    def handleEvents(self):

        currentclickstatus, _, _ = pygame.mouse.get_pressed()
        currenthoverstatus = self.checkHover()

        #handle hover edge trigger

        #start hovering
        if currenthoverstatus and not self.lasthoverstatus:
            self.color = self.color_hover
        
        #stop hovering
        if not currenthoverstatus and self.lasthoverstatus:
            self.color = self.color_default

            if currentclickstatus:
                if self.function_dragoff != None:
                    self.function_dragoff()

        
        #handle click edge trigger

        if self.checkHover():
            
            #held down
            if currentclickstatus:
                if self.function_hold != None:
                    self.function_hold()

            #up
            if ( not currentclickstatus and self.lastclickstatus):
                if self.function_up != None:
                    self.function_up()

                self.color = self.color_hover

            #down
            if (currentclickstatus and not self.lastclickstatus):
                if self.function_down != None:
                    self.function_down()

                self.color = self.color_clicked

        self.lastclickstatus = currentclickstatus
        self.lasthoverstatus = currenthoverstatus


    def draw(self):
        
        self.handleEvents()
        super().draw() 




























