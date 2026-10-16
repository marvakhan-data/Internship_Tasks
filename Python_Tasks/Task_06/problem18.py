# Problem 18: Set Mutations
# HackerRank Link : https://www.hackerrank.com/challenges/py-set-mutations/problem


n = int(input())
A = set(map(int, input().split()))

N = int(input())

for _ in range(N):
    operation, length = input().split()
    other_set = set(map(int, input().split()))

    if operation == "update":
        A.update(other_set)
    elif operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

print(sum(A))
