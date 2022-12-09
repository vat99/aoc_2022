import pytest
from solution import Part01, Part02

@pytest.mark.parametrize(
    "line, solution, answer",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", Part01(), 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", Part01(), 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", Part01(), 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", Part01(), 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", Part01(), 11),
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", Part02(), 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", Part02(), 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", Part02(), 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", Part02(), 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", Part02(), 26),
    ]
)
def test_score(line, solution, answer):
    assert solution.main(line) == answer