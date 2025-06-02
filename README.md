# plutorcon

A lightweight Python client for sending RCON and status queries to Plutonium servers. Supports remote command execution (kick, say, tell) and retrieving server information (current map, player list, server name). You can also obtain detailed player data, including client IP addresses and GUIDs. Ideal for bots, admin panels, or monitoring tools.

## Installation

```bash
pip install plutorcon
```

## Usage

```python
from plutorcon import PlutoniumRCON, Colors

server = PlutoniumRCON(ip="127.0.0.1", port=12500, password="mycoolpass")

# Get server status
overview = server.get_server_status()
print(overview)

# Get minimal player info (no IP)
players = server.get_players()
print(players)

# Get detailed player info (IP, Port, Guid, Name, etc.)
players_details = server.status()
print(players_details)

# Get server information
data = server.get_server_infos()
print(data)

# Send a global message
server.say("Hello, world!", Colors.RED)

# Send a private message to a player by ID
server.tell(0, "Hello you!", Colors.GREEN)

# Kick a player by ID
server.kick(0, "Bye bye!")

# Close the connection
server.close()
```

## Troubleshooting

If you encounter issues, please check the following:

- Ensure the client IP is whitelisted in the server's `server.cfg` file.
- Make sure the server is configured to allow RCON connections and the `rcon_password` is set correctly.
- Verify the server is running and accessible at the specified IP and port.

## Contributing

Contributions are welcome! There is a way to tempban players, but it is not yet implemented. If you would like to add this feature, please submit a pull request.

Feel free to open an issue or submit a pull request for any improvements or bug fixes.
