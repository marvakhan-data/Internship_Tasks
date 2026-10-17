# Problem 06 : Pangrams
# HackerRank List : https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    letters = set(s.lower())

    if len(letters.intersection("abcdefghijklmnopqrstuvwxyz")) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
