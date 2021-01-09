from Set import Set


class Match:
    listSets = []

    def __init__(self, sets=0, targetSets=2, setsPlayer1=0, setsPlayer2=0):
        self.sets = sets
        self.targetSets = targetSets
        self.setsPlayer1 = setsPlayer1
        self.setsPlayer2 = setsPlayer2
        self.winner = self.getWinner()

    def getWinner(self):
        print("---------------------------------------------->Start Match")
        while True:
            # print("ceva se intampla")
            newSet = Set(0, 6, 6, 7)
            self.listSets.append(newSet)
            # print("ceva se intampla2")
            if newSet.gamesCastigatePlayer1 > newSet.gamesCastigatePlayer2:
                self.setsPlayer1 += 1
                print("\n---------------------------------------------->Punctaj set:" + str(newSet.gamesCastigatePlayer1) + " - " + str(newSet.gamesCastigatePlayer2))
            else:
                self.setsPlayer2 += 1
                print("\n---------------------------------------------->Punctaj set:" + str(newSet.gamesCastigatePlayer1) + " - " + str(newSet.gamesCastigatePlayer2))

            if self.setsPlayer1 == self.targetSets:
                return True
            elif self.setsPlayer2 == self.targetSets:
                return False

    def playMatch(self, player1, player2):
        if self.winner is True:
            return player1
        else:
            return player2
