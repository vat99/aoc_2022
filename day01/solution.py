# day01: calorie counting
from typing import List
import heapq

"""
each empty line demarcates different elves

find the elf carrying the most calories
"""

class Solution:
    def part02(self, fname: str) -> int:
        """
        optimized - do read and finding maxes at same time
        uses heapq --> max heap [just insert negative values and do negative comparison]

        idk what the time complexity of this is - 
        """
        # we can't use this kind of init
        # max_sums = [float("inf")] * k
        # heapq.heapify(max_sums)
        k = 3
        max_sums = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            current_sum = 0
            for line in lines:
                if line == "\n":
                    if len(max_sums) < k:
                        max_sums.append(current_sum)
                        if len(max_sums) == k:
                            heapq.heapify(max_sums)
                    else:
                        if current_sum > max_sums[0]:
                            heapq.heapreplace(max_sums, current_sum)
                    current_sum = 0
                else:
                    num = int(line.split()[0])
                    current_sum += num
        # process the last current_sum
        if current_sum > max_sums[0]:
            heapq.heapreplace(max_sums, current_sum)
        return sum(max_sums)

    def heapify_test(self, nums: List[int], k: int) -> int:
        max_sums = nums[:k]
        heapq.heapify(max_sums) # this is linear time
        for num in nums[k:]:
            if num > max_sums[0]:
                heapq.heapreplace(max_sums, num)
        return sum(max_sums)
    
    def part01(self, fname: str) -> int:
        """
        optimized - do read and finding max at same time
        """
        max_sum = float("-inf")
        elves = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            current_elf = []
            current_sum = 0
            for line in lines:
                if line == "\n":
                    elves.append(current_elf)
                    current_elf = []
                    if current_sum > max_sum:
                        max_sum = current_sum
                    current_sum = 0
                else:
                    num = int(line.split()[0])
                    current_sum += num
                    current_elf.append(num)
        return max_sum
    
    def read_input(self, fname: str) -> List[List[int]]:
        elves = []
        with open(fname, 'r') as f:
            lines = f.readlines()
            current_elf = []
            for line in lines:
                if line == "\n":
                    elves.append(current_elf)
                    current_elf = []
                else:
                    current_elf.append(int(line.split()[0]))
        elves.append(current_elf)
        return elves

if __name__ == "__main__":
    solution = Solution()
    #print(solution.read_input("sample.txt"))
    #print(solution.part01("input.txt"))
    #print(solution.part02("sample.txt"))
    #print(solution.heapify_test([10,2,3,10,5,6,10,3,1],3))
    print(solution.part02("input.txt"))