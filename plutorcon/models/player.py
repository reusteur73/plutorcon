from dataclasses import dataclass

@dataclass
class Player:
    id: int 
    name: str
    ping: int
    score: int