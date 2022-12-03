from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideFoodAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        mush = cast.get_first_actor(MUSH_GROUP)
        foods = cast.get_actors(FOOD_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for brick in foods:
            mush_body = mush.get_body()
            food_body = brick.get_body()

            if self._physics_service.has_collided(mush_body, food_body):
                mush.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(FOOD_GROUP, brick)