# Problem 7: Symmetric Difference
# Link: https://www.hackerrank.com/challenges/symmetric-difference/problem



M = int(input())
A = set(map(int, input().split()))

N = int(input())
B = set(map(int, input().split()))

result = A ^ B

for num in sorted(result):
    print(num)
