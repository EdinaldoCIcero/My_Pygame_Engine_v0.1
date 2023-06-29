import pygame
import pygame.math

#----------------------------------------------------------
from scripts.globals.globalD import *
from scripts.globals.globals_vars import *
from scripts.system.py_gameObjects import PY_gameObjects

from scripts.system.inputKeys import InputKeysSystem
#from scripts.system.SpriteSheetSystem import SpriteAnimations

#----------------------------------------------------------





class PlayerController( PY_gameObjects ):
    def __init__(self  ):
        super().__init__()

        self.inputs_keys = InputKeysSystem()

        self.scale_X     = 400
        self.scale_Y     = 400


        #self.obj_rect = self.getRectObject( object_to_rect  = self.surf_sprite , 
                                           # positions       = [ 0 , 0 ] , 
                                           # scales          = [ self.scale_X  , self.scale_Y ]
                                           # )



        self.Center_X = LARGURA - self.obj_rect.center[0]
        self.Center_Y = ALTURA  - self.obj_rect.center[1]


        self.time           = 0
        self.frame          = 1

        self.SpeedMove  = 3
        self.vida       = 100
        self.Pos_X      = 0
        self.Pos_Y      = 0 

        

    def FrameTimeSprites(self):## Troca de FrameTimeSprites #######
        if self.time == 6:
            self.time  = 1
            self.frame += 1
        if self.frame >= 9:
            self.frame = 1
      

    def MovePlayer(self): ###### Movimentação do Player ######
        self.keys           = pygame.key.get_pressed()
        self.MousePos       = pygame.mouse.get_pos()
        self.mx , self.my   = pygame.mouse.get_pos()
        self.MouseB         = pygame.mouse.get_pressed()
        #----------------------------------------------------
        self.keys_bo = self.inputs_keys.inputsKeyboards()
        

        #if self.rect.collidepoint(self.MousePos) and self.MouseB[0]:
          #  self.rect.center = self.MousePos
          #  self.Pos_X = self.mx
          #  self.Pos_Y = self.my

       # else:


        if self.keys_bo["e"]:
            self.WorldPositions(  positions = [ 80 , 80 ] )
            print("Aqui E ")
        
        
        if self.keys_bo["w"]:
            self.Pos_Y -= self.SpeedMove
            
            self.WorldPositions(  positions = [ 80 , self.Pos_Y ] )
           


        self.applyMovement( vector = [ 2 , -2 ] )
        



    def ColisionPlayer(self , Object): #Logicas do Player 
        self.keys = pygame.key.get_pressed()
        self.MousePos = pygame.mouse.get_pos()
        self.mx , self.my = pygame.mouse.get_pos()
        self.MouseB = pygame.mouse.get_pressed()


        #self.ColidList = pygame.Rect.collidelist(Object)
        self.ColisionCasas = pygame.sprite.spritecollide( self , Object , False)

        if self.ColisionCasas:
            pass



    def LogicsPlayer(self , tela ): #Logicas do Player 
        self.keys = pygame.key.get_pressed()
        self.MousePos = pygame.mouse.get_pos()
        self.mx , self.my = pygame.mouse.get_pos()
        self.MouseB = pygame.mouse.get_pressed()

        #self.BarraVidaPlayer = pygame.Rect(( self.rect[0] - 20 , self.rect[1] -15 ), ( self.vida , 5))
        #tela.fill( [48,52,55] , self.BarraVidaPlayer)

        #self.DanoInimigo = pygame.sprite.spritecollide( P , GrupoDano , False)

        #if self.DanoInimigo:
            #self.vida -= 1
        pass


    def update( self , screen  ):
        #self.FrameTimeSprites()
       

        self.MovePlayer()
        
        #self.LogicsPlayer()
        #self.ColisionPlayer(Object)


        pass
