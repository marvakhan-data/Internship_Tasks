# Problem 01:Set .symmetric_difference() Operation
# HackerRank Link : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


# Number of students subscribed to English newspaper
n = int(input())
english = set(map(int, input().split()))

# Number of students subscribed to French newspaper
m = int(input())
french = set(map(int, input().split()))

# Find students subscribed to exactly one newspaper
result = english.symmetric_difference(french)

# Print the total number of such students
print(len(result))
