from random import random
from Game import Game


class Set:

    # games = numarul de game-uri jucate in setul curent
    # targetGames = numarul de jocuri necesare pentru a castiga setul
    # tiebreakGames = numarul de game-uri pe care fiecare jucator trebuie sa il aiba pt a se juca tiebreak
    # tiebreakPoints = numarul de puncte necesare pentru a castiga tiebreakul
    # winner = variabila booleana care este True atunci cand primul jucator castiga setul si False cand setul este castigat de cel de-al doilea jucator
    first_server_to_serve = True
    listaGames = []
    listaGamesPlayer1 = []
    listaGamesPlayer2 = []
    gamesCastigatePlayer1 = 0
    gamesCastigatePlayer2 = 0
    tiebreakPointsPlayer1 = 0
    tiebreakPointsPlayer2 = 0
    finalSet = False

    def __init__(self, games=0, targetGames=6, tiebreakGames=6, tiebreakPoints=7):
        if targetGames < 0:
            raise RuntimeError('Numarul de game-uri nu poate fi negativ')
        if (tiebreakGames is None) != (tiebreakPoints is None):
            raise RuntimeError('ambele variabile trebuie sa fie Nule sau ambele trebuie sa aiba valoare')

        self.games = games
        self.targetGames = targetGames
        self.tiebreakGames = tiebreakGames
        self.tiebreakPoints = tiebreakPoints
        self.winner = self.returnSetWinner()

    def Point(self):
        serverProbability = random()
        returnerProbability = random()
        if serverProbability > returnerProbability:
            self.tiebreakPointsPlayer1 += 1
        elif returnerProbability > serverProbability:
            self.tiebreakPointsPlayer2 += 1
        else:
            self.Point()

    def playTiebreak(self):
        while True:
            print("tiebreak server: ", self.tiebreakPointsPlayer1," - ",self.tiebreakPointsPlayer2,' tiebreak returner')
            if(self.tiebreakPointsPlayer1 > 20):
                self.tiebreakPointsPlayer1 = 0
                self.tiebreakPointsPlayer1 = 0
            if self.tiebreakPointsPlayer1 >= self.tiebreakPoints:
                if self.tiebreakPointsPlayer1 - self.tiebreakPointsPlayer2 >= 2:
                    newGame = Game(self.tiebreakPointsPlayer1, self.tiebreakPointsPlayer2, True)
                    self.listaGames.append(newGame)

                    return True
                else:
                    self.Point()
            elif self.tiebreakPointsPlayer1 < self.tiebreakPoints:
                if self.tiebreakPointsPlayer2 < self.tiebreakPoints:
                    self.Point()
                elif self.tiebreakPointsPlayer2 >= self.tiebreakPoints:
                    if self.tiebreakPointsPlayer2 - self.tiebreakPointsPlayer1 >= 2:
                        newGame = Game(self.tiebreakPointsPlayer1, self.tiebreakPointsPlayer2, True)
                        self.listaGames.append(newGame)
                        return False
                    else:
                        self.Point()

    def returnFirstServer(self):
        probabilityPlayer1 = random()
        probabilityPlayer2 = random()
        if probabilityPlayer1 > probabilityPlayer2:
            return True
        elif probabilityPlayer2 > probabilityPlayer1:
            return False
        else:
            self.returnFirstServer()

    def returnSetWinner(self):
        self.first_server_to_serve = self.returnFirstServer()

        if self.first_server_to_serve == True:
            print("Incepe sa serveasca primul jucator")
        else:
            print("Incepe sa serveasca al doilea jucator")


        while self.gamesCastigatePlayer2 < 7 and self.gamesCastigatePlayer1 < 7:
            print("---------------------------------------------->ScorGames:  Player1 ", self.gamesCastigatePlayer1, " - ", self.gamesCastigatePlayer2," Player2" )

            if self.gamesCastigatePlayer1 == 6:
                if self.gamesCastigatePlayer2 == 6:
                    variabilaTiebreak = self.playTiebreak()
                    self.finalSet = True
                    if self.first_server_to_serve is True:
                        if variabilaTiebreak is True:
                            self.gamesCastigatePlayer1 += 1
                            return True
                        else:
                            self.gamesCastigatePlayer2 += 1

                            return False
                    else:
                        if variabilaTiebreak is True:
                            self.gamesCastigatePlayer2 += 1
                            return False
                        else:
                            self.gamesCastigatePlayer1 += 1
                            return True
                if self.gamesCastigatePlayer1 - self.gamesCastigatePlayer2 >= 2:
                    return True

                if self.gamesCastigatePlayer1 - self.gamesCastigatePlayer2 < 2:
                    if self.first_server_to_serve is True:
                        newGame = Game(0, 0, False)
                        self.listaGames.append(newGame)
                        if newGame.winner is True:
                            self.gamesCastigatePlayer1 += 1
                        else:
                            self.gamesCastigatePlayer2 += 1
                        self.first_server_to_serve = False
                        print("\nServeste al doilea jucator")
                    else:
                        newGame = Game(0, 0, False)
                        self.listaGames.append(newGame)
                        if newGame.winner is True:
                            self.gamesCastigatePlayer2 += 1

                        else:
                            self.gamesCastigatePlayer1 += 1

                        self.first_server_to_serve = True
                        print("\nServeste primul jucator")

                if self.gamesCastigatePlayer2 > self.gamesCastigatePlayer1:
                    print("this is impossible")

            elif self.gamesCastigatePlayer2 == 6:
                if self.gamesCastigatePlayer1 == 6:
                    variabilaTiebreak = self.playTiebreak()
                    self.finalSet = True
                    if self.first_server_to_serve is True:
                        if variabilaTiebreak is True:
                            self.gamesCastigatePlayer1 += 1

                            return True
                        else:
                            self.gamesCastigatePlayer2 += 1

                            return False
                    else:
                        if variabilaTiebreak is True:
                            self.gamesCastigatePlayer2 += 1

                            return False
                        else:
                            self.gamesCastigatePlayer1 += 1

                            return True
                if self.gamesCastigatePlayer2 - self.gamesCastigatePlayer1 >= 2:

                    return False
                if self.gamesCastigatePlayer2 - self.gamesCastigatePlayer1 < 2:

                    if self.first_server_to_serve is True:
                        newGame = Game(0, 0, False)
                        self.listaGames.append(newGame)
                        if newGame.winner is True:
                            self.gamesCastigatePlayer1 += 1


                        else:
                            self.gamesCastigatePlayer2 += 1

                        self.first_server_to_serve = False
                        print("\nServeste al doilea jucator")
                    else:
                        newGame = Game(0, 0, False)
                        self.listaGames.append(newGame)
                        if newGame.winner is True:
                            self.gamesCastigatePlayer2 += 1

                        else:
                            self.gamesCastigatePlayer1 += 1
                            print("Player 1:", self.gamesCastigatePlayer1, " - Player2:", self.gamesCastigatePlayer2)

                        self.first_server_to_serve = True
                        print("\nServeste primul jucator")

                if self.gamesCastigatePlayer1 > self.gamesCastigatePlayer2:
                    print("this is impossible")

            elif self.gamesCastigatePlayer1 == 7:
                if self.gamesCastigatePlayer1 - self.gamesCastigatePlayer2 == 2:
                    print("Player 1:", self.gamesCastigatePlayer1, " - Player2:", self.gamesCastigatePlayer2)

                    return True
                else:
                    self.gamesCastigatePlayer2 = 0
                    self.gamesCastigatePlayer1 = 0
            elif self.gamesCastigatePlayer2 == 7:
                if self.gamesCastigatePlayer2 - self.gamesCastigatePlayer1 == 2:

                    return False
                else:
                    self.gamesCastigatePlayer2 = 0
                    self.gamesCastigatePlayer1 = 0

            elif self.gamesCastigatePlayer1 < 6:
                if self.gamesCastigatePlayer2 == 7:
                    if self.gamesCastigatePlayer2 - self.gamesCastigatePlayer1 == 2:

                        return False
                if self.gamesCastigatePlayer2 == 6:
                    if self.gamesCastigatePlayer2 - self.gamesCastigatePlayer1 >= 2:

                        return False
                if self.gamesCastigatePlayer2 < 6:
                    if self.first_server_to_serve is True:
                        newGame = Game(0, 0, False)
                        self.listaGames.append(newGame)
                        if newGame.winner is True:
                            self.gamesCastigatePlayer1 += 1

                        else:
                            self.gamesCastigatePlayer2 += 1

                        self.first_server_to_serve = False
                        print("\nServeste al doilea jucator")
                    else:
                        newGame = Game(0, 0, False)
                        self.listaGames.append(newGame)
                        if newGame.winner is True:
                            self.gamesCastigatePlayer2 += 1

                        else:
                            self.gamesCastigatePlayer1 += 1

                        self.first_server_to_serve = True
                        print("\nServeste primul jucator")

            elif self.gamesCastigatePlayer2 < 6:
                if self.gamesCastigatePlayer1 == 7:
                    if self.gamesCastigatePlayer1 - self.gamesCastigatePlayer2 == 2:

                        return True
                if self.gamesCastigatePlayer1 == 6:
                    if self.gamesCastigatePlayer1 - self.gamesCastigatePlayer2 >= 2:

                        return True
                if self.gamesCastigatePlayer1 < 6:
                    if self.first_server_to_serve is True:
                        newGame = Game(0, 0, False)
                        self.listaGames.append(newGame)
                        if newGame.winner is True:
                            self.gamesCastigatePlayer1 += 1


                        else:
                            self.gamesCastigatePlayer2 += 1

                        self.first_server_to_serve = False
                        print("\nServeste al doilea jucator")
                    else:
                        newGame = Game(0, 0, False)
                        self.listaGames.append(newGame)
                        if newGame.winner is True:
                            self.gamesCastigatePlayer2 += 1

                        else:
                            self.gamesCastigatePlayer1 += 1

                        self.first_server_to_serve = True
                        print("\nServeste primul jucator")


        return True

    def firstPlayerGames(self):
        return self.gamesCastigatePlayer1

    def secondPlayerGames(self):
        return self.gamesCastigatePlayer2
