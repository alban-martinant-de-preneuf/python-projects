#Chargement des anciens utilisateurs et scores :
users = []
try:
    with open("scores.txt", "r+") as scores:
        for line in scores:
            user = line.split(", ")
            users.append({"name" : user[0], "score" : int(user[1])})
except:
    pass

def displayTable(table):
    for line in table:
        for char in line:
            print(char, end="")
        print("")

def displayScores():
    for user in users:
        print("{0} : {1} point(s)".format(user["name"], user["score"]))

def checkWinner(table, users):
    for user in users:
        symbol = user["symbol"]
        #Vérification des lignes
        for i in range(len(table)):
            if table[i][0] == symbol and table[i][1] == symbol and table[i][2] == symbol:
                return user["name"]
        #vérification des colonnes
        for j in range(len(table[i])):
            if table[0][j] == symbol and table[1][j] == symbol and table[2][j] == symbol:
                return user["name"]
        #Vérification des diagonales
        diagonal1 = table[0][0] == symbol and table[1][1] == symbol and table[2][2] == symbol
        diagonal2 = table[0][2] == symbol and table[1][1] == symbol and table[2][0] == symbol
        if diagonal1 or diagonal2:
            return user["name"]
    #vérification si terminé et aucun gagnant
    noWinner = True
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == " - ":
                noWinner = False
    if noWinner:
        return "no winner"
    #Le jeu peut continuer si il n'y a pas de gagnants et qu'il reste des cases
    return "continue"


def displayResults(result, users):
    for user in users:
        if result == user["name"]:
            print("Bravo " + user["name"])
    if result == "no winner":
        print("Match nul")


def play():
    player1 = (input("Username 1 Croix : "))
    player2 = (input("Username 2 Rond : "))

    players = []

    player1WasIn = False
    for user in users:
        if user["name"] ==  player1:
            user["symbol"] = " X "
            players.append(user)
            player1WasIn = True

    player2WasIn = False
    for user in users:
        if user["name"] ==  player2:
            user["symbol"] = " O "
            players.append(user)
            player2WasIn = True

    if not player1WasIn:
        users.append({"symbol" : " X "})
        users[-1]["name"] = player1
        users[-1]["score"] = 0
        players.append(users[-1])

    if not player2WasIn:
        users.append({"symbol" : " O "})
        users[-1]["name"] = player2
        users[-1]["score"] = 0
        players.append(users[-1])
    
    table = [
        [" - ", " - ", " - "],
        [" - ", " - ", " - "],
        [" - ", " - ", " - "],
        ]

    displayTable(table)

    #Tant que la partie n'est pas terminé
    while checkWinner(table, players) == "continue":
        for i in range(2):
            #True tant qu'aucune nouvelle case n'est joué
            while True:
                #Redemander tant que les coordonnés sont invalides
                isvalid = False
                while not isvalid:
                    coordinates = input(players[i]["name"] + " joue (ligne puis colonne : ")
                    x = int(coordinates[0]) - 1
                    y = int(coordinates[-1]) -1
                    xOK = x >= 0 and x <= 2
                    yOK = y >= 0 and y <= 2

                    if xOK and yOK:
                        isvalid = True

                #Vérifier si la case est déjà joué :        
                if table[x][y] == " - ":
                    break
                else:
                    print("Déjà Joué !")

            #Enregistrer le nouveau symbol dans le tableau
            table[x][y] = players[i]["symbol"]

            displayTable(table)

            if checkWinner(table, players) != "continue":
                break
    
    winner = checkWinner(table, players)

    #Incrémenter les scores:
    for user in users:
        if user["name"] == winner:
            user["score"] += 1
            #Enregistrer les scores:
            with open("scores.txt", "w+") as scores:
                for user in users:
                    scores.write(user["name"] + ", " + str(user["score"]) + "\n")

    #Afficher les scores :
    displayResults(winner, users)

    
#programme principal :
wantExit = "N"
while wantExit == "N":
    userWantTo = ""
    while userWantTo != "jouer" and userWantTo != "scores" and userWantTo != "exit":
        userWantTo = input("Bonjour, souhaites tu <jouer> ou voir les <scores> ? ( <exit> pour quitter ) : ")

    match userWantTo:
        case "jouer":
            play()
        case "scores":
            displayScores()
        case "exit":
            exit()
    
    wantExit = input("Une autre partie ? (O/N) : ")