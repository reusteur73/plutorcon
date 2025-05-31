from dataclasses import dataclass

@dataclass
class ServerInfo:
    """Represents the server information."""
    netfieldchk: str
    protocol: int
    sessionmode: int       
    hostname: str
    mapname: str
    isInGame: bool
    com_maxclients: int
    gametype: str 
    game: str
    ff: int
    hw: int
    mod: int
    voice: int
    seckey: str
    secid: str
    hostaddr: str
    clients: int

@dataclass
class ServerStatus:
    """Represents the server status."""
    com_maxclients: int
    fs_game: str
    g_gametype: str
    g_randomSeed: str
    gamename: str
    mapname: str
    playlist_enabled: int
    playlist_entry: int
    protocol: int
    scr_team_fftype: int
    shortversion: int
    sv_allowAimAssist: int
    sv_allowAnonymous: int
    sv_clientFpsLimit: int
    sv_disableClientConsole: int
    sv_hostname: str
    sv_maxclients: int
    sv_maxPing: int
    sv_minPing: int
    sv_privateClients: int
    sv_privateClientsForClients: int
    sv_pure: int
    sv_voice: int
    sv_wwwBaseURL: str
    pswrd: bool
    mod: bool
