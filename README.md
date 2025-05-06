# plutorcon

A lightweight Python client for sending RCON and status queries to Plutonium servers.
Supports remote command execution such as kick, ban, say, tell, and retrieving server information like current map, player list, and server name.
Designed for use in bots, admin panels, or monitoring tools.

## Installation

```bash
pip install plutorcon
```

## Usage

```python
from plutorcon import PlutoniumRCON, Colors

server = PlutoniumRCON("127.0.0.1", 24999, password="mycoolpass")

status = server.get_server_status()
print(status)

players = server.get_players()
print(players)

info = server.get_server_infos()
print(info)

server.say("Hello, world!", Colors.RED)

server.tell(0, "Hello you!", Colors.GREEN)

server.kick(0, "Bye bye!")

server.close()
```

## Troubleshooting
If you encounter issues, please check the following:
- Ensure you whitelist the client IP in the server's `server.cfg` file.
- Make sure the server is configured to allow RCON connections. Check the `rcon_password` in the server's configuration.
- Verify that the server is running and accessible at the specified IP and port.

## Contributing

Contributions are welcome! I know there is a way to tempban players, but I haven't implemented it yet. If you want to add this feature, please do so!

Feel free to open an issue or submit a pull request.
