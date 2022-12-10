from constants import *
from game.scripting.action import Action


class DrawDropAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        drop = cast.get_first_actor(DROP_GROUP)
        body = drop.get_body()

        if drop.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = drop.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)