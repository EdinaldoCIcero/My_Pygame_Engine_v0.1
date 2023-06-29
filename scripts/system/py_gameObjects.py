import pygame
import pygame.math

#---------------------------------------------
from scripts.globals.globalD import *

#
# Classe principal responsavel por manipular todos os objetos do jogo #
#
#-------------------------------------------------------------------- # 


class PY_gameObjects():
    def __init__( self , type_object = "squad" , color = [ 255 , 255 , 255 ] , positions = [ 1024/2 , 720/2 ] , scales = [ 50 , 50 ] , border_radius = 5 ):
        super().__init__()

        self.owner              = self
        self.object_type        = type_object

        self.object_color       = color
        self.object_positions   = positions
        self.object_scales      = scales
        self.object_border_rad  = border_radius

        self.vector_object      = pygame.math.Vector2()
        
        #--------------------------------------------------------
        
        self.list_type_objects = [ "squad" , "cicle" ]
        self.x = 0
        self.y = 0


        

        pass


    def squadObject(self , screen ):
        
        objects_rects = { "squad" : pygame.draw.rect( surface = screen, 
                                                color = color , 
                                                rect = ( positions[0] , positions[1] , scales[0] , scales[1] ), 
                                                #width   = 0, 
                                                border_radius   = border_radius , 
                                                border_top_left_radius      =-1, 
                                                border_top_right_radius     =-1, 
                                                border_bottom_left_radius   =-1, 
                                                border_bottom_right_radius  =-1 ),


                    }
        
        
        return objects_rects[ self.object_type ] 

        pass


    
    def getRectObject( self , object_to_rect , positions = [ 0 , 0 ] , scales = [ 0 , 0 ] ):
        
        obj_image       = pygame.transform.scale( self.owner , [ scales[0] , scales[1] ] )
        #obj_image_mask  = pygame.mask.from_surface( obj_image )
        self.rect       = obj_image.get_rect()
        self.rect       = pygame.Rect( positions[0], positions[1] , scales[0] , scales[1] )
        self.owner      = self.rect


        return self.rect


    def WorldPositions( self , positions = [ 0 , 0 ] ):
        self.owner.x , self.owner.y = positions

        pass


    def getWorldPositions( self ):
        pass


    def applyMovement( self , vector = [ 0 , 0 ] ):
        
        mov_x , mov_y = self.owner.x , self.owner.y  

        if vector[0] != 0:
            self.owner.x += vector[0]

        if vector[1] != 0:
            self.owner.y += vector[1]


        pass
    
    def objectUpdate( self , screen ):
        objc = self.squadObject(self , 
                                screen , 
                                type_object = "squad" ,
                                color = [ 255 , 255 , 255 ] , positions = [ 1024/2 , 720/2 ] , 
                                scales = [ 50 , 50 ] , border_radius = 5 )

        pass


    def drawObject( self):

        pass