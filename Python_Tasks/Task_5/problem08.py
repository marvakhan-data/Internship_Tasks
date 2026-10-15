# Problem 8: Set .add()
# Link: https://www.hackerrank.com/challenges/py-set-add/problem



n = int(input())
countries = set()

for _ in range(n):
    countries.add(input())

print(len(countries))
