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
        mass    The mass of the body in kg
        pos_x   The current x-coordinate of the body
        pos_y   The current y-coordinate of the body


    """

    name = ""
    mass = 0.0
    pos_x, pos_y = 0.0, 0.0
    vel_x, vel_y = 0.0, 0.0

    def step(self):

        """
        Updates the pos for 1 step
        :return: Null
        """

        self.pos_x += self.vel_x
        self.pos_y += self.vel_y

        self.setx(self.pos_x)
        self.sety(self.pos_y)

        return None

    def g_attraction(self, other_body):

        """
        Returns the x,y-forces of attraction caused by a body other than the current body
        :param other_body:
        :return: fg_x, fg_y
        """

        if self == other_body:
            raise ValueError('Should not compute the gravitational attraction from itself')

        dx = self.pos_x - other_body.pos_x
        dy = self.pos_y - other_body.pos_y
        d = math.sqrt(dy ** 2 + dx ** 2)

        f = G * self.mass * other_body.mass / (d**2)

        angle = math.atan2(dy, dx)
        fg_x = math.cos(angle) * f
        fg_y = math.sin(angle) * f

        return fg_x, fg_y






def Update(Body, Bodies):

   """
   :param Body:
   :param Bodies:
   :return:
   """

   totalfx = 0.0
   totalfy = 0.0

   for OrbitingBody in Bodies:

       if OrbitingBody == Body:
           continue

       fx, fy = Body.g_attraction(OrbitingBody)
       totalfx += fx
       totalfy += fy

   dvx = totalfx / Body.mass
   dvy = totalfy / Body.mass
   Body.vel_x += dvx
   Body.vel_y += dvy

   Body.step()



def Play(Bodies):
    while True:
        for Body in Bodies:
            Update(Body, Bodies)








def main():


    Sun = OrbitingBody()
    Sun.mass = 100.0
    Sun.pos_x = 0.0
    Sun.pos_y = 0.0
    Sun.vel_x = 0.0
    Sun.vel_y = 0.0

    Earth = OrbitingBody()
    Earth.mass = 1.0
    Earth.pos_x = 100.0
    Earth.pos_y = 100.0
    Earth.vel_x = 3.0
    Earth.vel_y = 4.0

    list_of_bodies.append(Sun)
    list_of_bodies.append(Earth)

    Play(list_of_bodies)




if __name__ == '__main__':
    main()
