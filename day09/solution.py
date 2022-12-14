import abc
from typing import List, Tuple

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
    def read_file(self, fname: str) -> List[str]:
        with open(fname, 'r') as f:
            return f.readlines()

    @abc.abstractmethod
    def main(self) -> int:
        pass

class Part01(Solution):
    def change_state(self, direction: str, head_position: Tuple[int, int], tail_position: Tuple[int, int]) -> Tuple[Tuple[int,int], Tuple[int, int]]:
        """
            move `head_position` in `direction` by 1 step
            if `tail_position` is within 1 unit of `head_position` and not tiagonal:
                don't move `tail_position`
            else:
                if `head_position` is 2 units ahead of `tail_position`:
                    move `tail_position` 1 unit in direction
                if `tail_position` is 1 unit diagonally of old `head_position`:
                    move `tail_position` 1 unit behind `head_position`
        """
        old_head_position = head_position
        match direction:
            case "R":
                head_position = (head_position[0]+1, head_position[1])
            case "L":
                head_position = (head_position[0]-1, head_position[1])
            case "U":
                head_position = (head_position[0], head_position[1]+1)
            case "D":
                head_position = (head_position[0], head_position[1]-1)
        if not self.check_position(head_position, tail_position):
            tail_position = old_head_position

        return head_position, tail_position
        
    def transform_instruction(self, instruction: str) -> Tuple[str, int]:
        instruction = instruction.split()
        return (instruction[0], int(instruction[1]))

    def main(self, fname: str) -> int:
        # init
        head_position, tail_position = (0,0), (0,0)
        visited_set = set()
        visited_set.add(tail_position)
        instructions = self.read_file(fname)
        
        # read instructions
        for instruction in instructions:
            direction, count = self.transform_instruction(instruction)
            for _ in range(count):
                head_position, tail_position = self.change_state(direction, head_position, tail_position)
                visited_set.add(tail_position)
        return len(visited_set)
    
    def check_position(self, head_position: Tuple[int, int], tail_position: Tuple[int, int]) -> bool:
        return abs(head_position[0]-tail_position[0]) <= 1 and abs(head_position[1]-tail_position[1]) <= 1

    def check_diagonal(self, head_position: Tuple[int, int], tail_position: Tuple[int, int]) -> bool:
        """
        returns True if head_position 
        """
        return (head_position == (tail_position[0]+1, tail_position[1]+1)) or (head_position == (tail_position[0]-1, tail_position[1]+1)) or (head_position == (tail_position[0]+1, tail_position[1]-1)) or (head_position == (tail_position[0]-1, tail_position[1]-1))

@timer_func
def run(fname: str):
    solution = Part01()
    print(solution.main(fname))

if __name__ == "__main__":
    run("input.txt")