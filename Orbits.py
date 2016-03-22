import math
import turtle

"""
    Sources: https://en.wikipedia.org/wiki/N-body_problem
"""

G = 1
list_of_bodies = []

class OrbitingBody(turtle.Turtle):

    """
    An orbiting body simulates a mass in space

    Attributes:
        name    The name of the body
        mass    The mass of the body
        pos_x   The current x-coordinate of the body
        pos_y   The current y-coordinate of the body


    """

    name = ""
    mass = 0.0
    pos_x, pos_y = 0.0
    vel_x, vel_y = 0.0

    def gravitational_attaction(self, other_body):

        """
        Returns the x,y-forces of attraction caused by a body other than the current body
        :param other_body:
        :return: fg_x, fg_y
        """

        dx = self.pos_x - other_body.pos_x
        dy = self.pos_y - other_body.pos_y
        d = math.sqrt(dy ** 2 + dx ** 2)

        f = G * self.mass * other_body.mass / (d**2)

        angle = math.atan2(dy, dx)
        fg_x = math.cos(angle) * f
        fg_y = math.sin(angle) * f

        return fg_x, fg_y






def main():
    print("test")

if __name__ == '__main__':
    main()
