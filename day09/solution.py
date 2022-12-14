import abc
from typing import List, Tuple

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
        
    def main(self, fname: str) -> int:
        return 0

    def failed_main(self, fname: str) -> int:
        instructions = self.read_file(fname)
        head_position = (0,0)
        tail_position = (0,0)
        tail_visited = set()
        tail_visited.add(tail_position)
        was_diagonal = False
        for instruction in instructions:
            instruction = instruction.split()
            instruction[1] = int(instruction[1])
            print(f"head_position, tail_position: {head_position, tail_position}")
            print(f"instruction: {instruction}")
            match instruction:
                case ['R', x]:
                    for _ in range(x):
                        head_position = (head_position[0]+1, head_position[1])
                        if not self.check_position(head_position, tail_position):
                            if not was_diagonal:
                                tail_position = (tail_position[0]+1, tail_position[1])
                            else:
                                print("was diagonal")
                                tail_position = (head_position[0]-1, head_position[1]) # move tail to where head was
                        print(f"RIGHT head_position, tail_position: {head_position, tail_position}")
                case ['L', x]:
                    for _ in range(x):
                        head_position = (head_position[0]-1, head_position[1])
                        if not self.check_position(head_position, tail_position):
                            if not was_diagonal:
                                tail_position = (tail_position[0]-1, tail_position[1])
                            else:
                                print("was diagonal")
                                tail_position = (head_position[0]+1, head_position[1]) # move tail to where head was
                        print(f"LEFT head_position, tail_position: {head_position, tail_position}")
                case ['U', x]:
                    for _ in range(x):
                        head_position = (head_position[0], head_position[1]+1)
                        if not self.check_position(head_position, tail_position):
                            if not was_diagonal:
                                tail_position = (tail_position[0], tail_position[1]+1)
                            else:
                                print("was diagonal")
                                tail_position = (head_position[0], head_position[1]-1) # move tail to where head was
                        print(f"UP head_position, tail_position: {head_position, tail_position}")
                case ['D', x]:
                    for _ in range(x):
                        head_position = (head_position[0], head_position[1]-1)
                        if not self.check_position(head_position, tail_position):
                            if not was_diagonal:
                                tail_position = (tail_position[0], tail_position[1]-1)
                            else:
                                print("was diagonal")
                                tail_position = (head_position[0], head_position[1]+1) # move tail to where head was
                        print(f"DOWN tail_position: {head_position, tail_position}")
            was_diagonal = self.check_diagonal(head_position, tail_position)
            tail_visited.add(tail_position)
        #print(f"tail_visited: {tail_visited}")
        return tail_visited
    
    def check_position(self, head_position: Tuple[int, int], tail_position: Tuple[int, int]) -> bool:
        return abs(head_position[0]-tail_position[0]) <= 1 and abs(head_position[1]-tail_position[1]) <= 1

    def check_diagonal(self, head_position: Tuple[int, int], tail_position: Tuple[int, int]) -> bool:
        """
        returns True if head_position 
        """
        return (head_position == (tail_position[0]+1, tail_position[1]+1)) or (head_position == (tail_position[0]-1, tail_position[1]+1)) or (head_position == (tail_position[0]+1, tail_position[1]-1)) or (head_position == (tail_position[0]-1, tail_position[1]-1))

def test():
    solution = Part01()
    visited = solution.main("sample.txt")
    print(f"answer {len(visited)}")
    answer = set([
        (0,0),
        (1,0),
        (2,0),
        (3,0),
        (4,1),
        (4,2),
        (4,3),
        (3,3),
        (3,4),
        (2,4),
        (2,2),
        (1,2),
        (3,2),
    ])
    print(f"expected answer {len(answer)}")
    print(f"difference {answer-visited}")

if __name__ == "__main__":
    test()