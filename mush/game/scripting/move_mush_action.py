from constants import *
from game.scripting.action import Action


class MoveMushAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        mush = cast.get_first_actor(MUSH_GROUP)
        body = mush.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
