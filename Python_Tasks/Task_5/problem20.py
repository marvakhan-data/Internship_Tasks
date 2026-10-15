# Problem 20: Piling Up!
# Link: https://www.hackerrank.com/challenges/piling-up/problem



from collections import deque

for _ in range(int(input())):
    n = int(input())
    cubes = deque(map(int, input().split()))
    top = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > top:
            print("No")
            break

        top = current
    else:
        print("Yes")
