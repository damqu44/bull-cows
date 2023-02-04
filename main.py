
import random
import os

redFont = '\x1b[38;2;255;0;0m'
greenFont = '\x1b[38;2;124;252;0m'

words = [
    'karp', 'kura', 'foka', 'port', 'mowa', 'woda', 'krem', 'plan', 'lody', 'wiek', 'moda', 'duch', 'sowa', 'luty', 'blog', 'czar', 'metr', 'huta', 'blat', 'msza', 'hymn', 'wilk', 'dres', 'klej', 'loch', 'soda'
]


randomWord = random.sample(words, 1)
randomWordCharsList = []
# print(randomWord)

for char in randomWord:
    randomWordCharsList.append(char)


def isDuplicate(charsList):
    if len(charsList) == len(set(charsList)):
        return True
    else:
        return False


def checkBullsAndCows(charsList):
    bulls = 0
    cows = 0
    for x in charsList:
        n = charsList.index(x)
        if charsList[n] == char[n]:
            bulls = bulls + 1
        elif charsList[n] in randomWordCharsList:
            cows = cows + 1
    print('\n Bulls: ', bulls, 'Cows: ', cows)
    return bulls


def makingCharsList():
    userWords = input('\n Podaj 4 litery: ')
    charsList = []
    for char in userWords:
        if char.isalpha():
            charsList.append(char)
        else:
            return False
    return charsList


def checkTriesAndUserWord(tries):
    while tries > 0:
        charsList = makingCharsList()

        if charsList == False:
            os.system('cls')
            print('\n Podaj tylko litery, inne znaki są niedozwolone. Spróbuj ponownie.')
            continue

        if not isDuplicate(charsList):
            os.system('cls')
            print('\n Litery nie mogą się powtarzać. Spróbuj ponownie. ')
            continue

        if len(charsList) != 4:
            os.system('cls')
            print('\n Podaj dokładnie 4 litery. Spróbuj ponownie. ')
            continue

        bullsAmount = checkBullsAndCows(charsList)
        tries = tries - 1
        print('\n Pozostałe próby:', tries)

        if bullsAmount == 4:
            print('\n Zgadłeś ukryte słowo! Gratulacje!')
            input()
            break

    else:
        print('\n Skończyły ci się próby. Przegrałeś!')
        print('\n Ukryte słowo to: ', randomWord)
        input()


def printInfo():
    print('\n Odkryj ukryte słowo!')
    print('\n Bulls = poprawny kod, poprawna pozycja.')
    print('\n Cows = poprawny kod, zła pozycja.')
    tries = input('\n Podaj liczbę prób: ')

    inputCheck = True
    while inputCheck == True:
        if tries.isdigit():
            tries = int(tries)
            checkTriesAndUserWord(tries)
            inputCheck = False
        else:
            os.system('cls')
            tries = input("\n Podaj LICZBĘ prób: ")
            continue


printInfo()
