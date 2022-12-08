# Day 03: Camp Cleanup

from typing import List, Tuple
import abc
from functools import reduce
import re
from collections.abc import Iterable

class Solution(abc.ABC):
    def __init__(self, fname: str):
        lines = self.read_file(fname)
        self.stacks, self.instructions = self.parse_file(lines)

    def read_file(self, fname: str) -> List[str]:
        with open(fname, 'r') as f:
            return f.readlines()

    def main(self):
        print(self.perform_instructions())

    @abc.abstractmethod
    def perform_instructions(self) -> str:
        pass
    
    def parse_file(self, lines: List[str]) -> Tuple[List[List[str]], Iterable]:
        index_stack_instruction = self.find_double_new_line(lines)
        stack_lines = lines[:index_stack_instruction]
        instruction_lines = lines[(index_stack_instruction+1):]
        return self.parse_initial_stacks(stack_lines), self.parse_instructions(instruction_lines)

    def find_double_new_line(self, lines: List[str]) -> int:
        # brute force for now
        # condition: line is newline and previous line ends with newline
        prev_ends_w_newline = False
        for i, line in enumerate(lines):
            if line == '\n' and prev_ends_w_newline:
                return i
            elif line[-1] == '\n':
                prev_ends_w_newline = True
            else:
                prev_ends_w_newline = False
        return -1

    def parse_initial_stacks(self, stack_lines: List[str]) -> List[str]:
        # brute force
        num_stacks = len(stack_lines[-1].strip().split())
        stacks = [[] for _ in range(num_stacks)]

        capital_letter_pattern = re.compile("[A-Z]")
        for stack_line in stack_lines[:-1]:
            for i, value in enumerate(stack_line):
                if capital_letter_pattern.match(value):
                    stack_index = int(stack_lines[-1][i])-1
                    stacks[stack_index].append(value)
        return stacks

    def parse_instructions(self, instructions: List[str]) -> List[str]:
        def parse_instruction(instruction: str) -> Tuple[int, int, int]:
            split_instruction = instruction.split()
            values = (int(split_instruction[1]), int(split_instruction[3])-1, int(split_instruction[5])-1) # have to remove 1 from each index to make it match
            return values
        return map(parse_instruction, instructions)

    def visualize(self):
        # make a grid of max_len x 
        #max_len = max(map(max, self.stacks))
        print(self.stacks)
        print()

class Part01(Solution):
    def __init__(self, fname):
        super().__init__(fname)

    def perform_instructions(self) -> str:
        #self.visualize()
        for num_pops, original_stack_index, new_stack_index in self.instructions:
            for _ in range(num_pops):
                self.stacks[new_stack_index].insert(0, self.stacks[original_stack_index].pop(0))
                #self.visualize()
        return "".join([stack.pop(0) for stack in self.stacks])

class Part02(Solution):
    def __init__(self, fname):
        super().__init__(fname)

    def perform_instructions(self) -> str:
        #self.visualize()
        for num_pops, original_stack_index, new_stack_index in self.instructions:
            self.stacks[new_stack_index] = self.stacks[original_stack_index][:num_pops] + self.stacks[new_stack_index]
            self.stacks[original_stack_index] = self.stacks[original_stack_index][num_pops:]
            #self.visualize()
        return "".join([stack.pop(0) for stack in self.stacks])

def run(fname):
    problems = [Part01(fname), Part02(fname)]
    for solution in problems:
        solution.main()

if __name__ == "__main__":
    run("input.txt")