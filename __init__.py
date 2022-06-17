import pygame

pygame.font.init()

class button():

    def __init__(self,window,args):

        #region arg parsing
        self.window = window
        self.children = []

        if "outline" in args:
            self.outline = args["outline"]
            
        else:
            self.outline = False
            
        if "outline_size" in args:
            self.outline_size = args["outline_size"]

        else:
            self.outline_size = 5	
	    			    
        if "outline_color" in args:
            self.outline_color = args["outline_color"]
	    	 
        else:
            self.outline_color = (0,0,0)
				    
            
        if "parent" in args:
            self.parent = args["parent"]
            args["parent"].children.append(self)

        else:
            self.parent = None

        if "function_dragoff" in args:
            self.function_dragoff = args["function_dragoff"]
        else:
            self.function_dragoff = None

        self.hovering = False

        if "function_hold" in args:
            self.function_hold = args["function_hold"]
        else:
            self.function_hold = None

        if "function" in args:
            self.function = args["function"]
        else:
            self.function = lambda : print('Button Pressed')

                
        if "visible" in args:
            self.visible = args["visible"]

        else:
            self.visible = True
            	
        if "active" in args:
            self.active = args["active"]
            
        else:
            self.active = True			


        if "pos" in args:
            self.pos = args["pos"]

        else:
            self.pos = (0,0)

            
        if "color" in args:
            self.default_color = args["color"]
            self.color = args["color"]

        else:
            self.color = (60,125,255)
            self.default_color = (60,125,255)
                
        if "color_clicked" in args:
            self.color_clicked = args["color_clicked"]
				
        else:
            self.color_clicked = (100,100,100)
            
        if "color_hover" in args:
            self.color_hover = args["color_hover"]
				
        else:
            self.color_hover = (130,130,130)


        if "size" in args:
            self.size = args["size"]
            
        else:
            self.size = (50,50)

        self.lastClicked = 0
		
        #endregion

		#region setting rectangle
		
        if self.parent == None:

            self.background_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        else:

            self.background_rect = pygame.Rect(self.parent.pos[0]+self.pos[0], self.parent.pos[1]+self.pos[1], self.size[0], self.size[1])
		
        #endregion

		#region outlines
		
        if self.outline:
			
            if self.parent != None:

                self.outline_rect = pygame.Rect(
                
                    self.parent.pos[0]+self.pos[0]-self.outline_size, #X
                    self.parent.pos[1]+self.pos[1]-self.outline_size, #Y
                    self.size[0] + self.outline_size*2, # Size X
                    self.size[1] + self.outline_size*2  # Size Y
                    
                    )
            else:

                    self.outline_rect = pygame.Rect(
                
                    self.pos[0]-self.outline_size, #X
                    self.pos[1]-self.outline_size, #Y
                    self.size[0] + self.outline_size*2, # Size X
                    self.size[1] + self.outline_size*2  # Size Y
                    
                    )
        
        #endregion

    def checkDragOff(self,mouse_pos):

        x, y = mouse_pos
        hovering = False
        output = False

        if self.parent == None:
            if (x >= self.pos[0]) and (x <= self.pos[0]+self.size[0]):
                if (y >= self.pos[1]) and (y <= self.pos[1]+self.size[1]):
                    hovering = True


        else:
            if (x >= self.pos[0]+self.parent.pos[0]) and (x <= self.pos[0]+self.parent.pos[0]+self.size[0]):
                if (y >= self.pos[1]+self.parent.pos[1]) and (y <= self.pos[1]+self.parent.pos[1]+self.size[1]):
                    hovering = True

        #check if mouse is moved off of button
        if not hovering and self.hovering:
            output = True
        else:
            output = False

        self.hovering = hovering
        return output
        
    def checkClick(self):

        left, middle, right = pygame.mouse.get_pressed()

        output = False

        if left == 0 and self.lastClicked == 1:
            
            output = 'up'

        if left == 1 and self.lastClicked == 0:
            
            output = 'down'

        self.lastClicked = left

        return output

    def poll(self):
        
        left, _, _ = pygame.mouse.get_pressed()
        x,y = pygame.mouse.get_pos()
        clkstate = self.checkClick()

        #check drag-off
        if left == 1:
            if self.checkDragOff((x,y)):
                if self.function_dragoff != None:
                    self.function_dragoff()

        #X range
        if self.parent == None:

            if (x >= self.pos[0]) and (x <= self.pos[0]+self.size[0]):

                #Y range
                if (y >= self.pos[1]) and (y <= self.pos[1]+self.size[1]):

                    #repeating hold function
                    if left and self.function_hold != None:
                        self.function_hold()
                    
                    if self.lastClicked == 0:
                        self.color = self.color_hover 

                    if clkstate == 'up':
                        self.function()
                        self.color = self.color_hover
                    
                    if clkstate == 'down':
                        self.color = self.color_clicked


                else:

                    self.color = self.default_color

            else:
            
                self.color = self.default_color
            
        else:


            if (x >= self.pos[0]+self.parent.pos[0]) and (x <= self.pos[0]+self.parent.pos[0]+self.size[0]):

                #Y range
                if (y >= self.pos[1]+self.parent.pos[1]) and (y <= self.pos[1]+self.parent.pos[1]+self.size[1]):
                    
                    #repeating hold function
                    if left and self.function_hold != None:
                        self.function_hold()

                    if self.lastClicked == 0:
                        self.color = self.color_hover 

                    if clkstate == 'up':
                        self.function()
                        self.color = self.color_hover

                    if clkstate == 'down':
                        self.color = self.color_clicked


                else:

                    self.color = self.default_color

            else:
            
                self.color = self.default_color

    def draw(self):

        self.poll()
		
        if self.outline:
            pygame.draw.rect(self.window, self.outline_color, self.outline_rect)

        

        pygame.draw.rect(self.window, self.color, self.background_rect)

        for child in self.children:
            child.draw()
       
