# Problem 19 : Weighted Uniform Strings
# HackerRank Link : https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()
    previous = ""
    current_weight = 0

    for ch in s:
        weight = ord(ch) - ord('a') + 1

        if ch == previous:
            current_weight += weight
        else:
            current_weight = weight
            previous = ch

        weights.add(current_weight)

    return ["Yes" if q in weights else "No" for q in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
