import pytest
from solution import Part01, Part02

"""
Fixtures
"""
@pytest.fixture()
def part01():
    return Part01()

@pytest.fixture()
def part02():
    return Part02()

"""
E2E test
"""
# @pytest.mark.parametrize(
#     "input_file, solution, answer",
#     [
#         ("sample.txt", Part01(), 157),
#         ("sample.txt", Part02(), 70)
#     ]
# )
# def test_main(input_file, solution, answer):
#     assert solution.main(solution.read_file(input_file)) == answer

"""
Unit test for positions
"""
@pytest.mark.parametrize(
    "head_position, tail_position, answer",
    [
        ((0,0), (0,0), True),
        ((0,0), (0,1), True),
        ((0,0), (1,0), True),
        ((0,0), (1,1), True),
        ((0,0), (0,2), False),
    ]
)
def test_part01_check_position(part01, head_position, tail_position, answer):
    assert part01.check_position(head_position, tail_position) == answer

@pytest.mark.parametrize(
    "head_position, tail_position, answer",
    [
        ((4,0), (3,0), False),
        ((4,1), (3,0), True),
        ((4,2), (4,1), False),
    ]
)
def test_part01_check_digonal(part01, head_position, tail_position, answer):
    assert part01.check_diagonal(head_position, tail_position) == answer

@pytest.mark.parametrize(
    "direction, start_positions, answer",
    [
        ("R", ((0,0),(0,0)), ((1,0),(0,0))),
        ("R", ((3,0),(2,0)), ((4,0),(3,0))),
        ("U", ((4,0),(3,0)), ((4,1),(3,0))),
        ("U", ((4,1),(3,0)), ((4,2),(4,1))),
        ("U", ((4,3),(4,2)), ((4,4),(4,3))),
        ("L", ((4,4),(4,3)), ((3,4),(4,3))),
        ("L", ((3,4),(4,3)), ((2,4),(3,4))),
        ("L", ((2,4),(3,4)), ((1,4),(2,4))),
        ("D", ((1,4),(2,4)), ((1,3),(2,4))),
    ]
)
def test_part01_change_state(part01, direction, start_positions, answer):
    assert part01.change_state(direction, *start_positions) == answer

@pytest.mark.parametrize(
    "direction, start_positions, answer",
    [
        ("R", [(0,0) for _ in range(10)], [(1,0)] + [(0,0) for _ in range(9)]),
        ("U", [(4,1), (3,0), (2,0), (1,0)] + [(0,0) for _ in range(6)], [(4,2), (4,1), (3,1), (2,1), (1,1)] + [(0,0) for _ in range(5)])
    ]
)
def test_part02_change_states(part02, direction, start_positions, answer):
    assert part02.change_states(direction, start_positions) == answer

@pytest.mark.parametrize(
    "direction, steps, start_positions, answer",
    [
        ("R", 5, [(0,0) for _ in range(10)], [(x,0) for x in range(5,0,-1)]+[(0,0) for _ in range(5)]),
        ("U", 8, [(x,0) for x in range(5,0,-1)]+[(0,0) for _ in range(5)], [(5,8), (5,7), (5,6), (5,5), (5,4), (4,4), (3,3), (2,2), (1,1), (0,0)]),
    ]
)
def test_part02_change_states_with_steps(part02, direction, steps, start_positions, answer):
    for _ in range(steps):
        start_positions = part02.change_states(direction, start_positions)
    assert start_positions == answer