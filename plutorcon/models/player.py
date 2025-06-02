from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class Player:
    """**Represents a connected player on the server.**
    - Please note that the getting `Player` from `PlutoniumRCON().get_players()` method will not return IP, port, qport, guid, lastmsg, rate attributes.
    - These attributes are only available through the `PlutoniumRCON().status()` method."""
    id: Optional[int] = None
    name: Optional[str] = None
    ping: Optional[Union[int ,str]] = None
    score: Optional[int] = None
    ip: Optional[str] = None
    port: Optional[int] = None
    qport: Optional[int] = None
    guid: Optional[str] = None
    lastmsg: Optional[int] = None
    rate: Optional[int] = None