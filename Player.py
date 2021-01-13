class Player:
    nrTurneeCatigate = 0
    def __init__(self, firstName, lastName, country, rank):
        self.firstName = firstName
        self.lastName = lastName
        self.country = country
        self.rank = rank

    def __str__(self):
        return "First Name: " + self.firstName+" , Last Name: " + self.lastName + ", Country: " + self.country + ", Rank : " + self.rank + " " + "\n"

    def __repr__(self):
        return "First Name: " + self.firstName + " , Last Name: " + self.lastName + ", Country: " + self.country + ", Rank : " + self.rank + " " + "\n"

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getCountry(self):
        return self.country

    def getRank(self):
        return int(self.rank)
