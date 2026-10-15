# Problem 01: Find the Runner-Up Score!
# Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = list(set(arr))
    unique_scores.sort()

    print(unique_scores[-2])
