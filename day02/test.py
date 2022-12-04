import pytest
from solution import Part01, Part02

"""
E2E test
"""
@pytest.mark.parametrize(
    "input_file, solution, answer",
    [("sample.txt", Part01(), 15), ("sample.txt", Part02(), 12)]
)
def test_main(input_file, solution, answer):
    assert solution.main(solution.read_file(input_file)) == answer

"""
Unit test for score
"""
@pytest.mark.parametrize(
    "options, solution, answer",
    [
        (['A', 'Y'], Part01(), 8),
        (['B', 'X'], Part01(), 1),
        (['C', 'Z'], Part01(), 6),
        (['A', 'Y'], Part02(), 4),
        (['B', 'X'], Part02(), 1),
        (['C', 'Z'], Part02(), 7),
    ]
)
def test_score(options, solution, answer):
    assert solution.get_score(options) == answer