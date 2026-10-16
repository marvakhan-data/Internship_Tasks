# Problem 16 : Check Subset

# HackerRank List : https://www.hackerrank.com/challenges/py-check-subset/problem

T = int(input())

for _ in range(T):
    nA = int(input())
    A = set(map(int, input().split()))

    nB = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))


