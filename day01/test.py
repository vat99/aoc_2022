import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

test_read_cases = [
    ("sample.txt", [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]),
]

@pytest.mark.parametrize(
    "test_case", test_read_cases
)
def test_read(solution, test_case):
    assert solution.read_input(test_case[0]) == test_case[1]

test_cases_part_1 = [
    ("sample.txt", 24000),
]

@pytest.mark.parametrize(
    "test_case", test_cases_part_1
)
def test_part_1(solution, test_case):
    assert solution.part01(test_case[0]) == test_case[1]