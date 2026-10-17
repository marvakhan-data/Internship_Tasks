# Problem 13 : Sherlock and the Valid String
# HackerRank Link : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

def isValid(s):
    freq = Counter(Counter(s).values())

    if len(freq) == 1:
        return "YES"

    if len(freq) == 2:
        frequencies = list(freq.keys())
        counts = list(freq.values())

        f1, f2 = frequencies
        c1, c2 = counts

        if f1 == 1 and c1 == 1:
            return "YES"

        if f2 == 1 and c2 == 1:
            return "YES"

        if f1 == f2 + 1 and c1 == 1:
            return "YES"

        if f2 == f1 + 1 and c2 == 1:
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
