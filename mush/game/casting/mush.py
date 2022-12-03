import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Mush(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def bounce_x(self):
        """Bounces the ball in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the ball in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def release(self):
        """Release the ball in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-MUSH_VELOCITY * rn, MUSH_VELOCITY * rn])
        vy = -MUSH_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)