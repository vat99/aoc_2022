# Day 7: No Space Left on Device

import abc
from typing import List, TypeVar, Mapping, Dict
from dataclasses import dataclass

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
    @abc.abstractmethod
    def parse(self, lines: List[str]):
        pass

    def main(self, fname: str):
        lines = self.read_file(fname)
        print(self.parse(lines))
    def read_file(self, fname: str) -> List[str]:
        with open(fname, 'r') as f:
            return f.readlines()

TTreeNode = TypeVar("TTreeNode", bound="TreeNode")

@dataclass
class TreeNode:
    value: str
    size: int
    parent: TTreeNode
    children: Mapping[str, TTreeNode]

    """
    - Check if line is command ($)
        - cd -> moving the root pointer
            - cd x -> make a new TreeNode x; root = x
            - cd .. -> 
        - ls -> root.update_sums
    -
    """

class Part01(Solution):
    def parse(self, lines: List[str]) -> Dict[str, int]:
        """
        Use match case python

        Assumes we only call ls once per each unique dir name (otherwise we will be double counting the values of some dirs - no checks in place for this, also can't have both `/a/b` and `/b/`)
        """
        dir_sums = dict()
        pwd = [] # maintains stack of how we have traversed the tree (from / to cwd)
        for line in lines:
            match line.split():
                case ["$", "cd", ".."]:
                    pwd.pop(0)
                case ["$", "cd", dir_name]:
                    pwd.insert(0, dir_name)
                case [f_size, _]:
                    for dir in pwd:
                        dir_sums[dir] = dir_sums.get(dir, 0) + f_size
                case _: # case ["$", "ls"] | ["dir", dir_name]
                    pass
        return dir_sums
