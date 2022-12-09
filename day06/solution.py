# Day 03: Camp Cleanup

from typing import List, Tuple
import abc
from functools import reduce
import re
from collections.abc import Iterable

class Solution(abc.ABC):
    @abc.abstractmethod
    def main(self, line: str) -> int:
        pass

class Part01(Solution):
    def main(self, line: str) -> int:
        for i in range(len(line)-3):
            buffer = line[i:i+4]
            if len(set(buffer)) == 4:
                return i+4
        return -1

def run():
    line = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

    problems = [Part01()]
    for solution in problems:
        print(solution.main(line))

if __name__ == "__main__":
    run()