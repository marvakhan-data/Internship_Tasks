# Problem 19 : Company Logo
# HackerRank Link : https://www.hackerrank.com/challenges/most-commons/problem


from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = Counter(s)

    for char, count in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(char, count)
