import socket, re
from typing import Union
from .models import Player, Commands, Colors, ServerInfo, ServerStatus

class PlutoniumRCON:
    """A class to interact with a Plutonium server using RCON Q3"""
    def __init__(self, ip, port, password=None, timeout=2):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.password = password
        self.socket = None
        self._connect()

    def _connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(self.timeout)

    def _send_command(self, command: str, auth=False, arg="") -> list[str]:
        if not auth:
            request = b"\xFF\xFF\xFF\xFF" + command.encode('latin1') + b"\n"
        else:
            pre_request = f"rcon {self.password} {command}{' ' + arg if arg else ''}"
            request = b"\xFF\xFF\xFF\xFF" + pre_request.encode('latin1') + b"\n"
        try:
            self.socket.sendto(request, (self.ip, self.port))
            data, _ = self.socket.recvfrom(4096)
            response = data.decode("latin1", errors="ignore")
            return response.strip().split("\n")
        except socket.timeout:
            return []
        except Exception as e:
            return []

    def _strip_colors(self, text: str) -> str:
        return re.sub(r'\^\d', '', text)

    def get_players(self) -> list[Player]:
        """Get a list of players on the server.
        Returns:
            list[Player]: A list of Player objects representing players on the server.
            If the server is not responding, returns an empty list.
        """
        lines = self._send_command("getstatus")
        if not lines or not lines[0].strip().endswith("statusResponse"):
            return []
        players = []

        player_id = 0
        for line in lines[2:]:
            if not line.strip():
                continue
            parts = line.split(" ", 2)
            if len(parts) < 3:
                continue
            score, ping, raw_name = parts
            name_match = re.search(r'"(.*?)"', raw_name)
            name = name_match.group(1) if name_match else "Unknown"
            players.append(Player(id=player_id, name=self._strip_colors(name), ping=int(ping), score=int(score)))
            player_id += 1
        return players

    def get_server_status(self) -> dict | None:
        """Get server information.
        Returns:
            dict:
                A dictionary containing server information.
            If the server is not responding, returns **None**.
        """
        lines = self._send_command(Commands.GET_STATUS)
        if not lines or not lines[0].strip().endswith("statusResponse"):
            return None

        raw_info = lines[1]
        info_dict = {}
        entries = raw_info.strip("\\").split("\\")
        for i in range(0, len(entries) - 1, 2):
            key = entries[i]
            value = entries[i + 1]
            info_dict[key] = value
        info = ServerStatus(**info_dict)
        return info

    def get_server_infos(self) -> dict | None:
        """Get server informations.
        Returns:
            dict:
                A dictionary containing server information.
            If the server is not responding, returns **None**.
        """
        lines = self._send_command(Commands.GET_INFO)
        if not lines or not lines[0].strip().startswith("ÿÿÿÿinfoResponse"):
            return None

        raw_info = lines[1]
        info_dict = {}
        entries = raw_info.strip("\\").split("\\")
        for i in range(0, len(entries) - 1, 2):
            key = entries[i]
            value = entries[i + 1]
            info_dict[key] = value
        info = ServerInfo(**info_dict)
        return info

    def say(self, message: str, color: Colors=Colors.RED) -> bool:
        """Send a message to the server.
        Args:
            message (str): The message to send.
            color (Colors): The color of the message.
        Returns:
            bool: True if the message was sent successfully, False otherwise.
        """
        if not message or not isinstance(message, str) or not isinstance(color, Colors):
            return False
        response = self._send_command(Commands.SAY, True, f"{color.value}{message}")
        if not response:
            return False
        return True if response[0].startswith("say") else False

    def kick(self, player_id: Union[str, int], reason: str="You have been kicked by owner!") -> bool:
        """Kick a player from the server.
        Args:
            player_id (int): The ID of the player to kick.
            reason (str): The reason for kicking the player.
        Returns:
            bool: True if the player was kicked successfully, False otherwise.
        """
        if isinstance(player_id, int) and isinstance(reason, str):
            command = f'''{Commands.KICK} {player_id} "{reason}"'''
            response = self._send_command(command, True)
            if len(response) == 3 and "client" in response[2] and "disconnected" in response[2]:
                    return True
        return False

    def tell(self, player_id: Union[str, int], message: str, color: Colors=Colors.RED) -> bool:
        """Send a message to a specific player.
        Args:
            player_id (int | str): The ID of the player to send the message to.
            message (str): The message to send.
            color (Colors): The color of the message.
        Returns:
            bool: True if the message was sent successfully, False otherwise.
        """
        if not isinstance(player_id, int) or not isinstance(message, str) or not isinstance(color, Colors):
            return False
        response = self._send_command(Commands.TELL, True, f"{player_id} {color.value}{message}")
        if not response:
            return False
        return response[0].startswith("ÿÿÿÿprint")

    def close(self):
        """Close RCON socket connection."""
        if self.socket:
            self.socket.close()
            self.socket = None

    def __del__(self):
        self.close()
