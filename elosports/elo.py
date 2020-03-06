class Elo:

    def __init__(self, k, g=1, homefield=100):
        self.ratingDict = {}
        self.k = k
        self.g = g
        self.homefield = homefield

    def addPlayer(self, name, rating=1500):
        self.ratingDict[name] = rating

    def gameOver(self, winner, loser, location):
        """

        :param winner:
        :param loser:
        :param location: 'H' if the winner location is home, 'A' for away, 'N' for neutral
        :return:
        """
        if location == 'H':
            result = self.expectResult(self.ratingDict[winner] + self.homefield, self.ratingDict[loser])
        elif location == 'A':
            result = self.expectResult(self.ratingDict[winner], self.ratingDict[loser]+self.homefield)
        else:
            result = self.expectResult(self.ratingDict[winner], self.ratingDict[loser])

        self.ratingDict[winner] = self.ratingDict[winner] + (self.k*self.g)*(1 - result)
        self.ratingDict[loser] = self.ratingDict[loser] + (self.k*self.g)*(0 - (1 - result))

    def expectResult(self, p1, p2):
        exp = (p2-p1) / 400.0
        return 1 / ((10.0 ** exp) + 1)
