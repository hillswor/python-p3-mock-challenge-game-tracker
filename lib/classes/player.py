from operator import itemgetter


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2, 17):
            self._username = username
        else:
            raise Exception("Username must be a string with length between 2 and 16.")

    def results(self):
        from classes.result import Result

        return [r for r in Result.all if r.player == self]

    def games_played(self):
        return list(set([r.game for r in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        results = self.results()
        results_for_game = [r for r in results if r.game == game]
        return len(results_for_game)

    @classmethod
    def highest_scored(cls, game):
        return max(cls.all, key=lambda player: game.average_score(player))
