from projectile import Projectile
import math
def test_max_height():
    # analytical formula: h_max = h0 + (v * sin(angle))^2 / (2g)
    ball = Projectile(velocity=10.0, angle=90.0, initial_height=0.0, dt=0.01)
    expected = (10.0 ** 2) / (2 * 9.81)  # straight up shot, simplifies nicely
    assert abs(ball.get_max_height() - expected) < 0.01

def test_horizontal_distance_flat_ground():
    # at angle=45, v=10, h0=0: range = v^2 * sin(2*angle) / g
    ball = Projectile(velocity=10.0, angle=45.0, initial_height=0.0, dt=0.01)
    expected_range = (10.0 ** 2 * math.sin(math.radians(90))) / 9.81
    while ball.position[1] >= 0:
        ball.update_position(ball.dt)
    assert abs(ball.get_position()[0] - expected_range) < 0.1  # tolerance for dt discretization

def test_y_is_always_decreasing_after_peak():
    ball = Projectile(velocity=10.0, angle=45.0, initial_height=0.0, dt=0.01)
    positions = []
    while ball.position[1] >= 0:
        ball.update_position(ball.dt)
        positions.append(ball.get_position()[1])
    peak_idx = positions.index(max(positions))
    assert all(positions[i] >= positions[i+1] for i in range(peak_idx, len(positions)-1))