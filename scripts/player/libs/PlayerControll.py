import pygame


#----------------------------------------------------------
from scripts.globals.globalD import *

from scripts.system.inputKeys import InputKeysSystem
from scripts.system.playSpriteSheet import SpriteAnimations

#----------------------------------------------------------





class PlayerController( pygame.sprite.Sprite ):
    def __init__( self , filename_img ):
        super().__init__( )


        globalDict["PLAYER"] = self

        self.inputs_keys = InputKeysSystem()



        self.sprite_img = filename_img
        self.scale      = 64
        self.time       = 0


        self.sprite_sheet         = pygame.image.load( self.sprite_img ).convert()

        self.move_x_sprite          = 0
        self.move_y_sprite          = 0

        self.frame_delay_time       = 0 

        self.speed_move             = 5
        self.player_position_x      = 50
        self.player_position_y      = 50



        #self.sprite_sheet         = pygame.transform.scale( self.sprite_sheet , [ 576 , 24 ] )
        #self.sprite_sheet_rect    = self.sprite_sheet.get_rect()


    def drawSprite( self, screen , world_positions , x , y , w , h  ):
        end_sprite = self.getSprite(  x , y , w , h )
        screen.blit( end_sprite, ( world_positions[0] , world_positions[1] ) )
        pass



    def getSprite( self, x , y , w , h ):
        sprite = pygame.Surface( ( w , h ) )
        sprite.set_colorkey( ( 0 , 0 , 0 ) )
        
        #self.sprite_sheet = pygame.transform.scale( self.sprite_sheet , [  w , h ] )
        sprite.blit( self.sprite_sheet , ( 0,0 ) , ( x , y , w , h) )

        return sprite

        
    
    def playerAnimations( self ):

        if self.frame_delay_time >= 5 :
            self.move_x_sprite += 236
            self.frame_delay_time = 0

        if self.move_x_sprite == 1888:
            self.move_x_sprite = 0 

        
        pass


    def playerMovement(self):


        pass




    def playerUpdate( self , screen ):
        self.keys           = pygame.key.get_pressed()
        self.MousePos       = pygame.mouse.get_pos()
        self.mx , self.my   = pygame.mouse.get_pos()
        #----------------------------------------------------
        inputs_t = self.inputs_keys.inputsKeyboards()
        
        self.frame_delay_time += 1 

        
        #if self.keys[pygame.K_w]:
        
        if inputs_t["w"]:
            self.playerAnimations()
            self.player_position_y -= self.speed_move
            
        if inputs_t["s"]:
            self.playerAnimations()
            self.player_position_y += self.speed_move
            

        if inputs_t["a"]:
            self.playerAnimations()
            self.player_position_x -= self.speed_move
            self.move_y_sprite      = 228


        if inputs_t["d"]:
            self.playerAnimations()

            self.player_position_x += self.speed_move
            self.move_y_sprite      = 0
    
        
        if self.player_position_x >= 1024:
            self.player_position_x = -80 
        
        if self.player_position_y >= 600:
            self.player_position_y = 10 




        self.drawSprite(    screen = screen , 
                            world_positions = ( self.player_position_x , self.player_position_y ) ,  
                            x = self.move_x_sprite  , y = self.move_y_sprite  , 
                            
                            w = 236  , h = 228
                        )
  
        pass





