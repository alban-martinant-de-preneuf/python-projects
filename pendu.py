import random

with open("dico_france.txt", "r", encoding='ISO-8859-15') as dico:
    dicoList = dico.readlines()


#Enlever les \n, les majuscules, les accents, remplacer caractères spéciaux
forbChar = ("ÀÁÂÆÇÈÉÊËÌÍÎÏÑÒÓÔŒÙÚÛÜÝŸàáâæçèéêëìíîïñòóôœùúûüýÿ\nABCDEFGHIJKLMNOPQRSTUVWXYZ") 
correspondForChar = {
    "À" : "a",
    "Á" : "a",
    "Â" : "a",
    "Æ" : "ae",
    "Ç" : "c",
    "È" : "e",
    "É" : "e",
    "Ê" : "e",
    "Ë" : "e",
    "Ì" : "i",
    "Í" : "i",
    "Î" : "i",
    "Ï" : "i",
    "Ñ" : "n",
    "Ò" : "o",
    "Ó" : "o",
    "Ô" : "o",
    "Œ" : "oe",
    "Ù" : "u",
    "Ú" : "u",
    "Û" : "u",
    "Ü" : "u",
    "Ý" : "y",
    "Ÿ" : "y",
    "à" : "a",
    "á" : "a",
    "â" : "a",
    "æ" : "ae",
    "ç" : "c",
    "è" : "e",
    "é" : "e",
    "ê" : "e",
    "ë" : "e",
    "ì" : "i",
    "í" : "i",
    "î" : "i",
    "ï" : "i",
    "ñ" : "n",
    "ò" : "o",
    "ó" : "o",
    "ô" : "o",
    "œ" : "oe",
    "ù" : "u",
    "ú" : "u",
    "û" : "u",
    "ü" : "u",
    "ý" : "y",
    "ÿ" : "y",
    "\n" : "",
    "A" : "a",
    "B" : "b",
    "C" : "c",
    "D" : "d",
    "E" : "e",
    "F" : "f",
    "G" : "g",
    "H" : "h",
    "I" : "i",
    "J" : "j",
    "K" : "k",
    "L" : "l",
    "M" : "m",
    "N" : "n",
    "O" : "o",
    "P" : "p",
    "Q" : "q",
    "R" : "r",
    "S" : "s",
    "T" : "t",
    "U" : "u",
    "V" : "v",
    "W" : "w",
    "X" : "x",
    "Y" : "y",
    "Z" : "z",
    }

for i in range(0, len(dicoList)):
    tmpWord = []
    for letter in dicoList[i]:
        tmpWord.append(letter)
    for j in range(0, len(tmpWord)):
        if tmpWord[j] in forbChar:
            tmpWord[j] = correspondForChar[tmpWord[j]]
    dicoList[i] = "".join(tmpWord)


#fonction qui extraire les mots du nombre de lettre demandé :
def wordsWithXLetters(chosedNumber):
    filteredList = []
    for word in dicoList:
        nbOfLetters = 0
        for _ in word:
            nbOfLetters += 1
        if nbOfLetters == chosedNumber:
            filteredList.append(word)
    return filteredList


#Choix du niveau :
level = 0
nbOfLifes = 0
wordToGuess = ""
while not ( level <= 3 and level >= 1) or level == 0:
    print("Bonjour, à quel niveau souhaites tu jouer ?")
    level = int(input("Débutant : 1, intermédiaire : 2, expert : 3): "))

    #A décommenter pour permettre le choix de la taille des mots
    # wordSize = 0
    # while wordSize < 2 or wordSize > 10:
    #     wordSize = int(input("Quel taille de mot voulez-vous tenter deviner ? (entre 2 et 10) "))
    # dicoList = wordsWithXLetters(wordSize)

    wordToGuess = ""
    match level:
        case 1:
            wordToGuess = dicoList[random.randint(0, len(dicoList))]
            nbOfLifes = 10
        case 2:
            wordToGuess = dicoList[random.randint(0, len(dicoList))]
            nbOfLifes = 7
        case 3:
            wordToGuess = dicoList[random.randint(0, len(dicoList))]
            nbOfLifes = 4

#Affichage :
win = False
proposedLetters = ""
while not win and nbOfLifes > 0:
    print("Nombre de vie(s) restante(s) : " + str(nbOfLifes))
    print("Lettre(s) proposée(s) : " + proposedLetters)
    print(wordToGuess)
    
    for letter in wordToGuess:
        if letter in proposedLetters:
            print(" " + letter + " ", end="")
        elif letter == " " or letter == "'" or letter == "-":
            print(" " + letter + " ", end="")
        else:
            print(" _ ", end="")
    print("\n")

    proposition = input("Quelle lettre proposes tu ? ")
    proposedLetters += proposition
    if proposition not in wordToGuess:
        nbOfLifes -=1

    win = True
    for letter in wordToGuess:
        if letter != " ":
            if letter not in proposedLetters:
                win = False
                break

print("")
if win:
    print("Bravo, tu as gagné !")
else:
    print("Tu as perdu :(")
    print("La réponse était \"" + wordToGuess + "\"")
