# Problem 6: Introduction to Sets
# Link: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    unique_heights = set(array)
    return sum(unique_heights) / len(unique_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
