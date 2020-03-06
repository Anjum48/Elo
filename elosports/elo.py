class Elo:
    def __init__(self, k, home_advantage=100):
        """
        :param k: Elo K-Factor
        :param home_advantage: Home field advantage, Default=100
        """
        self.ratingDict = {}
        self.k = k
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
        :param location: Location of the winning team. 'H' if the played at home, 'A' for away, 'N' for neutral
        :return:
        """
        if location == 'H':  # Home
            result = self.expected_result(self.ratingDict[winner], self.ratingDict[loser], bias=self.home_advantage)
        elif location == 'A':  # Away
            result = self.expected_result(self.ratingDict[winner], self.ratingDict[loser], bias=-self.home_advantage)
        else:  # Neutral venue
            result = self.expected_result(self.ratingDict[winner], self.ratingDict[loser])

        self.ratingDict[winner] += self.k * (1 - result)  # score = 1 for win, minus expected score
        self.ratingDict[loser] += self.k * (0 - (1 - result))  # score = 0 for loss, minus expected score

    def expected_result(self, pr_a, pr_b, bias=0, names=False):
        """
        See https://en.wikipedia.org/wiki/Elo_rating_system#Mathematical_details
        :param pr_a: player A performance rating or names
        :param pr_b: player B performance rating or names
        :param bias: Bias number which adds a constant offset to the ratings. Positive bias factors favor player A
        :param names: Flag to indicate if the inputs re names or performance ratings
        :return: Expected score
        """

        if names:
            pr_a = self.ratingDict[pr_a]
            pr_b = self.ratingDict[pr_b]

        exp = (pr_b - pr_a + bias) / 400.0
        return 1 / (1 + 10.0 ** exp)
