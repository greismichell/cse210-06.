from constants import *
from game.scripting.action import Action


class ControlCatAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        cat = cast.get_first_actor(CAT_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            cat.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            cat.swing_right()  
        else: 
            cat.stop_moving()        