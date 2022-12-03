from constants import *
from game.scripting.action import Action


class ControlGrassAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        grass = cast.get_first_actor(GRASS_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            grass.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            grass.swing_right()  
        else: 
            grass.stop_moving()        