# OOP projectile motion
import math
import numpy as np
import matplotlib.pyplot as plt

class Particle(object):
    def __init__(self):
        self.position = [0.0, 0.0]

class Projectile(Particle):
    def __init__(self, velocity, angle, initial_height, dt):
        super().__init__()
        self.velocity = velocity
        self.angle = angle
        self.initial_height = initial_height
        self.position = [0.0, initial_height]
        self.time = 0.0
        self.dt = dt
        self.g = -9.81

    def update_position(self, dt):
        self.time += dt
        self.position[0] = self.velocity * math.cos(math.radians(self.angle)) * self.time
        self.position[1] = self.initial_height + (self.velocity * math.sin(math.radians(self.angle)) * self.time) + (0.5 * self.g * self.time ** 2)

    def get_position(self):
        return tuple(self.position)
    
    def get_time(self):
        return self.time
    
    def get_max_height(self):
        return self.initial_height + (self.velocity ** 2 * (math.sin(math.radians(self.angle))) ** 2) / (2 * -self.g)

# Input Parameters    
ball = Projectile(velocity=10.0, angle=45.0, initial_height=10.0, dt=0.1)
print(f"Initial x, y: {ball.get_position()} (m)")

while ball.position[1] >= 0:
     
    last_position = ball.get_position()
    last_time = ball.get_time()
    
    ball.update_position(ball.dt)

# Output final position, time, and max height
print(f"Final x, y: ({ball.get_position()[0]:.2f}, {ball.get_position()[1]:.2f}) (m)")
print(f"Travel time: {ball.get_time():.2f} s")
print(f"Max height: {ball.get_max_height():.2f} m")
