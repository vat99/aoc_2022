import pytest
from solution import Part01, Part02, Interval

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
        ("sample.txt", Part01(), 2),
        ("sample.txt", Part02(), 4),
    ]
)
def test_main(input_file, solution, answer):
    assert solution.main(solution.read_file(input_file)) == answer

"""
Unit tests
"""
@pytest.mark.parametrize(
    "solution, line, answer",
    [
        (Part01(), "2-4,6-8", ((Interval("2-4"),Interval("6-8")))),
        (Part01(), "52-53,53-98", ((Interval("52-53"),Interval("53-98")))),
        #(Part02(), "2-4,6-8", ((Interval("2-4"),Interval("6-8")))),
    ]
)
def test_solution_parse_line(solution, line, answer):
    assert solution.parse_line(line) == answer

    pair_a = (Interval("0-0"),Interval("1-1"))
    pair_b = (Interval("0-0"),Interval("1-1"))
    print(pair_a==pair_b)
@pytest.mark.parametrize(
    "pair, answer",
    [
        ((Interval("0-0"),Interval("1-1")),False),
        ((Interval("0-0"),Interval("0-0")),True),
    ]
)
def test_interval_eq(pair, answer):
    assert (pair[0] == pair[1]) == answer

@pytest.mark.parametrize(
    "pair, answer",
    [
        ((Interval("2-8"),Interval("3-7")),1),
        ((Interval("6-6"),Interval("4-6")),1),
        ((Interval("2-4"),Interval("6-8")),0),
        ((Interval("2-3"),Interval("4-5")),0),
        ((Interval("8-18"),Interval("10-19")),0),
        ((Interval("52-53"),Interval("53-98")),0),
        ((Interval("4-4"),Interval("3-91")),1),
        ((Interval("34-85"),Interval("34-85")),1),
        ((Interval("1-28"),Interval("1-29")),1), 
    ]
)
def test_part01_compare(part01, pair, answer):
    assert part01.compare(pair) == answer and part01.compare((pair[1],pair[0])) == answer

@pytest.mark.parametrize(
    "interval_a, interval_b, answer",
    [
        (Interval("8-18"),Interval("10-19"),False),
        (Interval("10-19"),Interval("8-18"),False),
    ]
)
def test_interval_contained_by(interval_a, interval_b, answer):
    interval_a.contained_by(interval_b) == answer

@pytest.mark.parametrize(
    "interval_a, interval_b, answer",
    [
        (Interval("8-18"),Interval("10-19"),True),
        (Interval("10-19"),Interval("8-18"),True),
        (Interval("0-1"),Interval("10-11"),False),
    ]
)
def test_interval_overlaps(interval_a, interval_b, answer):
    interval_a.overlaps(interval_b) == answer