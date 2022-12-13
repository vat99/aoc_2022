# Day 08: Treetop Tree House

import abc
from typing import List, TypeVar, Mapping, Dict, Tuple
from dataclasses import dataclass
from collections import defaultdict

import time

def timer_func(func):
    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func} took {time} seconds to complete its execution."
        print(msg.format(func = func.__name__,time = runtime))
        return value
    return function_timer

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
    @timer_func
    def main(self) -> int:
        """
        hella bruteforce
        """
        max_scenic_score = 0
        for i in range(1,self.num_rows-1):
            for j in range(1, self.num_cols-1):
                current_scenic_score = self.is_visible(i,j)
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
    
    def is_visible(self, i: int, j: int) -> bool:
        """
        bruteforce shieet
        """
        #print(f"value: {self.grid[i][j]}")
        #print(self.num_rows, self.num_cols)
        #import ipdb; ipdb.set_trace()
        return self.check_up(i,j) * self.check_down(i,j) * self.check_left(i,j) * self.check_right(i,j)
    
    @timer_func
    def main_optimized(self) -> int:
        """
        optimized
        """
        max_scenic_score = 0
        next_greater_right_rows, next_greater_left_rows, next_greater_up_cols, next_greater_down_cols = self.get_visibility_scores()
        #print(f"next_greater_right_rows: {next_greater_right_rows}")
        #print(f"next_greater_left_rows: {next_greater_left_rows}")
        #print(f"next_greater_up_cols: {next_greater_up_cols}")
        #print(f"next_greater_down_cols: {next_greater_down_cols}")
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                left_visibility = next_greater_left_rows[i][j]
                right_visibility = next_greater_right_rows[i][j]
                up_visibility = next_greater_up_cols[j][i]
                down_visibility = next_greater_down_cols[j][i]
                #import ipdb; ipdb.set_trace()
                score = left_visibility * right_visibility * up_visibility * down_visibility
                if score > max_scenic_score:
                    max_scenic_score = score
        return max_scenic_score

    def get_visibility_scores(self) -> Tuple[List[int], List[int], List[int], List[int]]:
        next_greater_right_rows = []
        next_greater_left_rows = []
        next_greater_up_cols = []
        next_greater_down_cols = []
        
        # rows
        for i in range(self.num_rows):
            right_result = self.next_greater_right(self.grid[i])
            next_greater_right_rows.append(right_result)
            left_result = self.next_greater_left(self.grid[i])
            next_greater_left_rows.append(left_result)

        # cols
        for j in range(self.num_cols):
            transposed_col = [self.grid[i][j] for i in range(self.num_rows)]
            #print(transposed_col)
            down_result = self.next_greater_right(transposed_col)
            next_greater_up_cols.append(down_result)
            up_result = self.next_greater_left(transposed_col)
            next_greater_down_cols.append(up_result)

        return next_greater_right_rows, next_greater_left_rows, next_greater_up_cols, next_greater_down_cols

    def next_greater_right(self, arr):
        res = [len(arr)-1-i for i in range(len(arr))] # start all indices at -1
        stack = []
        for i, num in enumerate(arr):
            while len(stack) > 0 and arr[stack[-1]] <= num:
                index = stack.pop()
                res[index] = i-index
            stack.append(i)
        return res

    def next_greater_left(self, arr):
        res = list(range(len(arr)))
        stack = []
        #for i, num in reversed(list(enumerate(arr))):
        for i in range(len(arr)-1, -1, -1):
            num = arr[i]
            #print(f"num, stack, res: {num, stack, res}")
            while len(stack) > 0 and arr[stack[-1]] <= num:
                index = stack.pop()
                res[index] = index-i
            stack.append(i)
        return res

def run(fname):
    solution = Part02(fname)
    #print(solution.is_visible(1,1)) # True
    #print(solution.is_visible(1,2)) # True
    #print(solution.is_visible(1,3)) # False
    print(solution.main())
    solution = Part02(fname)
    print(solution.main_optimized())

if __name__ == "__main__":
    run("input.txt")
