class Elo:
    def __init__(self, k, g=1, home_advantage=100):
        """
        :param k: Elo K-Factor
        :param g: g-value to prevent autocorrelation
        :param home_advantage: Home advantage, Default=100
        """
        self.ratingDict = {}
        self.k = k
        self.g = g
        self.home_advantage = home_advantage

    def add_player(self, name, rating=1500):
        """
        :param name: Player name
        :param rating: Initial rating. Default=1500
        :return:
        """
        self.ratingDict[name] = rating

    def game_over(self, winner, loser, location):
        """
        Update ratings after a game
        :param winner: Name of the winning team
        :param loser: Name of the losing team
        :param location: 'H' if the winner location is home, 'A' for away, 'N' for neutral
        :return:
        """
        if location == 'H':
            result = self.expected_result(self.ratingDict[winner] + self.home_advantage,
                                          self.ratingDict[loser])
        elif location == 'A':
            result = self.expected_result(self.ratingDict[winner],
                                          self.ratingDict[loser] + self.home_advantage)
        else:
            result = self.expected_result(self.ratingDict[winner], self.ratingDict[loser])

        self.ratingDict[winner] = self.ratingDict[winner] + (self.k * self.g) * (1 - result)
        self.ratingDict[loser] = self.ratingDict[loser] + (self.k * self.g) * (0 - (1 - result))

    def expected_result(self, pr_a, pr_b, names=False):
        """
        See https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details
        :param pr_a: player A performance rating or names
        :param pr_b: player B performance rating or names
        :param names: Flag to indicate if the inputs re names or performance ratings
        :return: Expected score
        """

        if names:
            pr_a = self.ratingDict[pr_a]
            pr_b = self.ratingDict[pr_b]

        exp = (pr_b - pr_a) / 400.0
        return 1 / ((10.0 ** exp) + 1)
