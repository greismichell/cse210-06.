from constants import *
from game.scripting.action import Action


class MoveDropAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        drop = cast.get_first_actor(DROP_GROUP)
        body = drop.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
