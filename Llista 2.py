import string
import random


#zadanie 1
# Prosze napisać skrypt, który liczy za użytkownika. Ma on umożliwić użytkownikowi wprowadzenie liczby
# początkowej, liczby końcowej i wielkości odstępu między podanymi liczbami.

def calcAbs(x: int, y: int):
    return abs(x - y) #obliczenie odległości pomiędzy liczbami na osi liczbowej za pomocą odjęcia liczy y od z i uzycie funkcji abs(wartość bezwzględna) w celu uzyskania dystansu (wartości dodatniej)

# print(calcAbs(5, 7))

#zadanie 2
# Proszę napisać skrypt, który wczytuje komunikat użytkownika, a następnie wypisuje go w odwrotnej kolejności.

def reverseInput():
    strin: string = input() #pobranie wyrazu od użytkownika
    print(strin[::-1]) #wyświetlenie odwróconego wyrazu pobranego od użytkownika

# reverseInput()

# zadanie 3
# Proszę napisać grę, w której komputer wybiera losowo słowo, które gracz musi odgadnąć.
# Komputer informuje gracza, ile liter znajduje się w wybranym słowie.
# Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera jest zawarta w tym słowie.
# Komputer może odpowiedzieć tylko "tak"lub "nie". Gracz musi odgadnąć słowo.

def guessTheWord():
    words = []
    #wczytanie słów z pliku z użyciem bloku try-except
    try:
        with open("words.txt", "r") as write:
            file = write
            for line in file:
              words.append(line.strip())
    except FileNotFoundError:
        print('Could not find file named words.txt')

    #wylosowanie słowa z tablicy words z wcześniej wczytanymi słowami
    wordToGuess = words[random.randint(0, len(words) - 1)]
    print(f'The word is {len(wordToGuess)} letters long.')
    # print(wordToGuess)

    #program pobiera słowo od użytkownika, jeżeli słowo się zgadza, gracz wygrywa; w przeciwnym razie program wyświetla informację, że słowo się nie zgadza i zmniejsza życia o 1
    lifes = 5
    while lifes > 0:
        strin = input('Guess word: ')
        if strin == wordToGuess:
            print('You guessed it!')
            return
        else:
            lifes -= 1
            print(f'Incorrect! {lifes} life(s) remain.')
    print('You lost!')

# guessTheWord()

