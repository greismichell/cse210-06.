from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.body import Body


class CollideBordersAction2(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        drop = cast.get_first_actor(DROP_GROUP)
        body = drop.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)

        if x < FIELD_LEFT:
            drop.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - DROP_WIDTH):
            drop.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            drop.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - DROP_HEIGHT):
            drop.bounce_y()
            self._audio_service.play_sound(bounce_sound)  
            