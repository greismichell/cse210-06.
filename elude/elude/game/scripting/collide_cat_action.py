from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideCatAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        drop = cast.get_first_actor(DROP_GROUP)
        cat = cast.get_first_actor(CAT_GROUP)
        over_sound = Sound(OVER_SOUND)
        
        drop_body = drop.get_body()
        cat_body = cat.get_body()

        if self._physics_service.has_collided(drop_body, cat_body):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()
            
            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)
             