#zadanie 4
def hangman():
    words = []
    #wczytanie słów z pliku z użyciem bloku try-except
    try:
        with open("words.txt", "r") as write:
            file = write
            for line in file:
              words.append(line.strip())
    except FileNotFoundError:
        print('Could not find file named words.txt')

    #wylosowanie słowa z tablicy words z wcześniej wczytanymi słowami
    wordToGuess = words[random.randint(0, len(words) - 1)]
    # print(wordToGuess)

    #życia
    numberOfTries = 10

    #wypełniamy tablicę którą będziemy wypełniać literami '_'
    result = ['_' for i in wordToGuess]
    print(result)

    #pętla działa dopóki mamy życia
    while numberOfTries > 0:
        #pobranie słowa od
        strin = input('Input a letter or guess a word: ')

        #jezeli litera znajduje się w zgadywanym słowie
        if strin in wordToGuess:
            #to umieszczamy ją na odpowiednim miejscu
            for i in range(0, len(wordToGuess)):
                if wordToGuess[i] == strin:
                    result[i] = wordToGuess[i]
        #w przeciwnym razie odejmujemy jedno życie
        else:
            numberOfTries -= 1

        print(result)
        print("Number of tries left: " + str(numberOfTries))

        #sprawdzamy czy nasza tablica result jest równa naszemu słowu który jest rzutowane do tablicy, jak to program się kończy
        #jeżeli jest, to gracz wygrywa
        if  result == list(wordToGuess):
            print("you won!")
            return
    #jeżeli pętla dojdzie do końca, to gracz przegrywa
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

    #funkcja spradzająca czy aktualny gracz nie wygrał
    def check():
        nonlocal moves
        #kolumny
        for i in range(0, 2):
            if (game[0][i] == player != '-') and (game[1][i] == player != '-') and (game[2][i] == player != '-'):
                print(player + " won!")
                moves = 9

        #wiersze
        for i in range(0, 2):
            if (game[i][0] == player != '-') and (game[i][1] == player != '-') and (game[i][2] == player != '-'):
                print(player + " won!")
                moves = 9

        #przekątna nr z lewej-góra do prawej-dół
        if (game[0][0] == player != '-') and (game[1][1] == player != '-') and (game[2][2] == player != '-'):
            print(player + " won!")
            moves = 9

        #przekątna z prawej-góra do lewej-dół
        if (game[0][2] == player != '-') and (game[1][1] == player != '-') and (game[2][0] == player != '-'):
            print(player + " won!")
            moves = 9

    print(str(game[0]) + '\n' + str(game[1]) + '\n' + str(game[2]))

    #gra toczy się do wygrania jednego z graczy albo do wykonania 9 ruchów
    while moves < 9:

        #gracz wybiera gdzie wstawić swój znaczek za pomocą słów
        strin1 = input('Column: ')
        strin2 = input('Row: ')

        #sprawdzamy czy pole jest wolne, jak jest to umieszczamy znacznik
        if game[rows[strin2]][cols[strin1]] == '-':
            game[rows[strin2]][cols[strin1]] = player
            #zwiększamy ruch jeżeli ruch był legalny
            moves += 1
        else:
            #jeżeli nie jest to legalny ruch, informujemy o tym gracz, tura nie zostaje zwiększona, a znaczek nie ulega zmianie (gracz może naprawić swój błąd)
            print("Illegal move!")

        print(str(game[0]) + '\n' + str(game[1]) + '\n' + str(game[2]))
        check()

        #zmieniamy znaczek gracza w zależnoci od tury
        if moves % 2 != 0:
            player = 'O'
        else:
            player = 'X'

# XO()

#zadanie 6
# Stwórz klasę Pojazd z atrybutami prędkość maksymalna i aktualna prędkość. Dodaj metody do przyspieszania i hamowania pojazdu.
# Następnie stwórz podklasy takie jak Samochod i Rower, które mają dodatkowe specyficzne metody (np. włączenie świateł dla samochodu).

class Pojazd:
    #konstruktor gdzie ustawiamy aktualną prędkości jak i prędkości maksymalną
    def __init__(self, speed, maxSpeed):
        self.speed = speed
        self.maxSpeed = maxSpeed

    #funckcja do przyśpieszania
    def speedUp(self, addSpeed):
        self.speed += addSpeed

    #funkcja do zwalniania
    def slowDown(self, removeSpeed):
        self.speed -= removeSpeed

#klasa dziedzicząca nr 1
class Rower(Pojazd):
    def __init__(self, speed, maxSpeed):
        super().__init__(speed, maxSpeed)

    #metoda klasy, która wydaje dźwiek dzwonka
    def useSoundSignal(self):
        print("drynn drynn!")

#klasa dziedzicząca nr 2
class Samochód(Pojazd):
    def __init__(self, speed, maxSpeed):
        super().__init__(speed, maxSpeed)
        self.lights = False

    #funkcja do przełączania świateł w samochodzie
    def cycleLights(self):
        if self.lights:
            self.lights = False
        else:
            self.lights = True

# samochód = Samochód(0, 250)
# samochód.speedUp(10)
# print(samochód.speed)
#
# rower = Rower(0, 45)
# rower.speedUp(15)
# rower.useSoundSignal()

# zadanie 7
# Stwórz klasę Uzytkownik z atrybutami login, hasło i email. Dodaj metody do zmiany hasła oraz sprawdzania poprawności hasła (np. czy ma odpowiednią długość).
# Następnie stwórz klasę SystemUzytkownikow, która pozwala na dodawanie nowych użytkowników oraz logowanie się przez podanie loginu i hasła.

