# OOP projectile motion
import math

class Particle(object):
    def __init__(self):
        self.position = [0,0]

class Projectile(Particle):
    def __init__(self, mass, velocity, angle, initial_height):
        super().__init__()
        self.mass = mass
        self.velocity = velocity
        self.angle = angle
        self.position = [0,0]
        self.initial_height = initial_height
        self.time = 0
        self.g = -9.81

    def update_position(self, dt):
        self.time += dt
        self.position[0] = self.velocity * math.cos(math.radians(self.angle)) * self.time
        self.position[1] = self.initial_height + (self.velocity * math.sin(math.radians(self.angle)) * self.time) + (0.5 * self.g * self.time ** 2)

    def get_position(self):
        return self.position
    
ball = Projectile(mass=1, velocity=10, angle=45, initial_height=10)
print(ball.get_position())
while ball.position[1] >= 0:
    ball.update_position(0.1)
print(ball.get_position())

