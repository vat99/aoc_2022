import pytest
from solution import Part01

"""
Fixtures
"""
@pytest.fixture()
def part01():
    return Part01()  

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