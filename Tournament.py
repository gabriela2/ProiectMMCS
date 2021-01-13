from Player import Player
from Match import Match
from math import log, ceil
import csv


class Tournament:
    myPlayers = []
    finalListWinners = []
    listWinnersFirstPart = []
    listWinnersFirstPart2 = []
    listWinnersSecondPart = []
    listWinnersSecondPart2 = []
    numberOfPlayers = 128
    listMatches = []
    winnerOfTheTournament = None

    @staticmethod
    def seed(n):
        ol = [1]
        for i in range(ceil(log(n) / log(2))):
            l = 2 * len(ol) + 1
            ol = [e if e <= n else 0 for s in [[el, l - el] for el in ol] for e in s]
        return ol

    def readPlayers(self):
        file1 = open("Players.txt", 'r')
        count = 0
        while True:
            count = count + 1
            line = file1.readline()
            element = line.split(',')
            element[3] = element[3].strip('\n')
            self.myPlayers.append(Player(element[1], element[0], element[2], element[3]))
            if count >= 128:
                break
        file1.close()
        # print(self.myPlayers)

    def splitPlayers(self):
        seedList = self.seed(self.numberOfPlayers)
        # print(seedList)
        length = len(seedList)
        middle_index = length // 2
        first_half = seedList[:middle_index]
        # print(first_half)
        second_half = seedList[middle_index:]
        # print(second_half)

        for i in first_half:
            for player in self.myPlayers:
                if player.getRank() == i:
                    self.listWinnersFirstPart.append(player)
                    self.finalListWinners.append(player)
        # print(self.listWinnersFirstPart)
        for i in second_half:
            for player in self.myPlayers:
                if player.getRank() == i:
                    self.listWinnersSecondPart.append(player)
                    self.finalListWinners.append(player)
        # print(self.listWinnersSecondPart)

    def getWinner(self):
        for j in range(7):
            if j == 0:
                print("\n\n*******************\n*     TURUL 1     *\n*******************\n")
            elif j == 1:
                print("\n\n*******************\n*     TURUL 2     *\n*******************\n")
            elif j == 2:
                print("\n\n*******************\n*     TURUL 3     *\n*******************\n")
            elif j == 3:
                print("\n\n*******************\n*     OPTIMI      *\n*******************\n")
            elif j == 4:
                print("\n\n*******************\n*    SFERTURI     *\n*******************\n")
            elif j == 5:
                print("\n\n*******************\n*   SEMI-FINALA   *\n*******************\n")
            else:
                print("\n\n*******************\n*     FINALA      *\n*******************\n")

            if j == 0:
                # FIRST PART
                print("\nPRIMA PARTE A TABELULUI")
                for i in range(0, pow(2, 6 - j)-1, 2):
                    # match = Match(0,2,0,0)
                    winner = (Match(0, 2, 0, 0).playMatch(self.listWinnersFirstPart[i], self.listWinnersFirstPart[i + 1]))
                    self.listWinnersFirstPart2.append(winner)
                    self.finalListWinners.append(winner)

                    print("Castigatorul dintre " + self.listWinnersFirstPart[i].firstName + " " + self.listWinnersFirstPart[i].lastName + " si " + self.listWinnersFirstPart[i + 1].firstName + " " + self.listWinnersFirstPart[i + 1].lastName + " este: " + winner.firstName + " " + winner.lastName + "\n\n\n")
                    # print("scorul a fost " + match.listSets[0].firstPlayerGames()+' - '+match.listSets[0].secondPlayerGames()+" ; " + + match.listSets[1].firstPlayerGames()+' - '+match.listSets[1].secondPlayerGames()+"  ; "++ match.listSets[2].firstPlayerGames()+' - '+match.listSets[2].secondPlayerGames())

                # SECOND PART
                print("\nA DOUA PARTE A TABELULUI")
                for i in range(0, pow(2, 6 - j)-1, 2):
                    match = Match(0, 2, 0, 0)
                    winner = match.playMatch(self.listWinnersSecondPart[i], self.listWinnersSecondPart[i + 1])
                    self.listWinnersSecondPart2.append(winner)
                    self.finalListWinners.append(winner)

                    print("Castigatorul dintre " + self.listWinnersSecondPart[i].firstName + " " + self.listWinnersSecondPart[i].lastName + " si " + self.listWinnersSecondPart[i + 1].firstName + " " + self.listWinnersSecondPart[i + 1].lastName + " este: " + winner.firstName + " " + winner.lastName + "\n\n\n")
            else:

                self.listWinnersFirstPart = self.listWinnersFirstPart2.copy()
                self.listWinnersSecondPart = self.listWinnersSecondPart2.copy()
                del self.listWinnersFirstPart2[:]
                del self.listWinnersSecondPart2[:]
                if j != 6:

                    # FIRST PART
                    print("\nPRIMA PARTE A TABELULUI")
                    for i in range(0, pow(2, 6 - j)-1, 2):
                        winner = Match(0, 2, 0, 0).playMatch(self.listWinnersFirstPart[i], self.listWinnersFirstPart[i + 1])
                        self.listWinnersFirstPart2.append(winner)
                        self.finalListWinners.append(winner)

                        print("Castigatorul dintre " + self.listWinnersFirstPart[i].firstName + " " + self.listWinnersFirstPart[i].lastName + " si " + self.listWinnersFirstPart[i + 1].firstName + " " + self.listWinnersFirstPart[i + 1].lastName + " este: " + winner.firstName + " " + winner.lastName + "\n\n\n")

                    # SECOND PART
                    print("\nA DOUA PARTE A TABELULUI")
                    for i in range(0, pow(2, 6 - j)-1, 2):
                        winner = Match(0, 2, 0, 0).playMatch(self.listWinnersSecondPart[i], self.listWinnersSecondPart[i + 1])
                        self.listWinnersSecondPart2.append(winner)
                        self.finalListWinners.append(winner)

                        print("Castigatorul dintre " + self.listWinnersSecondPart[i].firstName + " " + self.listWinnersSecondPart[i].lastName + " si " + self.listWinnersSecondPart[i + 1].firstName + " " + self.listWinnersSecondPart[i + 1].lastName + " este: " + winner.firstName + " " + winner.lastName+ "\n\n\n")

                else:
                    winner = Match(0, 2, 0, 0).playMatch(self.listWinnersFirstPart[0], self.listWinnersSecondPart[0])
                    self.finalListWinners.append(winner)
                    self.winnerOfTheTournament = winner

                    print("Castigatorul turneului dintre:" + self.listWinnersFirstPart[0].firstName + " "
                          + self.listWinnersFirstPart[0].lastName + " si " + self.listWinnersSecondPart[0].firstName + " "
                          + self.listWinnersSecondPart[0].lastName + " este: " + winner.firstName + " " + winner.lastName+ "\n")

    def writeCSV(self):
        with open('tennis_tournament.csv', mode='w') as tennis_file:
            tennis_writer = csv.writer(tennis_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            tennis_writer.writerow(['FirstName', 'LastName', 'Country', 'Rank'])
            for player in self.finalListWinners:
                tennis_writer.writerow([player.firstName, player.lastName, player.country, player.rank])

    def startTournament(self):
        self.readPlayers()
        self.splitPlayers()
        self.getWinner()
        self.writeCSV()
        return self.winnerOfTheTournament.firstName + " " + self.winnerOfTheTournament.lastName

