import pygame

class button():

    def __init__(self,window,args):

        if True:

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
				    
            
            if "parent" in args:
                self.parent = args["parent"]
                args["parent"].children.append(self)

            else:
                self.parent = None


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


            if "text" in args:
                self.text = args["text"]

            else:

                self.text = "button"
		
		#setting rectangle
		
        if self.parent == None:

            self.background_rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        else:

            self.background_rect = pygame.Rect(self.parent.pos[0]+self.pos[0], self.parent.pos[1]+self.pos[1], self.size[0], self.size[1])
		
		#outlines
		
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
                    self.size[0] + self.outline_size, # Size X
                    self.size[1] + self.outline_size  # Size Y
                    
                    )

    def checkHover(self):

        x,y = pygame.mouse.get_pos()
        
        left, middle, right = pygame.mouse.get_pressed()
        
        #X range
        if self.parent == None:

            if (x >= self.pos[0]) and (x <= self.pos[0]+self.size[0]):

                #Y range
                if (y >= self.pos[1]) and (y <= self.pos[1]+self.size[1]):

                    self.color = self.color_hover 

                    

                    if left:

                        self.function()

                else:

                    self.color = self.default_color

            else:
            
                self.color = self.default_color
            
        else:


            if (x >= self.pos[0]+self.parent.pos[0]) and (x <= self.pos[0]+self.parent.pos[0]+self.size[0]):

                #Y range
                if (y >= self.pos[1]+self.parent.pos[1]) and (y <= self.pos[1]+self.parent.pos[1]+self.size[1]):

                    self.color = self.color_hover 

                    left, middle, right = pygame.mouse.get_pressed()

                    if left:

                        self.function()

                else:

                    self.color = self.default_color

            else:
            
                self.color = self.default_color




    def draw(self):

        self.checkHover()
		
        if self.outline:
            pygame.draw.rect(self.window, self.outline_color, self.outline_rect)

        pygame.draw.rect(self.window, self.color, self.background_rect)
       
class panel():
    
    def __init__(self,window,args):

        self.children = []

        
        if True:

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
            
        #outlines
		
        if self.outline:
			
            if self.parent != None:

                self.outline_rect = pygame.Rect(
                
                    self.parent.pos[0]+self.pos[0]-self.outline_size, #X
                    self.parent.pos[1]+self.pos[1]-self.outline_size, #Y
                    self.size[0] + self.outline_size, # Size X
                    self.size[1] + self.outline_size  # Size Y
                    
                    )
            else:

                    self.outline_rect = pygame.Rect(
                
                    self.pos[0]-self.outline_size, #X
                    self.pos[1]-self.outline_size, #Y
                    self.size[0] + self.outline_size, # Size X
                    self.size[1] + self.outline_size  # Size Y
                    
                    )
				
    
    def draw(self):
		
        if self.outline:
            pygame.draw.rect(self.window, self.outline_color, self.outline_rect)

        pygame.draw.rect(self.window, self.color, self.background_rect)    
        
        #drawing children
        for child_obj in self.children:
            child_obj.draw()





