from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideGrassAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        mush = cast.get_first_actor(MUSH_GROUP)
        grass = cast.get_first_actor(GRASS_GROUP)
        
        mush_body = mush.get_body()
        grass_body = grass.get_body()

        if self._physics_service.has_collided(mush_body, grass_body):
            mush.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    