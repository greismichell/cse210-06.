from constants import *
from game.scripting.action import Action


class DrawMushAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        mush = cast.get_first_actor(MUSH_GROUP)
        body = mush.get_body()

        if mush.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = mush.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)