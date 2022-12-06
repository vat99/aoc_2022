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
@pytest.mark.parametrize(
    "input_file, solution, answer",
    [
        ("sample.txt", Part01(), 157),
        ("sample.txt", Part02(), 70)
    ]
)
def test_main(input_file, solution, answer):
    assert solution.main(solution.read_file(input_file)) == answer

"""
Unit test for score
"""
@pytest.mark.parametrize(
    "line, answer",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", ("vJrwpWtwJgWr", "hcsFMMfFFhFp")),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")),
        ("PmmdzqPrVvPwwTWBwg", ("PmmdzqPrV", "vPwwTWBwg"))
    ]
)
def test_part01_split(part01, line, answer):
    assert part01._split_line(line) == answer

@pytest.mark.parametrize(
    "lines, answer",
    [
        (["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"], "r"),
        (["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"], "Z")
    ]
)
def test_part02_find_common_letters(part02, lines, answer):
    assert part02.find_common_letter(lines) == answer

@pytest.mark.parametrize(
    "compartments, answer",
    [
        (("vJrwpWtwJgWr", "hcsFMMfFFhFp"), "p"),
        (("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"), "L"),
        (("PmmdzqPrV", "vPwwTWBwg"), "P"),
    ]
)
def test_part01_find_common_letters(part01, compartments, answer):
    assert part01.find_common_letter(*compartments) == answer

letter_priority_test_cases = [
    ("p", 16),
    ("L", 38),
    ("P", 42),
    ("v", 22),
    ("a", 1),
    ("t", 20),
    ("s", 19),
    ("A", 27)
]

letter_priority_test_cases = [(solution, *item) for item in letter_priority_test_cases for solution in [Part01(), Part02()]]

@pytest.mark.parametrize(
    "solution, letter, answer",
    letter_priority_test_cases
)
def test_letter_priority(solution, letter, answer):
    assert solution.get_letter_priority(letter) == answer