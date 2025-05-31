from dataclasses import dataclass

@dataclass
class Player:
    """Represents a connected player on the server."""
    id: int 
    name: str
    ping: int
    score: int