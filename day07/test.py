import pytest
from solution import Part01

@pytest.mark.parametrize(
    "fname, solution, answer",
    [
        ("sample.txt", Part01(), {'/': 48381165, 'a': 94853, 'e': 584, 'd': 24933642}),
    ]
)
def test_parse(fname, solution, answer):
    assert solution.parse(fname) == answer