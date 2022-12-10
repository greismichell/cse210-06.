from constants import *
from game.scripting.action import Action

class DrawFishAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        fish = cast.get_first_actor(FISH_GROUP)
        body = fish.get_body()

        if fish.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = fish.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)