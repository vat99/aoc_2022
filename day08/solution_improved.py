def next_greater_right(arr):
    res = [len(arr)-1-i for i in range(len(arr))] # start all indices at -1
    stack = []
    for i, num in enumerate(arr):
        while len(stack) > 0 and arr[stack[-1]] < num:
            index = stack.pop()
            res[index] = i-index
        stack.append(i)
    return res

def next_greater_left(arr):
    res = list(range(len(arr)))
    stack = []
    #for i, num in reversed(list(enumerate(arr))):
    for i in range(len(arr)-1, -1, -1):
        num = arr[i]
        #print(f"num, stack, res: {num, stack, res}")
        while len(stack) > 0 and arr[stack[-1]] < num:
            index = stack.pop()
            res[index] = index-i
        stack.append(i)
    return res

def get_right(arr):
    res_right = next_greater_right(arr)
    print(f"arr: {arr}")
    print(f"right: {res_right}")

def get_left(arr):
    res_left = next_greater_left(arr)
    print(f"arr: {arr}")
    print(f"left: {res_left}")

if __name__ == "__main__":
    arr = [1, 2, 5, 13, 9, 6, 4, 12, 7]
    get_right(arr)
    print()
    get_left(arr)
    """
    [1, 2, 5, 13, 9, 6, 4, 12, 7]
    right: [1, 1, 1, -1, 3, 2, 1, -1, -1] -> [1, 1, 1, 5, 3, 2, 1, 1, 0]
    left: [-1, -1, -1, -1, 1, 1, 1, 3, 1] -> [0, 1, 2, 3, 1, 1, 1, 4, 1]
    """