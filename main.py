from Tournament import Tournament
from matplotlib import pyplot as plt
import datetime
import  numpy as np

def main():
    statistics = {}
    i = int(input('Alegeti:\n\t1: Pentru simularea unui singur turneu\n\t2: Pentru simularea a n turnee\n'))
    if i == 1:
       Tournament().startTournament()
    elif i == 2:
        n = int(input('Introduceti numarul de turnee pe care doriti sa le simulati:\nn= '))
        a = datetime.datetime.now()
        for i in range(n):
            print (i)
            winner = Tournament().startTournament()
            if winner in statistics.keys():
                statistics[winner] += 1
            else:
                statistics[winner] = 1
        b = datetime.datetime.now()

        print(statistics)
        y_pos = np.arange(len(statistics.keys()))
        plt.bar(statistics.keys(), statistics.values())
        plt.xticks(y_pos, statistics.keys(), rotation=70, fontsize='8', horizontalalignment='right')
        plt.show()
        print(b-a)


if __name__ == "__main__":
    main()

