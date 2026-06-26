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

if __name__ == "__main__":
    ball = Projectile(velocity=10.0, angle=45.0, initial_height=10.0, dt=0.01)
    print(f"Initial x, y: {ball.get_position()} (m)")

    x_positions = [ball.get_position()[0]]
    y_positions = [ball.get_position()[1]]

    while ball.position[1] >= 0:
        ball.update_position(ball.dt)
        x_positions.append(ball.get_position()[0])
        y_positions.append(ball.get_position()[1])

    print(f"Final x, y: ...")

    fig, ax = plt.subplots(figsize=(8, 5))  # <-- moves in here
    ax.plot(x_positions, y_positions)
    plt.show()
