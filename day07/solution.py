# Day 7: No Space Left on Device

import abc
from typing import List, TypeVar, Mapping, Dict
from dataclasses import dataclass
from collections import defaultdict

"""
Part 1:
Find all directories with a total size of at most 100000.
What is the sum of the total sizes of those directories?

Approach:
Lets represent the file system as a tree with nodes that contain value, size, pointer to parent, map of pointers to children

The complexity will be in inserting elements
And upating the sums (have to just go back to the top)

Keep track of a list of all directories we have seen, and as we are updating sums remove any that we dont need

Potentially Optimized Approach:
[Ignore first attempt - too complicated]
Just use lists and pop/append too the list
(easy to add to the list every time we see an ls'd directory since we just go through for each file and add its size to the list of directories that contain it)
Keep track of sizes with a hashmap!

Assumptions:
every diretory is ls'd once
"""

class Solution(abc.ABC):
    def parse(self, lines: List[str]) -> Dict[str, int]:
        """
        Use match case python

        Assumes we only call ls once per each unique dir name (otherwise we will be double counting the values of some dirs - no checks in place for this, also can't have both `/a/b` and `/b/`) -> BAD ASSUMPTION GUH
        """
        dir_sums = defaultdict(int)
        pwd = [] # maintains stack of how we have traversed the tree (from / to cwd)
        for i,line in enumerate(lines):
            #import ipdb; ipdb.set_trace() 
            match line.split():
                case ["$", "cd", ".."]:
                    pwd.pop(0)
                    if len(pwd) == 0:
                        pwd = ["/"]
                case ["$", "cd", "/"]:
                    pwd = ["/"]
                case ["$", "cd", dir_name]:
                    pwd.insert(0, dir_name)
                case [f_size, _] if f_size.isdigit():
                    for j, dir in enumerate(pwd):
                        dir_name = "/".join(pwd[::-1][:len(pwd)-j])
                        dir_sums[dir_name] += int(f_size)
        print(dir_sums)
        return dir_sums

    @abc.abstractmethod
    def main(self, fname: str) -> int:
        pass

    def read_file(self, fname: str) -> List[str]:
        with open(fname, 'r') as f:
            return f.readlines()

class Part01(Solution):
    def main(self, fname: str) -> int:
        lines = self.read_file(fname)
        d = self.parse(lines)
        results = [val for val in d.values() if val <= 100000]
        return sum(results)

class Part02(Solution):
    def main(self, fname: str) -> int:
        lines = self.read_file(fname)
        d = self.parse(lines)
        total_space_remaining = 70000000-d["/"]
        print(total_space_remaining)
        for dir,val in d.items():
            if dir != "/":
                print(f"{dir}: {30000000-total_space_remaining+val}")
        return min(val for val in d.values() if val+total_space_remaining-30000000 >= 0)

def run(fname):
    solution = Part02()
    print(solution.main(fname))

if __name__ == "__main__":
    run("input.txt")
