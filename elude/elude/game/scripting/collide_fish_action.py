from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideFishAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        cat = cast.get_first_actor(CAT_GROUP)
        fish = cast.get_first_actor(FISH_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        cat_body = cat.get_body()
        fish_body = fish.get_body()

        if self._physics_service.has_collided(cat_body, fish_body):
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            points = fish.get_points()
            stats.add_points(points)
            cast.remove_actor(FISH_GROUP, fish)

        
