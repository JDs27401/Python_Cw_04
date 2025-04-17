import string
import random

#zadanie 1
# Prosze napisać skrypt, który liczy za użytkownika. Ma on umożliwić użytkownikowi wprowadzenie liczby
# początkowej, liczby końcowej i wielkości odstępu między podanymi liczbami.

def calcAbs(x: int, y: int):
    return abs(x - y)

# print(calcAbs(5, 7))

#zadanie 2
# Proszę napisać skrypt, który wczytuje komunikat użytkownika, a następnie wypisuje go w odwrotnej kolejności.

def reverseInput():
    strin: string = input()
    print(strin[::-1])

# reverseInput()

# zadanie 3
# Proszę napisać grę, w której komputer wybiera losowo słowo, które gracz musi odgadnąć.
# Komputer informuje gracza, ile liter znajduje się w wybranym słowie.
# Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera jest zawarta w tym słowie.
# Komputer może odpowiedzieć tylko "tak"lub "nie". Gracz musi odgadnąć słowo.

def guessTheWord():
    words = []
    try:
        with open("words.txt", "r") as write:
            file = write
            for line in file:
              words.append(line.strip())
    except FileNotFoundError:
        print('Could not find file named words.txt')

    wordToGuess = words[random.randint(0, len(words) - 1)]
    print('The word is {} letters long.'.format(len(wordToGuess)))
    # print(wordToGuess)

    lifes = 5
    while lifes > 0:
        strin = input('Guess word: ')
        if strin == wordToGuess:
            print('You guessed it!')
            return
        else:
            lifes -= 1
            print('Incorrect! {} life(s) remain.'.format(lifes))
    print('You lost!')
    # print(words)

# guessTheWord()

#zadanie 4
def hangman():
    word = "blablabla"
    numberOfTries = 10

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

        strin1 = input('Column: ')
        strin2 = input('Row: ')

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

# XO()



#zadanie 8
# Napisz zgodnie z zasadami programowania obiektowego program, który umieszcza na przekątnej tablicy 10 × 10 liczby losowe od 0 do 9, a poza nią zera.
# Dodatkowo program oblicza sumę liczb znajdujących się na przekątnej. W programie skorzystaj z metod: zapelnijTablicę() i obliczSume().
# Pierwsza z nich wypełnia przekątną tablicy liczbami losowymi od 0 do 9; natomiast druga oblicza sumę liczb na przekątnej.

#trzeba napisać klasę matrix, a następnie dodać do niej 2 metody opsiane powyrzej
# def matrix():
