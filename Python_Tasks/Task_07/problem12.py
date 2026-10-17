# Problem 12 : Making Anagrams
# HackerRank Link : https://www.hackerrank.com/challenges/making-anagrams/problem

def makingAnagrams(s1, s2):
    count = 0

    for char in set(s1 + s2):
        count += abs(s1.count(char) - s2.count(char))

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
