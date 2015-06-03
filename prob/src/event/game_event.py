
import random
import pygame
from consts import *
from event.base_event import *
from event.io_event import *
from event.ui_event import *

class EventCheckSnake( BaseEvent ):
    def __init__( self , env , priority ):
        self.env      = env
        self.priority = priority
        self.snake = self.env[ "snake" ]
        self.foods = self.env[ "foods" ]

    def check_is_dead( self ):
        # TODO
        pass

    def do_add_head( self ):
        # TODO
        pass

    def do_eat_foods( self ):
        # TODO
        pass

    def do_move( self ):
        # TODO
        pass

    def do_action( self ):
        if self.check_is_dead():
            self.env[ "pyQUIT" ] = True
            self.env[ "gamec" ].add_event( EventEndGame( self.env , self.priority + TICKS_PER_TURN ) )
            return

        # TODO

        self.env[ "gamec" ].add_event( EventCheckSnake( self.env , self.priority + TICKS_PER_TURN ) )

class EventAddFood( BaseEvent ):
    def __init__( self , env , priority ):
        self.env      = env
        self.priority = priority
        self.foods    = self.env[ "foods" ]
        self.snake    = self.env[ "snake" ]

    def do_action( self ):

        if len( self.foods ) > 40:
            self.env[ "gamec" ].add_event( EventAddFood( self.env , self.priority + FOOD_ADD_TIME ) )

        # TODO

        self.env[ "gamec" ].add_event( EventAddFood( self.env , self.priority + FOOD_ADD_TIME ) )

class EventStartGame( BaseEvent ):
    def __init__( self , env , random_seed , priority ):
        self.env = env
        self.random_seed = random_seed
        self.priority = priority

    def do_action( self ):
        random.seed( self.random_seed )
        self.env[ "dir" ] = ( 1 , 0 )
        self.env[ "snake" ] = [ ( 200 , 200 ) ]
        self.env[ "foods" ] = []
        self.env[ "pyQUIT" ] = False
        self.env[ "gamec" ].add_event( EventCheckSnake( self.env , self.priority + 300 ) )
        self.env[ "gamec" ].add_event( EventAddFood( self.env , self.priority + 300 + FOOD_ADD_TIME ) )
        self.env[ "uic" ].add_event( EventClearInit( self.env , self.priority ) )
        self.env[ "uic" ].add_event( EventDrawInit( self.env , self.priority ) )
        self.env[ "uic" ].add_event( EventIOEvent( self.env , self.priority + 300) )

class EventEndGame( BaseEvent ):
    def __init__( self , env , priority ):
        self.env = env
        self.priority = priority

    def do_action( self ):
        self.env[ "uic" ].stop()
        self.env[ "gamec" ].stop()

