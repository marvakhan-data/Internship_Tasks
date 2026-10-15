# Problem 18: The Minion Game
# Link: https://www.hackerrank.com/challenges/the-minion-game/problem



def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)
