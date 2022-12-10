from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body


class FishCollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        fish = cast.get_first_actor(FISH_GROUP)
        body = fish.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
                
        if x < FIELD_LEFT:
            fish.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - FISH_WIDTH):
            fish.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            fish.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - FISH_HEIGHT):
            fish.bounce_y()
            self._audio_service.play_sound(bounce_sound)  
            