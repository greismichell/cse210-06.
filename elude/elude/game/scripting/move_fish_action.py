from constants import *
from game.scripting.action import Action


class MoveFishAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        fish = cast.get_first_actor(FISH_GROUP)
        body = fish.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)