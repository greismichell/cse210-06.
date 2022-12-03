from constants import *
from game.scripting.action import Action


class DrawFoodsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        foods = cast.get_actors(FOOD_GROUP)
        
        for food in foods:
            body = food.get_body()

            if food.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = food.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)