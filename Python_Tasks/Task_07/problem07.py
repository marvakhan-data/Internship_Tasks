# Problem 07: Alphabet Rangoli
# HackerRank List : https://www.hackerrank.com/challenges/alphabet-rangoli/problem


import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    for i in range(size):
        # letters from the largest down to the current one, then mirrored back up
        left = [letters[size - 1 - j] for j in range(i + 1)]
        row = left + left[-2::-1]
        lines.append("-".join(row).center(width, "-"))

    # narrowest to widest, then back down without repeating the middle row
    print("\n".join(lines + lines[-2::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
