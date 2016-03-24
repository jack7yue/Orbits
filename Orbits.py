import math
import turtle

"""
    Sources: https://en.wikipedia.org/wiki/N-body_problem
"""

G = 1e-2
list_of_bodies = []


class OrbitingBody(turtle.Turtle):

    """
    An orbiting body simulates a mass in space

    Attributes:
        name    The name of the body
        mass    The mass of the body in kg
        pos_x   The current x-coordinate of the body
        pos_y   The current y-coordinate of the body


    """

    name = ""
    mass = 0.0
    pos_x, pos_y = 0.0, 0.0
    vel_x, vel_y = 0.0, 0.0

    def acceleration(self, other_body):

        """
        Returns the x,y-acceleration caused by the body affecting the current one
        :param other_body:
        :return: fg_x, fg_y
        """

        # Finding the distance vector and magnitude
        dx = other_body.pos_x - self.pos_x
        dy = other_body.pos_y - self.pos_y
        d = math.sqrt(dy ** 2 + dx ** 2)

        # If distance is zero, there will be a division by zero error
        if d == 0:
            raise ValueError("Distance cannot be zero, will result in division by zero")

        # Using Newton's Law of Universal Gravitation
        a = G * other_body.mass / (d**2)
        angle = math.atan2(dy, dx)
        ax = math.cos(angle) * a
        ay = math.sin(angle) * a

        return ax, ay


def update(bodies):

    """
    Updates the positions of the bodies using the Euler method
    :param bodies: A list of all the bodies in the system
    :return: None
    """

    while True:

        for Body in bodies:

            Body.penup()
            # Removes the trails from the turtles. This can be removed along with pendown() to see the trails

            net_ax, net_ay = 0.0, 0.0
            # Computing all the forces before performing operations

            for OtherBody in bodies:

                # Avoid gravitational attraction with itself (will result in division by zero)
                if Body == OtherBody:
                    continue

                ax, ay = Body.acceleration(OtherBody)
                net_ax += ax
                net_ay += ay

                dvx = net_ax
                dvy = net_ay

                Body.vel_x += dvx
                Body.vel_y += dvy
                Body.pos_x += Body.vel_x
                Body.pos_y += Body.vel_y

                Body.goto(Body.pos_x, Body.pos_y)
            Body.pendown()


def main():

    # The bodies are drawn using turtle so any changes to them can be adjusted with turtle

    turtle.bgcolor("black")
    turtle.speed(0)

    sun = OrbitingBody()
    sun.shapesize(2)
    sun.mass = 20000
    sun.color("yellow")
    sun.shape("circle")
    sun.name = "SUN"

    earth = OrbitingBody()
    earth.shapesize(0.1)
    earth.color("green")
    earth.shape("circle")
    earth.name = "EARTH"
    earth.mass = 1
    earth.pos_x = 150.0
    earth.vel_y = 1.25
    earth.vel_x = 0

    mars = OrbitingBody()
    mars.shapesize(.1)
    mars.shape("circle")
    mars.color("red")
    mars.name = "Mars"
    mars.mass = 1
    mars.pos_x = -150.0
    mars.vel_y = -1
    mars.vel_x = 0


    update([sun, earth, mars])

if __name__ == '__main__':
    main()
