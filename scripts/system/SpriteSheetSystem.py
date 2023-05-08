import pygame

#-------------------------------------------------------------
from scripts.globals.globalD import *
#from scripts.system.playSpriteSheet import SpriteAnimations

#-------------------------------------------------------------

class SpriteAnimations( pygame.sprite.Sprite ):
    def __init__( self , filename_img  ):
        super().__init__( )

        self.sprite_img             = filename_img
        self.sprite_sheet           = pygame.image.load( self.sprite_img ).convert()

        self.move_x_sprite          = 0
        self.frame_delay_time       = 0 

        self.speed_move             = 1
        self.player_position_x      = 50
        self.player_position_y      = 50

        self.scale_sprite_frame_w   = 0 
        self.scale_sprite_frame_h   = 0

    
#------------------------------------------------------------------------------
    def drawSprite( self, screen , world_positions , x , y , w , h  ):
        end_sprite = self.getSprite(  x , y , w , h )
        screen.blit( end_sprite, ( world_positions[0] , world_positions[1] ) )

        self.scale_sprite_frame_w = w
        self.scale_sprite_frame_h = h

        pass


#------------------------------------------------------------------------------
    def getSprite( self, x , y , w , h ):
        sprite = pygame.Surface( ( w , h ) )
        #sprite.set_colorkey( ( 0 , 0 , 0 ) )
        sprite.blit( self.sprite_sheet , ( 0 , 0 ) , ( x , y , w , h) )

        return sprite


#------------------------------------------------------------------------------
    def playAnimation( self , speed_animation , frame_start , frame_end ):
        self.keys           = pygame.key.get_pressed()
        self.MousePos       = pygame.mouse.get_pos()
        self.mx , self.my   = pygame.mouse.get_pos()
        #----------------------------------------------------
        self.move_x_sprite = frame_start

        self.frame_delay_time += 1 

        if self.frame_delay_time >= speed_animation :
            self.move_x_sprite += self.scale_sprite_frame_w
            self.frame_delay_time = 0

        if self.move_x_sprite == frame_start:
            self.move_x_sprite = frame_end 





        pass


