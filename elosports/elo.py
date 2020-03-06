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

    def game_over(self, winner_name, loser_name, location):
        """
        Update ratings after a game
        :param winner_name: Name of the winning team
        :param loser_name: Name of the losing team
        :param location: 'H' if the winner location is home, 'A' for away, 'N' for neutral
        :return:
        """
        if location == 'H':
            result = self.expected_result(self.ratingDict[winner_name] + self.home_advantage,
                                          self.ratingDict[loser_name])
        elif location == 'A':
            result = self.expected_result(self.ratingDict[winner_name],
                                          self.ratingDict[loser_name] + self.home_advantage)
        else:
            result = self.expected_result(self.ratingDict[winner_name], self.ratingDict[loser_name])

        self.ratingDict[winner_name] = self.ratingDict[winner_name] + (self.k * self.g) * (1 - result)
        self.ratingDict[loser_name] = self.ratingDict[loser_name] + (self.k * self.g) * (0 - (1 - result))

    def expected_result(self, player_a, player_b):
        """
        See https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details
        :param player_a: player A name
        :param player_b: player B name
        :return: Expected score
        """
        pr_a = self.ratingDict[player_a]
        pr_b = self.ratingDict[player_b]
        exp = (pr_a - pr_b) / 400.0
        return 1 / ((10.0 ** exp) + 1)
