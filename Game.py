from random import random


class Game:
    # serverPoints = numarul de puncte pe care le-a marcat jucatorul care serveste
    # returnerPoints = numarul de puncte pe care le-a marcat jucatorul care returneaza
    # finalPoint = este o variabila booleana prin care determinam daca game-ul s-a terminat sau nu
    # winner = variabila booleana care returneaza true daca serverul a castigat game ul, False daca returner ul a castigat si None in caz contrat

    def __init__(self, serverPoints=0, returnerPoints=0, finalPoint=False):
        self.serverPoints = serverPoints
        self.returnerPoints = returnerPoints
        self.finalPoint = finalPoint
        self.winner = self.returnGameWinner()

    @staticmethod
    def transformPoint(number):
        if number == 0:
            return 0
        elif number == 1:
            return 15
        elif number == 2:
            return 30
        elif number == 3:
            return 40

    def returnGameWinner(self):

        while self.finalPoint is False:
            print("s:", self.transformPoint(self.serverPoints), " - r:", self.transformPoint(self.returnerPoints))
            if self.returnerPoints == 3 and self. serverPoints == 3:
                if self.playAdvantage():
                    self.serverPoints += 1
                    self.finalPoint = True
                    return True
                else:
                    self.finalPoint = True
                    self.returnerPoints += 1
                    return False

            elif self.serverPoints < 3 and self.returnerPoints < 3:
                self.Point()

            elif self.serverPoints == 3 and self.returnerPoints < 3:
                self.finalPoint = True
                return True
            elif self.returnerPoints == 3 and self.serverPoints < 3:
                self.finalPoint = True
                return False

    @staticmethod
    def playAdvantage():
        pointsServer = 0
        pointsReturner = 0
        while True:
            print("Play Advantage\n")
            print("s adv: ", pointsServer, " - r adv: ", pointsReturner)
            serverProbability = random()
            returnerProbability = random()

            if pointsServer == 0 and pointsReturner == 0:
                if serverProbability > returnerProbability:
                    pointsServer += 1
                elif returnerProbability > serverProbability:
                    pointsReturner += 1
            elif pointsServer != 0 and pointsReturner == 0:
                if serverProbability > returnerProbability:
                    pointsServer += 1
                    print("s adv: ", pointsServer, " - r adv: ", pointsReturner)
                    return True
                elif returnerProbability > serverProbability:
                    pointsReturner = 0
                    pointsServer = 0
            elif pointsReturner != 0 and pointsServer == 0:
                if returnerProbability > serverProbability:
                    pointsReturner += 1
                    print("s adv: ", pointsServer, " - r adv: ", pointsReturner)
                    return False
                elif serverProbability > returnerProbability:
                    pointsReturner = 0
                    pointsServer = 0

    def Point(self):
        serverProbability = random()
        returnerProbability = random()
        if serverProbability > returnerProbability:
            self.serverPoints += 1
        elif returnerProbability > serverProbability:
            self.returnerPoints += 1
        else:
            self.Point()
