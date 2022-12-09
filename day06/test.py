import pytest
from solution import Part01

@pytest.mark.parametrize(
    "line, solution, answer",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", Part01(), 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", Part01(), 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", Part01(), 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", Part01(), 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", Part01(), 11),
    ]
)
def test_score(line, solution, answer):
    assert solution.main(line) == answer