import pygame

#-------------------------------------------------------------
from scripts.globals.globalD import *
from scripts.globals.globals_vars import *



#-------------------------------------------------------------

class SpriteAnimations( pygame.sprite.Sprite ):
    def __init__( self , filename_img , num_cols_ronw = [ 8 , 2] , resolutions = [ 1888 , 455 ] ):
        pygame.sprite.Sprite.__init__(self)


        self.sprite_img             = filename_img
        self.sprite_sheet           = pygame.image.load( self.sprite_img ).convert_alpha()

        self.resolutions            = resolutions
        self.cols_rows              = num_cols_ronw


        self.move_x_sprite          = 0
        self.frame_delay_time       = 0 

        self.speed_move             = 1

        self.sprite_position_x      = 0
        self.sprite_position_y      = 0

        self.scale_sprite_frame_w   = self.getSpriteSheetScales()[0] 
        self.scale_sprite_frame_h   = self.getSpriteSheetScales()[1]


        self.position_x        = 0
        self.position_y        = 0


        #print( self.scale_sprite_frame_w )

        #self.getSpriteSheetScales()



#------------------------------------------------------------------------------
    def getSpriteSheetScales( self ):

        end_sprite_scale_x = int( self.resolutions[0] / self.cols_rows[0] ) 
        end_sprite_scale_y = int( self.resolutions[1] / self.cols_rows[1] )

        return [ end_sprite_scale_x , end_sprite_scale_y ]


        pass




#------------------------------------------------------------------------------
    def getSprite( self, x , y ):
        dimensions = self.getSpriteSheetScales()

        sprite = pygame.Surface( ( dimensions[0] , dimensions[1] ) )
        sprite.set_colorkey( ( 0 , 0 , 0 ) )

        sprite.blit( self.sprite_sheet , ( 0 , 0 ) , ( x , y ,  dimensions[0] , dimensions[1]  ) )

        return sprite



#------------------------------------------------------------------------------
    def drawSprite( self, screen ):
        end_sprite = self.getSprite(  self.sprite_position_x  , self.sprite_position_y )

        screen.blit( end_sprite, ( self.position_x  , self.position_y ) )


        pass





#------------------------------------------------------------------------------
    def playAction( self , speed_animation , orientation = "horizontal" ):
        self.keys           = pygame.key.get_pressed()
        self.MousePos       = pygame.mouse.get_pos()
        self.mx , self.my   = pygame.mouse.get_pos()
        #----------------------------------------------------
        oriens = [  "horizontal" , "vertical" ] 
        self.frame_delay_time += 1 


        if self.frame_delay_time >= speed_animation :

            if orientation == oriens[0]:
                self.sprite_position_x += self.scale_sprite_frame_w
                if self.sprite_position_x >= self.resolutions[0] :
                    self.sprite_position_x = 0
            
            if orientation == oriens[1]:
                self.sprite_position_y += self.scale_sprite_frame_w
                if self.sprite_position_y >= self.resolutions[1] :
                    self.sprite_position_y = 0




            self.frame_delay_time = 0




        pass


