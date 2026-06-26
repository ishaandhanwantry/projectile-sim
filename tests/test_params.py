from projectile import Projectile
import math
def test_initial_position():
    ball = Projectile(velocity=10.0, angle=45.0, initial_height=5.0, dt=0.01)
    assert ball.get_position() == (0.0, 5.0)

def test_zero_initial_height():
    ball = Projectile(velocity=10.0, angle=45.0, initial_height=0.0, dt=0.01)
    assert ball.get_position()[1] == 0.0