class panel():
    
    def __init__(self,window,args):

        #region arg parsing

        self.children = []
        self.window = window
            
            
        if "outline" in args:
             self.outline = args["outline"]

        else:
            self.outline = False
	    	
	    	
        if "outline_size" in args:
            self.outline_size = args["outline_size"]
	    		
        else:
            self.outline_size = 5	
	    			    
        if "outline_color" in args:
            self.outline_color = args["outline_color"]
	    	 
        else:
            self.outline_color = (0,0,0)
	    		

        if "visible" in args:
            self.visible = args["visible"]
            
        else:
            self.visible = True
            	
            	
        if "pos" in args:
            self.pos = args["pos"]
            
        else:

            self.pos = (0,0)

            #color
        if "color" in args:
            self.color = args["color"]

        else:

            self.color = (255,125,125)


        #size
        if "size" in args:
            self.size = args["size"]

        else:

            self.size = (100,100)

        #parent

        if "parent" in args:
            self.parent = args["parent"]
            args["parent"].children.append(self)

        else:

            self.parent = None
    
        
        if self.parent == None:

            self.background_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        else:

            self.background_rect = pygame.Rect(self.parent.pos[0]+self.pos[0], self.parent.pos[1]+self.pos[1], self.size[0], self.size[1])
            
        #endregion

        #region outlines
		
        if self.outline:
			
            if self.parent != None:

                self.outline_rect = pygame.Rect(
                
                    self.parent.pos[0]+self.pos[0]-self.outline_size, #X
                    self.parent.pos[1]+self.pos[1]-self.outline_size, #Y
                    self.size[0] + self.outline_size*2, # Size X
                    self.size[1] + self.outline_size*2  # Size Y
                    
                    )
            else:

                self.outline_rect = pygame.Rect(
                
                    self.pos[0]-self.outline_size, #X
                    self.pos[1]-self.outline_size, #Y
                    self.size[0] + self.outline_size*2, # Size X
                    self.size[1] + self.outline_size*2  # Size Y
                    
                    )
        
        #endregion
				
    def draw(self):
		
        if self.outline:
            pygame.draw.rect(self.window, self.outline_color, self.outline_rect)

        pygame.draw.rect(self.window, self.color, self.background_rect)    
        
        #drawing children
        for child_obj in self.children:
            child_obj.draw()
    
    def checkHover(self):

        x, y = pygame.mouse.get_pos()

        #parent
        if self.parent != None:

            adj_x = self.pos[0]+self.parent.pos[0]
            adj_y = self.pos[1]+self.parent.pos[1]

            if (x > adj_x and x < adj_x + self.size[0]) and (y > adj_y and y < adj_y + self.size[1]):
                return True
            else:
                return False


        #no parent
        elif(x > self.pos[0] and x < self.pos[0] + self.size[0]) and (y > self.pos[1] and y < self.pos[1] + self.size[1]):
            return True
        else:
            return False



