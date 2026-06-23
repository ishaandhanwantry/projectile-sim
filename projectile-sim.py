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
        self.initial_height = initial_height
        self.position = [0, initial_height]
        self.time = 0
        self.g = -9.81

    def update_position(self, dt):
        self.time += dt
        self.position[0] = self.velocity * math.cos(math.radians(self.angle)) * self.time
        self.position[1] = self.initial_height + (self.velocity * math.sin(math.radians(self.angle)) * self.time) + (0.5 * self.g * self.time ** 2)

    def get_position(self):
        return self.position
    
    def get_time(self):
        return self.time
    
    def get_max_height(self):
        return self.initial_height + (self.velocity ** 2 * (math.sin(math.radians(self.angle))) ** 2) / (2 * -self.g)
    
ball = Projectile(mass=1, velocity=10, angle=45, initial_height=10)
print(f"initial x, y: {ball.get_position()}(m)")
while ball.position[1] >= 0:
    ball.update_position(0.1)
print(f"x, y: {ball.get_position()}(m),", f"travel time: {ball.get_time()}s,", f"max height: {ball.get_max_height()}m")

