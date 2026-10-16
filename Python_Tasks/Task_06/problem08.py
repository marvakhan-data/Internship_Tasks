# Problem 8: Tuples
# HackerRank Link: https://www.hackerrank.com/challenges/python-tuples/problem

def old_tuple_hash(t):
    # Tuple hash algorithm used before Python 3.8
    M = 2 ** 64
    length = len(t)
    mult = 1000003
    x = 0x345678
    for item in t:
        length -= 1
        x = ((x ^ hash(item)) * mult) % M
        mult = (mult + 82520 + length + length) % M
    x = (x + 97531) % M
    if x >= 2 ** 63:
        x -= M
    return -2 if x == -1 else x


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    t = tuple(integer_list)
    print(old_tuple_hash(t))
