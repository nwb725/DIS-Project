from typing import Dict

class Sport():
    def __init__(self, sport_data: Dict):
        self.SPORT = sport_data.get('SPORT')
        self.speed = sport_data.get('speed')
        self.strength = sport_data.get('strength')
        self.durability = sport_data.get('durability')