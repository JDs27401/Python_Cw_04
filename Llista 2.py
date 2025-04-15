import string

#zadanie 1
# Prosze napisać skrypt, który liczy za użytkownika. Ma on umożliwić użytkownikowi wprowadzenie liczby
# początkowej, liczby końcowej i wielkości odstępu między podanymi liczbami.

def calcAbs(x: int, y: int):
    if x < y:
        return y - x
    elif y < x:
        return x - y
    elif x == y:
        return 0

# print(calcAbs(7, 7))

#zadanie 2
# Proszę napisać skrypt, który wczytuje komunikat użytkownika, a następnie wypisuje go w odwrotnej kolejności.

def reverseInput():
    strin: string = input()
    print(strin[::-1])

# reverseInput()

# zadanie 3



#zadanie 4
def hangman():
    word= "blablabla"
    numberOfTries= 10

    result = ['_' for i in word]
    print(result)

    while numberOfTries > 0:
        strin = input()
        # if strin in word:
        #     result = [strin if letter == strin else '_' for letter in word]
        # else:
        #     numberOfTries -= 1
        if strin in word:
            for i in range(0, len(word)):
                if word[i] == strin:
                    result[i] = word[i]
        else:
            numberOfTries -= 1

        print(result)
        print("Number of tries left: " + str(numberOfTries))

        if  result == list(word):
            print("you won!")
            return
    print("you lost!")

# hangman()

#zadanie 5
def XO():
    player = 'X'
    moves = 0

    game = [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]

    cols = {"left": 0,
            "center": 1,
            "right": 2}

    rows = {"top": 0,
            "center": 1,
            "bottom": 2}

    def check():
        nonlocal moves
        for i in range(0, 2):
            if (game[0][i] == player != '-') and (game[1][i] == player != '-') and (game[2][i] == player != '-'):
                print(player + " won!")
                moves = 9

        for i in range(0, 2):
            if (game[i][0] == player != '-') and (game[i][1] == player != '-') and (game[i][2] == player != '-'):
                print(player + " won!")
                moves = 9

        if (game[0][0] == player != '-') and (game[1][1] == player != '-') and (game[2][2] == player != '-'):
            print(player + " won!")
            moves = 9

        if (game[0][2] == player != '-') and (game[1][1] == player != '-') and (game[2][0] == player != '-'):
            print(player + " won!")
            moves = 9

    print(str(game[0]) + '\n' + str(game[1]) + '\n' + str(game[2]))

    while moves < 9:

        strin1 = input()
        strin2 = input()

        if game[rows[strin2]][cols[strin1]] == '-':
            game[rows[strin2]][cols[strin1]] = player
            moves += 1
        else:
            print("debil bo zajęte")

        print(str(game[0]) + '\n' + str(game[1]) + '\n' + str(game[2]))
        check()

        if moves % 2 != 0:
            player = 'O'
        else:
            player = 'X'

XO()