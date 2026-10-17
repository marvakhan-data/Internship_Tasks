# Problem 03: Mars Exploration
# HackerRank List : https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    expected = "SOS" * (len(s) // 3)
    count = 0

    for i in range(len(s)):
        if s[i] != expected[i]:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