class text():

    def __init__(self,window,args):
        
        self.window = window
        self.children = []

        #region arg parsing

        if "text" in args:
            self.text = args["text"]

        else:
            self.text = 'text'

        if "parent" in args:
            self.parent = args["parent"]
            args["parent"].children.append(self)
        
        else:
            self.parent = None

        if "pos" in args:
            self.pos = args["pos"]

        else:
            self.pos = (0,0)

        if 'bold' in args:
            self.bold = args['bold']
            
        else:
            self.bold = False

        if 'italic' in args:
            self.italic = args['italic']
            
        else:
            self.italic = False

        if 'size' in args:
            self.size = args['size']
            
        else:
            self.size = 20

        if 'color' in args:
            self.color = args['color']
            
        else:
            self.color = (0,0,0)

        if 'font' in args:
            self.font = args['font']
            
        else:
            self.font = None

        if 'underline' in args:
            self.underline = args['underline']
            
        else:
            self.underline = False


    
    def draw(self):

        #customize font
        self.font_object = pygame.font.SysFont(self.font, self.size)
        self.font_object.set_underline(self.underline)
        self.font_object.set_bold(self.bold)
        self.font_object.set_italic(self.italic)

        #create drawable object
        self.text_surface = self.font_object.render(self.text, True, self.color)
        
        if self.parent == None:
            self.window.blit(self.text_surface,self.pos)

        else:
            self.window.blit(self.text_surface,(self.parent.pos[0]+self.pos[0],self.parent.pos[1]+self.pos[1]))

        for child in self.children:
            child.draw()

class image():

    def __init__(self,window,args):

        self.window = window
        self.children = []

        if 'pos' in args:
            self.pos = args["pos"]

        else:
            self.pos = (0,0)

        self.image = pygame.image.load(args["image"]).convert_alpha()      

        if 'parent' in args:
            self.parent = args["parent"]
            self.parent.children.append(self)

        else:
            self.parent = None

        if 'size' in args:
            self.size = args["size"]
        
        else:
            self.size = None

        if 'outline' in args:
            self.outline = args["outline"]
        
        else:
            self.outline = False

        if 'outline_size' in args:
            self.outline_size = args['outline_size']

        else:
            self.outline_size = 5

        if 'outline_color' in args:
            self.outline_color = args["outline_color"]
        
        else:
            self.outline_color = (0,0,0)

        
    def draw(self):


        if self.outline:

            if self.parent == None:

                self.outline_rect = pygame.Rect(
                
                    self.pos[0]-self.outline_size, #X
                    self.pos[1]-self.outline_size, #Y
                    self.size[0] + self.outline_size*2, # Size X
                    self.size[1] + self.outline_size*2  # Size Y
                    
                 )
            
            else:

                self.outline_rect = pygame.Rect(
                
                    self.parent.pos[0]+self.pos[0]-self.outline_size, #X
                    self.parent.pos[1]+self.pos[1]-self.outline_size, #Y
                    self.size[0] + self.outline_size*2, # Size X
                    self.size[1] + self.outline_size*2  # Size Y
                    
                    )

        #transforming
        if self.size != None:
            self.image = pygame.transform.scale(self.image,self.size)


        if self.outline:
            pygame.draw.rect(self.window, self.outline_color, self.outline_rect)
        
        if self.parent == None:
            self.window.blit(self.image,self.pos)
        else:
            self.window.blit(self.image,(self.pos[0]+self.parent.pos[0],self.pos[1]+self.parent.pos[1]))


        for child in self.children:
            child.draw()