import pygame

from scripts.globals.globalD import *


class InputKeysSystem():
    def __init__( self ):


        pass


    def inputsKeyboards( self ):
        self.keys           = pygame.key.get_pressed()
        self.MousePos       = pygame.mouse.get_pos()
        self.mx , self.my   = pygame.mouse.get_pos()
        #----------------------------------------------------
        
        return {
            "a" : self.keys[pygame.K_a] ,
            "b" : self.keys[pygame.K_b] ,
            "c" : self.keys[pygame.K_c] ,
            "d" : self.keys[pygame.K_d] ,
            "e" : self.keys[pygame.K_e] ,
            "f" : self.keys[pygame.K_f] ,

            "g" : self.keys[pygame.K_g] ,
            "h" : self.keys[pygame.K_h] ,
            "i" : self.keys[pygame.K_i] ,
            "j" : self.keys[pygame.K_j] ,
            "k" : self.keys[pygame.K_k] ,

            "l" : self.keys[pygame.K_l] ,
            "m" : self.keys[pygame.K_m] ,
            "n" : self.keys[pygame.K_n] ,
            "o" : self.keys[pygame.K_o] ,
            "p" : self.keys[pygame.K_p] ,

            "q" : self.keys[pygame.K_q] ,
            "r" : self.keys[pygame.K_r] ,
            "s" : self.keys[pygame.K_s] ,
            "t" : self.keys[pygame.K_t] ,

            "u" : self.keys[pygame.K_u] ,
            "v" : self.keys[pygame.K_v] ,
            "w" : self.keys[pygame.K_w] ,
            "x" : self.keys[pygame.K_x] ,
            "y" : self.keys[pygame.K_y] ,
            "z" : self.keys[pygame.K_z] ,


            "backspace" : self.keys[pygame.K_BACKSPACE],
            "tab"       : self.keys[pygame.K_TAB],
            "clear"     : self.keys[pygame.K_CLEAR],
            "return"    : self.keys[pygame.K_RETURN],
            "pause"     : self.keys[pygame.K_PAUSE],
            "escape"    : self.keys[pygame.K_ESCAPE],
            "space"     : self.keys[pygame.K_SPACE],
            "exclaim"   : self.keys[pygame.K_EXCLAIM],
            "quotedbl"  : self.keys[pygame.K_QUOTEDBL],
            "hash"      : self.keys[pygame.K_HASH],
            "dollar"    : self.keys[pygame.K_DOLLAR],
            "ampersand" : self.keys[pygame.K_AMPERSAND],
            "quote"     : self.keys[pygame.K_QUOTE],
            "leftparen" : self.keys[pygame.K_LEFTPAREN],
            "rightparen": self.keys[pygame.K_RIGHTPAREN],
            "asterisk"  : self.keys[pygame.K_ASTERISK],
            "plus"      : self.keys[pygame.K_PLUS],
            "comma"     : self.keys[pygame.K_COMMA],
            "minus"     : self.keys[pygame.K_MINUS],
            "period"    : self.keys[pygame.K_PERIOD],
            "slash"     : self.keys[pygame.K_SLASH ],

            #------------------------------------------------
            "0" : self.keys[ pygame.K_0 ] ,
            "1" : self.keys[ pygame.K_1 ] ,
            "2" : self.keys[ pygame.K_2 ] ,
            "3" : self.keys[ pygame.K_3 ] ,
            "4" : self.keys[ pygame.K_4 ] ,
            "5" : self.keys[ pygame.K_5 ] ,
            "6" : self.keys[ pygame.K_6 ] ,
            "7" : self.keys[ pygame.K_7 ] ,
            "8" : self.keys[ pygame.K_8 ] ,
            "9" : self.keys[ pygame.K_9 ] ,
            
            "colon"         : self.keys[pygame.K_COLON],
            "semicolon"     : self.keys[pygame.K_SEMICOLON],
            "less"          : self.keys[pygame.K_LESS],
            "equals"        : self.keys[pygame.K_EQUALS],
            "greater"       : self.keys[pygame.K_GREATER],
            "question"      : self.keys[pygame.K_QUESTION],
            "at"            : self.keys[pygame.K_AT],
            "leftbracket"   : self.keys[pygame.K_LEFTBRACKET],
            "backslash"     : self.keys[pygame.K_BACKSLASH],
            "rightbracket"  : self.keys[pygame.K_RIGHTBRACKET],
            "caret"         : self.keys[pygame.K_CARET],
            "underscore"    : self.keys[pygame.K_UNDERSCORE],
            "bakcquote"     : self.keys[pygame.K_BACKQUOTE],
            "delete"        : self.keys[pygame.K_DELETE],


            "keypad_0"  : self.keys[pygame.K_KP0],
            "keypad_1"  : self.keys[pygame.K_KP1],
            "keypad_2"  : self.keys[pygame.K_KP2],
            "keypad_3"  : self.keys[pygame.K_KP3],
            "keypad_4"  : self.keys[pygame.K_KP4],
            "keypad_5"  : self.keys[pygame.K_KP5],
            "keypad_6"  : self.keys[pygame.K_KP6],
            "keypad_7"  : self.keys[pygame.K_KP7],
            "keypad_8"  : self.keys[pygame.K_KP8],
            "keypad_9"  : self.keys[pygame.K_KP9],


            "keypad_period"     : self.keys[pygame.K_KP_PERIOD],
            "keypad_divide"     : self.keys[pygame.K_KP_DIVIDE],
            "keypad_multiply"   : self.keys[pygame.K_KP_MULTIPLY],
            "keypad_minus"      : self.keys[pygame.K_KP_MINUS],
            "keypad_plus"       : self.keys[pygame.K_KP_PLUS],
            "keypad_enter"      : self.keys[pygame.K_KP_ENTER],
            "keypad_equals"     : self.keys[pygame.K_KP_EQUALS],

            "up_arrow"      : self.keys[pygame.K_UP],
            "down_arrow"    : self.keys[pygame.K_DOWN],
            "right_arrow"   : self.keys[pygame.K_RIGHT],
            "left_arrow"    : self.keys[pygame.K_LEFT],

            "insert"    : self.keys[pygame.K_INSERT],
            "home"      : self.keys[pygame.K_HOME],
            "end"       : self.keys[pygame.K_END],
            "page_up"   : self.keys[pygame.K_PAGEUP],
            "page_down" : self.keys[pygame.K_PAGEDOWN],

            "F1"    : self.keys[pygame.K_F1],
            "F2"    : self.keys[pygame.K_F2],
            "F3"    : self.keys[pygame.K_F3],
            "F4"    : self.keys[pygame.K_F4],
            "F5"    : self.keys[pygame.K_F5],
            "F6"    : self.keys[pygame.K_F6],
            "F7"    : self.keys[pygame.K_F7],
            "F8"    : self.keys[pygame.K_F8],
            "F9"    : self.keys[pygame.K_F9],
            "F10"   : self.keys[pygame.K_F10],
            "F11"   : self.keys[pygame.K_F11],
            "F12"   : self.keys[pygame.K_F12],
            "F13"   : self.keys[pygame.K_F13],
            "F14"   : self.keys[pygame.K_F14],
            "F15"   : self.keys[pygame.K_F15],


            "numlock"   : self.keys[pygame.K_NUMLOCK],
            "capslock"   : self.keys[pygame.K_CAPSLOCK],
            "scrollock"   : self.keys[pygame.K_SCROLLOCK],
            "right_shift"   : self.keys[pygame.K_RSHIFT],
            "left_shift"   : self.keys[pygame.K_LSHIFT],
            "right_control"   : self.keys[pygame.K_RCTRL],
            "left_control"   : self.keys[pygame.K_LCTRL],
            "right_alt"   : self.keys[pygame.K_RALT],

            "left_alt"   : self.keys[pygame.K_LALT],
            "right_meta"   : self.keys[pygame.K_RMETA],
            "left_meta"   : self.keys[pygame.K_LMETA],
            "left_Windows_key"   : self.keys[pygame.K_LSUPER],
            "right_Windows_key"   : self.keys[pygame.K_RSUPER],
            "mode_shift"   : self.keys[pygame.K_MODE],
            "help"   : self.keys[pygame.K_HELP],
            "print_screen"   : self.keys[pygame.K_PRINT],


            "sysrq"                 : self.keys[pygame.K_SYSREQ],
            "break"                 : self.keys[pygame.K_BREAK],
            "menu"                  : self.keys[pygame.K_MENU],
            "power"                 : self.keys[pygame.K_POWER],
            "euro"                  : self.keys[pygame.K_EURO],
            "Android_back_button"   : self.keys[pygame.K_AC_BACK],

             
            
         

        }


        pass