class Uzytkownik:
    #konstruktor gdzie ustawiamy nazwę użytkownika, hasłó i email, jednocześnie sprawdzając czy hasło ma przynajmniej 8 znaków
    def __init__(self, username, password, email):
        self.meetsRequirements(password)
        self.username = username
        self.password = password
        self.email = email

    #metoda klasowa (statyczna) do sprawdzania czy hasło ma przynajmniej 8 znaków, jak nie ma to podnosi wyjątek
    @staticmethod
    def meetsRequirements(string):
        if len(string) < 8:
            raise AttributeError('Password is too short!')

    #metoda do zmiany hasła
    def changePassword(self, newPassword):
        self.meetsRequirements(newPassword)
        self.password = newPassword

class SystemUzytkownikow:
    #konstruktor w którym tworzymy pusty słownik na użytkowników i ustawiamy aktywnego użytkownika na None
    def __init__(self):
        self.users = {}
        self.activeUser = None

    def showUsers(self):
        for username, user in self.users.items():
            print(f'username: {username}, email: {user.email}')

    def showActiveUser(self):
        print(f'Active user: {self.activeUser.username}')

    #metoda do dodawania użytkowników do słownika w obiekcie tej klasy, gdzie kluczem jest username, a wartością obiekt użytkownika
    def addUser(self, user: Uzytkownik):
        self.users[user.username] = user

    #metoda służąca do logowania
    def login(self, username, password):
        #sprawdzamy czy w słowniku jest podany username
        if username in self.users:
            #sprawdzamy czy hasło użytkowanika zgadza się z podanym hasłem
            if self.users[username].password == password:
                #jak tak, to ustawiamy na aktywnego użytkownika, użytkownika odczytanego ze słownika za pomoca klucza username
                self.activeUser = self.users[username]
                print('Login successful!')
            else:
                print('Password is incorrect!')
        else:
            print('Username is incorrect!')

# system1 = SystemUzytkownikow()
# user1 = Uzytkownik('dd', 'dddddddd', 'dd@dd.dd')
# system1.addUser(user1)
# system1.showUsers()
# system1.login('dd', 'dddddddd')
# system1.showActiveUser()

#zadanie 8
# Napisz zgodnie z zasadami programowania obiektowego program, który umieszcza na przekątnej tablicy 10 × 10 liczby losowe od 0 do 9, a poza nią zera.
# Dodatkowo program oblicza sumę liczb znajdujących się na przekątnej. W programie skorzystaj z metod: zapelnijTablicę() i obliczSume().
# Pierwsza z nich wypełnia przekątną tablicy liczbami losowymi od 0 do 9; natomiast druga oblicza sumę liczb na przekątnej.

class Matrix:
    #konstruktor inicjujący pustą tablicę 10 x 10
    def __init__(self):
        self.matrix = [[None for empty in range(10)] for empty in range(10)]

    #metoda służaca do wypełnienia tablicy zgodnie z treścią zadania
    def fillMatrix(self):
        for i in range(10):
            for j in range(10):
                if i == j:
                    #na przekątnej znajdzie się wylosowana liczba z przedziału 0-9
                    self.matrix[i][j] = random.randint(0, 9)
                else:
                    #a w pozostałych polach liczba 0
                    self.matrix[i][j] = 0

    def printMatrix(self):
        for i in self.matrix:
            print(f'{i}')
        # for i, row in enumerate(self.matrix):
        #     line = ""
        #     for j, val in enumerate(row):
        #         if i == j:
        #             # kolorowanie prezkątnej
        #             line += f"\033[92m{val:^3}\033[0m "  # 92 = zielony, ^3 = wyśrodkowanie w szerokości 3
        #         else:
        #             line += f"{val:^3} "
        #     print(line)

    #metoda sumująca liczby na przekątnej
    def countDiag(self):
        sum = 0
        for i in range(10):
            sum += self.matrix[i][i]
        return sum

# matrix1 = Matrix()
# matrix1.fillMatrix()
# matrix1.printMatrix()
# print(matrix1.countDiag())