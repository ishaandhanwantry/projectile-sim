from projectile import Projectile
import math
import pytest
def test_time_increases():
    ball = Projectile(velocity=10.0, angle=45.0, initial_height=0.0, dt=0.01)
    ball.update_position(ball.dt)
    assert ball.get_time() == pytest.approx(0.01)

def test_time_accumulates():
    ball = Projectile(velocity=10.0, angle=45.0, initial_height=0.0, dt=0.01)
    for _ in range(5):
        ball.update_position(ball.dt)
    assert ball.get_time() == pytest.approx(0.05)