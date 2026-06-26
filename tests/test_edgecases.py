from projectile import Projectile
import math
def test_90_degree_angle():
    # straight up — x should stay ~0
    ball = Projectile(velocity=10.0, angle=90.0, initial_height=0.0, dt=0.01)
    while ball.position[1] >= 0:
        ball.update_position(ball.dt)
    assert abs(ball.get_position()[0]) < 0.01

def test_zero_velocity():
    # with no velocity, ball should just fall from initial height
    ball = Projectile(velocity=0.0, angle=45.0, initial_height=10.0, dt=0.01)
    while ball.position[1] >= 0:
        ball.update_position(ball.dt)
    assert abs(ball.get_position()[0]) < 0.01  # no horizontal motion