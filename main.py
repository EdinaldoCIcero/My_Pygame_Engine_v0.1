
import os
import sys
from pprint import pprint, pformat
from ast import literal_eval
import pygame
from pygame.locals import *


dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen",False):
    os.chdir(sys._MEIPASS)

#---------------------------------------------
from random import randint 
import pygame.math


#---------------------------------------------
from scripts.globals.globals_vars import *
from scripts.globals.globalD import *

from scripts.player.libs.PlayerControll import PlayerController

from scripts.system.SpriteSheetSystem import SetSpriteSheetSystem

#---------------------------------------------
pygame.init()




TELA = pygame.display.set_mode([LARGURA , ALTURA])# , pygame.RESIZABLE
pygame.mouse.set_visible(True)
pygame.display.set_caption("<Display-Game-Engine>")
#pygame.display.set_icon( )






#---------------------------------------------
class GameEngine():
    def __init__(self):
        super().__init__()


        self.image_player_path = "assets/sprites/characters/player/dino_run_sheet.png" 


        
        #self.player = PlayerController( self.player_group )

        
        self.player_1    = SetSpriteSheetSystem( filename_img   = self.image_player_path ,
                                                num_cols_ronw  = [ 8, 2] , 
                                                resolutions    = [ 1888 , 455 ] 
                                                )



        self.player_sprite_group    = pygame.sprite.Group()
        self.player_sprite_group.add( self.player_1  )


        print( self.player_sprite_group )


        
        

    
        pass


#-------------------------------------------------------------------------------

    def updateElements(self):
        pass


    def DrawGrid(self):
        cor         = [ 82 , 18 , 44 ]
        larguraline = 1
        colunas     = 0
        lines       = 0
        #-----------------------------



        for i in range(1 , 80 ):
            colunas += 32 
            line_1 = pygame.draw.line( TELA , cor , ( colunas , 0), (  colunas , 600 ), larguraline )

        for i in range(1 , 30 ):
            lines += 32 
            line_2 = pygame.draw.line( TELA , cor , ( 0 , lines), (  1024 ,lines ), larguraline )

           


        pass


#-------------------------------------------------------------------------------
    def DrawElements(self):
        MousePos = pygame.mouse.get_pos()


        self.DrawGrid()


        self.player_1.draw( screen = TELA )
        self.player_1.playAction( speed_animation = 5 , orientation = "horizontal"  )
        self.player_1.position_x += 1 

       

       
        pass








    def runEvents(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pass



#-------------------------------------------------------------------------------

    def main(self):
        self.MouseB     = pygame.mouse.get_pressed()
        self.MousePos   = pygame.mouse.get_pos()
        self.keys       = pygame.key.get_pressed()
        #--------------------------------------------
        

        while GAMELOOP:
            delta_Timer = FPS.tick(60)
            TELA.fill( COLOR_SCREEN )
            self.runEvents()

           


            #self.player.update( screen = TELA )



            self.DrawElements()

            pygame.display.update()
        pygame.quit()  



#-------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    game = GameEngine()
    game.main()

#-------------------------------------------------------------------------------------------------------




