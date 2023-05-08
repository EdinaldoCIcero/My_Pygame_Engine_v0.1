
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


from scripts.globals.globalD import *
from scripts.player.libs.PlayerControll import PlayerController

#---------------------------------------------
pygame.init()




TELA             = pygame.display.set_mode([LARGURA , ALTURA])# , pygame.RESIZABLE
pygame.mouse.set_visible(True)
pygame.display.set_caption("<Display-Game-Engine>")
#pygame.display.set_icon( )

#player_sheet_sprite = PlayerController( filename_img = "doux.png")



#---------------------------------------------
class GameEngine():
    def __init__(self):
        super().__init__()

        self.player_sheet_sprite = PlayerController( filename_img = "assets/sprites/characters/player/dino_run_sheet.png" )

        

    
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


        self.player_sheet_sprite.playerUpdate( screen = TELA)
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


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #if event.type == VIDEORESIZE:
                   # screen = pygame.display.set_mode([event.w , event.h] , pygame.RESIZABLE)


               
          




            self.DrawElements()
            pygame.display.update()
        pygame.quit()  

#-------------------------------------------------------------------------------------------------------

game = GameEngine()
game.main()

#-------------------------------------------------------------------------------------------------------




