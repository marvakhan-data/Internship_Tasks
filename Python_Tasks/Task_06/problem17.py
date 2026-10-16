# Problem 17 : Check Strict Superset
# HackerRank Link : https://www.hackerrank.com/challenges/py-check-strict-superset/problem


A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    B = set(map(int, input().split()))

    if not A > B:
        result = False
        break

print(result)
