from pygame import *

class panel():
    
    def __init__(self,args):

        self.children = []

        
        if True:
            #position
            if "pos" in args:
                self.pos = (args["pos"])
            
            else:

                self.pos = (0,0)

            #color
            if "col" in args:
                self.color = args["col"]

            else:

                self.color = (255,125,125)


            #size
            if "size" in args:
                self.size = args[size]

            else:

                self.size = (100,100)

        

        

panel({"pos":(255,321)})












