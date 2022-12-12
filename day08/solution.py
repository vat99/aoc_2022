# Day 08: Treetop Tree House

import abc
from typing import List, TypeVar, Mapping, Dict, Tuple
from dataclasses import dataclass
from collections import defaultdict

class Solution(abc.ABC):
    def __init__(self, fname):
        self.grid, self.num_rows, self.num_cols = self.parse(self.read_file(fname))

    @abc.abstractmethod
    def main(self) -> int:
        pass

    def read_file(self, fname: str) -> List[str]:
        with open(fname, 'r') as f:
            return f.readlines()

    def parse(self, lines: List[str]) -> Tuple[List[List[int]], int, int]:
        grid = []
        num_rows = len(lines)
        num_cols = len(lines[0].strip())
        for i, line in enumerate(lines):
            row = []
            line = line.strip()
            for j, digit in enumerate(line):
                row.append(int(digit))
            grid.append(row)
        return grid, num_rows, num_cols

class Part01(Solution):
    def main(self) -> int:
        """
        hella bruteforce
        """
        visible_count = 2 * (self.num_cols - 2) + 2 * (self.num_rows)
        for i in range(1,self.num_rows-1):
            for j in range(1, self.num_cols-1):
                visible_count += 1 if self.is_visible(i,j) else 0
        return visible_count
    
    def check_up(self, i, j):
        for r in range(i-1,-1,-1):
            #print(f"up: {self.grid[r][j]}")
            if self.grid[i][j] <= self.grid[r][j]:
                return False
        return True
    
    def check_down(self, i, j):
        for r in range(i+1,self.num_rows):
            #print(f"down: {self.grid[r][j]}")
            if self.grid[i][j] <= self.grid[r][j]:
                return False
        return True
    
    def check_left(self, i, j):
        for c in range(j-1,-1,-1):
            #print(f"left: {self.grid[i][c]}")
            if self.grid[i][j] <= self.grid[i][c]:
                return False
        return True
    
    def check_right(self, i, j):
        for c in range(j+1,self.num_cols):
            #print(f"right: {self.grid[i][c]}")
            if self.grid[i][j] <= self.grid[i][c]:
                return False
        return True
    
    def is_visible(self, i: int, j: int) -> bool:
        """
        bruteforce shieet
        """
        #print(f"value: {self.grid[i][j]}")
        #print(self.num_rows, self.num_cols)
        #import ipdb; ipdb.set_trace()
        return self.check_up(i,j) or self.check_down(i,j) or self.check_left(i,j) or self.check_right(i,j)

class Part02(Solution):
    def main(self) -> int:
        """
        hella bruteforce
        """
        max_scenic_score = 0
        for i in range(1,self.num_rows-1):
            for j in range(1, self.num_cols-1):
                current_scenic_score = self.visible_score(i,j)
                if current_scenic_score > max_scenic_score:
                    max_scenic_score = current_scenic_score
        return max_scenic_score 
    
    def check_up(self, i, j):
        for r in range(i-1,-1,-1):
            #print(f"up: {self.grid[r][j]}")
            if self.grid[i][j] <= self.grid[r][j]:
                return i-r
        return i
    
    def check_down(self, i, j):
        for r in range(i+1,self.num_rows):
            #print(f"down: {self.grid[r][j]}")
            if self.grid[i][j] <= self.grid[r][j]:
                return r-i
        return self.num_rows-1-i
    
    def check_left(self, i, j):
        for c in range(j-1,-1,-1):
            #print(f"left: {self.grid[i][c]}")
            if self.grid[i][j] <= self.grid[i][c]:
                return j-c
        return j
    
    def check_right(self, i, j):
        for c in range(j+1,self.num_cols):
            #print(f"right: {self.grid[i][c]}")
            if self.grid[i][j] <= self.grid[i][c]:
                return c-j
        return self.num_cols-1-j
    
    def visible_score(self, i: int, j: int) -> bool:
        """
        bruteforce shieet
        """
        return self.check_up(i,j) * self.check_down(i,j) * self.check_left(i,j) * self.check_right(i,j)

def run(fname):
    solution = Part02(fname)
    #print(solution.is_visible(1,1)) # True
    #print(solution.is_visible(1,2)) # True
    #print(solution.is_visible(1,3)) # False
    print(solution.main())

if __name__ == "__main__":
    run("input.txt")
