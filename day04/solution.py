# Day 03: Camp Cleanup

from typing import List, Tuple, TypeVar
import abc
from functools import reduce

"""
We could use something fancy like an interval tree or a segment tree (for optimized global performance ~ this is super handwavy BS)

Will use a proxy to first sort all of the intervals by len
Still need a way to encapsulate the Interval --> Make an Interval class!

Could have done this pretty quickly with set(range(start,end)) [time to code wise]
"""

# have to put this at the top
TInterval = TypeVar("TInterval", bound="Interval")

class Interval():
    def __init__(self, interval: str):
        split_interval = interval.split("-")
        self.start = int(split_interval[0])
        self.end = int(split_interval[1])

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Interval) and (self.start == __o.start and self.end == __o.end)

    def __repr__(self) -> str:
        return f"Interval({self.start},{self.end})"
    
    def contained_by(self, other: TInterval) -> bool:
        """
        Returns true if this interval is fully contained by the other
        """
        return (other.start <= self.start) and (self.end <= other.end)

    def overlaps(self, other: TInterval) -> bool:
        self_range = set(range(self.start, self.end+1))
        other_range = set(range(other.start, other.end+1))
        return len(self_range & other_range) > 0

class Solution(abc.ABC):
    def read_file(self, fname: str) -> List[str]:
        with open(fname, 'r') as f:
            return f.readlines()

    def main(self, lines: List[str]) -> int:
        return reduce(lambda x,line: x+self.compare(self.parse_line(line.strip())), lines, 0)

    @abc.abstractmethod
    def compare(self, pair: Tuple[TInterval, TInterval]) -> int:
        pass

    def parse_line(self, line: str) -> Tuple[TInterval, TInterval]:
        str_intervals = line.split(",")
        return (Interval(str_intervals[0]), Interval(str_intervals[1]))

class Part01(Solution):
    """
    Find how many assignment pairs does one range fully contain the other
    """
    def compare(self, pair: Tuple[TInterval, TInterval]) -> int:
        """
        This is a super brute force way to calculate this (only works for comparing a small number of Intervals)
        """
        interval_a, interval_b = pair
        return 1 if interval_a.contained_by(interval_b) or interval_b.contained_by(interval_a) else 0

class Part02(Solution):
    """
    Find how many assignment pairs do assignment pair have overlapping ranges?
    """
    def compare(self, pair: Tuple[TInterval, TInterval]) -> int:
        """
        This is a super brute force way to calculate this (only works for comparing a small number of Intervals)
        """
        interval_a, interval_b = pair
        #breakpoint()
        return 1 if interval_a.overlaps(interval_b) else 0

def check():
    t = 0
    for i, line in enumerate(open("input.txt")):
        a, b, x, y = map(int, line.replace(",", "-").split("-"))
        if a <= x and b >= y or x <= a and y >= b:
            t += 1
    print(t)

def run():
    problems = [Part01(), Part02()]
    for solution in problems:
        lines = solution.read_file("input.txt")
        print(solution.main(lines))

def contained_by_test():
    pairs = [
        (Interval("8-18"),Interval("10-19")),
        (Interval("10-19"),Interval("8-18")),
        (Interval("5-5"),Interval("5-82")),
        (Interval("5-82"),Interval("5-5"))
    ]
    for interval_a, interval_b in pairs:
        print()
        print(interval_a.contained_by(interval_b))

def debug():
    solution = Part02()
    input_file = "sample.txt"
    #import ipdb; ipdb.set_trace()
    solution.main(solution.read_file(input_file))

if __name__ == "__main__":
    #contained_by_test()
    run()
    #debug()