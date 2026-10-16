# Problem 10: Designer Door Mat
# HackerRank Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = map(int, input().split())

# Top half
for i in range(n // 2):
    pattern = '.|.' * (2 * i + 1)
    print(pattern.center(m, '-'))

# Middle line
print('WELCOME'.center(m, '-'))

# Bottom half (top half in reverse)
for i in range(n // 2 - 1, -1, -1):
    pattern = '.|.' * (2 * i + 1)
    print(pattern.center(m, '-'))
