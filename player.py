class Player:
    """
        name
        round
        score
    """

    def __init__(self, name):
        self._name = name
        self._score = 0

    def __str__(self):
        return "Player {} - Score {}".format(self._name, self._score)
    
    @property
    def name(self):
        return self._name
    
    @property
    def score(self):
        return self._score
    
    @property
    def round(self):
        return self._round
        
    def addScore(self, score):
        self._score += score