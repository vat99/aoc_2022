# Day 02: Rock Paper Scissors
from typing import List

class Solution:
    def read_file(self, fname: str) -> List[str]:
        with open(fname, 'r') as f:
            return f.readlines()

    def main(self, lines: List[str]) -> int:
        score = 0
        for line in lines:
            options = line.split()
            score += self.get_score(options)
        return score

    def get_score(self, options: List[str]) -> int:
        pass

class Part02(Solution):
    def get_score(self, options: List[str]) -> int:
        outcome_score = {
            'X': 0,
            'Y': 3,
            'Z': 6,
        }
        shape_score = {
            'A': {
                'X': 3, # lose-->rock-scissor
                'Y': 1, # tie-->rock-rock
                'Z': 2, # win-->rock-paper
            },
            'B': {
                'X': 1, # lose-->paper-rock
                'Y': 2, # tie-->paper-paper
                'Z': 3, # win-->paper-scissors
            },
            'C': {
                'X': 2, # lose-->scissors-paper
                'Y': 3, # tie-->scissors-scissors
                'Z': 1, # win-->scissors-rock
            },
        }
        return outcome_score[options[1]] + shape_score[options[0]][options[1]]

class Part01(Solution):
    def get_score(self, options: List[str]) -> int:
        shape_score = {
            'X': 1,
            'Y': 2,
            'Z': 3,
        }
        outcome_score = {
            'A': {
                'X': 3, # rock-rock
                'Y': 6, # rock-paper
                'Z': 0, # rock-scissors
            },
            'B': {
                'X': 0, # paper-rock
                'Y': 3, # paper-paper
                'Z': 6, # paper-scissors
            },
            'C': {
                'X': 6, # scissors-rock
                'Y': 0, # scissors-paper
                'Z': 3, # scissors-scissors
            },
        }
        return shape_score[options[1]] + outcome_score[options[0]][options[1]]

if __name__ == "__main__":
    solution = Part01()
    lines = solution.read_file("input.txt")
    print(solution.main(lines))