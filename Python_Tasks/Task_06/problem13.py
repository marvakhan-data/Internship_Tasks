# Problem 13:Set .union() Operation
# Hacker Rank Link :https://www.hackerrank.com/challenges/py-set-union/problem


n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

print(len(english.union(french)))
