def minion_game(string):
    vowels = 'AEIOU'
    str_length = len(string) # Corrected the spelling of length
    kevin_score, stuart_score = 0, 0

    for i in range(str_length):
        if string[i] in vowels: # s could not be accessed, used the variable in the parenthesis
            kevin_score += (str_length - i)
        else:
            stuart_score += (str_length - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
