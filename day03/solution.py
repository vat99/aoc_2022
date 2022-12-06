# Day 03: Rucksack Reorginzation

from typing import List, Tuple
import abc
from functools import reduce

class Solution(abc.ABC):
    def read_file(self, fname: str) -> List[str]:
        with open(fname, 'r') as f:
            return f.readlines()

    @abc.abstractmethod
    def main(self, lines: List[str]) -> int:
        pass

    @abc.abstractmethod
    def find_common_letter(self):
        pass
    
    def get_letter_priority(self, letter: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        if letter.isupper():
            return letters.index(letter.swapcase()) + 27
        else:
            return letters.index(letter) + 1

class Part02(Solution):
    def main(self, lines: List[str]) -> int:
        priority_sum = 0
        line_groups = [lines[n:n+3] for n in range(0, len(lines), 3)]
        for line_group in line_groups:
            striped_line_group = list(map(lambda foo: foo.strip(), line_group))
            letter = self.find_common_letter(striped_line_group)
            priority_sum += self.get_letter_priority(letter)
        return priority_sum

    def find_common_letter(self, lines: List[str]) -> str:
        """
        Returns the set of letters in common between some number of lines compartments
        Time complexity of O(n) across length of each string (which is constant)
        Assumes that there is only 1 letter in common between all lines
        """
        # only the first element needs to be a set, rest can be iterables
        letter_set = reduce(lambda x,y: x.intersection(y), lines[1:], set(lines[0])) # function, iterable, initial
        return letter_set.pop()

class Part01(Solution):
    def main(self, lines: List[str]) -> int:
        priority_sum = 0
        for line in lines:
            line = line.strip()
            compartments = self._split_line(line)
            letter = self.find_common_letter(*compartments)
            priority_sum += self.get_letter_priority(letter)
        return priority_sum

    def find_common_letter(self, compartment: str, other_compartment: str) -> str:
        """
        Returns the set of letters in common between the two compartments
        Time complexity of O(n) across length of each string (which is constant)
        Assumes that there is only 1 letter in common between both compartments
        """
        letter_set = set(compartment).intersection(other_compartment)
        return letter_set.pop()

    def _split_line(self, line: str) -> Tuple[str, str]:
        """
        Assumes that the length of the line is even
        """
        split_index = len(line) // 2
        return (line[:split_index], line[split_index:])

if __name__ == "__main__":
    problems = [Part01(), Part02()]
    for solution in problems:
        lines = solution.read_file("input.txt")
        print(solution.main(lines))