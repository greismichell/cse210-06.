from constants import *
from game.scripting.action import Action


class DrawCatAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        cat = cast.get_first_actor(CAT_GROUP)
        body = cat.get_body()

        if cat.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        
        animation = cat.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)